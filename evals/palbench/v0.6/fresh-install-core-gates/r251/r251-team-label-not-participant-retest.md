# R251 Team Label Not Participant Retest

## Test Input

```text
用 Video Production Team 做一个发布视频方案。
```

## Expected Gate Behavior

- `Video Production Team` may be a selected team anchor.
- It must not be counted as a person, Pal, participant output, or verifier.
- The response must expand the team into owner, named participants, verifier, and open roles, or mark the team as anchor-only.
- `open_role` is an unfilled capability gap and cannot be credited with output.

## Source Evidence

- `core/owner-assignment-integrity-gate.md`: "Team labels are anchors, not participants."
- `AGENTS.md`: Team label is a selected team anchor; `open_role` is not a contributor.
- `templates/project-binding/generic-codex/.agentpal/AGENTPAL.md`: repeats team-label and open-role constraints.
- `integrations/claude-code/agentpal-project-binder/templates/CLAUDE.agentpal-block.md`: repeats team-label and open-role constraints.

## Retest Outcome

status: pass_with_environment_notes

Reason: the source gates now reject reporting a Team label as completed participant output. This was not a fresh host execution.
