# What Is AgentPal

AgentPal is a Pal layer and Pal Pack Standard practice for agent runtimes.

It packages identity, knowledge, skills, memory boundaries, workflows, context rules, output contracts, verification habits, and collaboration protocols into runtime-readable working assets.

AgentPal v0.3.0-rc.1 is a Markdown / JSON / protocol workspace. It is not an Agent layer, not a multi-agent runtime, not an execution layer, not a desktop app, and not a marketplace.

## The Short Version

AgentPal gives an existing agent runtime a structured Pal Workspace.

The runtime still performs execution: reading files, writing files, calling tools, running commands, publishing, deleting, or modifying systems. AgentPal provides the Pal layer that helps the runtime decide who should answer, which assets to read, what boundaries apply, and how evidence should be reported.

## Workspace, Not One Pal Pack

The AgentPal root is the AgentPal Workspace. It contains the shared central contacts, orchestration protocols, templates, prompts, examples, evals, release files, and public-safe placeholders.

Single Pal Packs live under `official/pals/<Pal-Directory>/`. Each Pal Pack owns its own identity, output contract, professional knowledge, skills, runbooks, workflows, examples, evals, and learning rules.

## Current Runtime Path

AgentPal v0.3.0-rc.1 uses Simple Pal Mode for task handling and provides Deep Conductor as no-code protocols, templates, examples, evals, task packages, and replay reports. It is not automatic runtime execution.

Mira receives ordinary messages. When a substantive task belongs to a registered Pal, Mira gives a short handoff and stops. The owner Pal answers immediately in the same response using its own assets and Output Contract.

Direct calls such as `/pal Harper` enter that Pal's working mode. They do not start an independent agent process.

## Continue Reading

- [Current status](01-current-status.md)
- [Repository map](02-repository-map.md)
- [What is a Pal?](../01-concepts/01-what-is-a-pal.md)
- [What is a Pal Pack?](../01-concepts/02-what-is-a-pal-pack.md)
- [Simple Pal Mode](../01-concepts/05-simple-pal-mode.md)

