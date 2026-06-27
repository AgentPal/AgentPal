# Runtime Skill Fallback Package

Use this package when a Runtime Skill, plugin, or MCP candidate is unavailable, fails, returns untrusted output, or cannot be used safely.

```yaml
schema: agentpal.runtime_skill_fallback_package.v0.1
fallback_id: ""
original_task_id: ""
missing_or_failed_candidate:
  name: ""
  type: ""
  status: "" # unavailable | failed | unsafe | untrusted-output | not-run | unknown
what_to_do_if_skill_missing:
  - "Report unavailable or unknown explicitly."
  - "Use ordinary Runtime Task Package if the task can still be completed safely."
  - "Ask the user whether to install/enable a Skill or choose another Runtime when the Skill is essential."
what_to_do_if_skill_execution_fails:
  - "Preserve the failure message or evidence summary."
  - "Do not retry outside the approved scope."
  - "Return a repair or alternate execution package."
what_to_do_if_output_untrusted:
  - "Route output through Pal verification."
  - "Require source, artifact, diff, screenshot, test, or inspection evidence as appropriate."
  - "Mark result partial, fail, blocked, or not-run if evidence is insufficient."
ordinary_task_package_fallback:
  allowed: true
  conditions:
    - "The task can be completed with normal Runtime reads/writes/tools."
    - "Privacy and file boundaries remain valid."
record_failed_usage:
  required: true
  fields:
    - candidate
    - failure_or_unavailable_reason
    - fallback_used
    - verification_result
    - next_time_candidate_guidance
not_a_fixed_route: true
```

Fallback results must keep failure visible. Do not turn unavailable, failed, or unverified Runtime Skill use into a pass.
