# Routing Decisions Example JSONL

Synthetic public-safe examples only.

```jsonl
{"schema":"agentpal.routing-decision-record.v0.3","record_id":"route-example-001","created_at":"2026-01-01","task_summary":"Synthetic release readiness review","task_type":"release-review","topology_candidate":"owner_plus_verifier","owner_pal_candidate":"Mira","verifier_pal_candidate":"Quinn","runtime_candidate":"codex-workspace","model_or_reasoning_candidate":"high","context_index_known_count":8,"context_content_read_count":4,"decision_basis":["release evidence needs independent verification","current contacts include Quinn as quality verifier"],"privacy_review":{"public_safe":true,"sensitive_context_excluded":true},"not_a_fixed_route":true}
{"schema":"agentpal.routing-result-record.v0.3","record_id":"route-result-example-001","decision_record_id":"route-example-001","completed_at":"2026-01-01","verification_result":"pass","evidence_summary":["JSON parse check passed","no-runtime scan passed"],"not_run_items":[],"false_completion_caught":"not_applicable","rework_count":0,"user_accepted":"unknown","failure_reason":"","next_time_recommendation":"Owner + Verifier is a useful candidate for similar release reviews when evidence is available; still rerun current task judgement.","privacy_review":{"public_safe":true,"no_private_content":true},"not_a_fixed_route":true}
```
