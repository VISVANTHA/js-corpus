# KestrelHearth

KestrelHearth is a small JavaScript service for **Archive box indexes**.

This repository is corpus item `CE-N16-047`: Node.js 16, Parcel, bun, Monolith.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Parcel (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- bun as package manager is not runnable on Node 16; bun.lock is a declared lockfile artifact. Install on a newer host if you need node_modules.

## License

MIT

Generated as `javascript-repo-n16-047`.
