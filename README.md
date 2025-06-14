# LumenSpire

LumenSpire is a small JavaScript service for **Field sample tracking**.

This repository is corpus item `CE-N16-052`: Node.js 16, Turbopack, yarn (Berry), Microservices.

It is a realistic original product used as White Box ground truth. Metric coverage is listed in `docs/METRIC_COVERAGE.md` for this Node version only (17 unique metrics on the combo sheet).

## Scripts

- `npm test` (or the repo package manager) — mocha, with nyc when that family applies
- `npm run build` — Turbopack (or a copy fallback when the bundler cannot run on this Node)


## Compatibility notes

- Turbopack CLI is not supported on Node 16; build copies src/ to dist/.
- Yarn Berry is pinned to 3.2.x for Node 16 (Yarn 4 needs a newer Node).

## License

MIT

Generated as `javascript-repo-n16-052`.
