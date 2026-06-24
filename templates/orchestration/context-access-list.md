# Context Access List Template

Use this template to state what a recipient may read for a specific workflow step.

```yaml
schema: agentpal.context-access-list.v0.1
workflow_id:
step_id:
stage_id:
stage_goal:
recipient_type: pal | runtime | skill | plugin | mcp | verifier | team-leader-summary
recipient_id:
recipient_candidate:
  id:
  why_candidate:
  not_a_fixed_route: true
task:
need_output:
can_read_paths:
  - path:
    reason:
can_read_summaries:
  - summary_id:
    reason:
can_receive_outputs_from:
  - step_id:
    output_type:
cannot_read:
  - full_agentpal_workspace
  - all_pals
  - all_project_files
  - unrelated_pal_memory
  - private_user_memory
  - credentials_or_secrets
  - unapproved_external_directories
sensitive_context_boundary:
private_memory_boundary:
content_read_budget:
  max_files:
  max_large_files:
index_known_paths:
  - path:
    source:
content_read_files:
  - path:
    evidence:
output_contract:
verification_required: false
verification:
  expected_evidence:
  verifier:
stage_boundary:
  can_receive_outputs_from:
  must_not_read_unrelated_stage_drafts: true
  implementation_stage_must_use_pal_layer_task_package: true
```
