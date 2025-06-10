# Metric coverage — CopperMeadow (`CE-N24-003`)

Node.js **24**. Combo sheet unique metrics: **45**.
WB-060 Path Execution Trace is not listed for JavaScript combo rows.

| Metric | Technique | Tool | Evidence |
| --- | --- | --- | --- |
| Technical Debt Impact | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
| Unit Test Complexity | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
| Defect Probability | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
| Modularization Opportunity | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
| Reviewer Fatigue Factor | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
| QA Resource Allocation | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
| Human Cognitive Load | Cognitive Complexity | eslint-plugin-sonarjs | nested control flow in policy |
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
