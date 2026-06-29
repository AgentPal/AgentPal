# R159 Codex Subagent / External Agent / Explicit Tool Results

Status: executed-local
Date: 2026-06-29
Decision: `codex_subagent_and_direct_tool_partial_pass_ready_for_r160_pack_evidence_tightening`

## Summary

R159 completed the requested bounded real-host checks. It created real Codex background threads, started and closed one real Codex subagent, ran minimal external-agent calls where available, and produced direct-use evidence for explicit `pdf:pdf` and `product-design:audit` directives.

Plan Mode and Goal Mode were recorded as recommendation-only because this run did not programmatically switch the Codex UI mode. Claude Code was actually invoked for a minimal AgentPal handoff, but this is not a full Claude Code host acceptance test.

## Result Counts

| result | count |
| --- | ---: |
| pass | 11 |
| partial | 3 |
| fail | 0 |
| blocked | 0 |

## Detailed Results

| test_id | prompt | decision_card | child_thread_decision_card | explicit_tool_directive_record | host snapshot | codex_mode | codex_mode_executed | subthread_created | child_thread_ids | child_thread_outputs | external_agent | external_agent_minimal_call | skill/plugin invoked | invocation_type | evidence_path | safety_gate_result | score | issue_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R159-01 | Parallel review Delivery Pack A/B shape | use child/background thread only for independent review | yes | n/a | fixtures/r159/host-capability-snapshot.json | `parallel_review` | yes | yes | `019f137e-9e81-79d2-9000-301e16c96747` | blocked by missing Delivery Pack A content; valid enum | n/a | n/a | n/a | background_thread | r159-child-thread-decision-records.md | pass, read-only | partial | R159-LOW-01 |
| R159-02 | Simple rewrite should not trigger child/plugin/heavy path | direct owner answer | n/a | n/a | fixtures/r159/host-capability-snapshot.json | `normal_chat` | yes | no | `019f137f-24e2-7e91-97b8-ed618f344b5b` | subagent proved decision should be no subagent | n/a | n/a | n/a | anti-trigger | r159-child-thread-decision-records.md | pass | pass | none |
| R159-03 | Privacy-sensitive task | require CAL/approval before distribution | no child by default | n/a | fixtures/r159/host-capability-snapshot.json | `plan_mode` | recommendation-only | no | none | n/a | n/a | n/a | n/a | privacy_gate | r159-codex-subagent-external-agent-results.md | pass | pass | none |
| R159-04 | Research -> script -> QA chain | sequential chain | no | n/a | fixtures/r159/host-capability-snapshot.json | `sequential_chain` | decision-only | no | none | n/a | n/a | n/a | n/a | mode_decision | r159-codex-subagent-external-agent-results.md | pass | pass | none |
| R159-05 | Plan Mode positive | recommend Plan Mode | no | n/a | fixtures/r159/host-capability-snapshot.json | `plan_mode` | recommendation-only | no | none | n/a | n/a | n/a | n/a | mode_recommendation | r159-codex-subagent-external-agent-results.md | pass with UI limitation | partial | R159-LOW-02 |
| R159-06 | Goal Mode positive | recommend Goal Mode | no | n/a | fixtures/r159/host-capability-snapshot.json | `goal_mode` | recommendation-only | no | none | n/a | n/a | n/a | n/a | mode_recommendation | r159-codex-subagent-external-agent-results.md | pass with UI limitation | partial | R159-LOW-02 |
| R159-07 | Faye Delivery Pack privacy with verifier | Faye owner + Quinn verifier | no | n/a | fixtures/r159/host-capability-snapshot.json | `owner_verifier` | decision-only | no | none | n/a | n/a | n/a | n/a | owner_verifier | r159-codex-subagent-external-agent-results.md | pass | pass | none |
| R159-08 | User specified PDF Skill | Morgan direct-use with explicit directive | no | yes | fixtures/r159/host-capability-snapshot.json | `owner_verifier` | yes | no | none | n/a | n/a | n/a | `pdf:pdf` | real public fixture PDF parse | fixtures/r159/pdf-direct-use-evidence.json | pass, public fixture | pass | none |
| R159-09 | Workflow specified Product Design audit | Nova direct-use with explicit workflow directive | no | yes | fixtures/r159/host-capability-snapshot.json | `owner_verifier` | yes | no | none | n/a | n/a | n/a | `product-design:audit` | local screenshot audit evidence | fixtures/r159/product-design-direct-use-evidence.json | pass, public local screenshot | pass | none |
| R159-10 | Pal workflow specified Claude Code handoff | Atlas external handoff | no | yes | fixtures/r159/host-capability-snapshot.json | `external_agent_handoff` | yes, minimal | no | none | n/a | Claude Code | yes | n/a | minimal_handoff | fixtures/r159/claude-minimal-handoff-evidence.json | pass, no full-host claim | pass | none |
| R159-11 | Claude minimal AgentPal handoff | external handoff acceptance | no | yes | fixtures/r159/host-capability-snapshot.json | `external_agent_handoff` | yes, minimal | no | none | n/a | Claude Code | yes | n/a | minimal_handoff | fixtures/r159/claude-minimal-handoff-evidence.json | pass | pass | none |
| R159-12 | CodeWhale/OpenCode/Gemini/DeepSeek probes | external capability snapshot | no | yes | fixtures/r159/host-capability-snapshot.json | `external_agent_handoff` | partial | no | none | n/a | CodeWhale, DeepSeek, DeepSeek-TUI | CodeWhale prompt pass; DeepSeek version/help only; OpenCode/Gemini unavailable | n/a | minimal_startup_probe | fixtures/r159/codewhale-minimal-startup-evidence.json; fixtures/r159/deepseek-tui-startup-evidence.json | pass with availability notes | partial | R159-NOTE-01; R159-NOTE-02 |
| R159-13 | Each Pal Codex expert smoke | Quinn evidence audit | no new child for smoke; background thread used as test host | n/a | fixtures/r159/host-capability-snapshot.json | `normal_chat` | yes in background thread | yes | `019f1381-eca3-7913-a042-d57f2458f220` | 10 Pal result_status pass, valid enum only | n/a | n/a | n/a | background_thread_smoke | r159-each-pal-codex-expert-smoke-results.md | pass, read-only | pass | none |
| R159-14 | R158 enum regression | child card must use R157 enum only | yes | n/a | fixtures/r159/host-capability-snapshot.json | `parallel_review` | yes | yes | `019f137e-e464-7493-ae3d-96db772bc43` | no `background_thread_review`; blocked only by missing Delivery Pack B content | n/a | n/a | n/a | background_thread_enum_regression | r159-child-thread-decision-records.md | pass | pass | none |

## Negative Checks

- No push, pull, fetch, tag, GitHub Release, external deploy, connector install, daemon, scanner, database, marketplace, or auto external `.agentpal` write was performed.
- `New1/.agentpal` remained thin: only `AGENTPAL.md` and `project.json`.
- No customer-private data was written into public examples, Pal Packs, or global knowledge.
- R158 invalid `background_thread_review` was not used as an actual `codex_mode` result in R159 child records.

