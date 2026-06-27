# Runtime Skill Browser Check Task Example

## User Input

"Check whether the local report page renders correctly on desktop and mobile."

## Pal-owned Skills Used

- Atlas implementation evidence framing.
- Quinn visual verification criteria.

## Runtime Skill Candidates

- Browser Runtime Skill candidate for screenshots or DOM checks.
- Optional plugin candidate if the host Runtime exposes browser automation through a plugin.

## Availability Check

The Runtime must confirm whether a browser Skill/plugin is installed and available for local targets.

## Runtime Skill-aware Task Package

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
task_id: browser-check-example
user_goal: "Verify local page rendering."
owner_pal:
  name: Quinn
  reason: "The requested deliverable is a verification result."
pal_owned_skills_used:
  - pal: Quinn
    skill_or_method: "evidence-first verification"
    purpose: "Define pass/fail/not-run criteria."
host_runtime_candidate:
  name: "current host Runtime"
  reason: "Only it can confirm browser capability."
runtime_skill_candidates:
  - name: "browser inspection Skill"
    type: "browser"
    reason: "May capture viewport evidence and interaction state."
    required_inputs: ["local URL or file path", "viewport list"]
    evidence_required: ["screenshots", "console/network notes", "viewport sizes"]
plugin_candidates:
  - name: "browser plugin"
    reason: "Candidate only if current Runtime exposes it."
mcp_tool_candidates: []
availability_check_required: true
if_available_use:
  - "Capture required viewport evidence."
if_unavailable_fallback:
  - "Report browser check not-run and provide manual visual checklist."
runtime_skill_usage_reason: "Visual rendering needs current Runtime browser evidence."
allowed_files: ["target page and its assets"]
cannot_read: ["unrelated local files", "private browser profile data"]
execution_steps:
  - "Confirm browser capability."
  - "Open target only if allowed."
  - "Capture desktop and mobile evidence."
verification_requirements:
  - "Report pass/fail/not-run per viewport."
expected_outputs: ["viewport evidence", "issues list", "not-run if browser unavailable"]
final_report_required:
  required: true
runtime_skill_usage_memory_writeback:
  required: true
not_a_fixed_route: true
```

## Verification Plan

Quinn checks whether evidence covers the requested viewports and whether failures remain visible.

## Usage Memory Writeback

Record whether the browser candidate was available and whether screenshot evidence was sufficient.

## Fallback Path

If unavailable, return a manual checklist and mark browser evidence `not-run`.

## No-code Boundary Note

AgentPal does not open the browser itself. The host Runtime does, if available and allowed.
