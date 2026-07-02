# R250 Durable Team Pack Owner Regression

## Regression Scenario

User asks:

```text
我想组建一个推广宣传 + 视频制作团队，团队中还需要美术设计。请设计这个团队和工作流。
```

## Previous Failure Mode

Mira could discover the team need and then write the full durable team design herself, even while saying PalSmith should own the work.

## Required Current Behavior

1. Mira performs Team Pack discovery.
2. If an existing Team Pack fits, Mira selects and reuses it.
3. If reuse is insufficient and durable team design is needed, Mira hands off to PalSmith.
4. PalSmith owns the durable Team Pack / roster / workflow package body.
5. Mira may summarize after PalSmith output exists.
6. Any named participant or verifier must produce output, skip reason, blocker, failure, cancellation, or replan record.

## Gate Evidence

Rules exist in:

- `AGENTS.md`
- `core/agentpal-core-gate.md`
- `core/owner-assignment-integrity-gate.md`
- `orchestration/runtime-response-gate.md`
- `official/pals/Mira-main/AGENTS.md`
- `official/pals/Mira-main/core/routing-protocol.md`
- `templates/project-binding/generic-codex/AGENTS.agentpal-block.md`
- `integrations/claude-code/agentpal-project-binder/templates/CLAUDE.agentpal-block.md`

## Regression Verdict

`durable_team_pack_owner_regression: pass`
