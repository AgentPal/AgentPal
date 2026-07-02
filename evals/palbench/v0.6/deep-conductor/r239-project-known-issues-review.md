# R239 Project Known Issues Review

## Source File

```yaml
source_path: docs/project-known-issues.md
git_status_before_r239: untracked
git_diff_before_r239: none
classification: case_a_deep_conductor_known_issue
```

## Classification Reason

The file records one issue:

```text
Owner 判断正确但未真正 handoff
```

This is directly related to R238 DeepConductor closure because it describes fake handoff / owner assignment integrity:

- Mira judges that PalSmith should own a Team Pack creation task.
- Mira continues writing the PalSmith-owned professional body.
- The selected owner does not actually speak or produce an output record.
- Workflow Execution Contract / Closure Gate could miss the fake handoff if not checked.

## Handling Decision

```yaml
handling: moved_into_r239_evidence
new_evidence_path: evals/palbench/v0.6/deep-conductor/r239-project-known-issues-review.md
docs_project_known_issues_md_after_r239: removed_from_main_docs
reason: >
  The issue is not a general public docs page. It is DeepConductor / Owner
  Assignment Integrity evidence and should live with the R239 closure evidence.
```

## Closure Status

```yaml
issue_id: KI-2026-07-02-01
issue_summary: "Mira can assign PalSmith but continue writing PalSmith's work body"
closed_by:
  - core/owner-assignment-integrity-gate.md
  - AGENTS.md Runtime Response Gate order
  - core/agentpal-core-gate.md owner assignment integrity line
  - orchestration/runtime-response-gate.md Owner Assignment Integrity Gate section
  - templates/orchestration/workflow-execution-contract.md assignment_integrity block
  - evals/palbench/v0.6/deep-conductor/r238-closure-gate-result.md
  - evals/palbench/v0.6/deep-conductor/r239-focused-deep-conductor-closure-regression.md
status_after_r239: closed_for_deep_conductor_user_test
residual_risk: >
  Future fresh host sessions still need ordinary runtime regression, but the
  core no-code gate and evidence trace now define fake handoff as a Closure Gate
  failure.
```

## Original Issue Content Summary

```yaml
expected_behavior:
  - Mira completes intake and Team Pack discovery.
  - If owner is PalSmith, Mira immediately hands off.
  - PalSmith speaks in the same response and owns team design / roster / open_roles / WEC / Closure Gate.
  - Faye can only be a workflow framing consultant and must exit after workflow definition.
repair_direction:
  - tighten Mira owner-routing / handoff entry
  - add same-response owner appearance check
  - add fake handoff regression check
```
