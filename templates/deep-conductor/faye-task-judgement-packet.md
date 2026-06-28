# Faye Task Judgement Packet Template

```yaml
packet_id:
status: draft
created_at:
owner: Faye
user_request:
delivery_goal:
requested_deliverables:
delivery_pack_ref:
org_pack_refs:
fde_pack_refs:
missing_information:
  - item:
    impact:
    status: missing
assumptions:
  - assumption:
    confidence: low | medium | high
    review_required: true
risk:
  customer_private_data: unknown
  professional_claims: unknown
  external_system_operation: false
  credential_or_secret_handling: false
  public_publication: false
workflow_topology:
  selected_mode: fast_route | owner_plus_verifier | plan_execute_verify | parallel_review | sequential_chain
  reason:
candidate_pals_as_ai_judgement_inputs:
  - pal:
    candidate_reason:
    expected_output:
runtime_or_skill_candidates:
  - id:
    type: runtime | skill | plugin | mcp | tool
    availability: unknown | available | unavailable | not-run
    evidence:
context_access_list_ref:
task_package_ref:
verification_required: true
human_review_required: true
forbidden_actions:
  - keyword routing
  - connector call
  - scanner or validator program
  - automatic external execution
  - external project .agentpal asset write
```
