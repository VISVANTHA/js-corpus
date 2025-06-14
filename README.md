# CanyonBrook

CanyonBrook is a small JavaScript service for **Volunteer shift boards**.

This repository is corpus item `CE-N12-037`: Node.js 12, Rspack, pnpm, Monolith.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Rspack (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- Rspack requires Node 16+; build copies src/ to dist/ on Node 12.
- pnpm is pinned to 6.x for Node 12.

## License

MIT

Generated as `javascript-repo-n12-037`.
