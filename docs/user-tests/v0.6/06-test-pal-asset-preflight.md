# 06 Test Pal Asset Preflight

## Goal

Verify that a Pal uses its assets before substantive work.

## Prompt

```text
请让合适的 Pal 帮我设计一段面向第一批 AgentPal 测试用户的邀请说明。回答前请说明这个 Pal 使用了哪些人格、语气、思维方式、知识、Skill、Workflow、Memory 或模型配置资产。
```

## Expected Result

The selected owner Pal should:

- State why it owns the task.
- Name relevant assets.
- Produce a Task Asset Packet or compact Asset Preflight.
- Distinguish Pal assets from tools.
- Use the assets to shape the answer.
- Output an Asset Use Summary or equivalent.

## Tool Boundary

Tools are execution layer, not Pal capability assets.

Correct chain:

```text
Pal asset judgement -> decide method/tool if needed -> execute -> verify with Pal quality criteria
```

## Fail Signals

- The answer only uses a Pal name and generic model writing.
- The answer says a tool was used and treats that as Pal capability.
- The answer directly calls a tool before asset judgement.
- No missing-asset fallback appears when assets are unavailable.
