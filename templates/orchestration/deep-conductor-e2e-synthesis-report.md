# Deep Conductor E2E Synthesis Report Template

```yaml
schema: agentpal.deep-conductor-e2e-synthesis-report.v0.3
report_id: e2e-report-<short-id>
goal: <original user goal>

what_was_planned:
  package_id: <Deep Conductor E2E Package id>
  topology: <selected topology>
  owner_candidates: []
  runtime_candidates: []
  verification_approach: <summary>

what_was_executed_by_runtime:
  status: <executed | not_run | partially_executed | blocked>
  runtime: <host Runtime or unknown>
  evidence: []
  affected_paths: []
  not_run: []

what_was_verified:
  status: <pass | fail | partial | not_run | blocked | unknown>
  evidence_checked: []
  missing_evidence: []
  verifier_candidate: <Pal or verifier gap>

agreement:
  points: []

conflicts:
  points: []
  owner_to_resolve: <Pal | user | runtime | unknown>

risks:
  items: []

missing_evidence:
  items: []

context_usage_summary:
  read_tier_used: <tier>
  index_known_count: <number or unknown>
  content_read_count: <number or unknown>
  profile_read_count: <number or unknown>
  memory_used: <yes | no | not_approved | stale | unknown>
  exact_token_or_cost_claim: false

runtime_skill_usage_summary:
  candidates_named: []
  availability: <available | unavailable | unknown | blocked | not_needed>
  used_by_host_runtime: <yes | no | not_run | unknown>
  fallback_used: <yes | no | not_needed | unknown>

memory_writeback_summary:
  routing_memory_candidate: <created | not_needed | blocked | not_run>
  runtime_skill_usage_memory_candidate: <created | not_needed | blocked | not_run>
  private_content_excluded: true

next_round_recommendation:
  action: <next action>
  reason: <why>
  not_a_fixed_route: true

requires_user_decision:
  needed: <true | false>
  decisions: []
```
