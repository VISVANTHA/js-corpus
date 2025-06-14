# AlderFen

AlderFen is a small JavaScript service for **Clinic intake queues**.

This repository is corpus item `CE-N12-014`: Node.js 12, Vite (built as esbuild), pnpm, Microservices.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Vite (built as esbuild) (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- pnpm is pinned to 6.x for Node 12.

## License

MIT

Generated as `javascript-repo-n12-014`.
