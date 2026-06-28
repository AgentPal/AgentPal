# Delivery Workflow Plan Template

```yaml
workflow_id:
status: draft
owner: Faye
topology: fast_route | owner_plus_verifier | plan_execute_verify | parallel_review | sequential_chain
goal:
delivery_pack_ref:
stages:
  - stage_id:
    stage_goal:
    owner_candidate:
    owner_candidate_is_route: false
    inputs:
    context_access_list_entry:
    expected_output:
    verification:
      required: true
      verifier_candidate:
      not_run_allowed: true
      missing_evidence_blocks_pass: true
human_review:
  required: true
  reviewer_role:
governance_record_target:
routing_memory_candidate_target:
forbidden:
  connector_used: false
  keyword_routing_used: false
  auto_execution_used: false
  customer_private_data_in_reusable_pack: false
```
