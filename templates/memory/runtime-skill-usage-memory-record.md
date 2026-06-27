# Runtime Skill Usage Memory Record

This template records observed use of a host Runtime Skill, plugin, MCP tool, or similar capability.

The Skill belongs to the host Runtime. A Pal may record usage experience, but the Pal does not own, install, or execute the Skill.

```yaml
schema: agentpal.runtime_skill_usage_memory_record.v0.1
usage_id: ""
created_at: ""
runtime_id: ""
runtime_skill_candidate:
  name: ""
  type: "" # Agent Skill | plugin | MCP | browser | office document | repo analysis | other
availability_confirmed: "" # true | false | unknown | not-run
task_type: ""
input_summary: ""
output_summary: ""
success: "" # true | false | partial | not-run | unknown
verification_result: "" # pass | fail | partial | not-run | blocked
fallback_used: "" # none | ordinary-task-package | alternate-candidate | user-confirmation | blocked | unknown
known_limits:
  - ""
risk_notes:
  - ""
recommended_prompt_shape:
  - ""
next_time_candidate_use: ""
not_a_fixed_route: true
privacy_notes:
  public_safe: false
  private_inputs_excluded: true
  credentials_excluded: true
  local_paths_excluded: true
```

## Rules

- Record current evidence, not assumptions.
- Do not treat previous Skill availability as proof that the current Runtime has the Skill.
- Do not put Runtime-installed Skills under Pal-owned Skills.
- Keep future use as `candidate` guidance only.
- Record both availability and verification. A Skill can be available but still fail verification.
- If fallback was used, record the fallback path and keep the original Skill result visible.
