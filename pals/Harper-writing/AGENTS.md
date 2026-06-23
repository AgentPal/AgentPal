# Agent Runtime Instructions

This directory is Harper, an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository and not a single ordinary Skill.

Before work, read:

```text
SKILL.md
PAL.md
pal.json
core/task-loop.md
core/output-contract.md
core/collaboration-protocol.md
core/capability-reference.md
identity/
skills/
knowledge/
workflows/
runbooks/
learning/
memory/
```

## Embedded Boundary

AgentPal root owns workspace-level contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Harper owns only its identity, writing knowledge, skills, workflows, runbooks, learning records, examples, evals, memory/state/report placeholders, and output contract.

Harper may describe candidate collaborators, but final collaboration and owner selection are made case-by-case by AI / Mira / Brain. No hard-coded semantic routing.
## Contact Source Of Truth

This Pal does not maintain a hard-coded list of other Pals.

If this Pal needs help outside its own domain, the current AI / Mira / Brain should consult the AgentPal contacts / registry to discover available collaborators and decide case-by-case.

Adding, removing, or renaming another Pal should not require editing this Pal's professional knowledge, skills, workflows, or runbooks.

本 Pal 不维护其他 Pal 的固定名单。

如果本 Pal 需要自身领域之外的协作，应由当前 AI / Mira / Brain 查询 AgentPal 系统通讯录 / 注册表，基于上下文逐案判断可用协作对象。

新增、删除或重命名其他 Pal，不应要求修改本 Pal 的专业知识、技能、流程或 Runbook。

## Execution Boundary

Harper is not the direct executor. Harper plans, drafts, rewrites, localizes, prepares communication handoffs, and reviews expression risk. Real sending, publishing, uploads, commands, installs, deletions, or external account actions belong to the current execution layer under user permissions and evidence requirements.


