# BrambleMarina

BrambleMarina is a small JavaScript service for **Maker-space access**.

This repository is corpus item `CE-N12-028`: Node.js 12, Rollup, yarn (Berry), Microservices.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Rollup (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- Yarn Berry is pinned to 3.2.x for Node 12 (Yarn 4 needs a newer Node).

## License

MIT

Generated as `javascript-repo-n12-028`.
