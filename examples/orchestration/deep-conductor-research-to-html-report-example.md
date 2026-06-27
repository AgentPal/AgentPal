# Deep Conductor Research To HTML Report Example

## User Input

```text
Help me research 2026 Agent trends, write a detailed report, and turn it into a polished HTML page.
```

## Memory Used

- User output preference memory may help if approved.
- Prior report routing memory may inform topology, not ownership rules.

## Capability Inventory Read

- Runtime profile: host Runtime candidate for web research and file writing;
- Skill profile candidates: web research Skill, browser Skill, HTML / repo editing Skill if installed;
- Pal profile candidates: Vega, Harper, Atlas, Quinn, Mira.

## Topology Selected

Project Conductor Workflow + staged deliverable judgement + Plan -> Execute -> Verify.

Reason: the goal has research, writing, implementation-shaped HTML, and verification stages. `HTML` does not automatically route to Atlas; implementation owner is selected by current judgement.

## Project Task Map

```yaml
schema: agentpal.project_conductor_task_map.v0.1
project_goal: "Research Agent trends and produce report plus HTML page."
project_state_summary: "No sources or artifact exist yet."
known_constraints:
  - "No private sources."
phases:
  - phase_id: research
    goal: "Collect current source-backed evidence."
    deliverables: ["source inventory", "evidence matrix"]
    tasks:
      - task_id: source-plan
        task_goal: "Create research query and source plan."
        priority: high
        complexity: high
        risk_level: medium
        owner_pal_candidates:
          - pal: Vega
            reason: "Research framing and evidence quality are central."
        runtime_candidates:
          - runtime: Codex
            reason: "May browse or collect sources if available."
            evidence_required: ["current web access or source inputs"]
        runtime_skill_candidates:
          - skill_or_tool: "web research Skill"
            type: "Agent Skill"
            reason: "May reduce source collection cost if installed."
            evidence_required: ["host Runtime confirms availability"]
        pal_owned_skills_used:
          - pal: Vega
            skill_or_method: "source credibility judgement"
            purpose: "Separate facts from inference."
        context_needs:
          index_only: ["capability profiles"]
          full_text: ["selected source summaries after collection"]
          summarize_first: []
          cannot_read: ["private paid sources", "secrets"]
        verification_needs: ["source freshness and citation check"]
        expected_output: "research package"
        status: ready_next_round
  - phase_id: html-artifact
    goal: "Turn accepted report into HTML page."
    deliverables: ["HTML file", "visual verification note"]
    tasks:
      - task_id: html-page-package
        task_goal: "Package accepted report into HTML artifact."
        priority: medium
        complexity: medium
        risk_level: medium
        owner_pal_candidates:
          - pal: Atlas
            reason: "Implementation-shaped artifact may need development ownership after research content exists."
        runtime_candidates:
          - runtime: Codex
            reason: "Can edit files and run local checks when available."
            evidence_required: ["workspace write access"]
        runtime_skill_candidates:
          - skill_or_tool: "browser preview Skill"
            type: "browser"
            reason: "May verify rendered page if installed."
            evidence_required: ["current Runtime confirms browser capability"]
        pal_owned_skills_used: []
        context_needs:
          index_only: []
          full_text: ["accepted report", "HTML requirements"]
          summarize_first: []
          cannot_read: ["research drafts not accepted for implementation"]
        verification_needs: ["render check or not-run reason"]
        expected_output: "HTML page task package"
        status: candidate
next_round_candidates:
  - task_id: source-plan
    reason: "Research evidence must precede writing and HTML."
blocked_items:
  - "Need source collection before report writing."
user_decisions_needed:
  - "Confirm target audience and HTML style."
routing_memory_candidates:
  - summary: "Research-to-HTML used staged research, writing, implementation, verification."
    not_a_fixed_route: true
```

## Context Budget

Use summarize-first for broad sources, full-text only for selected source evidence, and do not forward full research drafts into the HTML stage until accepted.

## Runtime Skill-aware Task Package

Web research, browser, and HTML/repo editing Skills are Runtime-installed candidates only. The host Runtime must prove they are available.

## Verification Plan

- Vega verifies source quality.
- Harper or Morgan may review report clarity if selected by current judgement.
- Atlas packages implementation after accepted content.
- Quinn checks final evidence and not-run items.

## Routing Memory Writeback Candidate

Record stage topology, source quality result, HTML verification result, context counts, and any rework.

## User-facing Explanation

Mira should explain stages and next-round task package. She should not say that research or HTML has been executed before Runtime evidence exists.

## No-Code Boundary Note

This example is a no-code planning example. It does not browse, write HTML, open a browser, or execute Deep Conductor automatically.
