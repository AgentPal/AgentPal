# Runtime Skill Usage Memory Reuse Example

## User Input

```text
Last time Claude Code's document Skill handled a document task well. Can we use that experience this time?
```

## Previous Memory

```yaml
schema: agentpal.runtime_skill_usage_memory_record.v0.1
runtime_id: claude-code
runtime_skill_candidate:
  name: document-skill
  type: Agent Skill
availability_confirmed: true
task_type: "document restructuring"
success: true
verification_result: pass
fallback_used: none
known_limits:
  - "Needed a clear output format."
recommended_prompt_shape:
  - "Provide source summary, target format, and verification requirements."
next_time_candidate_use: "Consider if current Claude Code session confirms the Skill is available."
not_a_fixed_route: true
```

## Current Runtime

Current runtime candidate: Claude Code or another host Runtime with a document Skill candidate.

## Memory Snapshot

The previous Skill result is useful prompt-shaping memory. It is not a Pal-owned Skill and not proof that the Skill is installed now.

## Deep Conductor Decision

Selected topology: Runtime Skill-aware Task Package.

Reason: a host Runtime Skill may reduce document handling risk, but Pal Skill and Runtime Skill layers must remain separate.

## Task Package

```yaml
schema: agentpal.runtime_skill_aware_task_package.v0.1
availability_check_required: true
runtime_skill_candidates:
  - name: document-skill
    type: Agent Skill
    reason: "Previous verified Runtime Skill Usage Memory suggests it may help."
    evidence_required:
      - "current Skill availability"
pal_owned_skills_used:
  - pal: Morgan
    skill_or_method: "document judgement method"
    purpose: "shape document task requirements"
if_unavailable_fallback:
  - "Use ordinary document task package or ask user to choose a document-capable Runtime."
verification_requirements:
  - "Verify output against the current source and requested format."
runtime_skill_usage_memory_writeback:
  required: true
not_a_fixed_route: true
```

## Verification Plan

- If the Skill is unavailable, mark `not-run`.
- If used, report input summary, output summary, artifact evidence, and verification result.
- Do not say Morgan or any Pal executed the host Skill.
- Availability and verification are separate. An available Skill can still produce a failed or partial result.

## Memory Writeback Candidate

Create or update Runtime Skill Usage Memory after evidence exists. Include availability, success/failure, verification result, fallback used, privacy notes, and `not_a_fixed_route: true`.

## No-Code Boundary Note

Runtime Skill Usage Memory records experience. It does not install or invoke the Skill.
