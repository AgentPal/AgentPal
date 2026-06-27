# Deep Conductor Project Release Example

## User Input

```text
Mira, help me move this project toward release. First make the overall plan, task split, and next-round execution package.
```

## Memory Used

- project status summary candidate: previous release-readiness notes, if available;
- Routing Memory candidate: prior release checks, not as fixed route;
- memory_used: yes, if current session has approved memory or reports.

## Capability Inventory Read

- runtime profile candidate: Codex or another repo-editing host Runtime;
- reasoning profile candidate: high for release planning;
- Pal profile candidates: Mira, Quinn, Rhea, Atlas, Morgan.

Profiles are judgement inputs only. They do not prove current availability.

## Topology Selected

Project Conductor Workflow + Owner + Verifier.

Reason: release planning is project-level, evidence-heavy, and needs next-round task packages plus verification planning.

## Project Task Map

```yaml
schema: agentpal.project_conductor_task_map.v0.1
project_goal: "Prepare the project for release readiness."
project_state_summary: "Existing docs and release notes need scoped verification."
known_constraints:
  - "No push, tag, or release from this planning example."
phases:
  - phase_id: release-readiness
    goal: "Reach evidence-backed release readiness."
    deliverables:
      - release blocker list
      - verification package
      - next-round Runtime task package
    tasks:
      - task_id: release-doc-audit
        task_goal: "Audit release docs and public boundary language."
        priority: high
        complexity: medium
        risk_level: medium
        owner_pal_candidates:
          - pal: Morgan
            reason: "Document structure and release notes are central."
        runtime_candidates:
          - runtime: Codex
            reason: "Repo file reading and Markdown editing may be needed."
            evidence_required: ["current workspace access"]
        runtime_skill_candidates: []
        pal_owned_skills_used:
          - pal: Quinn
            skill_or_method: "completion evidence review"
            purpose: "Define release acceptance evidence."
        context_needs:
          index_only: ["RESOURCE_INDEX.md"]
          full_text: ["release checklist and changed docs"]
          summarize_first: []
          cannot_read: ["private memory", "secrets"]
        verification_needs:
          - "Quinn or Rhea candidate verifies no-code and release evidence."
        expected_output: "release readiness task package"
        status: ready_next_round
next_round_candidates:
  - task_id: release-doc-audit
    reason: "Highest release blocker discovery value."
blocked_items: []
user_decisions_needed:
  - "Confirm whether publish actions are in scope."
routing_memory_candidates:
  - summary: "Release planning used Project Conductor + Owner/Verifier."
    not_a_fixed_route: true
```

## Context Budget

- index-only: `RESOURCE_INDEX.md`, roadmap index;
- full-text: release checklist, current release notes, changed docs;
- profile_read_count: only profiles needed for release safety and quality;
- memory_used: yes if approved release notes exist.

## Runtime Skill-aware Task Package

Runtime Skill candidates are none by default. If the host Runtime has a repository-analysis Skill, list it as a candidate and require current evidence.

## Verification Plan

- verifier candidate: Quinn for evidence completeness;
- safety candidate: Rhea if runtime or release action risk appears;
- result record: `templates/orchestration/verification-result-record.md`;
- `not-run` required for any skipped release check.

## Routing Memory Writeback Candidate

Record topology, owner candidates, runtime candidate, context counts, verification result, and rework count after actual evidence exists.

## User-facing Explanation

Mira should explain that this is a release planning package, not a release action. The next step is a bounded host Runtime task package.

## No-Code Boundary Note

This example does not push, tag, publish, run a release robot, create a validator, or execute Deep Conductor automatically.
