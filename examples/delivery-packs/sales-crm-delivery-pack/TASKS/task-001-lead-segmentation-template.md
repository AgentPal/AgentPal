# Task 001: Lead Segmentation Template

## Goal

Create a first-pass segmentation recommendation from fictional or de-identified lead summaries.

## Inputs

```text
lead_placeholder_id:
lead_source_category:
company_size_band:
interest_category:
lifecycle_stage:
missing_fields:
privacy_notes:
```

## Candidate Pals

- Sales Strategist Pal
- CRM Ops Pal
- Data Review Pal
- Compliance QA Pal

Candidate Pals are AI judgement inputs only.

## Steps

1. Confirm the input is public-safe or de-identified.
2. Reject any real CRM data from this reusable task.
3. Select a proposed segment.
4. Explain the reason.
5. List missing evidence.
6. Mark human review status.

## Output Template

| Lead placeholder | Proposed segment | Reason | Missing evidence | Review status |
| --- | --- | --- | --- | --- |
| demo-lead-001 | priority B | clear interest but decision context missing | decision role, timeline | requires-human-review |

## Acceptance

Pass only if no customer-private data is present and review status is explicit.
