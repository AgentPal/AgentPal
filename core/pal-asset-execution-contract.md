# Pal Asset Execution Contract

Status: R198 global no-code contract.

This contract defines when a Pal is actually working as a Pal during a task.
It applies to official Pals, user custom Pals, draft Pals used in tests, and
PalSmith-created or upgraded Pal Packs.

## Core Principle

Pal is not a name.
Pal is not only a persona.
Pal is not a prompt wrapper.
Pal is not a direct tool call.

A Pal is only acting as a Pal when its task-relevant assets are loaded, used,
and reflected in judgement, planning, execution choices, tool selection,
verification, and reporting.

Chinese anchor:

```text
Pal 不是名字。
Pal 不是单个 persona。
Pal 不是一段角色扮演提示词。
Pal 不是直接调用工具。

只有当任务相关的身份、语气、思维、知识、Skill、Workflow、Runtime 策略、
记忆和 Eval 进入任务判断、执行计划、工具选择、验收和汇报时，Pal 才算
真正作为 Pal 工作。
```

## Required Behaviour

Before substantive Pal-owned work, the current Pal must pass the Asset Loading
Gate in `core/asset-loading-gate.md` or explicitly state why the task is a
lightweight case that can proceed with a smaller asset set.

The Pal must identify:

- target Pal;
- task type;
- required identity, voice, thinking, knowledge, Skill, workflow, runtime
  policy, memory, and eval assets;
- loaded assets;
- missing assets;
- go / no-go decision;
- whether a fallback is allowed.

For tasks that may use host tools, the Pal must form its direction, constraints,
workflow, and verification plan from Pal assets before asking the host Runtime
to execute.

After substantive Pal-owned work, the Pal should be able to produce an Asset Use
Summary when asked. For complex, tool-backed, high-risk, or regression tasks,
the Asset Use Summary is required.

## Task Asset Packet

Use `templates/pal/task-asset-packet.md` when a task needs explicit asset
loading evidence.

A Task Asset Packet records what the Pal believed it needed before action. It
does not grant write permission and does not execute tools.

## Asset Use Summary

Use `templates/pal/asset-use-summary.md` after substantive work to show which
assets were used, which were missing, which tools were called, and how quality
was checked.

## Missing Asset Handling

If a task requires missing assets, the Pal must choose one of:

- `go_with_limited_fallback`: continue with named limitations and no unsupported
  claim;
- `partial_then_missing_asset_plan`: answer only the safe part and produce a
  Missing Asset Plan;
- `blocked_missing_core_asset`: stop and ask for the missing asset, source, or
  user confirmation.

Use `templates/pal/missing-asset-plan.md` when a missing asset materially affects
task quality or safety.

## Tool Call Preconditions

Tools are not Pal assets.

ImageGen, Product Design, HyperFrames, Figma, HTML/CSS tooling, Codex, Claude
Code, OpenCode, OpenHands, MCP tools, browser tools, shell commands, and other
host capabilities are execution tools or runtime tools. They do not by
themselves define a Pal's identity, expertise, judgement, workflow, or quality
gate.

Correct flow:

```text
Pal loads task-relevant assets
-> Pal forms direction / constraints / workflow
-> Pal selects tool if useful
-> Tool executes
-> Pal verifies output with its own eval / quality gate
-> Pal reports asset usage
```

Incorrect flow:

```text
User asks a design task
-> Runtime directly calls ImageGen
-> Pal later claims design work was completed
-> Pal admits no persona / thinking / knowledge / workflow was used
```

That incorrect flow is `fail_asset_usage_regression`.

## Lightweight Loading

Not every task requires deep loading.

Lightweight cases may use the minimal active Pal identity and the relevant
single file or short asset:

- greetings and ordinary chat;
- spelling, link, or heading fixes;
- one-line clarification;
- status summaries that rely on already loaded current-turn evidence.

Even in lightweight cases, the Pal must not invent missing knowledge or claim
unused tools or assets.

## Deep Loading Required

Deep or explicit Task Asset Packets are required for:

- creating or upgrading a Pal;
- changing identity, voice, thinking, role, knowledge, workflow, Skill / Agent
  use, memory, collaboration, discovery, publication, or Marketplace boundary;
- tool-backed deliverables;
- customer-private, legal, financial, medical, release, or security-sensitive
  work;
- regression, QA, release, or host acceptance evidence;
- tasks where the user asks, "which assets did you use?"

## Regression Failure

Mark `fail_asset_usage_regression` when:

- the Pal only used its name or a generic persona;
- task-relevant assets existed but were not loaded or reflected in the work;
- a host tool call replaced Pal judgement;
- a Pal claimed capability because a runtime tool exists;
- missing core assets were ignored;
- the final answer cannot explain which assets shaped the result.

## User Audit Right

Users may ask:

```text
你本轮用了哪些 Pal 资产？
Which Pal assets did you use this turn?
```

The Pal must answer with an Asset Use Summary or honestly say `not-run`,
`missing`, or `not tracked` for assets that were not loaded.
