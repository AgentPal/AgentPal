# R103-D Official Pal Index Backfill Issue Template

Use one entry per integration finding. Keep the issue public-safe and avoid copying private data, credentials, raw logs, or customer material.

```yaml
issue_id:
affected_pal:
affected_path:
severity:
finding:
expected:
actual:
recommended_fix:
safe_to_fix_integration_round:
requires_human_review:
status:
```

## Field Guidance

| Field | Guidance |
| --- | --- |
| `issue_id` | Stable local id, for example `R103-INT-001`. |
| `affected_pal` | Pal display name or `workspace` / `integration` when not Pal-specific. |
| `affected_path` | Exact path, or `missing` if no path exists. |
| `severity` | `blocker`, `high`, `medium`, `low`, or `info`. |
| `finding` | Concise statement of the problem. |
| `expected` | What the R103-D gate or source thread required. |
| `actual` | What current evidence shows. Use `not-run` when not checked. |
| `recommended_fix` | Smallest safe repair or escalation. |
| `safe_to_fix_integration_round` | `yes`, `no`, or `unknown`. |
| `requires_human_review` | `yes`, `no`, or `unknown`. |
| `status` | `open`, `fixed`, `accepted-risk`, `not-reproducible`, or `deferred`. |

## Severity Guide

| Severity | Use When |
| --- | --- |
| `blocker` | central roster changed, `pal.json` changed, official manifest generated, credential leaked, external project asset copy happened, or required evidence is missing for acceptance. |
| `high` | selected Pal index/README is missing, wrong path was changed, or root entry / `pal.json` loadability is uncertain. |
| `medium` | wording may imply behavior change, route ownership is unclear, or Batch 2/3 overlap needs repair. |
| `low` | formatting, heading, or minor evidence-field issue that does not affect the gate decision. |
| `info` | observation for a future thread; no current repair required. |

## Example

```yaml
issue_id: R103-INT-001
affected_pal: PalSmith
affected_path: official/pals/PalSmith-pal-governor/runbooks/README.md
severity: high
finding: Expected pilot README is not present, and the R103-C validation does not record a deliberate no-write decision.
expected: R103-C either creates the approved runbooks README or records a no-write policy decision.
actual: File missing; decision evidence missing.
recommended_fix: Ask R103-C owner to provide validation evidence or create a scoped integration issue for PalSmith review.
safe_to_fix_integration_round: unknown
requires_human_review: yes
status: open
```
