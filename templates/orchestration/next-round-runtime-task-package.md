# Next-Round Runtime Task Package

Use this template to turn a Project Conductor task map into a bounded next-round task for Codex, Claude Code, OpenCode, OpenHands, Gemini CLI, or another host Runtime.

The host Runtime executes. AgentPal does not execute.

```yaml
schema: agentpal.next_round_runtime_task_package.v0.1
round_goal: ""
target_runtime_candidate:
  name: ""
  reason: ""
  evidence_required: []
target_model_or_reasoning_candidate:
  model: ""
  reasoning: ""
  reason: ""
runtime_skill_candidates:
  - name: ""
    type: "" # Agent Skill | plugin | MCP | browser | office document | repo analysis | other
    reason: ""
    evidence_required: []
required_context: []
forbidden_context: []
task_scope:
  in_scope: []
  out_of_scope: []
steps:
  - ""
acceptance_criteria:
  - ""
verification_plan:
  verifier_candidate: ""
  evidence_required: []
  result_record_template: ""
final_report_format:
  must_include:
    - files_read_or_changed
    - runtime_skills_used_or_not_run
    - evidence
    - verification_result
    - blockers
stop_conditions:
  - ""
```

## Rules

- `target_runtime_candidate` is not a fixed route.
- `runtime_skill_candidates` are executed only by the host Runtime when available and authorized.
- The package must not imply AgentPal has already performed the work.
- If a stop condition occurs, the Runtime should stop and report evidence or blocker state.
