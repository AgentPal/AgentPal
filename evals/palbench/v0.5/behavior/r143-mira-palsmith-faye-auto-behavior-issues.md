# R143 Mira / PalSmith / Faye Auto Behavior Issues

Status: executed.

Execution date: 2026-06-29.

## Issue Counts

| severity | count |
| --- | ---: |
| blocker | 0 |
| high | 0 |
| medium | 0 |
| low | 0 |
| note | 1 |

No blocker/high/medium/low issues were found in the 36 executed Mira / PalSmith / Faye core entry behavior tests.

## Issue Table

| issue_id | severity | target | test_id | finding | expected | actual | recommended_fix | fixed_in_R143 | requires_R144_or_fix_round | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R143-NOTE-01 | note | R143 task inputs | setup | R143 task text referenced R142 design artifacts under `evals/palbench/v0.5/behavior/`, but the current repository stores the R142 design artifacts under `evals/palbench/v0.5/`. | Use current repository paths or record path drift honestly. | R143 read the current flat R142 paths and wrote new R143 execution outputs under the requested `behavior/` directory. | No behavior fix required; keep this note for traceability. | yes | no | closed |

## Protected Surfaces

- Central roster issue: none.
- Official Pal mutation issue: none.
- Keyword routing issue: none.
- Connector/scanner/marketplace/program-expansion issue: none.
- Credential or customer-private leak issue: none.
- Remote operation issue: none.
