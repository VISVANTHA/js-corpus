#!/usr/bin/env python3
"""
Parameterized generator for the javascript-combos corpus.

Produces, for one Node-version family at a time, the full 64-branch
combo grid (8 bundlers x 4 package managers x 2 architectures), writing
real application code, real tool configs, and a real dataset.json answer
key into each branch's existing git worktree directory.

Domain layer is byte-identical across all 576 branches (product:
GraniteMill / package: granite-mill / id prefix: GM-). Only the
build/package/architecture/tool-pin layer varies by branch, exactly as
required by the sibling C#/Java/Python/TypeScript corpora.

Usage (run from inside the corpus root, e.g. via device_bash):
    python3 gen_js_corpus.py --family 12 --root "." --old-prefix CE-N12 --dry-run
    python3 gen_js_corpus.py --family 12 --root "." --old-prefix CE-N12
"""
import argparse, json, os, sys, textwrap

# ---------------------------------------------------------------------------
# 1. Per-Node-family tool pin table (live-verified against registry.npmjs.org
#    engines.node ranges on 2026-09-16; prereleases excluded).
# ---------------------------------------------------------------------------
PINS = {
    "cyclomatic-complexity":       {12: None,      14: "1.0.0", 16: "1.2.4", 18: "1.2.5", 20: "1.2.5", 21: "1.2.5", 22: "1.2.5", 24: "1.2.5", 26: "1.2.5"},
    "eslint-plugin-sonarjs":       {12: "4.2.1",   14: "4.2.1", 16: "4.2.1", 18: "4.2.1", 20: "4.2.1", 21: "4.2.1", 22: "4.2.1", 24: "4.2.1", 26: "4.2.1"},
    "cognitive-complexity-ts":     {12: "0.8.2",   14: "0.8.2", 16: "0.8.2", 18: "0.8.2", 20: "0.8.2", 21: "0.8.2", 22: "0.8.2", 24: "0.8.2", 26: "0.8.2"},
    "jscpd":                       {12: "4.3.0",   14: "4.3.0", 16: "4.3.0", 18: "5.2.1", 20: "5.2.1", 21: "5.2.1", 22: "5.2.1", 24: "5.2.1", 26: "5.2.1"},
    "@dodona/dolos":               {12: "1.6.0",   14: "2.3.0", 16: "2.5.1", 18: "2.9.3", 20: "2.9.3", 21: "2.9.3", 22: "2.9.3", 24: "2.9.3", 26: "2.9.3"},
    "eslint":                      {12: "8.57.1",  14: "8.57.1", 16: "8.57.1", 18: "9.39.5", 20: "10.10.0", 21: "9.39.5", 22: "10.10.0", 24: "10.10.0", 26: "10.10.0"},
    "oxlint":                      {12: "1.16.0",  14: "1.16.0", 16: "1.16.0", 18: "1.16.0", 20: "1.83.0", 21: "1.16.0", 22: "1.83.0", 24: "1.83.0", 26: "1.83.0"},
    "eslint-plugin-security":      {12: "2.1.1",   14: "2.1.1", 16: "2.1.1", 18: "4.0.1", 20: "4.0.1", 21: "4.0.1", 22: "4.0.1", 24: "4.0.1", 26: "4.0.1"},
    "nyc":                         {12: "15.1.0",  14: "15.1.0", 16: "15.1.0", 18: "17.1.0", 20: "18.0.0", 21: "17.1.0", 22: "18.0.0", 24: "18.0.0", 26: "18.0.0"},
    "mocha":                       {12: "9.2.2",   14: "10.8.2", 16: "10.8.2", 18: "11.8.0", 20: "12.0.1", 21: "11.8.0", 22: "12.0.1", 24: "12.0.1", 26: "12.0.1"},
    "monocart-coverage-reports":   {12: "2.13.0",  14: "2.13.0", 16: "2.13.0", 18: "2.13.0", 20: "2.13.0", 21: "2.13.0", 22: "2.13.0", 24: "2.13.0", 26: "2.13.0"},
    "@stryker-mutator/core":       {12: "5.6.1",   14: "6.4.2", 16: "7.3.0", 18: "8.7.1", 20: "9.6.1", 21: "9.6.1", 22: "10.0.0", 24: "10.0.0", 26: "10.0.0"},
    "@stryker-mutator/mocha-runner": {12: "5.6.1", 14: "6.4.2", 16: "7.3.0", 18: "8.7.1", 20: "9.6.1", 21: "9.6.1", 22: "10.0.0", 24: "10.0.0", 26: "10.0.0"},
    "gutcheck":                    {12: None, 14: None, 16: None, 18: None, 20: "0.10.0", 21: "0.10.0", 22: "0.10.0", 24: "0.10.0", 26: "0.10.0"},
    "eslint-scope":                {12: "7.2.2",   14: "7.2.2", 16: "7.2.2", 18: "8.4.0", 20: "9.1.2", 21: "8.4.0", 22: "9.1.2", 24: "9.1.2", 26: "9.1.2"},
    "knip":                        {12: None, 14: None, 16: "2.43.0", 18: "5.88.1", 20: "6.36.0", 21: "5.88.1", 22: "6.36.0", 24: "6.36.0", 26: "6.36.0"},
    "git-spark":                   {12: None, 14: None, 16: None, 18: "1.0.265", 20: "1.3.0", 21: "1.3.0", 22: "1.3.2", 24: "1.3.2", 26: "1.3.2"},
}
# bundled-npm-per-family (documented from the existing corpus + npm's own release notes;
# Node 20's bundled npm is filled in from npm's public release history, same method as
# every other cell in this table, and should be re-verified live once N20 is bootstrapped
# for real by Claude Code, per README caveat).
BUNDLED_NPM = {12: "6.14.18", 14: "6.14.18", 16: "8.19.4", 18: "9.8.1", 20: "10.8.2", 21: "10.9.2", 22: "10.9.2", 24: "10.9.2", 26: "10.9.2"}

# Node full patch used in engines/.nvmrc/CI (matches the resolver's own NODE_PATCH table).
NODE_PATCH = {12: "12.22.12", 14: "14.21.3", 16: "16.20.2", 18: "18.20.8", 20: "20.20.2",
              21: "21.7.3", 22: "22.23.2", 24: "24.20.0", 26: "26.8.1"}

ESLINT_FLAT_CONFIG_FAMILIES = {18, 20, 21, 22, 24, 26}  # eslint 9+/10+ -> flat config

BUNDLERS = ["ESBUILD", "VITE", "WEBPACK", "ROLLUP", "RSPACK", "PARCEL", "TURBOPACK", "SWC"]
BUNDLER_LABEL = {"ESBUILD": "esbuild", "VITE": "Vite (built as esbuild)", "WEBPACK": "Webpack",
                 "ROLLUP": "Rollup", "RSPACK": "Rspack", "PARCEL": "Parcel",
                 "TURBOPACK": "Turbopack", "SWC": "SWC"}
PMS = ["NPM", "YARN", "PNPM", "BUN"]
PM_LABEL = {"NPM": "npm", "YARN": "yarn (Berry)", "PNPM": "pnpm", "BUN": "bun"}
ARCHES = ["MONO", "MICRO"]
ARCH_LABEL = {"MONO": "Monolith", "MICRO": "Microservices"}

# ---------------------------------------------------------------------------
# 2. Repaired 103-metric roster (source: JavaScript Tools List.xlsx, sheet
#    Testable_Strategy_Metrics_Mappi, re-read row by row 2026-09-16).
#    Fixes applied vs the original sheet:
#      - Cyclomatic Complexity alt "debtmap" (not a real npm package) -> cyclomatic-complexity
#      - Cognitive Complexity alt "cccc" (resolves to an unrelated cache-clearing
#        package on npm, not a complexity tool) -> cognitive-complexity-ts
#      - Path Coverage primary column was a copy-paste artifact incrementing a
#        fake "nyc v17.1.X" patch version row by row (v17.1.0..v17.1.2) with no
#        real meaning (nyc does not do path analysis) -> normalized to the real
#        tool actually doing the work: "nyc + mocha" (branch-coverage used as an
#        honest, documented proxy -- no JS-native path-coverage tool exists)
#        for rows about coverage-of-paths, and "ESLint (eslint-scope) + nyc +
#        mocha" for the three rows about cross-function/CI/aggregate path %.
#      - All Definition/All Uses Coverage (Data-Flow) primary column carried
#        the SAME fake incrementing "nyc v17.1.X" counter (continuing 0..5 then
#        6..15 across the two blocks -- proof it's one continuous copy-paste
#        error) -> normalized to "ESLint (eslint-scope)" alone (the real
#        def-use static-analysis script; nyc is a coverage tool, not a
#        data-flow tool, so pairing it here was a fabricated conflation).
#      - Data-Flow alternative column cycled inconsistently through
#        gutcheck/CodeQL/knip/Opengrep row by row with no logic ->
#        normalized to a single consistent alternative: knip.
#      - Dependency Risk (SCA) primary column mixed "npm ls" / "npm audit +
#        npm ls" / "N/A" for what is the same underlying check -> normalized
#        to "npm audit + npm ls" throughout.
#    Left unchanged (already correct/real): Code Duplication (jscpd/Dolos),
#    Lint/Rule Violations (eslint/oxlint), SAST (eslint-plugin-security/
#    OpenGrep), Statement/Branch Coverage (nyc+mocha/monocart), Mutation
#    Score (StrykerJS+Mocha/gutcheck), Coverage Delta (diff-cover/monocart),
#    Code Churn (pydriller/Git-Spark).
# ---------------------------------------------------------------------------
ROSTER = [
    {"block": "Cyclomatic Complexity", "metrics": 6, "primary": "Lizard", "primary_kind": "external",
     "alt": "cyclomatic-complexity", "alt_pin_key": "cyclomatic-complexity"},
    {"block": "Cognitive Complexity", "metrics": 7, "primary": "eslint-plugin-sonarjs", "primary_pin_key": "eslint-plugin-sonarjs",
     "alt": "cognitive-complexity-ts", "alt_pin_key": "cognitive-complexity-ts"},
    {"block": "Code Duplication", "metrics": 7, "primary": "jscpd", "primary_pin_key": "jscpd",
     "alt": "Dolos", "alt_pin_key": "@dodona/dolos"},
    {"block": "Lint / Rule Violations", "metrics": 12, "primary": "eslint", "primary_pin_key": "eslint",
     "alt": "oxlint", "alt_pin_key": "oxlint"},
    {"block": "Static Vulnerabilities (SAST)", "metrics": 7, "primary": "eslint-plugin-security", "primary_pin_key": "eslint-plugin-security",
     "alt": "OpenGrep", "alt_kind": "external"},
    {"block": "Dependency Risk (SCA)", "metrics": 8, "primary": "npm audit + npm ls", "primary_kind": "bundled",
     "alt": "trivy", "alt_kind": "external"},
    {"block": "Statement Coverage", "metrics": 5, "primary": "nyc + mocha", "primary_pin_key": "nyc",
     "alt": "monocart-coverage-reports", "alt_pin_key": "monocart-coverage-reports"},
    {"block": "Branch Coverage", "metrics": 7, "primary": "nyc + mocha", "primary_pin_key": "nyc",
     "alt": "monocart-coverage-reports", "alt_pin_key": "monocart-coverage-reports"},
    {"block": "Path Coverage", "metrics": 10, "primary": "nyc + mocha (branch-coverage proxy)", "primary_pin_key": "nyc",
     "alt": "monocart-coverage-reports", "alt_pin_key": "monocart-coverage-reports",
     "note": "No JS-native path-coverage tool resolved; branch coverage used as a documented proxy."},
    {"block": "Mutation Score", "metrics": 7, "primary": "StrykerJS + Mocha", "primary_pin_key": "@stryker-mutator/core",
     "alt": "gutcheck", "alt_pin_key": "gutcheck"},
    {"block": "Coverage Delta", "metrics": 6, "primary": "diff-cover", "primary_kind": "external",
     "alt": "monocart-coverage-reports", "alt_pin_key": "monocart-coverage-reports"},
    {"block": "All Definition Coverage", "metrics": 6, "primary": "ESLint (eslint-scope)", "primary_pin_key": "eslint-scope",
     "alt": "knip", "alt_pin_key": "knip"},
    {"block": "All Uses Coverage", "metrics": 10, "primary": "ESLint (eslint-scope)", "primary_pin_key": "eslint-scope",
     "alt": "knip", "alt_pin_key": "knip"},
    {"block": "Code Churn", "metrics": 5, "primary": "pydriller", "primary_kind": "external",
     "alt": "Git-Spark", "alt_pin_key": "git-spark"},
]
assert sum(b["metrics"] for b in ROSTER) == 103, sum(b["metrics"] for b in ROSTER)

PRODUCT_NAME = "GraniteMill"
PACKAGE_NAME = "granite-mill"
ID_PREFIX = "GM-"
DOMAIN = "Community garden plots"


def pin(pkg, fam):
    return PINS[pkg].get(fam)


def combo_for_index(idx0):
    """idx0: 0-based index into the 64-branch family grid."""
    bundler = BUNDLERS[idx0 // 8]
    pm = PMS[(idx0 % 8) // 2]
    arch = ARCHES[idx0 % 2]
    return bundler, pm, arch


# ---------------------------------------------------------------------------
# 3. Byte-identical domain layer (genericized: no per-branch product name,
#    no per-branch hardcoded ID prefix -- both are now corpus-wide constants).
# ---------------------------------------------------------------------------

def domain_files():
    f = {}
    f["src/result.js"] = """\
'use strict';

function ok(value) {
  return { ok: true, value };
}

function err(message) {
  return { ok: false, error: message };
}

function mapResult(result, fn) {
  if (!result.ok) return result;
  return ok(fn(result.value));
}

module.exports = { ok, err, mapResult };
"""

    f["src/clock.js"] = """\
'use strict';

class FixedClock {
  constructor(date) {
    this._date = date;
  }
  now() {
    return new Date(this._date.getTime());
  }
}

const DATASET_CLOCK = new FixedClock(new Date('2026-03-15T12:00:00.000Z'));

module.exports = { FixedClock, DATASET_CLOCK };
"""

    f["src/ids.js"] = f'''\
'use strict';

const PREFIX = '{ID_PREFIX}';

function isProductId(value) {{
  return typeof value === 'string' && value.startsWith(PREFIX) && value.length > PREFIX.length;
}}

function toProductId(seq) {{
  const n = Number(seq);
  if (!Number.isInteger(n) || n < 0) {{
    throw new TypeError('toProductId requires a non-negative integer sequence');
  }}
  return PREFIX + String(n).padStart(4, '0');
}}

module.exports = {{ PREFIX, isProductId, toProductId }};
'''

    f["src/sanitize.js"] = """\
'use strict';

function sanitizeText(input) {
  if (typeof input !== 'string') return '';
  return input.replace(/[<>]/g, '').trim().slice(0, 240);
}

function allowRole(role) {
  return role === 'owner' || role === 'editor' || role === 'viewer';
}

module.exports = { sanitizeText, allowRole };
"""

    f["src/auth.js"] = """\
'use strict';

function authorize(actor, action) {
  if (!actor || typeof actor.role !== 'string') {
    return { allowed: false, reason: 'unknown-actor' };
  }
  if (actor.role === 'viewer' && action === 'write') {
    return { allowed: false, reason: 'viewer-cannot-write' };
  }
  return { allowed: true, reason: 'ok' };
}

module.exports = { authorize };
"""

    f["src/dataflow.js"] = """\
'use strict';

function tallyHours(records, limit) {
  const bands = { low: 0, mid: 0, high: 0, invalid: 0 };
  let total = 0;
  for (let i = 0; i < records.length; i += 1) {
    const hours = Number(records[i] && records[i].hours);
    if (Number.isNaN(hours) || hours < 0) {
      bands.invalid += 1;
      continue;
    }
    const capped = typeof limit === 'number' && hours > limit ? limit : hours;
    total += capped;
    if (capped < 4) bands.low += 1;
    else if (capped < 8) bands.mid += 1;
    else bands.high += 1;
  }
  return { total, bands };
}

module.exports = { tallyHours };
"""

    f["src/http-errors.js"] = """\
'use strict';

class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

function notFound(message) {
  return new HttpError(404, message || 'not found');
}

function badRequest(message) {
  return new HttpError(400, message || 'bad request');
}

function forbidden(message) {
  return new HttpError(403, message || 'forbidden');
}

module.exports = { HttpError, notFound, badRequest, forbidden };
"""

    # Deliberate near-duplicate pair -- planted jscpd/Dolos duplication fixture.
    f["src/http-errors-legacy.js"] = """\
'use strict';

class LegacyHttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

function legacyNotFound(message) {
  return new LegacyHttpError(404, message || 'not found (legacy)');
}

function legacyBadRequest(message) {
  return new LegacyHttpError(400, message || 'bad request (legacy)');
}

function legacyForbidden(message) {
  return new LegacyHttpError(403, message || 'forbidden (legacy)');
}

module.exports = { LegacyHttpError, legacyNotFound, legacyBadRequest, legacyForbidden };
"""

    f["src/policy.js"] = f'''\
'use strict';

const {{ isProductId }} = require('./ids');

function evaluatePolicy(record, role) {{
  if (!record || !isProductId(record.id)) {{
    return {{ allowed: false, reason: 'invalid-id' }};
  }}
  if (role === 'viewer') {{
    return {{ allowed: record.status === 'published', reason: 'viewer-read-only' }};
  }}
  if (role === 'editor') {{
    if (record.status === 'archived') {{
      return {{ allowed: false, reason: 'archived-locked' }};
    }}
    return {{ allowed: true, reason: 'editor-ok' }};
  }}
  if (role === 'owner') {{
    return {{ allowed: true, reason: 'owner-ok' }};
  }}
  return {{ allowed: false, reason: 'unknown-role' }};
}}

function canTransition(from, to) {{
  const graph = {{
    draft: ['published', 'archived'],
    published: ['archived'],
    archived: [],
  }};
  switch (from) {{
    case 'draft':
    case 'published':
    case 'archived':
      return (graph[from] || []).includes(to);
    default:
      return false;
  }}
}}

module.exports = {{ evaluatePolicy, canTransition }};
'''

    f["src/store.js"] = """\
'use strict';

class MemoryStore {
  constructor() {
    this._data = new Map();
  }
  put(id, value) {
    this._data.set(id, value);
    return value;
  }
  get(id) {
    return this._data.get(id);
  }
  list() {
    return Array.from(this._data.values());
  }
}

module.exports = { MemoryStore };
"""

    f["src/service.js"] = """\
'use strict';

const { evaluatePolicy, canTransition } = require('./policy');
const { ok, err } = require('./result');
const { toProductId } = require('./ids');

function createService(store) {
  let seq = 0;

  function upsert(fields, role) {
    const id = fields.id || toProductId(seq++);
    const record = Object.assign({ id, status: 'draft' }, fields, { id });
    const decision = evaluatePolicy(record, role);
    if (!decision.allowed) return err(decision.reason);
    store.put(id, record);
    return ok(record);
  }

  function move(id, toStatus, role) {
    const record = store.get(id);
    if (!record) return err('not-found');
    const decision = evaluatePolicy(record, role);
    if (!decision.allowed) return err(decision.reason);
    if (!canTransition(record.status, toStatus)) return err('invalid-transition');
    const next = Object.assign({}, record, { status: toStatus });
    store.put(id, next);
    return ok(next);
  }

  function all() {
    return store.list();
  }

  return { upsert, move, all };
}

module.exports = { createService };
"""

    f["src/index.js"] = f'''\
'use strict';

const {{ createService }} = require('./service');
const {{ MemoryStore }} = require('./store');

function createApp() {{
  const store = new MemoryStore();
  const service = createService(store);
  return {{
    product: '{PRODUCT_NAME}',
    domain: '{DOMAIN}',
    service,
  }};
}}

module.exports = {{ createApp }};
'''

    f["tests/auth.test.js"] = """\
'use strict';

const assert = require('assert');
const { authorize } = require('../src/auth');

describe('auth', function () {
  it('blocks viewers from writing', function () {
    const decision = authorize({ role: 'viewer' }, 'write');
    assert.strictEqual(decision.allowed, false);
  });

  it('allows editors to write', function () {
    const decision = authorize({ role: 'editor' }, 'write');
    assert.strictEqual(decision.allowed, true);
  });

  it('rejects an unknown actor', function () {
    const decision = authorize(null, 'write');
    assert.strictEqual(decision.allowed, false);
    assert.strictEqual(decision.reason, 'unknown-actor');
  });
});
"""

    f["tests/policy.test.js"] = f'''\
'use strict';

const assert = require('assert');
const {{ evaluatePolicy, canTransition }} = require('../src/policy');
const {{ toProductId }} = require('../src/ids');

describe('policy', function () {{
  const id = toProductId(1);

  it('lets owners do anything', function () {{
    const decision = evaluatePolicy({{ id, status: 'draft' }}, 'owner');
    assert.strictEqual(decision.allowed, true);
  }});

  it('blocks editors on archived records', function () {{
    const decision = evaluatePolicy({{ id, status: 'archived' }}, 'editor');
    assert.strictEqual(decision.allowed, false);
  }});

  it('only lets viewers read published records', function () {{
    const decision = evaluatePolicy({{ id, status: 'draft' }}, 'viewer');
    assert.strictEqual(decision.allowed, false);
  }});

  it('validates status transitions', function () {{
    assert.strictEqual(canTransition('draft', 'published'), true);
    assert.strictEqual(canTransition('published', 'draft'), false);
    assert.strictEqual(canTransition('archived', 'published'), false);
  }});
}});
'''

    f["tests/service.test.js"] = """\
'use strict';

const assert = require('assert');
const { createService } = require('../src/service');
const { MemoryStore } = require('../src/store');

describe('service', function () {
  it('creates and lists records', function () {
    const service = createService(new MemoryStore());
    const result = service.upsert({ title: 'Plot A' }, 'owner');
    assert.strictEqual(result.ok, true);
    assert.strictEqual(service.all().length, 1);
  });

  it('rejects viewer writes', function () {
    const service = createService(new MemoryStore());
    const result = service.upsert({ title: 'Plot B' }, 'viewer');
    assert.strictEqual(result.ok, false);
  });
});
"""
    return f


DATAFLOW_SCRIPT = """\
#!/usr/bin/env node
'use strict';
/*
 * Real, self-authored def-use static-analysis script (not a stub). Walks
 * every module under src/ with Espree + eslint-scope, reports every
 * variable definition and every place it is subsequently read, and
 * flags any definition that is never used (an "unreached" definition).
 * This is the corpus's Primary tool for the All Definition Coverage /
 * All Uses Coverage blocks (see dataset.json / README.md for why nyc is
 * NOT used here: nyc measures line/branch execution, not data flow).
 */
const fs = require('fs');
const path = require('path');
const espree = require('espree');
const eslintScope = require('eslint-scope');

function listSourceFiles(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...listSourceFiles(full));
    else if (entry.isFile() && entry.name.endsWith('.js')) out.push(full);
  }
  return out;
}

function analyze(file) {
  const code = fs.readFileSync(file, 'utf8');
  const ast = espree.parse(code, { ecmaVersion: 2022, sourceType: 'script', loc: true, range: true });
  const scopeManager = eslintScope.analyze(ast, { ecmaVersion: 2022, sourceType: 'script' });
  const defs = [];
  const uses = [];
  for (const scope of scopeManager.scopes) {
    for (const variable of scope.variables) {
      for (const def of variable.defs) {
        defs.push({ name: variable.name, line: def.name.loc.start.line });
      }
      for (const ref of variable.references) {
        if (!ref.init) uses.push({ name: variable.name, line: ref.identifier.loc.start.line });
      }
    }
  }
  const usedNames = new Set(uses.map((u) => u.name));
  const unreached = defs.filter((d) => !usedNames.has(d.name));
  return { file, defs: defs.length, uses: uses.length, unreached: unreached.length };
}

function main() {
  const root = process.argv[2] || 'src';
  if (!fs.existsSync(root)) {
    console.log(JSON.stringify({ root, files: [], totals: { defs: 0, uses: 0, unreached: 0 } }));
    return;
  }
  const files = listSourceFiles(root).map(analyze);
  const totals = files.reduce(
    (acc, f) => ({ defs: acc.defs + f.defs, uses: acc.uses + f.uses, unreached: acc.unreached + f.unreached }),
    { defs: 0, uses: 0, unreached: 0 }
  );
  console.log(JSON.stringify({ root, files, totals }, null, 2));
}

main();
"""


def gitignore_text():
    return "\n".join([
        "node_modules/", "dist/", "coverage/", ".nyc_output/", ".stryker-tmp/",
        ".parcel-cache/", ".turbo/", ".yarn/", ".pnp.*", "*.log", "",
    ])


def license_text():
    return textwrap.dedent(f"""\
        MIT License

        Copyright (c) 2026 {PRODUCT_NAME} corpus contributors

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
        """)


ESBUILD_BACKEND_CONFIG = """\
const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['{entry}'],
  bundle: true,
  platform: 'node',
  outfile: 'dist/index.js',
}).catch((err) => {
  console.error(err);
  process.exit(1);
});
"""


def bundler_config(bundler, arch):
    """Returns a list of (filename, content) tuples -- most bundlers write
    exactly one config file, but Turbopack needs two (see below)."""
    entry = "src/index.js" if arch == "MONO" else "packages/api/src/index.js"
    if bundler == "ESBUILD":
        return [("esbuild.config.cjs", ESBUILD_BACKEND_CONFIG.replace("{entry}", entry))]
    if bundler == "VITE":
        return [("vite.config.js", f"""\
const {{ defineConfig }} = require('vite');

module.exports = defineConfig({{
  build: {{
    lib: {{
      entry: '{entry}',
      formats: ['cjs'],
      fileName: () => 'index.js',
    }},
    outDir: 'dist',
    target: 'node18',
  }},
}});
""")]
    if bundler == "WEBPACK":
        return [("webpack.config.cjs", f"""\
const path = require('path');

module.exports = {{
  entry: './{entry}',
  target: 'node',
  mode: 'production',
  output: {{
    path: path.resolve(__dirname, 'dist'),
    filename: 'index.js',
    libraryTarget: 'commonjs2',
  }},
}};
""")]
    if bundler == "ROLLUP":
        return [("rollup.config.mjs", f"""\
export default {{
  input: '{entry}',
  output: {{
    file: 'dist/index.js',
    format: 'cjs',
  }},
}};
""")]
    if bundler == "RSPACK":
        return [("rspack.config.cjs", f"""\
module.exports = {{
  entry: './{entry}',
  target: 'node',
  mode: 'production',
  output: {{
    filename: 'index.js',
    path: __dirname + '/dist',
    library: {{ type: 'commonjs2' }},
  }},
}};
""")]
    if bundler == "PARCEL":
        return [(".parcelrc", """\
{
  "extends": "@parcel/config-default"
}
""")]
    if bundler == "TURBOPACK":
        # Turbopack ships no standalone Node-library CLI outside Next.js.
        # turbopack.config.json documents the declared/intended tool
        # (declared support is a claim); esbuild.config.cjs is the real
        # file the build script actually invokes (invoking is the fact) --
        # both are written so the claim and the fact are both on disk and
        # neither one silently references a file that doesn't exist.
        return [
            ("turbopack.config.json", json.dumps({
                "note": "Turbopack has no standalone Node-library CLI outside Next.js; "
                        "this config documents the intended entry/output. The actual "
                        "build script below invokes esbuild.config.cjs as the real "
                        "bundling backend -- see that file, not this one, for what "
                        "`npm run build` actually runs.",
                "entry": entry, "outDir": "dist",
            }, indent=2) + "\n"),
            ("esbuild.config.cjs", ESBUILD_BACKEND_CONFIG.replace("{entry}", entry)),
        ]
    if bundler == "SWC":
        return [(".swcrc", json.dumps({
            "jsc": {"parser": {"syntax": "ecmascript"}, "target": "es2020"},
            "module": {"type": "commonjs"},
        }, indent=2) + "\n")]
    raise ValueError(bundler)


def build_script_for(bundler, arch):
    # Parcel takes its entry point as a CLI argument, not from a config file
    # the way every other bundler here does -- so unlike `main` in package.json,
    # it needs its own explicit architecture branch or it silently points at
    # a Monolith-only path on Microservices branches ("Entry ... does not exist").
    parcel_entry = "src/index.js" if arch == "MONO" else "packages/api/src/index.js"
    return {
        "ESBUILD": "node esbuild.config.cjs",
        "VITE": "vite build",
        "WEBPACK": "webpack --config webpack.config.cjs",
        "ROLLUP": "rollup -c rollup.config.mjs",
        "RSPACK": "rspack build -c rspack.config.cjs",
        "PARCEL": f"parcel build {parcel_entry} --target node --dist-dir dist",
        "TURBOPACK": "node esbuild.config.cjs",
        "SWC": "swc src -d dist --config-file .swcrc",
    }[bundler]


def bundler_dev_dependencies(bundler, fam):
    """Returns a dict of {package: versionRange} — every package the bundler's
    own CLI needs to actually run, not just the headline one. (Webpack 5 split
    its CLI into a separate `webpack-cli` package; declaring `webpack` alone
    gets you the bundling engine with no way to invoke it.)"""
    esbuild_dep = {"esbuild": "^0.19.0" if fam <= 16 else "^0.25.0"}
    return {
        "ESBUILD": esbuild_dep,
        "VITE": {"vite": "^4.5.0" if fam <= 16 else "^5.4.0"},
        "WEBPACK": {"webpack": "^5.90.0", "webpack-cli": "^5.1.4"},
        "ROLLUP": {"rollup": "^3.29.0" if fam <= 16 else "^4.24.0"},
        "RSPACK": {"@rspack/cli": "^1.0.0", "@rspack/core": "^1.0.0"},
        # pnpm's strict node_modules isolation refuses phantom dependencies:
        # .parcelrc's "extends": "@parcel/config-default" needs that package
        # declared directly, not just reachable as parcel's own transitive
        # dependency (which npm/yarn/bun's flatter resolution tolerates).
        "PARCEL": {"parcel": "^2.12.0", "@parcel/config-default": "^2.12.0"},
        # Turbopack has no standalone Node-library CLI outside Next.js (see
        # bundler_config's turbopack.config.json note) -- the branch's real
        # build backend is esbuild, so esbuild is the actual devDependency;
        # turbopack.config.json documents the declared/intended tool.
        "TURBOPACK": esbuild_dep,
        "SWC": {"@swc/cli": "^0.3.0", "@swc/core": "^1.9.0"},
    }[bundler]


def pm_files(pm, arch, fam):
    """Returns list of (path, content) for package-manager-specific manifests."""
    out = []
    if pm == "YARN":
        out.append((".yarnrc.yml", "nodeLinker: node-modules\nenableGlobalCache: false\n"))
    elif pm == "PNPM" and arch == "MICRO":
        out.append(("pnpm-workspace.yaml", "packages:\n  - 'packages/*'\n"))
    elif pm == "BUN":
        out.append(("bunfig.toml", "[install]\nexact = true\n"))
    return out


def package_manager_field(pm, fam):
    return {
        "NPM": None,  # engines.node + bundled npm documented, no packageManager field
        "YARN": "yarn@4.5.3",
        "PNPM": "pnpm@9.12.3",
        "BUN": "bun@1.1.34",
    }[pm]


def eslint_config(fam):
    """Returns (filename, content) — flat config for eslint 9+/10+, legacy for 8.x."""
    if fam in ESLINT_FLAT_CONFIG_FAMILIES:
        return ("eslint.config.js", """\
'use strict';

const sonarjs = require('eslint-plugin-sonarjs');
const security = require('eslint-plugin-security');

module.exports = [
  {
    files: ['src/**/*.js', 'packages/**/*.js'],
    plugins: { sonarjs, security },
    languageOptions: { ecmaVersion: 2022, sourceType: 'commonjs' },
    rules: {
      'sonarjs/cognitive-complexity': ['warn', 15],
      'security/detect-object-injection': 'warn',
      'security/detect-non-literal-fs-filename': 'warn',
      'no-unused-vars': 'warn',
    },
  },
];
""")
    return (".eslintrc.json", json.dumps({
        "root": True,
        "env": {"node": True, "es2021": True, "mocha": True},
        "parserOptions": {"ecmaVersion": 2021, "sourceType": "script"},
        "plugins": ["sonarjs", "security"],
        "extends": ["eslint:recommended"],
        "rules": {
            "sonarjs/cognitive-complexity": ["warn", 15],
            "security/detect-object-injection": "warn",
            "security/detect-non-literal-fs-filename": "warn",
            "no-unused-vars": "warn",
        },
    }, indent=2) + "\n")


def nycrc():
    return json.dumps({
        "all": True, "check-coverage": False,
        "include": ["src/**/*.js", "packages/**/*.js"],
        "exclude": ["tests/**", "dist/**", "scripts/**"],
        "reporter": ["text", "lcov", "cobertura"],
        "report-dir": "coverage",
    }, indent=2) + "\n"


def jscpd_config():
    # Lockfiles are inherently repetitive (many structurally-identical
    # dependency-resolution blocks) and jscpd's "json"/"yaml" format
    # scanners pick them up like any other source file -- without an
    # explicit exclusion, a large package-lock.json/pnpm-lock.yaml alone
    # can trip the 0% threshold on its own, independent of anything in
    # actual source. report/** is jscpd's own prior output, excluded for
    # the same reason.
    return json.dumps({
        "threshold": 0, "reporters": ["json", "consoleFull"],
        "ignore": ["**/node_modules/**", "**/dist/**", "**/coverage/**", "**/report/**",
                   "**/package-lock.json", "**/yarn.lock", "**/pnpm-lock.yaml",
                   "**/bun.lockb", "**/bun.lock"],
        "absolute": True,
    }, indent=2) + "\n"


def stryker_config(fam, arch):
    globs = ["src/**/*.js"] if arch == "MONO" else ["packages/**/src/**/*.js"]
    # Stryker's mocha-runner has its own test discovery, separate from the
    # "test" npm script -- without an explicit spec glob here it finds zero
    # tests and exits before running a single mutant ("No tests were
    # executed"). Must match the same glob the "test" script itself uses.
    spec = ["tests/**/*.test.js"] if arch == "MONO" else ["packages/shared/tests/**/*.test.js"]
    return json.dumps({
        "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
        "packageManager": "npm", "testRunner": "mocha", "reporters": ["clear-text", "json"],
        "coverageAnalysis": "perTest", "mutate": globs,
        "mochaOptions": {"spec": spec},
        # Stryker's default plugin auto-discovery globs node_modules/@stryker-mutator/*
        # expecting real directories; under pnpm's symlink-based layout that scan finds
        # nothing ("no TestRunner plugins were loaded") even though the package is
        # perfectly import()-able. Naming it explicitly skips the broken glob step.
        "plugins": ["@stryker-mutator/mocha-runner"],
    }, indent=2) + "\n"


def knip_config(arch):
    entry = ["src/index.js"] if arch == "MONO" else ["packages/*/src/index.js"]
    return json.dumps({"entry": entry, "project": ["src/**/*.js", "packages/**/*.js"]}, indent=2) + "\n"


def oxlint_config():
    return json.dumps({"rules": {"correctness": "warn", "suspicious": "warn"}}, indent=2) + "\n"


def ci_workflow(node_patch, branch_id):
    return f"""\
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '{node_patch}'
      - run: npm install --no-audit --no-fund || true
      - run: npm test || true
      # {branch_id}: exit-code contract is enforced by the corpus's own
      # verification script, not by this placeholder workflow -- see
      # javascript-repos-build-contract.md for the 0/1/3/4 gate.
"""


def readme_for_branch(branch_id, fam, bundler, pm, arch):
    return f"""\
# {branch_id}

Part of the `javascript-combos` white-box test-repo corpus ({PRODUCT_NAME} /
`{PACKAGE_NAME}`, domain: {DOMAIN}).

- **Node.js:** {NODE_PATCH[fam]} (family V{fam})
- **Bundler:** {BUNDLER_LABEL[bundler]}
- **Package manager:** {PM_LABEL[pm]}
- **Architecture:** {ARCH_LABEL[arch]}

The application code under `src/` (or `packages/*/src/` for Microservices
branches) is byte-identical across all 576 branches of this corpus; only the
build tool, package manager, architecture layout, and the resolved tool-pin
table below vary.

## Resolved tool pins for Node {fam}

| Block | Primary | Alternative |
| --- | --- | --- |
""" + "\n".join(
        f"| {b['block']} | {b['primary']}"
        f"{' ' + str(pin(b['primary_pin_key'], fam)) if b.get('primary_pin_key') and pin(b['primary_pin_key'], fam) else (' (not available on Node ' + str(fam) + ')' if b.get('primary_pin_key') and not pin(b['primary_pin_key'], fam) else '')}"
        f" | {b['alt']}"
        f"{' ' + str(pin(b['alt_pin_key'], fam)) if b.get('alt_pin_key') and pin(b['alt_pin_key'], fam) else (' (not available on Node ' + str(fam) + ')' if b.get('alt_pin_key') and not pin(b['alt_pin_key'], fam) else '')}"
        f" |"
        for b in ROSTER
    ) + f"""

See `javascript-repos-build-contract.md` in the Testable (Tools) project for
the full 103-metric roster, the repair notes, and the live pin-resolution
method (npm registry `engines.node` ranges, prereleases excluded).
"""


def dataset_json(branch_id, fam, bundler, pm, arch):
    metrics = []
    for b in ROSTER:
        primary_version = pin(b["primary_pin_key"], fam) if b.get("primary_pin_key") else None
        alt_version = pin(b["alt_pin_key"], fam) if b.get("alt_pin_key") else None
        compat_notes = []
        if b.get("primary_pin_key") and not primary_version:
            compat_notes.append(f"{b['primary']} not available on Node {fam} (engines.node excludes this family)")
        if b.get("alt_pin_key") and not alt_version:
            compat_notes.append(f"{b['alt']} not available on Node {fam} (engines.node excludes this family)")
        if b.get("note"):
            compat_notes.append(b["note"])
        metrics.append({
            "block": b["block"], "metricCount": b["metrics"],
            "primaryTool": b["primary"], "primaryVersion": primary_version,
            "alternativeTool": b["alt"], "alternativeVersion": alt_version,
            "compatNotes": compat_notes,
        })
    return {
        "id": branch_id,
        "productName": PRODUCT_NAME,
        "packageName": PACKAGE_NAME,
        "domain": DOMAIN,
        "language": "JavaScript",
        "node": NODE_PATCH[fam],
        "nodeFamily": fam,
        "bundler": BUNDLER_LABEL[bundler],
        "packageManager": PM_LABEL[pm],
        "bundledNpm": BUNDLED_NPM[fam],
        "architecture": ARCH_LABEL[arch],
        "toolRosterVersion": "js-roster-v2-2026-09-16",
        "uniqueMetrics": 103,
        "metrics": metrics,
        "status": "generated",
    }


def package_json(branch_id, fam, bundler, pm, arch):
    node_patch = NODE_PATCH[fam]
    deps = {}
    for key in ["eslint", "eslint-plugin-sonarjs", "eslint-plugin-security", "eslint-scope",
                "jscpd", "nyc", "mocha", "monocart-coverage-reports",
                "@stryker-mutator/core", "@stryker-mutator/mocha-runner",
                "cognitive-complexity-ts", "@dodona/dolos"]:
        v = pin(key, fam)
        if v:
            deps[key] = "^" + v
    for optional_key in ["cyclomatic-complexity", "oxlint", "knip", "gutcheck"]:
        v = pin(optional_key, fam)
        if v:
            deps[optional_key] = "^" + v
    for bname, bver in bundler_dev_dependencies(bundler, fam).items():
        deps[bname] = bver
    deps["espree"] = "^9.6.1" if fam <= 16 else "^10.2.0"

    # Test/coverage glob is architecture-aware: Monolith keeps its domain
    # tests at tests/, Microservices branches keep theirs under
    # packages/shared/tests/ (see generate_branch) -- a single hardcoded
    # glob silently finds zero tests on one of the two architectures
    # ("No test files found" reads as a pass to a naive exit-code check).
    test_glob = "tests/**/*.test.js" if arch == "MONO" else "packages/shared/tests/**/*.test.js"

    # No `|| true` on any of these: the whole corpus's exit-code contract
    # (0 ran / 1 failed / non-zero crash) only means anything if a tool's
    # real exit code is allowed to propagate. Masking it here would hide a
    # tool crash behind the same exit 0 as a clean run -- exactly the
    # "collapsed exit codes" failure mode the corpus's own methodology
    # prohibits. `audit` keeps its own non-zero-on-findings semantics,
    # which is real signal, not a crash, so it's left unmasked too.
    scripts = {
        "build": build_script_for(bundler, arch),
        "test": f"mocha {test_glob}",
        "lint": "eslint .",
        "lint:oxlint": "oxlint ." if pin("oxlint", fam) else "echo 'oxlint unavailable on this Node family' && exit 3",
        "coverage": "nyc npm test",
        "duplication": "jscpd .",
        "mutation": "stryker run" if pin("@stryker-mutator/core", fam) else "echo 'stryker unavailable' && exit 3",
        "dataflow": f"node scripts/dataflow-scope.js {'src' if arch == 'MONO' else 'packages'}",
        "audit": "npm audit --json",
    }

    pkg = {
        "name": PACKAGE_NAME,
        "version": "1.0.0",
        "description": f"{PRODUCT_NAME} -- {DOMAIN} ({branch_id})",
        "private": True,
        "main": "src/index.js" if arch == "MONO" else "packages/api/src/index.js",
        "engines": {"node": f">={node_patch}"},
        "scripts": scripts,
        "devDependencies": dict(sorted(deps.items())),
    }
    if bundler == "PARCEL":
        # The build script passes --target node; Parcel refuses to run a
        # named target that isn't declared here ("Could not find target
        # with name 'node'") -- the CLI flag alone was never sufficient.
        pkg["targets"] = {"node": {"context": "node", "includeNodeModules": True}}
    pm_field = package_manager_field(pm, fam)
    if pm_field:
        pkg["packageManager"] = pm_field
    return json.dumps(pkg, indent=2) + "\n"


def write_file(base, rel, content, dry_run):
    full = os.path.join(base, rel)
    if dry_run:
        return full
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", newline="\n") as fh:
        fh.write(content)
    return full


def clean_stale_content(base, dry_run):
    """Wipe pre-existing legacy content from this worktree -- but NEVER
    touch anything a real local install/verification run produced
    (node_modules, any package-manager lockfile, coverage output, mutation
    output, or workspace/package-manager caches). This generator only owns
    source/config/docs; real install and test artifacts belong to whoever
    ran the real toolchain (Claude Code) and are never regenerated content.
    The pre-existing corpus (before this rebuild) carried inconsistent
    legacy structure per branch (different product names, stray
    ESM-syntax duplicates under packages/*/src, stale lockfiles for the
    OLD product name, old docs) -- clearing that is still necessary for
    the byte-identical domain invariant to hold, but it must stop at the
    boundary of anything a real install run has since produced.
    """
    if dry_run or not os.path.isdir(base):
        return
    keep = {
        ".git", "node_modules",
        "package-lock.json", "yarn.lock", "bun.lock", "bun.lockb", "pnpm-lock.yaml",
        "coverage", ".nyc_output", ".stryker-tmp", "reports",
        ".yarn", ".pnp.cjs", ".pnp.loader.mjs",
    }
    for name in os.listdir(base):
        if name in keep:
            continue
        full = os.path.join(base, name)
        if os.path.isdir(full):
            import shutil
            shutil.rmtree(full)
        else:
            os.remove(full)


def generate_branch(root, branch_dir_name, branch_id, fam, bundler, pm, arch, dry_run):
    base = os.path.join(root, branch_dir_name)
    clean_stale_content(base, dry_run)
    written = []

    # Domain layer (byte-identical) laid out per architecture.
    dfiles = domain_files()
    if arch == "MONO":
        for rel, content in dfiles.items():
            written.append(write_file(base, rel, content, dry_run))
    else:
        # Microservices: shared domain lives in packages/shared/src, api/worker
        # re-export from it. Byte-identical shared content across all 576
        # branches; api/worker wrapper files are also identical to each other
        # architecture-wide (only the shared import path is fixed).
        for rel, content in dfiles.items():
            if rel.startswith("src/"):
                shared_rel = "packages/shared/src/" + rel[len("src/"):]
                written.append(write_file(base, shared_rel, content, dry_run))
            elif rel.startswith("tests/"):
                # packages/shared/tests/*.test.js sits at the same relative
                # depth from packages/shared/src/ as tests/ sits from src/
                # in the Monolith layout (one level up, then into src/) --
                # the require('../src/...') path in the domain test files is
                # therefore ALREADY correct for both layouts and must not be
                # rewritten. (A previous version of this generator rewrote it
                # to './src/...', which pointed at a directory that doesn't
                # exist -- packages/shared/tests/src/ -- and broke every
                # Microservices test file. Found by Claude Code's real
                # mocha runs once the test-glob fix let them execute for the
                # first time; see javascript-repos-build-contract.md.)
                test_rel = "packages/shared/" + rel
                written.append(write_file(base, test_rel, content, dry_run))
        api_index = """\
'use strict';

const { createApp } = require('../../shared/src/index');

module.exports = createApp();
"""
        worker_index = """\
'use strict';

const { createApp } = require('../../shared/src/index');

const app = createApp();
module.exports = { app };
"""
        written.append(write_file(base, "packages/api/src/index.js", api_index, dry_run))
        written.append(write_file(base, "packages/worker/src/index.js", worker_index, dry_run))
        written.append(write_file(base, "packages/shared/package.json",
                                   json.dumps({"name": PACKAGE_NAME + "-shared", "version": "1.0.0", "private": True}, indent=2) + "\n",
                                   dry_run))
        written.append(write_file(base, "packages/api/package.json",
                                   json.dumps({"name": PACKAGE_NAME + "-api", "version": "1.0.0", "private": True}, indent=2) + "\n",
                                   dry_run))
        written.append(write_file(base, "packages/worker/package.json",
                                   json.dumps({"name": PACKAGE_NAME + "-worker", "version": "1.0.0", "private": True}, indent=2) + "\n",
                                   dry_run))

    # Bundler config
    for bfile, bcontent in bundler_config(bundler, arch):
        written.append(write_file(base, bfile, bcontent, dry_run))

    # Package-manager-specific manifests
    for rel, content in pm_files(pm, arch, fam):
        written.append(write_file(base, rel, content, dry_run))

    # Tool configs
    efile, econtent = eslint_config(fam)
    written.append(write_file(base, efile, econtent, dry_run))
    written.append(write_file(base, ".nycrc.json", nycrc(), dry_run))
    written.append(write_file(base, ".jscpd.json", jscpd_config(), dry_run))
    if pin("@stryker-mutator/core", fam):
        written.append(write_file(base, "stryker.conf.json", stryker_config(fam, arch), dry_run))
    if pin("knip", fam):
        written.append(write_file(base, "knip.json", knip_config(arch), dry_run))
    if pin("oxlint", fam):
        written.append(write_file(base, ".oxlintrc.json", oxlint_config(), dry_run))
    written.append(write_file(base, "scripts/dataflow-scope.js", DATAFLOW_SCRIPT, dry_run))

    # Root-level project files
    written.append(write_file(base, "package.json", package_json(branch_id, fam, bundler, pm, arch), dry_run))
    written.append(write_file(base, ".gitignore", gitignore_text(), dry_run))
    written.append(write_file(base, ".nvmrc", str(fam) + "\n", dry_run))
    written.append(write_file(base, "LICENSE", license_text(), dry_run))
    written.append(write_file(base, "README.md", readme_for_branch(branch_id, fam, bundler, pm, arch), dry_run))
    written.append(write_file(base, ".github/workflows/ci.yml", ci_workflow(NODE_PATCH[fam], branch_id), dry_run))
    written.append(write_file(base, "dataset.json", json.dumps(dataset_json(branch_id, fam, bundler, pm, arch), indent=2) + "\n" if False else json.dumps(dataset_json(branch_id, fam, bundler, pm, arch), indent=2) + "\n", dry_run))

    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", type=int, required=True, choices=list(NODE_PATCH.keys()))
    ap.add_argument("--root", default=".")
    ap.add_argument("--old-prefix", required=True, help="e.g. CE-N12 (existing worktree dir prefix for this family)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", type=int, default=None, help="1-based combo index within the family, for testing a single branch")
    args = ap.parse_args()

    fam = args.family
    total_written = 0
    indices = [args.only - 1] if args.only else range(64)
    for idx0 in indices:
        bundler, pm, arch = combo_for_index(idx0)
        old_dir = f"{args.old_prefix}-{idx0 + 1:03d}"
        branch_id = f"JS_V{fam}_{bundler}_{pm}_{arch}"
        files = generate_branch(args.root, old_dir, branch_id, fam, bundler, pm, arch, args.dry_run)
        total_written += len(files)
        print(f"{old_dir:16s} -> {branch_id:34s} ({len(files)} files){' [dry-run]' if args.dry_run else ''}")

    print(f"\nfamily V{fam}: {len(list(indices))} branches, {total_written} files "
          f"{'planned' if args.dry_run else 'written'}.")


if __name__ == "__main__":
    main()
