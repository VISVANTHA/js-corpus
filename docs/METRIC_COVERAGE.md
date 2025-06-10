# Metric coverage — DriftFen (`CE-N12-062`)

Node.js **12**. Combo sheet unique metrics: **17**.
WB-060 Path Execution Trace is not listed for JavaScript combo rows.

| Metric | Technique | Tool | Evidence |
| --- | --- | --- | --- |
| Execution Path Integrity | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Decision Outcome Verification | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Logical Sub-expression Validation | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Total Logical Combinatorial Coverage | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| Technical Debt Impact | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
| QA Resource Allocation | Cyclomatic Complexity | Lizard | `src/policy.js` (or `packages/shared/src/policy.js`) decision-heavy policy |
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
