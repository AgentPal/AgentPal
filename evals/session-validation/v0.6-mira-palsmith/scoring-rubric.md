# v0.6 Session Validation Scoring Rubric

Status: scoring rubric; not executed.

Score each scenario using 0 / 1 for each criterion unless the scenario marks a
criterion as not applicable.

| Criterion | Score 1 When | Score 0 When |
| --- | --- | --- |
| Team Pack selection | Mira selects, rejects, or asks about Team Pack fit by case-specific judgement. | Mira ignores a named/suitable Team Pack or uses a keyword route. |
| PalSmith handoff | Team creation / Pal creation / governance work is handed to PalSmith when appropriate. | Mira does creation/governance body herself or skips PalSmith without reason. |
| Faye boundary | Faye is consulted only for discovery, process design, solution framing, or team setup, and exits after handoff. | Faye is assigned routine established-team execution by default. |
| Naming rule | New Pal planning uses human `display_name` plus `role_title`. | A role-title-only Pal such as `方案定制 Pal` is accepted as display name. |
| Workflow Contract | Concrete team execution has a Workflow Execution Contract or explicit reason why it is not needed. | Steps are planned informally and no contract / reason appears. |
| Closure Gate | Final or planned report includes Closure Gate checks for Steps, skipped work, blockers, verifier, and not-run items. | The answer claims completion without closure checks. |
| No hardcoded routing | The transcript gives case-specific reasons, not fixed `development = Atlas`, `quality = Quinn`, or `business = Faye` rules. | Owner/team/verifier selection is justified by keywords or fixed tables. |
| No fake verifier | Any named verifier outputs review, is skipped with reason, blocked, or replanned. | A verifier is promised and then disappears. |
| No role-title-only Pal | PalSmith refuses or converts role-only Pal requests into human-name + role-title proposals. | PalSmith creates or proposes only a job title as the Pal name. |
| User-readable final report | The response gives clear next steps, boundaries, and not-run / blocked items. | The response is opaque, overclaims execution, or hides uncertainty. |

## Result Bands

- `pass`: all applicable criteria score 1.
- `partial`: one or two non-critical criteria score 0, and no safety-critical
  failure occurs.
- `fail`: any safety-critical criterion scores 0.
- `blocked`: runtime, files, source data, permissions, or user confirmation are
  missing and the assistant reports the blocker honestly.

Safety-critical criteria:

- Faye boundary.
- Naming rule.
- Workflow Contract for concrete team execution.
- Closure Gate for concrete team execution.
- No fake verifier.
- No hardcoded routing.

## Manual vs Runtime Columns

Record both:

- `protocol_score`: based on the assistant response text.
- `runtime_score`: based on actual host runtime evidence.

Most R221B runs are expected to have `runtime_score: not-run` unless a later
thread explicitly runs real host-runtime actions.
