# HavenTerrace

HavenTerrace is a small JavaScript service for **Studio kiln schedules**.

This repository is corpus item `CE-N14-056`: Node.js 14, Turbopack, bun, Microservices.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Turbopack (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- bun as package manager is not runnable on Node 14; bun.lock is a declared lockfile artifact. Install on a newer host if you need node_modules.
- Turbopack CLI is not supported on Node 14; build copies src/ to dist/.

## License

MIT

Generated as `javascript-repo-n14-056`.
