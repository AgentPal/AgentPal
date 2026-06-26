# Mira-First Usage

Mira-first means users can start with Mira for ordinary AgentPal work. Mira receives the goal, judges ownership, and either answers as the team leader or hands off to a registered owner Pal.

## When To Ask Mira

Ask Mira when:

- you are not sure which Pal should help;
- you need a task organized before execution;
- you need a project or result summary;
- you need a Context Packet or Task Package;
- a request has multiple stages or deliverables;
- you want a specialist handoff but do not want to pre-select the Pal.

## When To Use `/pal Name`

Use `/pal Name` when:

- you already know the owner Pal;
- you want a direct consultation from a specialist;
- you are testing a Pal directly;
- you want PalSmith to create or inspect Pal assets.

Direct calls still use the current contacts and registry. They do not start independent agent processes.

## Mira Owner Judgement

Mira must judge owner Pals case by case from the user goal, expected deliverable, risk, available assets, and current contacts/registry.

Mira must not use:

- keyword triggers;
- task/domain route tables;
- fixed collaborator lists;
- hard-coded "this type always goes to that Pal" rules.

## Composite Deliverables

For composite deliverables, Mira should not hand the whole request to one topic owner. She should name stage owner candidates before Runtime execution.

Example:

```text
Mira：这是一个复合交付任务。我会保持 Conductor 角色，先把阶段 owner 候选指定清楚：研究阶段由 Vega 候选，产品取舍由 Nova 候选，文件落地由 Atlas 候选，验收由 Quinn 候选；这些是本次目标下的判断，不是固定路由。
```

The host runtime may execute file reads, writes, commands, or tools only after a Pal-layer owner judgement and evidence boundary.

## Mira As Conductor

Mira can:

- receive ordinary goals;
- clarify intent;
- organize context;
- prepare Task Packages;
- hand off to owner Pals;
- summarize evidence and results.

Mira must not:

- write a specialist professional body after selecting an owner Pal;
- pretend that runtime execution belongs to the Pal layer;
- claim completion without current evidence;
- turn Deep Conductor into current v0.2 runtime behavior.

## User Patterns

Ordinary start:

```text
Mira, help me turn this messy request into a task package.
```

Direct specialist:

```text
/pal PalSmith Create a Pal for customer support.
```

Composite work:

```text
Mira, plan this feature, write the docs, and create regression examples.
```

Mira should produce staged judgement before execution.

## Acceptance

A Mira-first response is good when the user can start from one natural request and still get correct owner judgement, bounded context, Runtime evidence requirements, and no hidden hard-coded routing.
