# Runtime Skill-aware Task Package

This template keeps Pal-owned Skills separate from Runtime-installed Skills.

`runtime_skill_candidates` are installed host Runtime Skill candidates. They may include Agent Skills, plugins, MCP tools, browser tools, office-document tools, repository analysis tools, or other host capabilities. They are candidates, not fixed routes, and must be verified by the current Runtime.

`pal_owned_skills_used` are Pal methods, workflows, runbooks, output contracts, or judgement skills used to prepare the package. They do not execute host tools.

Availability is unknown by default. Set `availability_check_required: true` unless the current host Runtime has already reported that the candidate exists and can be used for this task.

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
task_id: example-task-id
user_goal: ""
owner_pal:
  name: ""
  reason: ""
pal_owned_skills_used:
  - pal: ""
    skill_or_method: ""
    purpose: ""
host_runtime_candidate:
  name: ""
  reason: ""
  availability_evidence_required: true
runtime_skill_candidates:
  - name: ""
    type: "" # Agent Skill | plugin | MCP | browser | office document | repo analysis | other
    reason: ""
    required_inputs: []
    evidence_required: []
plugin_candidates:
  - name: ""
    reason: ""
mcp_tool_candidates:
  - name: ""
    reason: ""
availability_check_required: true
if_available_use:
  - ""
if_unavailable_fallback:
  - ""
runtime_skill_usage_reason: ""
required_inputs: []
allowed_files: []
cannot_read: []
execution_steps:
  - ""
prompt_shaping_notes:
  runtime_notes: ""
  model_notes: ""
  reasoning_notes: ""
  skill_notes: ""
verification_requirements:
  - ""
expected_outputs:
  - ""
final_report_required:
  required: true
  must_include:
    - files_changed_or_read
    - commands_or_tools_used
    - runtime_skills_used_or_not_run
    - availability_check_result
    - fallback_used
    - verification_results
    - blockers
runtime_skill_usage_memory_writeback:
  required: true
  fields:
    - task_type
    - owner_pal
    - host_runtime_candidate
    - runtime_skill_candidates
    - runtime_skills_used
    - availability_confirmed
    - fallback_used
    - pal_owned_skills_used
    - context_read_count
    - profile_read_count
    - memory_used
    - verification_result
    - rework_count
    - notes_for_next_time
not_a_fixed_route: true
```

## Use Rule

Use this template when a task may benefit from a host Runtime Skill, plugin, MCP tool, or special tool surface.

The package must not imply that AgentPal owns, installs, invokes, or verifies the Skill by itself.

The host Runtime performs availability checks and execution. The Pal layer prepares the package, separates capability types, and verifies returned evidence.
