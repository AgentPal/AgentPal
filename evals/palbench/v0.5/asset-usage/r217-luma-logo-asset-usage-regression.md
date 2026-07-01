# R217 Luma Logo Asset Usage Regression

Prompt:

```text
User:
让 Luma 帮我设计 AgentPal logo。
```

## Target Presence

- registered official Luma Pal: absent
- central contacts Luma entry: absent
- controlled fixture used: `evals/palbench/v0.5/asset-usage/r217-fixtures/LumaDesignPal/`

This regression must not claim that a real Luma Pal exists, was upgraded, or
was executed.

## Expected Task Asset Packet

| Field | Expected |
| --- | --- |
| target_pal | LumaDesignPal fixture |
| required_identity_assets | `PAL.md`, `pal.json` |
| required_voice_assets | `identity/voice.md` |
| required_thinking_assets | `knowledge/design-thinking.md` |
| required_workflows | `workflows/logo-workflow.md` |
| required_runtime_policy | `SKILL.md` ImageGen boundary |
| required_eval_assets | `evals/logo-asset-usage-case.md` |
| optional_tools | ImageGen only after visual direction exists |
| go_no_go_decision | `go_asset_grounded` for fixture regression; `blocked_missing_core_asset` if any listed fixture asset is absent |

## Expected Behavior

1. Load persona / voice / design-thinking / logo workflow / skill-map or tool
   boundary / ImageGen policy from fixture assets.
2. Output visual direction before ImageGen.
3. If ImageGen is later used, state that it is only a host execution tool.
4. Output Asset Use Summary with actual fixture paths.
5. If any key asset is missing, produce Missing Asset Plan before visual
   direction.

## Verdict

```text
luma_logo_asset_usage_regression_pass_as_fixture
```
