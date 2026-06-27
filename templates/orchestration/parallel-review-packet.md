# Parallel Independent Review Package

Use this package when Mira or an owner Pal organizes several independent reviewer candidates and later synthesizes their final reports.

```yaml
schema: agentpal.parallel-review-package.v0.3
workflow_id:
created_at:
user_goal:
review_need:
summary_owner_candidate:
workflow_boundary:
  no_code_staged_workflow: true
  no_group_chat: true
  no_automatic_parallel_execution: true
  no_subagent_mode: true
  no_external_agent_calls: true
  runtime_may_simulate_sequentially: true
  candidates_not_fixed_routes: true

reviewers:
  - review_id:
    reviewer_candidate:
    reviewer_fit_reason:
    review_angle:
    packet_template: templates/orchestration/reviewer-context-packet.md
    final_report_template: templates/orchestration/reviewer-final-report.md
    must_not_read:
      - peer_reviewer_drafts
      - peer_hidden_reasoning
      - full_chat_history_by_default
      - unauthorized_private_memory

synthesis_stage:
  synthesis_owner_candidate: Mira | owner_pal_candidate
  can_read:
    - reviewer_final_reports
  cannot_read:
    - reviewer_drafts
    - hidden_reasoning
    - unauthorized_private_memory
  synthesis_template: templates/orchestration/parallel-review-synthesis-summary.md
  required_output:
    - agreement
    - disagreement
    - conflicts
    - risks
    - decision_options
    - recommended_next_step
    - minority_opinion_preserved

optional_routing_memory:
  write_candidate_after_outcome_evidence: false
```
