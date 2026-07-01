# R208 R209 Scoped Certification Execution Package

Status: copyable package for R209. This is not an execution result.

## Objective

R209 should run a scoped certification review for selected official Pal task
families. Certification must be recorded per Pal plus task family.

## Recommended Strategy

### Option A: High-Priority First

Review the five R205 high-priority task families first:

| Pal | Task family | Candidate level | Evidence paths |
| --- | --- | --- | --- |
| Mira-main | release readiness coordination | scoped_certification_candidate | `evals/palbench/v0.5/asset-usage/r205-mira-release-readiness-host-regression.md`; `official/pals/Mira-main/evals/asset-execution-example.md`; `evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md` |
| PalSmith-pal-governor | existing Pal composite upgrade planning | scoped_certification_candidate | `evals/palbench/v0.5/asset-usage/r205-palsmith-existing-pal-upgrade-host-regression.md`; `official/pals/PalSmith-pal-governor/evals/asset-execution-example.md`; `evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md` |
| Atlas-developer | docs-first development task package | scoped_certification_candidate | `evals/palbench/v0.5/asset-usage/r205-atlas-development-task-package-host-regression.md`; `official/pals/Atlas-developer/evals/asset-execution-example.md`; `evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md` |
| Quinn-quality | completion report / false completion review | scoped_certification_candidate | `evals/palbench/v0.5/asset-usage/r205-quinn-completion-report-review-host-regression.md`; `official/pals/Quinn-quality/evals/asset-execution-example.md`; `evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md` |
| Nova-product | product privacy and authorization-boundary decision | scoped_certification_candidate | `evals/palbench/v0.5/asset-usage/r205-nova-product-privacy-boundary-host-regression.md`; `official/pals/Nova-product/evals/asset-execution-example.md`; `evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md` |

Expected R209 output:

- one scoped certification record per selected Pal plus task family;
- one Quinn review;
- one summary matrix;
- validation report;
- no broad certification wording.

### Option B: 10-Pal Readiness Review

Review all 10 official Pals for certification readiness but do not grant
certification by default. Keep Faye, Harper, Morgan, Rhea, and Vega at
`representative_regression_passed` unless R209 also supplies the missing
example / checklist evidence and Quinn accepts it.

### Option C: Return To Release

Do not run certification. Use R208 wording in release docs:

```text
Official bundled Pals have scoped representative task-family host regression
evidence for Pal Asset Execution adoption. Formal scoped certification remains
a separate review gate.
```

## Quinn Review Requirements

Quinn should verify:

- each certification record is one Pal plus one task family;
- the evidence gate has all required items;
- host thread IDs and paths exist;
- missing assets are not ignored;
- no-code boundary wording is preserved;
- release wording is not overclaimed;
- no remote operation is included.

## Forbidden Claims

Do not claim:

- official roster broad certification;
- every task family coverage;
- R207 as certification;
- R209 as done before it runs;
- new runtime or backend behavior;
- contacts mutation;
- user custom Pal promotion;
- publication, tag, or release action.

## Recommended R209 Decision Values

- `scoped_certification_review_pass_with_notes`
- `partial_scoped_certification_review`
- `blocked_with_reasons`
