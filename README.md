# EmberLantern

EmberLantern is a small JavaScript service for **Farmers market stalls**.

This repository is corpus item `CE-N14-006`: Node.js 14, esbuild, pnpm, Microservices.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — esbuild (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- pnpm is pinned to 6.x for Node 14.

## License

MIT

Generated as `javascript-repo-n14-006`.
