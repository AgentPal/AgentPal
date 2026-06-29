# R149 Manual Test Record Template

Status: designed
Date: 2026-06-29

Use these templates during R150+ manual execution. R149 itself does not fill actual test results.

## Single Test Record

```markdown
## Manual Test Record

- test_id:
- tester:
- date:
- host_runtime:
- host_runtime_version_if_known:
- model:
- reasoning_strength:
- capability_profile_status: unknown | runtime-evidence | manual-profile | unavailable | blocked
- capability_profile_source:
- prompt:
- expected_behavior:
- actual_response_summary:
- Pal_involved:
- mode_decision:
- artifacts_produced:
- evidence_path:
- result: pass | partial | fail | blocked
- issue_severity: blocker | high | medium | low | note | none
- issue_description:
- follow_up_action:
- user_experience_notes:
- not_run_items:
- missing_evidence:
- privacy_boundary_result:
- capability_boundary_result:
- project_root_boundary_result:
- deterministic_routing_result:
- legacy_positioning_result:
```

## Single Round Summary

```markdown
# R15x Manual Test Summary

Status:
Date:
Tester:
Host runtime:
Model / reasoning strength:
Capability profile status:

## Scope

- planned_test_count:
- executed_test_count:
- not_run_test_count:
- blocked_test_count:

## Result Counts

| Result | Count |
| --- | ---: |
| Pass | 0 |
| Partial | 0 |
| Fail | 0 |
| Blocked | 0 |
| Not-run | 0 |

## Severity Counts

| Severity | Count |
| --- | ---: |
| Blocker | 0 |
| High | 0 |
| Medium | 0 |
| Low | 0 |
| Note | 0 |

## Coverage

- hosts_covered:
- Pals_covered:
- scenario_groups_covered:
- Deep_Conductor_modes_covered:
- thin_binding_cases_covered:
- writeback_cases_covered:
- legacy_regression_cases_covered:

## Evidence

- evidence_dir:
- record_files:
- screenshots_or_transcripts:
- unavailable_evidence:

## Decision

- decision: continue | fix_required | blocked
- rationale:
- next_round:
```

## Issue Template

```markdown
## Manual Test Issue

- issue_id:
- source_test_id:
- severity: blocker | high | medium | low | note
- title:
- host_runtime:
- Pal_or_role:
- scenario_group:
- expected:
- actual:
- evidence_path:
- reproduction_prompt:
- privacy_or_boundary_impact:
- suspected_owner:
- recommended_fix_round:
- blocks_R150_plus:
- blocks_release_candidate:
```

## Evidence Template

```markdown
## Evidence Note

- evidence_id:
- test_id:
- evidence_type: transcript | screenshot | file | command-output | runtime-report | user-confirmation | unavailable
- path_or_location:
- captured_by:
- captured_at:
- proves:
- does_not_prove:
- missing_or_not_run:
- privacy_review:
```

## Storage Guidance

Manual execution records should be stored under a future manual execution directory such as:

```text
evals/palbench/v0.5/manual/r150-results/
evals/palbench/v0.5/manual/r151-results/
```

Do not place real customer-private transcripts, credentials, local machine secrets, or private project facts into public reusable result files. If a transcript contains private data, store only a redacted public-safe summary plus a private evidence pointer.

