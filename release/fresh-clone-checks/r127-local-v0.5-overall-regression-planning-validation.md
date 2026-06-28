# R127 - Local v0.5 Overall Regression Planning Validation

## Validation Summary

Validation round: R127 planning validation.

Validation scope: planning artifacts only. v0.5 overall regression execution remains not-run and is assigned to R128.

Result: pass.

Clean copy path: `C:\Users\Administrator\AppData\Local\Temp\AgentPal_R127_clean_20260628231727`

## Required Artifact Existence

| Artifact | Path | Result |
| --- | --- | --- |
| Overall regression plan | `evals/palbench/v0.5/r127-v0.5-overall-regression-plan.md` | pass |
| Overall regression test matrix | `evals/palbench/v0.5/r127-v0.5-overall-regression-test-matrix.md` | pass |
| Evidence map | `release/integration-notes/r127-v0.5-overall-regression-evidence-map.md` | pass |
| Issue template | `release/integration-notes/r127-v0.5-overall-regression-issue-template.md` | pass |
| R128 checklist | `release/integration-notes/r127-r128-overall-regression-execution-checklist.md` | pass |
| R128 readiness decision | `release/integration-notes/r127-r128-readiness-decision.md` | pass |

## Required Planning Checks

| Check | Required Result | Actual Result |
| --- | --- | --- |
| 12 groups covered in plan | pass | pass - 12 group rows found |
| 12 groups covered in matrix | pass | pass - 12 `V05-R127-Gxx` rows found |
| Matrix has required fields | pass | pass |
| Evidence map covers required modules | pass | pass |
| Issue template has required fields | pass | pass |
| R128 checklist covers required safety gates | pass | pass |
| JSON parse | pass | pass - 19 scoped JSON files parsed |
| Clean-copy validation | pass | pass - required paths missing 0; scoped JSON failures 0 |
| Central roster count | 9/9 | pass - 9 active registered Pals |
| Official Pal directory count | 9 | pass |
| Active keyword routing | none | pass - no active true keyword route flags found |
| Connector/scanner/marketplace expansion | none | pass - changed-file hits are forbidden/safety-context references only |
| Credential/customer-private leak in R127 public outputs | none | pass - changed-file hits are safety boundary references only |
| Push/pull/fetch/tag/release | not performed | pass |

## Notes

Planning validation passed. This validation does not execute the v0.5 overall regression; R128 must still run the 12 test groups.
