# Runtime Skill Repo Analysis Task Example

## User Input

"Analyze this repository and tell me which files are most relevant to the failing auth flow."

## Pal-owned Skills Used

- Atlas repository task framing.
- Rhea file-boundary safety notes when local inspection is involved.

## Runtime Skill Candidates

- Repository analysis Skill candidate.
- Search/tooling available in the host Runtime as ordinary capability.

## Availability Check

Ask the Runtime whether a repo-analysis Skill is installed. If unknown, use ordinary bounded file search.

## Runtime Skill-aware Task Package

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
task_id: repo-analysis-example
user_goal: "Find relevant files for a failing auth flow."
owner_pal:
  name: Atlas
  reason: "The deliverable is engineering analysis and task scoping."
pal_owned_skills_used:
  - pal: Atlas
    skill_or_method: "repository handoff judgement"
    purpose: "Define read scope and evidence needs."
host_runtime_candidate:
  name: "current host Runtime"
  reason: "It can inspect the repository and report evidence."
runtime_skill_candidates:
  - name: "repo-analysis Skill"
    type: "repo analysis"
    reason: "May speed up graph or symbol navigation if installed."
    required_inputs: ["repo root", "auth-flow symptoms"]
    evidence_required: ["files inspected", "why each file is relevant", "unknown areas"]
plugin_candidates: []
mcp_tool_candidates: []
availability_check_required: true
if_available_use:
  - "Use only within the repository root and requested feature scope."
if_unavailable_fallback:
  - "Use ordinary bounded Runtime search and report read counts."
runtime_skill_usage_reason: "Repo-analysis may reduce context waste but is not required."
allowed_files: ["repo files relevant to auth flow"]
cannot_read: ["secrets", "unrelated private directories", "external project roots"]
execution_steps:
  - "Confirm candidate availability."
  - "Inspect bounded auth-related paths."
  - "Return relevance map with evidence."
verification_requirements:
  - "Do not claim full-repo certainty if only a slice was read."
expected_outputs: ["file relevance table", "content_read_count", "gaps"]
final_report_required:
  required: true
runtime_skill_usage_memory_writeback:
  required: true
not_a_fixed_route: true
```

## Verification Plan

Atlas checks that the relevance map is tied to actual files read. Quinn may review if a quality gate is needed.

## Usage Memory Writeback

Record whether repo-analysis helped, failed, or was bypassed by ordinary search.

## Fallback Path

Use ordinary `rg`/file reads or equivalent Runtime search with a strict read budget.

## No-code Boundary Note

AgentPal does not scan repositories automatically. It packages a bounded analysis request.
