# Deep Conductor PalSmith AI Team Build Example

## User Input

```text
PalSmith, help me design an AI team for a product launch project and prepare the first build package.
```

## Memory Used

- PalSmith may use public-safe Pal creation preferences if approved.
- Routing Memory may inform useful Pal team patterns but cannot decide the team by rule.

## Capability Inventory Read

- Pal profiles: Mira, PalSmith, Nova, Vega, Atlas, Quinn, Harper, Morgan, Rhea;
- runtime profile: current host Runtime candidate for file creation;
- Runtime Skill candidates: repository analysis or document Skill only if available.

## Topology Selected

Project Conductor Workflow with PalSmith as Pal asset governance owner candidate and Mira as conductor candidate.

## Deep Conductor Plan

```yaml
schema: agentpal.deep_conductor_plan.v0.1
user_goal: "Design an AI team for a product launch project."
task_kind: project_level
project_or_single_task: project
memory_used:
  used: true
  sources: ["approved Pal creation preferences"]
capabilities_read:
  profile_read_count: 3
  profiles: ["pal profiles", "runtime profile", "reasoning profile"]
topology_selected: "Project Conductor + PalSmith asset governance"
topology_reason: "The output is an AI team plan plus next-round creation package."
alternatives_rejected:
  - topology: "Fast Route only"
    reason: "The goal includes multiple Pal roles and governance checks."
context_budget:
  context_read_count: 4
  index_only_sources: ["contacts / registry"]
  full_text_sources: ["PalSmith PAL and output guidance"]
  summarize_first_sources: []
  cannot_read: ["private memory", "unapproved imported assets"]
task_packages:
  - package_id: palsmith-team-build-next-round
    owner_pal_candidate: PalSmith
    runtime_candidate: Codex
    runtime_skill_candidates: []
    template: "templates/orchestration/next-round-runtime-task-package.md"
verification_plan:
  verifier_candidates: ["Quinn for readiness evidence", "Rhea for no-code boundary"]
  evidence_required: ["created files list", "Pal Pack checklist", "no private memory in public assets"]
  result_record: "templates/orchestration/verification-result-record.md"
routing_memory_writeback:
  write_candidate: true
  not_a_fixed_route: true
user_explanation: "This creates a no-code team build package, not files yet."
```

## Context Budget

Read only PalSmith assets, contacts/registry, selected Pal profiles, and the requested user goal. Do not load all Pal Packs.

## Runtime Skill-aware Task Package

If the host Runtime has a document generation or repository Skill, it may be listed under `runtime_skill_candidates`. PalSmith does not execute that Skill.

## Verification Plan

- PalSmith checks Pal Pack completeness and team coherence.
- Quinn checks readiness evidence.
- Rhea checks no-code and public/private boundary if public assets are produced.

## Routing Memory Writeback Candidate

Record which team topology was useful after user acceptance or verification evidence exists.

## User-facing Explanation

PalSmith should explain the proposed team, why each Pal candidate exists, what the host Runtime should create next, and what remains user decision.

## No-Code Boundary Note

This example generates a project conductor task map and next-round task package. It does not install Pals, run imports, execute Runtime Skills, or update contacts automatically.
