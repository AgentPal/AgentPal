# Deep Conductor Cross-Runtime Continuation Example

## User Input

```text
This project had one round in Codex. I want to continue in Claude Code with the same Pal.
```

## Memory Used

- Pal memory: prior project goal and accepted direction;
- project state: last known task map or completion report;
- Routing Memory: prior Runtime result candidate;
- Runtime Skill usage memory: prior Skill result, if recorded.

## Capability Inventory Read

- Codex runtime profile as previous Runtime evidence;
- Claude Code runtime profile as current target Runtime candidate;
- cross-runtime memory protocol;
- relevant Pal profile.

## Topology Selected

Project Conductor Workflow + Cross-runtime continuation package.

Reason: the Runtime changes, but Pal memory and project continuity should continue.

## Deep Conductor Plan

```yaml
schema: agentpal.deep_conductor_plan.v0.1
user_goal: "Continue the same project in Claude Code."
task_kind: continuation
project_or_single_task: project
memory_used:
  used: true
  sources:
    - "approved Pal memory"
    - "previous routing result candidate"
  freshness_or_risk_notes:
    - "Current Claude Code capability must be verified fresh."
capabilities_read:
  profile_read_count: 2
  profiles:
    - "previous Runtime result"
    - "Claude Code runtime profile candidate"
topology_selected: "Project Conductor cross-runtime continuation"
topology_reason: "Runtime changed; Pal continuity and next-round package are needed."
alternatives_rejected:
  - topology: "Assume Codex state applies directly"
    reason: "Runtime-specific state cannot be assumed current."
context_budget:
  context_read_count: 3
  index_only_sources: ["project file index"]
  full_text_sources: ["last accepted summary", "current project binding"]
  summarize_first_sources: []
  cannot_read: ["private memory without approval", "secrets"]
task_packages:
  - package_id: claude-code-continuation-package
    owner_pal_candidate: Mira
    runtime_candidate: Claude Code
    runtime_skill_candidates: []
    template: "templates/orchestration/next-round-runtime-task-package.md"
verification_plan:
  verifier_candidates: ["Quinn if completion evidence is reviewed"]
  evidence_required: ["Claude Code can read project and AgentPal workspace"]
  result_record: "templates/orchestration/verification-result-record.md"
routing_memory_writeback:
  write_candidate: true
  not_a_fixed_route: true
user_explanation: "Pal memory continues, Runtime state is refreshed."
```

## Context Budget

Read previous accepted summaries and current project binding. Do not copy full Codex chat history into Claude Code.

## Runtime Skill-aware Task Package

Claude Code Skill candidates are listed only after Claude Code confirms availability. Prior Codex Skill success is not proof of Claude Code availability.

## Verification Plan

- verify Claude Code can read required AgentPal core gates and project files;
- verify Pal memory continuity source;
- report missing or stale memory as `not-run` or `unknown`.

## Routing Memory Writeback Candidate

Record whether cross-runtime continuation worked, what had to be refreshed, and what current Runtime evidence was required.

## User-facing Explanation

Mira should say the same Pal can continue the project, but Claude Code must verify current access and available Skills.

## No-Code Boundary Note

This example does not migrate data automatically, create a database, run Claude Code, or call external Agents.
