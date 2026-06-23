# AgentPal

AgentPal is a Pal layer for coding agents.

It is not an Agent layer, not a multi-agent runtime, and not an execution layer. AgentPal gives an existing runtime a structured Pal workspace: identity, knowledge, skills, context, memory, output contracts, coordination rules, review habits, summaries, and learning storage.

AgentPal v0.1 is a Markdown / JSON / protocol workspace. It has no desktop UI, web UI, daemon, scanner, installer, service, or required runtime dependency.

## Current Runtime

AgentPal v0.1 uses Simple Pal Mode only.

In Simple Pal Mode:

- Mira receives ordinary messages.
- Mira judges substantive requests case-by-case.
- If a registered Pal can own the work, Mira gives a short handoff and stops.
- The owner Pal answers immediately in the same response.
- The owner Pal uses its own `PAL.md`, `SKILL.md`, `pal.json`, relevant assets, Output Contract, and honest fallback when assets are missing.
- AgentPal does not print runtime-mode metadata in normal answers.

AgentPal can be used from Codex, Claude Code, CodeWhale, Gemini CLI, DeepSeek-TUI, or another Markdown/JSON-capable agent runtime, because the Pal layer is plain files and protocols.

## What A Pal Is

A Pal is not an independent runtime process. A Pal is a task-facing package of:

- identity and role
- knowledge and skills
- context and memory boundaries
- output contract
- review and summary habits
- learning and Skill storage rules

The runtime still performs actual file reads, writes, commands, tool calls, publishing, and other execution actions. AgentPal helps the runtime decide who should answer, what assets to use, and how to report honestly.

## Bundled Pals

The bundled Pals are:

- Mira: Main Pal and secretary coordinator
- Atlas: development perspective
- Vega: research and evidence perspective
- Rhea: local system and environment perspective
- Quinn: quality, risk, evidence, and acceptance perspective
- Morgan: document and file workflow perspective
- Harper: writing and communication perspective
- Nova: product and decision perspective

Capability notes are examples only. They are not a route map. Owner selection is AI judgement case-by-case from the current request, context, constraints, risk, requested output, and available Pal assets.

## Quick Start

1. Open this workspace in your agent runtime.
2. Run or paste `INIT_PROMPT.md`.
3. Talk to Mira normally.
4. Use `/pal Name` to call a Pal directly.
5. Put additional Pal Packs under `pals/` and refresh contacts / registry when needed.

## External Project Workgroup

AgentPal can be added to an external project as a workgroup reference. In an external project-bound session:

- the external project is the active project
- AgentPal is only the Pal source and routing reference
- "this project" means the external project, not the AgentPal workspace

Use `prompts/join-external-project-workgroup.md` or the files under `projects/project-workgroup-template/agentpal/` to bind a project.

## Skill Storage

If the user explicitly asks to save a method as a Skill, or similar operations happen more than 3 times, the owner Pal stores the formal Skill under its own directory:

```text
pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md
```

Do not store AgentPal Pal-owned Skills in global runtime skill folders unless the user explicitly asks for a global runtime Skill.

## Future Runtime Orchestration

Future designs for child workflows, non-Pal runtimes, MCP-hosted agents, or remote agent services are documented separately in `docs/future-agent-orchestration.md`. They are not active in AgentPal v0.1 runtime behavior.


