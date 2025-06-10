# Metric coverage — MossMeadow (`CE-N18-003`)

Node.js **18**. Combo sheet unique metrics: **47**.
WB-060 Path Execution Trace is not listed for JavaScript combo rows.

| Metric | Technique | Tool | Evidence |
| --- | --- | --- | --- |
| Execution Path Integrity | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Decision Outcome Verification | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Logical Sub-expression Validation | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Total Logical Combinatorial Coverage | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Technical Debt Impact | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| QA Resource Allocation | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Multi-Point Failure Probability | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Redundancy Localization | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Structural Cleanliness Score | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Test Suite Streamlining | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Abstraction Potential | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Regression Focus Mapping | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Synchronization Verification | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Best Practice Compliance | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Entry Point Sanitization | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Sensitive Information Tracking | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Access Control Verification | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Supply Chain Security | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Regulatory Alignment | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Exploit Surface Identification | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Test Case Granularity | Statement Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Unreachable Logic Identification | Statement Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Coverage Gap Analysis | Statement Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Surface-Level Correctness | Statement Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Statement Coverage % | Statement Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Boolean Accuracy Check | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Sequence Integrity Mapping | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Iteration Boundary Verification | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Boundary Failure Identification | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Branch Misdirection Discovery | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Decision Coverage Gap Analysis | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Branch Coverage % | Branch Coverage | nyc + mocha | `tests/*.test.js`, `.nycrc.json` |
| Logic Error Sensitivity | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Test Rigor Assessment | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Weak Spot Localization | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Boundary Mutant Analysis | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Coverage Delta % | Coverage Delta | diff-cover | git history with tests after features; nyc cobertura/lcov |
| Discovery Power Assessment | Coverage Delta | diff-cover | git history with tests after features; nyc cobertura/lcov |
| Deployment Readiness Guard | Coverage Delta | diff-cover | git history with tests after features; nyc cobertura/lcov |
| Ripple Effect Mapping | Coverage Delta | diff-cover | git history with tests after features; nyc cobertura/lcov |
| Fresh Logic Proofing | Coverage Delta | diff-cover | git history with tests after features; nyc cobertura/lcov |
| Structural Health Benchmarking | Coverage Delta | diff-cover | git history with tests after features; nyc cobertura/lcov |
| Code Churn Score | Code Churn | pydriller | 12+ commits; policy.js hotspot edits |
| Impact-Driven Verification | Code Churn | pydriller | 12+ commits; policy.js hotspot edits |
| Fault Probability Modeling | Code Churn | pydriller | 12+ commits; policy.js hotspot edits |
| Validation Suite Updates | Code Churn | pydriller | 12+ commits; policy.js hotspot edits |
| Side Effect Mapping | Code Churn | pydriller | 12+ commits; policy.js hotspot edits |
