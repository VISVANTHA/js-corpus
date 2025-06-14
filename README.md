# HavenBrook

HavenBrook is a small JavaScript service for **Volunteer shift boards**.

This repository is corpus item `CE-N14-053`: Node.js 14, Turbopack, pnpm, Monolith.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Turbopack (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- Turbopack CLI is not supported on Node 14; build copies src/ to dist/.
- pnpm is pinned to 6.x for Node 14.

## License

MIT

Generated as `javascript-repo-n14-053`.
