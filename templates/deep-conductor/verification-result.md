# Verification Result Template

```yaml
verification_id:
status: draft
workflow_id:
task_package_ref:
checked_by:
checked_at:
overall_result: pass | fail | partial | missing | not-run | blocked | requires-human-review
checks:
  - check_id:
    requirement:
    status: pass | fail | missing | not-run | blocked | requires-human-review
    evidence:
    missing_evidence:
    risk:
    required_fix:
human_review:
  required: true
  reviewer_role:
  review_status: not-run
runtime_execution:
  performed: false
  evidence:
forbidden_actions_check:
  keyword_routing_used: false
  connector_used: false
  scanner_or_validator_program_used: false
  marketplace_or_installer_used: false
  external_project_agentpal_written: false
  credentials_included: false
  customer_private_data_in_reusable_pack: false
decision:
  accepted_for_reusable_pack: false
  accepted_for_private_project_use: false
  next_action:
```
