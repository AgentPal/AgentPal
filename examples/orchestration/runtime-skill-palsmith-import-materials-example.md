# Runtime Skill PalSmith Import Materials Example

## User Input

"Use my uploaded notes to create a draft Pal knowledge set."

## Pal-owned Skills Used

- PalSmith material ingestion and content-preservation judgement.
- Rhea privacy boundary review when source material is sensitive.

## Runtime Skill Candidates

- Document/PDF extraction Skill candidate.
- OCR candidate only if source material requires it and the Runtime confirms support.

## Availability Check

The Runtime must confirm which extraction capability is available before reading or transforming user materials.

## Runtime Skill-aware Task Package

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
task_id: palsmith-import-materials-example
user_goal: "Prepare a draft Pal knowledge set from user-provided notes."
owner_pal:
  name: PalSmith
  reason: "The deliverable is Pal asset governance and material ingestion planning."
pal_owned_skills_used:
  - pal: PalSmith
    skill_or_method: "user material ingestion"
    purpose: "Preserve source meaning and public/private boundaries."
host_runtime_candidate:
  name: "current host Runtime"
  reason: "Only it can read uploaded files and use extraction Skills."
runtime_skill_candidates:
  - name: "document extraction Skill"
    type: "office document"
    reason: "May extract source text or structure from user-provided files."
    required_inputs: ["approved uploaded files"]
    evidence_required: ["files read", "extraction summary", "failed pages if any"]
plugin_candidates: []
mcp_tool_candidates: []
availability_check_required: true
if_available_use:
  - "Extract only approved user-provided files."
if_unavailable_fallback:
  - "Ask user for plain-text/Markdown source or prepare a manual ingestion checklist."
runtime_skill_usage_reason: "Source extraction may reduce user copy/paste, but privacy comes first."
allowed_files: ["explicitly approved source files"]
cannot_read: ["private memory", "unapproved project files", "credentials"]
execution_steps:
  - "Confirm extraction capability."
  - "Read only approved files."
  - "Return source inventory and extraction notes."
verification_requirements:
  - "PalSmith checks content preservation and public/private split."
expected_outputs: ["source inventory", "draft knowledge sections", "privacy notes"]
final_report_required:
  required: true
runtime_skill_usage_memory_writeback:
  required: true
not_a_fixed_route: true
```

## Verification Plan

PalSmith checks whether source meaning was preserved and whether private material stayed out of public assets.

## Usage Memory Writeback

Record extraction quality, privacy limits, fallback used, and next-time candidate guidance.

## Fallback Path

Ask the user for Markdown/plain text or create a manual source inventory template.

## No-code Boundary Note

PalSmith is not an importer or extractor. It prepares and reviews the ingestion package.
