# Runtime Skill-aware Task Package Self-Test

## Purpose

Verify that Runtime Skill-aware packages separate host Runtime capabilities from Pal methods.

## Pass Criteria

- Required YAML fields are present: `schema`, `task_id`, `user_goal`, `owner_pal`, `pal_owned_skills_used`, `host_runtime_candidate`, `runtime_skill_candidates`, `plugin_candidates`, `mcp_tool_candidates`, `availability_check_required`, `if_available_use`, `if_unavailable_fallback`, `runtime_skill_usage_reason`, `required_inputs`, `allowed_files`, `cannot_read`, `execution_steps`, `prompt_shaping_notes`, `verification_requirements`, `expected_outputs`, `final_report_required`, `runtime_skill_usage_memory_writeback`, and `not_a_fixed_route: true`.
- `runtime_skill_candidates` are installed host Skill candidates, not Pal methods.
- `pal_owned_skills_used` are Pal methods, workflows, runbooks, or output contracts.
- Availability is checked by the host Runtime unless current evidence already exists.
- Fallback is explicit before execution.
- Candidate wording remains non-binding.
- Verification requirements name evidence and `not-run` reporting.
- No fixed route or keyword route is introduced.
- No internal path or private project data appears.

## Fail Criteria

- The package implies AgentPal installs or invokes Runtime Skills.
- The package omits final report or Runtime Skill Usage Memory writeback requirements.
- The package accepts Runtime Skill output without verification.
