# R250 Team Label Not Participant Regression

## Regression Scenario

A response names:

```text
selected_team: video-production-team
assignee: Video Production Team
```

and then treats that Team label as if it produced human / Pal output.

## Required Current Behavior

- `selected_team` may name the Team Pack anchor.
- The Team label itself is not a person, Pal, participant output, verifier, or human contributor.
- The Team must be expanded into owner, participants, verifier, and open roles, or marked as anchor-only.
- `open_role` must be recorded as an unfilled gap and cannot be credited with output.

## Evidence

The phrase `Team label is not participant` is now an explicit Claude Code binder runtime anchor, and equivalent language appears in:

- `core/owner-assignment-integrity-gate.md`
- `orchestration/runtime-response-gate.md`
- `templates/project-binding/claude-code/.agentpal/AGENTPAL.md`
- `templates/project-binding/generic-codex/.agentpal/AGENTPAL.md`
- `plugins/codex/plugins/agentpal/skills/agentpal-enable/SKILL.md`
- `integrations/claude-code/agentpal-project-binder/scripts/agentpal_binding.py`
- `integrations/claude-code/agentpal-project-binder/references/status-model.md`

## Regression Verdict

`team_label_not_participant_regression: pass`
