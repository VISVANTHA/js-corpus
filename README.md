# JS_V14_RSPACK_NPM_MICRO

Part of the `javascript-combos` white-box test-repo corpus (GraniteMill /
`granite-mill`, domain: Community garden plots).

- **Node.js:** 14.21.3 (family V14)
- **Bundler:** Rspack
- **Package manager:** npm
- **Architecture:** Microservices

The application code under `src/` (or `packages/*/src/` for Microservices
branches) is byte-identical across all 576 branches of this corpus; only the
build tool, package manager, architecture layout, and the resolved tool-pin
table below vary.

## Resolved tool pins for Node 14

| Block | Primary | Alternative |
| --- | --- | --- |
| Cyclomatic Complexity | Lizard | cyclomatic-complexity 1.0.0 |
| Cognitive Complexity | eslint-plugin-sonarjs 4.2.1 | cognitive-complexity-ts 0.8.2 |
| Code Duplication | jscpd 4.3.0 | Dolos 2.3.0 |
| Lint / Rule Violations | eslint 8.57.1 | oxlint 1.16.0 |
| Static Vulnerabilities (SAST) | eslint-plugin-security 2.1.1 | OpenGrep |
| Dependency Risk (SCA) | npm audit + npm ls | trivy |
| Statement Coverage | nyc + mocha 15.1.0 | monocart-coverage-reports 2.13.0 |
| Branch Coverage | nyc + mocha 15.1.0 | monocart-coverage-reports 2.13.0 |
| Path Coverage | nyc + mocha (branch-coverage proxy) 15.1.0 | monocart-coverage-reports 2.13.0 |
| Mutation Score | StrykerJS + Mocha 6.4.2 | gutcheck (not available on Node 14) |
| Coverage Delta | diff-cover | monocart-coverage-reports 2.13.0 |
| All Definition Coverage | ESLint (eslint-scope) 7.2.2 | knip (not available on Node 14) |
| All Uses Coverage | ESLint (eslint-scope) 7.2.2 | knip (not available on Node 14) |
| Code Churn | pydriller | Git-Spark (not available on Node 14) |

See `javascript-repos-build-contract.md` in the Testable (Tools) project for
the full 103-metric roster, the repair notes, and the live pin-resolution
method (npm registry `engines.node` ranges, prereleases excluded).
