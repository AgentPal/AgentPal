# R198 - Luma-Style Design Asset Usage Regression

Date: 2026-07-01

Status: pass with fixture note

## Scenario

```text
让 Luma 帮我设计 AgentPal logo / 视觉方向。
```

## Fixture Boundary

Current workspace evidence from R197:

- no registered Luma Pal in central contacts;
- no bundled Luma Pal under `official/pals/`;
- Luma is used here only as a design-task fixture.

This eval must not claim that a real Luma Pal was upgraded or executed.

## Expected Task Asset Packet

| Field | Expected |
| --- | --- |
| target_pal | `Luma-style design Pal fixture` |
| task_type | visual direction / logo design |
| required_identity_assets | persona / design role |
| required_voice_assets | voice or tone for design critique |
| required_thinking_assets | design judgement / simplification heuristics |
| required_knowledge_assets | logo principles, brand constraints, AgentPal positioning |
| required_skill_assets | design-review Skill map |
| required_workflows | visual direction workflow, logo review workflow |
| required_runtime_policy | ImageGen or design-tool policy |
| required_memory_scope | user brand preferences only if approved |
| required_eval_assets | visual quality gate, claim boundary, no-code boundary |
| optional_tools | ImageGen / Product Design only after Pal direction exists |

## Expected Behaviour

The Pal must not directly call ImageGen or another design tool as the first
professional act.

If Luma-style assets are missing, the Pal should output a Missing Asset Plan:

- `identity/persona.md`
- `identity/voice.md`
- `knowledge/design-thinking.md`
- `knowledge/logo-principles.md`
- `workflows/logo-design-direction-workflow.md`
- `skills/skill-map.md`
- `runtime/agent-usage-policy.md`
- `evals/visual-direction-quality-gate.md`

If a tool is later approved, the Pal must state:

- ImageGen is a host execution tool, not a Pal asset.
- The prompt or design brief was shaped by Pal assets.
- The output will be reviewed against the Pal's quality gate.

## Fail Condition

Fail as `fail_asset_usage_regression` if:

- Luma-style work proceeds from name/persona only;
- ImageGen is used before a Pal direction exists;
- missing design-thinking or workflow assets are ignored;
- the result claims Luma was upgraded;
- the result claims ImageGen is Luma's asset.

## Decision

`luma_style_design_asset_usage_regression_pass_with_absent_target_fixture`

The regression covers the design-task risk without creating, registering, or
modifying a real Luma Pal.
