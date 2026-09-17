# JavaScript repos build contract (`javascript-combos`)

Companion to `csharp-repos-build-contract.md`, `java-repos-build-contract.md`,
`python-grid-repos-build-contract.md`, and `typescript-repos-build-contract.md`.
Same methodology, same invariants, applied to the JavaScript white-box combo
corpus. Written 2026-09-16 after rebuilding the corpus from a broken prior
state (see "What was broken" below).

## Corpus shape

Single GitHub repo (`javascript-combos`), one git repo with `main` as the
primary worktree and each of **576 branches** checked out as its own linked
worktree directory (identified by a `.git` *file*, not a `.git` directory).

576 = 9 Node.js version families x 8 bundlers x 4 package managers x 2
architectures.

- **Node families:** 12, 14, 16, 18, 20, 21, 22, 24, 26
- **Bundlers:** esbuild, Vite (built as esbuild), Webpack, Rollup, Rspack,
  Parcel, Turbopack (ships esbuild as its actual bundling backend — see
  note below), SWC
- **Package managers:** npm, yarn (Berry), pnpm, bun
- **Architectures:** Monolith (`src/`), Microservices
  (`packages/{api,shared,worker}/src/`)

## Branch naming

`JS_V{version}_{BUNDLER}_{PACKAGE_MANAGER}_{ARCHITECTURE}`, e.g.
`JS_V12_ESBUILD_NPM_MONO`. Matches the convention already in use on the
Python corpus (`PY_V313_POETRY_PIP_MONO`). Retires two earlier naming
schemes: split-repo-per-Node-version, then the briefly-used
`CE-N{version}-{id}` single-repo scheme. `branch_rename_map.csv` +
`rename_branches.sh` (in `main/`) carry out that migration; not yet applied
as of this writing — the user runs it locally via Claude Code once all 9
families are real-verified (see "Local verification" below).

## What was broken (prior state, before this rebuild)

1. **Node 20 family was entirely empty** — 64 bare worktree placeholders
   with no application code at all.
2. **Tool roster wiring was incoherent across families** — tools like
   stryker, eslint-plugin-security, and jscpd appeared/disappeared between
   Node families with no measured compatibility logic behind it.
3. **Domain layer was not byte-identical** — each branch had a different
   fictional product name (AlderMill, BrambleMill, EmberVault, ember-mill,
   inlet-mill, moss-mill, ridge-mill, vale-mill, copper-mill, iron-mill,
   canyon-atlas, ...) and a branch-specific hardcoded ID prefix
   (`"AL12-001-"` etc.) baked into `src/ids.js`, breaking the
   byte-identical-domain invariant every sibling corpus relies on.
4. **Microservices branches carried stale duplicate source** — old
   ES-module-syntax copies of the domain files sat directly under
   `packages/api/src/` and `packages/worker/src/` (not just the thin
   `index.js` wrapper), plus stale `package-lock.json` files pinned to the
   old per-branch product name, and stale `docs/*.md` referencing the old
   naming. None of this matched the (also stale) `package.json`.
5. **The roster spec sheet itself (`JavaScript Tools List.xlsx`) had real
   defects**, confirmed by re-reading all 103 rows on 2026-09-16:
   - Cyclomatic Complexity alternative tool **"debtmap"** does not exist
     on npm — fabricated.
   - Cognitive Complexity alternative tool **"cccc"** resolves on npm to
     an unrelated cache-clearing package, not a complexity tool —
     fabricated/category error.
   - Path Coverage's Primary column was a copy-paste artifact: `nyc
     v17.1.0`, `v17.1.1`, `v17.1.2`, ... incrementing by row with no real
     meaning (nyc does not measure path coverage).
   - All Definition Coverage / All Uses Coverage (the Data-Flow blocks)
     carried the **same** fake incrementing counter, continuing from
     `v17.1.0` through `v17.1.15` across both blocks — proof it's one
     continuous copy-paste error, not sixteen independent decisions.
   - The Data-Flow Alternative column cycled inconsistently through
     gutcheck / CodeQL / knip / Opengrep row by row with no logic.
   - Dependency Risk (SCA) Primary column mixed `npm ls` / `npm audit +
     npm ls` / `N/A` for what is the same underlying check.

## Roster repair (103 metrics, 14 blocks)

Verified against npm's real registry data on 2026-09-16 (`registry.npmjs.org/<pkg>`,
`engines.node` ranges, prereleases excluded). Left unchanged where already
correct: Code Duplication, Lint/Rule Violations, SAST, Statement/Branch
Coverage, Mutation Score, Coverage Delta, Code Churn.

| Block | Metrics | Primary | Alternative | Fix applied |
| --- | --- | --- | --- | --- |
| Cyclomatic Complexity | 6 | Lizard (external, all versions) | `cyclomatic-complexity` (npm) | replaced fabricated "debtmap" |
| Cognitive Complexity | 7 | eslint-plugin-sonarjs | `cognitive-complexity-ts` (npm) | replaced fabricated "cccc" |
| Code Duplication | 7 | jscpd | @dodona/dolos | none needed |
| Lint / Rule Violations | 12 | eslint | oxlint | none needed |
| Static Vulnerabilities (SAST) | 7 | eslint-plugin-security | OpenGrep (external) | none needed |
| Dependency Risk (SCA) | 8 | npm audit + npm ls | trivy (external) | normalized Primary label |
| Statement Coverage | 5 | nyc + mocha | monocart-coverage-reports | none needed |
| Branch Coverage | 7 | nyc + mocha | monocart-coverage-reports | none needed |
| Path Coverage | 10 | nyc + mocha (branch-coverage proxy) | monocart-coverage-reports | removed fake per-row nyc version drag; documented as an honest proxy since no JS-native path-coverage tool exists |
| Mutation Score | 7 | StrykerJS + Mocha | gutcheck | none needed |
| Coverage Delta | 6 | diff-cover (external) | monocart-coverage-reports | none needed |
| All Definition Coverage | 6 | ESLint (eslint-scope) | knip | removed fake nyc pairing (nyc doesn't do data-flow); normalized Alternative to knip |
| All Uses Coverage | 10 | ESLint (eslint-scope) | knip | same as above |
| Code Churn | 5 | pydriller (external) | Git-Spark | none needed |

`6+7+7+12+7+8+5+7+10+7+6+6+10+5 = 103`.

The Primary for the two Data-Flow blocks is a real, self-authored script
(`scripts/dataflow-scope.js`, byte-identical across all 576 branches) that
walks every module with Espree + `eslint-scope` and reports every
definition/use pair and every unreached definition — not a stub.

## Live-verified per-Node-family tool pins

Resolved 2026-09-16 from npm registry `engines.node` data (same method as
the TypeScript corpus's derived tool-gradient table). `null` = not
installable on that Node family; the branch's `dataset.json` records this
as a `compatNotes` entry rather than silently omitting the row.

| package | 12 | 14 | 16 | 18 | 20 | 21 | 22 | 24 | 26 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cyclomatic-complexity | — | 1.0.0 | 1.2.4 | 1.2.5 | 1.2.5 | 1.2.5 | 1.2.5 | 1.2.5 | 1.2.5 |
| eslint-plugin-sonarjs | 4.2.1 | 4.2.1 | 4.2.1 | 4.2.1 | 4.2.1 | 4.2.1 | 4.2.1 | 4.2.1 | 4.2.1 |
| cognitive-complexity-ts | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 | 0.8.2 |
| jscpd | 4.3.0 | 4.3.0 | 4.3.0 | 5.2.1 | 5.2.1 | 5.2.1 | 5.2.1 | 5.2.1 | 5.2.1 |
| @dodona/dolos | 1.6.0 | 2.3.0 | 2.5.1 | 2.9.3 | 2.9.3 | 2.9.3 | 2.9.3 | 2.9.3 | 2.9.3 |
| eslint | 8.57.1 | 8.57.1 | 8.57.1 | 9.39.5 | 10.10.0 | 9.39.5 | 10.10.0 | 10.10.0 | 10.10.0 |
| oxlint | 1.16.0 | 1.16.0 | 1.16.0 | 1.16.0 | 1.83.0 | 1.16.0 | 1.83.0 | 1.83.0 | 1.83.0 |
| eslint-plugin-security | 2.1.1 | 2.1.1 | 2.1.1 | 4.0.1 | 4.0.1 | 4.0.1 | 4.0.1 | 4.0.1 | 4.0.1 |
| nyc | 15.1.0 | 15.1.0 | 15.1.0 | 17.1.0 | 18.0.0 | 17.1.0 | 18.0.0 | 18.0.0 | 18.0.0 |
| mocha | 9.2.2 | 10.8.2 | 10.8.2 | 11.8.0 | 12.0.1 | 11.8.0 | 12.0.1 | 12.0.1 | 12.0.1 |
| monocart-coverage-reports | 2.13.0 | 2.13.0 | 2.13.0 | 2.13.0 | 2.13.0 | 2.13.0 | 2.13.0 | 2.13.0 | 2.13.0 |
| @stryker-mutator/core | 5.6.1 | 6.4.2 | 7.3.0 | 8.7.1 | 9.6.1 | 9.6.1 | 10.0.0 | 10.0.0 | 10.0.0 |
| gutcheck | — | — | — | — | 0.10.0 | 0.10.0 | 0.10.0 | 0.10.0 | 0.10.0 |
| eslint-scope | 7.2.2 | 7.2.2 | 7.2.2 | 8.4.0 | 9.1.2 | 8.4.0 | 9.1.2 | 9.1.2 | 9.1.2 |
| knip | — | — | 2.43.0 | 5.88.1 | 6.36.0 | 5.88.1 | 6.36.0 | 6.36.0 | 6.36.0 |
| git-spark | — | — | — | 1.0.265 | 1.3.0 | 1.3.0 | 1.3.2 | 1.3.2 | 1.3.2 |

Bundled npm per family (documented, needs live re-verification on real
installs): 12→6.14.18, 14→6.14.18, 16→8.19.4, 18→9.8.1, 20→10.8.2 (not yet
live-verified, since N20 had no real install before this rebuild),
21/22/24/26→10.9.2.

### Two real, dated findings surfaced by this resolution (mirrors the TS
### sibling corpus's own Node-21 finding)

- **Node 21 resolves backward for 5 tools** (eslint, nyc, mocha,
  eslint-scope, knip): each drops to an older pinned version on Node 21
  than what's available on Node 20 or 22, because their current majors'
  `engines.node` ranges exclude the never-LTS Node 21.
- **oxlint's floor tightened mid-stream**: v1.16.0 (published 2025-09-16)
  declared `engines.node: ">=8.*"`; v1.17.0 (published one week later,
  2025-09-23) tightened to `^20.19.0 || >=22.12.0`, and every release since
  (through 1.83.0) kept that floor — hence oxlint pins to 1.16.0 on every
  pre-Node-20 family and jumps straight to 1.83.0 on Node 20+.

## Domain invariant

Byte-identical across all 576 branches (verified by SHA-256 over every
`src/*.js` / `packages/shared/src/*.js` file post-generation: exactly one
distinct hash-set for all 288 Monolith branches, exactly one for all 288
Microservices branches).

- **Product:** GraniteMill (`granite-mill`)
- **Domain:** Community garden plots
- **ID prefix:** `GM-` (generic corpus-wide constant, replacing the old
  per-branch `"AL12-001-"`-style hardcoding in `src/ids.js`)
- 12 domain source files + 3 mocha test files, unchanged from the
  Node-12 canonical source except for the two fixes above.
- Deliberate near-duplicate pair `src/http-errors.js` /
  `src/http-errors-legacy.js` — the planted jscpd/Dolos duplication
  fixture (unchanged from before).
- Microservices layout: full domain lives in `packages/shared/src/`;
  `packages/api/src/index.js` and `packages/worker/src/index.js` are thin
  wrappers requiring the shared module — also byte-identical across all
  288 Microservices branches.

## Generator

`main/generator/gen_js_corpus.py` — single parameterized Python script,
one Node family at a time (`--family 12 --old-prefix CE-N12`), idempotent
(wipes each branch's directory down to its `.git` worktree marker before
writing, so stale legacy content from any prior state can never coexist
with the regenerated files — see the exception list below). Per branch it
writes: package.json (pinned devDependencies from the table above, wired
scripts for every Primary tool), the bundler config file(s),
package-manager-specific manifests (`.yarnrc.yml` / `pnpm-workspace.yaml`
/ `bunfig.toml`), the eslint config (flat `eslint.config.js` for eslint
9+/10+ families, legacy `.eslintrc.json` for 8.x families), `.nycrc.json`,
`.jscpd.json`, `stryker.conf.json` (omitted where stryker doesn't
resolve), `knip.json` (omitted where knip doesn't resolve),
`.oxlintrc.json` (omitted where oxlint doesn't resolve),
`scripts/dataflow-scope.js`, `dataset.json` (full 103-metric answer key
with per-family `compatNotes`), README.md, LICENSE, `.gitignore`,
`.nvmrc`, and a GitHub Actions CI workflow pinned to that family's exact
Node patch version.

Turbopack note: it has no standalone Node-library CLI outside Next.js, so
its branches carry **two** files — `turbopack.config.json` (the declared
intent) and `esbuild.config.cjs` (the real bundling backend the `build`
script actually invokes) — declared support is a claim, invoking is the
fact, and both are on disk so neither one silently references something
that doesn't exist.

The clean-before-write step never touches anything a real local
install/verification run produced: `node_modules`, any package-manager
lockfile (`package-lock.json` / `yarn.lock` / `bun.lock` / `bun.lockb` /
`pnpm-lock.yaml`), `coverage/`, `.nyc_output/`, `.stryker-tmp/`, or yarn's
own cache/PnP files. The generator owns source/config/docs only; real
install and test artifacts belong to whoever ran the real toolchain.

## Local verification (Claude Code, real installs — in progress)

Per the corpus's own standard (matching what actually happened on the
C#/Java/Python/TS siblings — see e.g. the Python corpus's real `semgrep`
invocation crash, or the C# corpus's real `CS0579` compile error found
only by actually compiling every microservices branch), `dataset.json`'s
claims are meant to be **verified ground truth**, not npm-registry-derived
guesses left untested. Real per-branch installs, test runs, and live pin
verification are being done locally via Claude Code, family by family,
starting with Node 12 as the floor family. Findings so far:

### Node 12 pilot run — first pass caught 3 real scaffolding bugs (fixed 2026-09-16, this generator, before continuing to other families)

Running the full 64-branch, six-check sweep on Node 12 (the required
"parity" family — see below) surfaced three defects that were bugs in the
generator itself, not properties of Node 12, confirmed because the same
report explicitly separated "scaffolding bug — will reproduce identically
on every family" from "genuine Node-12 incompatibility":

1. **`test` script was not architecture-aware.** It was hardcoded to
   `mocha tests/**/*.test.js`, but Microservices branches keep their
   tests under `packages/shared/tests/`. Mocha silently reported "No test
   files found" and exited 0 — a false pass on every one of the 288
   Microservices branches. Fixed: the script is now
   `mocha packages/shared/tests/**/*.test.js` on Microservices branches,
   `mocha tests/**/*.test.js` on Monolith.
2. **Webpack branches were missing `webpack-cli`.** Webpack 5 split its
   CLI into a separate package; declaring `webpack` alone gets the
   bundling engine with no way to invoke it from the command line. Fixed:
   `webpack-cli` is now an explicit devDependency alongside `webpack`.
   (`@swc/core` was added alongside `@swc/cli` for the same reason, as a
   precaution, though SWC's actual N12 failure turned out to be a genuine
   Node incompatibility — see below.)
3. **Turbopack's `build` script referenced a file that didn't exist.**
   `esbuild.config.cjs` was the invoked script, but the generator only
   wrote `turbopack.config.json` for Turbopack branches. Fixed: Turbopack
   branches now get both files (see Generator section above).

A fourth issue was a design mistake, not a bug: `lint`, `lint:oxlint`,
`duplication`, and `mutation` all had `|| true` appended, which collapses
a real tool crash to the same exit 0 as a clean run — exactly the
"collapsed exit codes" failure the rest of this corpus's methodology
(0 ran / 1 failed / 3 skipped / 4 not-installed, never collapsed)
explicitly prohibits. Removed; `audit`'s `|| true` was kept since npm
audit's non-zero exit means "found vulnerabilities," which is real signal
rather than a crash.

**A real near-miss during the fix**: regenerating N12 after the fix
initially wiped the real lockfiles and `coverage/` output Claude Code had
already produced for branches 1–39 (the clean-before-write step's original
keep-list only protected `node_modules` and `.git`, not lockfiles or
coverage). Caught before it reached branches 40–64; the keep-list now
also protects every package-manager lockfile and test/coverage output
(see Generator section). Branches 1–39 need their installs/tests re-run
once regardless, since `package.json` itself changed (added
`webpack-cli`, fixed the test glob) — but this was still a real process
gap in the generator, recorded here rather than glossed over.

### Node 12 pilot run — genuine Node-12 findings (after the scaffolding fix)

- **Every Vite, Rollup, Rspack, Parcel, and SWC branch's build genuinely
  cannot run on Node 12** — only esbuild builds cleanly (16/64). Root
  causes, each individually diagnosed rather than assumed: Vite's CLI
  uses top-level `await` (needs Node 14.8+); Rollup and Rspack's CLIs use
  the `node:` built-in-module import prefix (needs Node 14.18+); Parcel's
  CLI uses `??`; SWC's CLI dependency chain (`@swc/cli` → `piscina`) uses
  an `exports` map Node 12 doesn't resolve correctly.
- **`eslint-plugin-sonarjs`, `oxlint`, `jscpd` (via `fs-extra`), and
  `stryker` (via `inquirer`) all genuinely crash on Node 12** — each
  because their own dependency code uses `?.` or `??`, syntax Node 12's
  V8 (7.8) has no support for at all (native support shipped with V8 8.0
  / Node 14). These would have been silently masked as "passing" by the
  `|| true` bug above; only removing the masking surfaced them.
- **Architecture is NOT inert for these checks** — confirmed by running
  the full 64-branch sweep on N12 specifically to test this: every
  Monolith/Microservices pair disagreed on `test` (and therefore
  `coverage`, which wraps it), because of scaffolding bug #1 above. Per
  protocol, this means every remaining family (14 onward) also gets the
  full 64-branch six-check sweep — no 32-branch architecture-collapsed
  shortcut, since the one family tested for it found real disagreement.

### Node 12 re-run — parity check caught a fourth, deeper scaffolding bug (fixed 2026-09-17)

The re-run confirmed the test-glob fix worked (mocha now finds the
Microservices test files) but surfaced a second bug hiding directly
behind it: `packages/shared/tests/*.test.js` did `require('./src/auth')`,
which resolves to a directory that doesn't exist
(`packages/shared/tests/src/`). The real file is one level up, at
`packages/shared/src/auth.js`.

Root cause: the generator explicitly rewrote the domain test files'
`require('../src/...')` to `require('./src/...')` when copying them into
the Microservices layout, on the mistaken assumption the relative path
needed adjusting for the new location. It didn't —
`packages/shared/tests/` sits at the exact same relative depth from
`packages/shared/src/` as `tests/` sits from `src/` in the Monolith
layout (one level up, then into `src/`), so `../src/...` was already
correct unchanged. The rewrite is what broke it. Fixed by deleting the
rewrite entirely; verified with a real `mocha` run (9/9 passing) before
redeploying to all 576 branches.

Same category as bug #1 (Microservices-layout-specific, Node-version-independent,
reproduces identically on every family) — just one layer deeper, only
visible once bug #1's fix let these files actually execute for the first
time. Comprehensive re-check across all 32 Mono/Micro pairs after fix
#1 but before this one: `test`/`coverage` 0/32 agree (this bug); `build`,
`lint`, `lint:oxlint`, `duplication`, `mutation`, `dataflow` 32/32 agree
(unaffected, consistent with the first pilot run).

**Scoping decision for families 14–26**, made once the corpus's parity
evidence was fully consistent (two independent runs, before and after
fix #1, both showing the disagreement isolated to test/coverage and
nothing else): install+test+build run on all 64 branches per family
(genuine per-branch variance lives here); lint/lint:oxlint/duplication/
mutation/dataflow drop to 32 (one architecture per bundler+package-manager
combo — zero architecture dependency shown across two separate N12 runs);
coverage is not run as a separate check, since its pass/fail is
mechanically downstream of test, which is already checked on all 64.

Still pending from Claude Code's local run: the final clean N12 re-run
confirming all six checks now agree on every Mono/Micro pair, the
npm-version cross-check against the bundled-npm table above (a local copy
of this doc is now on the machine at `main/javascript-repos-build-contract.md`
so this no longer needs relaying by hand), and the remaining 8 families.

## Verification performed in this Cowork session (2026-09-16, before local installs)

All 576 branches, all 9 families:
- Every `.json` file parses (`json.load`) — 0 failures.
- Every `.js`/`.cjs` file parses as valid JavaScript
  (`node --check` / `vm.Script`) — 0 failures.
- Domain layer executes correctly: `createApp()` wiring (auth, policy,
  service, store, result, ids) verified behaviorally on both a Monolith
  and a Microservices branch (owner-write succeeds, viewer-write is
  blocked, `GM-0000`-style IDs issued correctly).
- No stray legacy files remain (old per-branch product names, ESM-syntax
  duplicate sources under `packages/*/src/`, stale lockfiles, stale docs)
  — spot-checked and swept via the generator's own clean step.
- `.git` worktree markers (576 of 576) left intact by the clean step.

This pass could not, by construction, catch the three scaffolding bugs
above — none of them are JSON or JS syntax errors, and the domain-layer
smoke test doesn't invoke the bundler/test/lint scripts. That's exactly
why the real local install-and-run pass exists; see "Local verification"
above for what it's for and what it already found.
