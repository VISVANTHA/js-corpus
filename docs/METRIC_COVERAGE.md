# Metric coverage — JuniperSpire (`CE-N26-020`)

Node.js **26**. Combo sheet unique metrics: **75**.
WB-060 Path Execution Trace is not listed for JavaScript combo rows.

| Metric | Technique | Tool | Evidence |
| --- | --- | --- | --- |
| Multi-Point Failure Probability | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Redundancy Localization | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Structural Cleanliness Score | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Test Suite Streamlining | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Abstraction Potential | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Regression Focus Mapping | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Synchronization Verification | Code Duplication | jscpd | `http-errors.js` + `http-errors-legacy.js` |
| Violation Density per KLOC | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Resource Waste Identification | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Semantic Consistency Score | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Syntactic Uniformity Score | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Structural Threshold Monitoring | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Impact Prioritization | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Aggregated Risk Assessment | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Accuracy Tuning | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Project-Specific Enforcement | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Environment Standardization | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Automated Gatekeeping | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Quality Audit Trail | Lint / Rule Violations | eslint | `.eslintrc.cjs` + custom `eslint-rules/id-prefix.js` |
| Best Practice Compliance | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Entry Point Sanitization | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Sensitive Information Tracking | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Access Control Verification | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Supply Chain Security | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Regulatory Alignment | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Exploit Surface Identification | Static Vulnerabilities (SAST) | eslint-plugin-security | `src/auth.js`, `src/sanitize.js` |
| Hidden Relationship Mapping | Dependency Risk (SCA) | npm ls | lockfile + `package.json` |
| Legal Risk Validation | Dependency Risk (SCA) | npm ls | lockfile + `package.json` |
| Trust Integrity Verification | Dependency Risk (SCA) | npm audit + npm ls | lockfile + `package.json` |
| Community Vitality Tracking | Dependency Risk (SCA) | npm audit + npm ls | lockfile + `package.json` |
| Mitigation Effort Ranking | Dependency Risk (SCA) | npm audit + npm ls | lockfile + `package.json` |
| Real-Time Alerting | Dependency Risk (SCA) | npm audit + npm ls | lockfile + `package.json` |
| Known CVE Count | Dependency Risk (SCA) | npm audit + npm ls | lockfile + `package.json` |
| Version Lag Assessment | Dependency Risk (SCA) | npm audit + npm ls | lockfile + `package.json` |
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
| Full Logic Validation | Path Coverage | nyc v17.1.1 | `tests/*.test.js`, `.nycrc.json` |
| Gap Identification | Path Coverage | nyc v17.1.2 | `tests/*.test.js`, `.nycrc.json` |
| Deep Logic Probing | Path Coverage | nyc v17.1.3 | `tests/*.test.js`, `.nycrc.json` |
| Iterative Route Analysis | Path Coverage | nyc v17.1.3 | `tests/*.test.js`, `.nycrc.json` |
| Ghost Code Discovery | Path Coverage | nyc v17.1.3 | `tests/*.test.js`, `.nycrc.json` |
| Error Flow Verification | Path Coverage | nyc v17.1.3 | `tests/*.test.js`, `.nycrc.json` |
| Cross-Component Mapping | Path Coverage | ESLint (eslint-scope) + nyc v17.1.0 | `tests/*.test.js`, `.nycrc.json` |
| Automated Quality Enforcement | Path Coverage | ESLint (eslint-scope) + nyc v17.1.1 | `tests/*.test.js`, `.nycrc.json` |
| Path Coverage % | Path Coverage | ESLint (eslint-scope) + nyc v17.1.2 | `tests/*.test.js`, `.nycrc.json` |
| Logic Error Sensitivity | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Test Rigor Assessment | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Weak Spot Localization | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| Boundary Mutant Analysis | Mutation Score | StrykerJS + Mocha | `stryker.conf.json` mutates policy |
| All-Defs Coverage % | All Definition Coverage | ESLint (eslint-scope) + nyc v17.1.0 | `tests/*.test.js`, `.nycrc.json` |
| Data Path Correlation | All Definition Coverage | ESLint (eslint-scope) + nyc v17.1.1 | `tests/*.test.js`, `.nycrc.json` |
| DU-Path Validation | All Definition Coverage | ESLint (eslint-scope) + nyc v17.1.2 | `tests/*.test.js`, `.nycrc.json` |
| Dead Data Identification | All Definition Coverage | ESLint (eslint-scope) + nyc v17.1.3 | `tests/*.test.js`, `.nycrc.json` |
| Null and Boundary Flow Analysis | All Definition Coverage | ESLint (eslint-scope) + nyc v17.1.4 | `tests/*.test.js`, `.nycrc.json` |
| Audit Trail Verification | All Definition Coverage | ESLint (eslint-scope) + nyc v17.1.5 | `tests/*.test.js`, `.nycrc.json` |
| Data Processing Validation | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.6 | `tests/*.test.js`, `.nycrc.json` |
| Logic Influence Assessment | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.7 | `tests/*.test.js`, `.nycrc.json` |
| Path Correlation Mapping | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.8 | `tests/*.test.js`, `.nycrc.json` |
| Comprehensive Data Proofing | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.9 | `tests/*.test.js`, `.nycrc.json` |
| Data Flow Gap Analysis | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.10 | `tests/*.test.js`, `.nycrc.json` |
| Ambiguity Resolution | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.11 | `tests/*.test.js`, `.nycrc.json` |
| Inter-procedural Tracking | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.12 | `tests/*.test.js`, `.nycrc.json` |
| Ghost Use Identification | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.13 | `tests/*.test.js`, `.nycrc.json` |
| Data Integrity Audit | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.14 | `tests/*.test.js`, `.nycrc.json` |
| All-Uses Coverage % | All Uses Coverage | ESLint (eslint-scope) + nyc v17.1.15 | `tests/*.test.js`, `.nycrc.json` |
