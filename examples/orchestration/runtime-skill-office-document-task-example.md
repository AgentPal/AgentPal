# Runtime Skill Office Document Task Example

## User Input

"Please turn this approved Markdown outline into a polished Word document and PDF."

## Pal-owned Skills Used

- Morgan document planning and source-preservation judgement.
- Quinn evidence criteria for exported artifacts.

These are Pal-owned methods. They do not perform Office conversion.

## Runtime Skill Candidates

- `office-document` Runtime Skill candidate: create or render `.docx` / `.pdf` if the host Runtime has such a Skill.
- `filesystem` ordinary Runtime capability: read allowed source files and write approved outputs.

## Availability Check

Use `templates/orchestration/runtime-skill-availability-check-package.md` and ask the host Runtime to report whether an office-document Skill is installed and usable for this task.

## Runtime Skill-aware Task Package

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
task_id: office-document-output-example
user_goal: "Create approved document outputs from a source outline."
owner_pal:
  name: Morgan
  reason: "Document structure, source preservation, and output review are the main stage."
pal_owned_skills_used:
  - pal: Morgan
    skill_or_method: "document workflow judgement"
    purpose: "Define layout, source handling, and review requirements."
host_runtime_candidate:
  name: "current host Runtime"
  reason: "Only the Runtime can confirm and use installed document Skills."
runtime_skill_candidates:
  - name: "office-document Skill"
    type: "office document"
    reason: "May render or export the requested Office/PDF outputs."
    required_inputs: ["approved Markdown source", "output filename"]
    evidence_required: ["output paths", "render/export result", "not-run if unavailable"]
plugin_candidates: []
mcp_tool_candidates: []
availability_check_required: true
if_available_use:
  - "Use within the approved source/output paths only."
if_unavailable_fallback:
  - "Prepare a normal document task package or ask user to choose a Runtime with document support."
runtime_skill_usage_reason: "Document output benefits from host document rendering if available."
allowed_files: ["approved source files", "approved output directory"]
cannot_read: ["private unrelated documents", "credentials", "unapproved folders"]
execution_steps:
  - "Confirm availability."
  - "Generate outputs only from approved source."
  - "Return artifact paths and export evidence."
verification_requirements:
  - "Morgan checks structure and source preservation."
  - "Quinn checks evidence completeness if selected."
expected_outputs: ["docx path", "pdf path", "artifact summary"]
final_report_required:
  required: true
runtime_skill_usage_memory_writeback:
  required: true
not_a_fixed_route: true
```

## Verification Plan

Check that the artifacts exist, preserve the source outline, and have reported render/export evidence. If rendering was not run, report `not-run`.

## Usage Memory Writeback

Record availability, success or failure, verification result, fallback used, and next-time candidate guidance without private paths.

## Fallback Path

If the office-document Skill is unavailable, produce a Markdown-only output package or ask the user whether to enable a document-capable Runtime.

## No-code Boundary Note

AgentPal does not provide an Office converter. It only prepares the no-code package and verifies evidence.
