# EmberKiln

EmberKiln is a small JavaScript service for **River gauge readings**.

This repository is corpus item `CE-N14-011`: Node.js 14, Vite (built as esbuild), yarn (Berry), Monolith.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Vite (built as esbuild) (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- Yarn Berry is pinned to 3.2.x for Node 14 (Yarn 4 needs a newer Node).

## License

MIT

Generated as `javascript-repo-n14-011`.
