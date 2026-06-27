# Pal Teams, Multi-Pal Collaboration, and Deep Conductor

AgentPal is not limited to a single Pal.

A single Pal can be enough for many tasks. For example, Mira can clarify intent, Atlas can handle a development-focused review, Quinn can run a release gate, and Harper can shape public writing.

As work becomes larger, the useful unit is often not one Pal, but a Pal Team: a group of professional Pals that help the current runtime understand the task, divide responsibility, shape context, define evidence, review outputs, and preserve reusable learning.

## Current Status

This document applies to AgentPal `v0.1.0-rc.1`.

- Simple Pal Mode is the only active task-handling path.
- Fast Route and Task Package are current AgentPal methods.
- Multi-Pal collaboration is current as a Pal-layer working method inside the active runtime.
- Deep Conductor is a future orchestration design, not an active runtime feature in `v0.1.0-rc.1`.
- Subagent calls, parallel child workflows, and multi-agent execution are runtime-layer capabilities. AgentPal does not provide them by itself.

## What a Pal Team Is

A Pal Team is a set of registered Pal Packs that contribute different professional perspectives to the same user goal.

For a release-readiness task, a Pal Team might involve:

| Pal | Possible contribution |
| --- | --- |
| Mira | Intake, owner judgment, stage framing, handoff, and final summary |
| Atlas | Development structure, implementation boundaries, code-facing risks |
| Quinn | Quality evidence, release gate checks, regression risk, verification |
| Harper | Public writing, release notes, documentation tone, editorial consistency |
| Rhea | Local system, command, path, permission, and environment boundaries |
| Nova | Product scope, user value, feature framing, release positioning |
| Vega | Research quality, source review, trend analysis, evidence framing |
| PalSmith | Pal Pack design, authoring guidance, template and structure review |

These Pals do not become separate running agents. They are Pal-layer working assets that guide the current runtime.

A Pal Team helps answer questions such as:

- Who should own this task?
- Which parts of the task are distinct stages?
- What context does each stage need?
- Which risks need review before execution?
- What should the Runtime do, and under whose Pal-layer task package?
- What evidence is required before the final answer is trustworthy?
- What reusable lesson should become a Skill, Runbook, Workflow, or memory candidate later?

## What a Pal Team Is Not

A Pal Team is not:

- a multi-agent runtime
- a group of background worker processes
- a desktop app, web app, installer, or daemon
- a fixed keyword routing table
- a permission system for running commands automatically
- a claim that every registered Pal must participate in every task

AgentPal remains a Pal layer. The host runtime, such as Codex, Claude Code, or another CLI agent, performs file reads, writes, shell commands, tool calls, browsing, publishing, and deletion.

## Simple Pal Mode First

In `v0.1.0-rc.1`, the current runtime works through Simple Pal Mode.

When a user writes:

```text
/pal Atlas
```

the current runtime does not start a new Atlas Agent. Instead, it works in Atlas Pal mode: it reads Atlas assets, follows Atlas boundaries, and uses Atlas output expectations for the task.

The same rule applies to all Pals.

A Pal is a working companion with identity, knowledge, skills, workflows, output contracts, and context boundaries. It is not an Agent Runtime.

## Fast Route for Clear Tasks

Most work should stay simple.

Fast Route is appropriate when:

- the request has a clear owner
- one Pal can handle the work well
- the context scope is small
- risk can be handled through ordinary evidence checks
- a multi-Pal workflow would add overhead without improving the result

For example, a focused documentation edit can go to Harper. A release gate can go to Quinn. A system startup audit can go to Rhea.

The owner is still selected by AI judgment from the current request and the current central contacts. AgentPal does not use hard-coded keyword routing.

## Multi-Pal Collaboration for Complex Work

Some tasks naturally span several kinds of expertise.

For example:

```text
Can this workspace be released? If not, what blocks it, what should be fixed,
and what should the final release note say?
```

That request may involve product scope, documentation readiness, repository state, release evidence, public-safe boundaries, Git tags, and user-facing language. A single Pal may own the answer, but several Pals may provide bounded input.

A practical multi-Pal flow looks like this:

1. The first Pal that receives the task identifies the expected deliverable.
2. The current AI judges candidate owner Pals from central contacts.
3. The task is split into clear stages only when the deliverable requires it.
4. Each stage receives a provisional Pal-layer owner.
5. Runtime tools or Skills are treated as execution support, not as Pal owners.
6. Each Pal receives only the context needed for its role.
7. The owner Pal or Mira summarizes conflicts, risks, and next actions.
8. Verification evidence is recorded before claiming completion.

The goal is not to make the conversation look busy. The goal is to make complex work safer, clearer, and easier to verify.

## Subagent and Multi-Agent Calls Are Runtime Capabilities

Many agent runtimes may support subagents or multiple agents.

For example, a runtime may split a larger task into several execution units:

- one subagent checks documentation
- one subagent checks code
- one subagent runs tests
- one subagent performs release checks
- one subagent summarizes results

That is an Agent Runtime capability.

A Pal does not need to pretend to be those subagents. A Pal does not become an execution worker just because a runtime can run parallel work.

The Pal-layer responsibility is different:

> Decide whether subagents are useful, create clear Task Packages, control which context each execution unit may see, define the required output format and acceptance criteria, and review the returned results.

In other words:

- A Pal Team is responsible for how to understand, divide, frame, and verify the work.
- Subagents or multi-agent runtimes are responsible for how to execute, parallelize, operate, and return evidence.

The two layers can work together, but they are not the same thing.

## Deep Conductor

Deep Conductor is AgentPal's future design for transparent orchestration of complex work.

It is meant for tasks where the system must reason about:

- task complexity and risk
- candidate Pal owners and reviewers
- runtime capability
- model and reasoning needs
- Skill, plugin, MCP, and tool availability
- context slicing and context access limits
- Task Package boundaries
- evidence requirements
- routing decisions
- verification records
- repeated-task learning

Deep Conductor is not active as a full runtime feature in `v0.1.0-rc.1`.

In current AgentPal usage, Deep Conductor should be treated as design language and a future direction. It can help document how complex orchestration should work, but it should not be described as a currently running multi-agent system.

## Pal Team and Runtime Relationship

The clean boundary is:

| Layer | Role |
| --- | --- |
| Skill | A capability or reusable operation |
| Pal | A professional working companion that organizes capability, context, judgment, and output |
| Pal Team | A collaboration layer across multiple professional Pals |
| Agent Runtime | The execution layer that reads files, calls tools, runs commands, and writes changes |
| Deep Conductor | A future transparent orchestration design for complex multi-stage work |

AgentPal helps the runtime use professional working assets well. It does not replace the runtime.

## When Not to Use Multi-Pal Collaboration

Do not turn every task into a Pal Team workflow.

Use a simpler path when:

- Mira can answer ordinary conversation directly
- the user directly calls a Pal with `/pal Name`
- one owner Pal can handle the request
- a small Task Package is enough
- the cost of orchestration is higher than the value it adds

Simple tasks should remain simple. Complex tasks should become explicit, staged, and verifiable.

## Related Documents

- [What is a Pal?](01-what-is-a-pal.md)
- [What is a Pal Pack?](02-what-is-a-pal-pack.md)
- [Pal vs Agent vs Skill](03-pal-vs-agent-vs-skill.md)
- [Pal Team vs Agent Team](04-pal-team-vs-agent-team.md)
- [Simple Pal Mode](05-simple-pal-mode.md)
- [Pal Teams and Deep Conductor methodology](../05-orchestration-methodology/11-pal-teams-and-deep-conductor.md)
- [Runtime compatibility](../04-runtime-guides/00-runtime-compatibility.md)
