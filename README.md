# DriftInlay

DriftInlay is a small JavaScript service for **Fleet maintenance logs**.

This repository is corpus item `CE-N12-064`: Node.js 12, SWC, bun, Microservices.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — SWC (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- bun as package manager is not runnable on Node 12; bun.lock is a declared lockfile artifact. Install on a newer host if you need node_modules.

## License

MIT

Generated as `javascript-repo-n12-064`.
