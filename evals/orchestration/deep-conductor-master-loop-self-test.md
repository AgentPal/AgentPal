# Deep Conductor Master Loop Self-Test

## Purpose

Verify the Deep Conductor 12-step loop, project-level usability, and no-executor boundary.

## Input

```text
Mira, help me move this project toward release. First make the overall plan, task split, and next-round execution package.
```

## Pass Criteria

- The response uses the 12 operational steps: Goal Intake; Project / Pal Memory Loading; Deliverable and Stage Judgement; Capability Inventory Read; Runtime Skill / Plugin / MCP Awareness; Workflow Topology Selection; Context Access Planning; Prompt Shaping and Token Budgeting; Runtime Task Package Generation; Verification Planning; Synthesis and User-facing Explanation; Routing Memory Writeback Candidate.
- The response states whether this is a project-level goal or a single task.
- Capability Inventory read or honest fallback is present.
- Runtime Skill candidates and Pal-owned Skills are separated.
- Context budget includes `context_read_count`, `profile_read_count`, and `memory_used`.
- Verification plan includes evidence requirements and result-record shape.
- Routing Memory writeback candidate is present and marked not a fixed route.
- Deep Conductor is not described as an executor.
- No internal path or private project data appears.

## Fail Criteria

- Deep Conductor claims to automatically run agents, Runtimes, Skills, tools, or commands.
- Deep Conductor is treated as a service, daemon, database, project bot, or automation runtime.
- The response hardcodes owner Pal routes or `HTML -> Atlas`.
