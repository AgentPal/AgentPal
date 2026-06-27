# Project Conductor Task Map

This template turns a project-level goal into a no-code project map that a host Runtime can use to plan the next round.

The task map is not an automatic execution plan. It does not start tasks, run commands, call external Agents, or create a background project system.

```yaml
schema: agentpal.project_conductor_task_map.v0.1
project_goal: ""
project_state_summary: ""
known_constraints: []
release_or_completion_target: ""
phases:
  - phase_id: ""
    goal: ""
    deliverables: []
    tasks:
      - task_id: ""
        task_goal: ""
        priority: "" # high | medium | low
        complexity: "" # low | medium | high
        risk_level: "" # low | medium | high
        owner_pal_candidates:
          - pal: ""
            reason: ""
        runtime_candidates:
          - runtime: ""
            reason: ""
            evidence_required: []
        runtime_skill_candidates:
          - skill_or_tool: ""
            type: "" # Agent Skill | plugin | MCP | browser | office document | repo analysis | other
            reason: ""
            evidence_required: []
        pal_owned_skills_used:
          - pal: ""
            skill_or_method: ""
            purpose: ""
        context_needs:
          index_only: []
          full_text: []
          summarize_first: []
          cannot_read: []
        verification_needs: []
        expected_output: ""
        status: "" # candidate | ready_next_round | blocked | done | not-run
next_round_candidates:
  - task_id: ""
    reason: ""
blocked_items: []
user_decisions_needed: []
routing_memory_candidates:
  - summary: ""
    not_a_fixed_route: true
```

## Field Rules

- `owner_pal_candidates` are case-specific candidates, not fixed routes.
- `runtime_skill_candidates` are host Runtime Skill / Plugin / MCP candidates.
- `pal_owned_skills_used` are Pal methods, workflows, runbooks, or output contracts.
- `runtime_candidates` are execution-layer candidates, not Pal-layer owners.
- `routing_memory_candidates` are possible future evidence, not route rules.
