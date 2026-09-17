# JS_V16_VITE_NPM_MICRO

Part of the `javascript-combos` white-box test-repo corpus (GraniteMill /
`granite-mill`, domain: Community garden plots).

- **Node.js:** 16.20.2 (family V16)
- **Bundler:** Vite (built as esbuild)
- **Package manager:** npm
- **Architecture:** Microservices

The application code under `src/` (or `packages/*/src/` for Microservices
branches) is byte-identical across all 576 branches of this corpus; only the
build tool, package manager, architecture layout, and the resolved tool-pin
table below vary.

## Resolved tool pins for Node 16

| Block | Primary | Alternative |
| --- | --- | --- |
| Cyclomatic Complexity | Lizard | cyclomatic-complexity 1.2.4 |
| Cognitive Complexity | eslint-plugin-sonarjs 4.2.1 | cognitive-complexity-ts 0.8.2 |
| Code Duplication | jscpd 4.3.0 | Dolos 2.5.1 |
| Lint / Rule Violations | eslint 8.57.1 | oxlint 1.16.0 |
| Static Vulnerabilities (SAST) | eslint-plugin-security 2.1.1 | OpenGrep |
| Dependency Risk (SCA) | npm audit + npm ls | trivy |
| Statement Coverage | nyc + mocha 15.1.0 | monocart-coverage-reports 2.13.0 |
| Branch Coverage | nyc + mocha 15.1.0 | monocart-coverage-reports 2.13.0 |
| Path Coverage | nyc + mocha (branch-coverage proxy) 15.1.0 | monocart-coverage-reports 2.13.0 |
| Mutation Score | StrykerJS + Mocha 7.3.0 | gutcheck (not available on Node 16) |
| Coverage Delta | diff-cover | monocart-coverage-reports 2.13.0 |
| All Definition Coverage | ESLint (eslint-scope) 7.2.2 | knip 2.43.0 |
| All Uses Coverage | ESLint (eslint-scope) 7.2.2 | knip 2.43.0 |
| Code Churn | pydriller | Git-Spark (not available on Node 16) |

See `javascript-repos-build-contract.md` in the Testable (Tools) project for
the full 103-metric roster, the repair notes, and the live pin-resolution
method (npm registry `engines.node` ranges, prereleases excluded).
