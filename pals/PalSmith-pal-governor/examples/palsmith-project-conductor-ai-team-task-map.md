# PalSmith Project Conductor AI Team Task Map Example

## User Input

```text
PalSmith, design an AI team for a product launch project and prepare the first build package.
```

## Project Conductor Task Map

```yaml
schema: agentpal.project_conductor_task_map.v0.1
project_goal: "Create a no-code AI team for a product launch project."
project_state_summary: "No team assets created yet."
known_constraints:
  - "Do not install Pals or update contacts automatically."
phases:
  - phase_id: team-design
    goal: "Design team roles and Pal candidates."
    deliverables:
      - AI team blueprint
      - first build package
    tasks:
      - task_id: role-model
        task_goal: "Define launch team responsibilities and needed Pal candidates."
        priority: high
        complexity: medium
        risk_level: medium
        owner_pal_candidates:
          - pal: PalSmith
            reason: "Pal asset governance and AI team creation are central."
          - pal: Mira
            reason: "Team conductor summary may be needed."
        runtime_candidates:
          - runtime: current host Runtime
            reason: "May create files only after user approval."
            evidence_required: ["workspace write permission"]
        runtime_skill_candidates: []
        pal_owned_skills_used:
          - pal: PalSmith
            skill_or_method: "AI team creation workflow"
            purpose: "Structure Pal roles and readiness checks."
        context_needs:
          index_only: ["contacts", "registry"]
          full_text: ["PalSmith task-package examples"]
          summarize_first: []
          cannot_read: ["private memory", "secrets", "unapproved imports"]
        verification_needs:
          - "PalSmith readiness review"
          - "Quinn evidence review candidate if files are created"
        expected_output: "next-round Runtime task package"
        status: ready_next_round
next_round_candidates:
  - task_id: role-model
    reason: "Needed before file creation."
blocked_items: []
user_decisions_needed:
  - "Confirm team scope and whether Runtime may create files."
routing_memory_candidates:
  - summary: "AI team creation used Project Conductor and PalSmith governance."
    not_a_fixed_route: true
```

## Boundary

PalSmith does not execute Runtime Skills, install Pals, or update contacts. It generates the no-code task map and Task Package for the host Runtime.
