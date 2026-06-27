# Runtime Skill Fallback Example

## User Input

"Use the browser Skill to verify this page."

## Pal-owned Skills Used

- Quinn not-run and evidence review.
- Rhea runtime boundary review.

## Runtime Skill Candidates

- Browser Skill candidate.

## Availability Check

The current Runtime reports: browser Skill unavailable.

## Runtime Skill-aware Task Package

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
task_id: runtime-skill-fallback-example
user_goal: "Verify page rendering."
owner_pal:
  name: Quinn
  reason: "The deliverable is a verification report."
pal_owned_skills_used:
  - pal: Quinn
    skill_or_method: "not-run handling"
    purpose: "Preserve the unavailable check honestly."
host_runtime_candidate:
  name: "current host Runtime"
  reason: "It reported browser Skill unavailable."
runtime_skill_candidates:
  - name: "browser Skill"
    type: "browser"
    reason: "Candidate requested by user."
    required_inputs: ["target URL"]
    evidence_required: ["availability result", "screenshots if available"]
plugin_candidates: []
mcp_tool_candidates: []
availability_check_required: true
if_available_use:
  - "Capture viewport evidence."
if_unavailable_fallback:
  - "Mark browser evidence not-run."
  - "Provide manual checklist or ask user to choose a browser-capable Runtime."
runtime_skill_usage_reason: "User requested browser verification."
allowed_files: ["target page assets if local and approved"]
cannot_read: ["unrelated local files"]
execution_steps:
  - "Use fallback package because browser Skill is unavailable."
verification_requirements:
  - "Do not claim visual pass without browser evidence."
expected_outputs: ["not-run browser evidence", "manual checklist", "next action"]
final_report_required:
  required: true
runtime_skill_usage_memory_writeback:
  required: true
not_a_fixed_route: true
```

## Verification Plan

Quinn returns `not-run` for browser evidence and does not turn the fallback checklist into a pass.

## Usage Memory Writeback

Record `availability_confirmed: false`, `success: not-run`, `fallback_used: user-confirmation`, and `not_a_fixed_route: true`.

## Fallback Path

Ask whether the user wants to run the check in a browser-capable Runtime or accept a manual checklist.

## No-code Boundary Note

AgentPal does not emulate a missing browser Skill.
