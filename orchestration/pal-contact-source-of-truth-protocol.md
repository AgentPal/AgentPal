# Pal Contact Source Of Truth Protocol

## Purpose

AgentPal uses workspace contacts and registry as the single source of truth for Pal discovery.

Individual Pal Packs must not maintain hard-coded lists of other Pals. They may describe collaboration abstractly, but they must not name a specific Pal as a required collaborator, default collaborator, or fixed owner for a task type.

## Source Of Truth

Pal discovery comes from:

- `contacts/pals.json`
- `contacts/PAL_CONTACTS.md`
- `contacts/mention-aliases.md`
- `registry/pal.index.json`
- `registry/pal.index.md`
- `registry/pal-subagent-map.json`
- `registry/pal-subagent-map.md`

These files define currently available Pal names, aliases, roles, paths, contactability, and subagent suitability.

## Pal Pack Boundary

Each Pal Pack owns its own identity, professional knowledge, skills, workflows, runbooks, examples, evals, learning records, and output contract.

Each Pal Pack must not:

- keep a local list of other Pals
- say a certain task must go to a named Pal
- name a specific Pal as a required collaborator
- encode a fixed multi-Pal combination
- duplicate contacts or registry data inside its own professional files

Each Pal Pack may say:

- collaboration may be useful
- a suitable collaborator should be resolved from current contacts / registry
- the current AI / Mira / Brain should decide case-by-case
- a Context Packet should be prepared for the selected collaborator

## Collaboration Resolution

If collaboration is needed:

1. The current AI / Mira / Brain reads the current contacts / registry.
2. It judges the user goal, context, risk, output need, available assets, and cost case-by-case.
3. It selects an owner Pal, consultant Pal, reviewer Pal, runtime, or fallback path from the current workspace state.
4. It prepares a Context Packet for the selected collaborator.

This is not a keyword route and not a task-domain map.

## Adding Or Removing Pals

Adding a Pal should mainly update contacts / registry.

Removing a Pal should mainly remove it from contacts / registry and public official Pal lists.

Adding, removing, or renaming another Pal should not require broad edits to existing Pals' professional knowledge, skills, workflows, runbooks, examples, or evals.

## Examples And Evals

Examples may mention specific Pals only as non-binding examples.

Evals may mention specific Pals only as test fixtures.

Examples and evals must not become routing rules. They must not say that a task shape requires a fixed Pal, fixed Pal set, or keyword-triggered collaborator.

## 中文规则

Pal 发现来自 AgentPal 系统通讯录 / 注册表。

单个 Pal Pack 不应写死其他 Pal 的身份。

Pal 可以抽象地说明需要协作，但不应把某个具体 Pal 写成必需协作者、默认协作者或某类任务的固定 owner。

如需协作，由当前 AI / Mira / Brain 读取当前 contacts / registry，并基于用户目标、上下文、风险、输出需求、可用资产和成本逐案判断。

新增或删除 Pal，主要修改 contacts / registry，不应大面积修改每个 Pal 的专业知识、技能、流程或 Runbook。

示例中的具体 Pal 名称都是非绑定示例。

eval 中的具体 Pal 名称只是测试夹具，不是路由规则。
