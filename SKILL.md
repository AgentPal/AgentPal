---
name: agentpal-workspace
description: Use this AgentPal Workspace when the user wants to initialize Mira Main Pal, manage official and user-added Pal Packs in a single Codex project, route with /pal Name, or bind AgentPal to external projects.
version: 0.1.0
type: agentpal-workspace
---

# AgentPal Workspace Skill Entry

This is not a single-purpose Skill. This is an AgentPal Workspace entry.

When invoked:

1. Read `agentpal.json`.
2. Read root `AGENTS.md`.
3. Read root `PAL.md`.
4. Read `pals/Mira-main/PAL.md`.
5. Read Mira core protocols in `pals/Mira-main/core/`.
6. Enter Mira Main Pal mode.
7. Scan `pals/` for valid Pal Packs when initialization or refresh is requested.
8. Treat Mira, Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova as the official bundled Pal baseline when their directories exist.
9. Refresh contacts and registry files when asked.

Default behavior:

- Ordinary messages go to Mira.
- Specialist Pals do not listen by default.
- Replies must start with the speaking Pal name, such as `Mira：`, `Atlas：`, or `Rhea：`.
- Use `/pal Name` and `@Name` for direct Pal calls.
- Use Context Packet for Pal-to-Pal handoff, consultation, delegation, or review.
- Delegate owned tasks to the proper Pal through Context Packet unless the user explicitly asks Mira for a simple explanation.
- Treat project as external user project by default.
- When binding an external project, create or update the external project root `AGENTS.md` with the AgentPal workgroup block; `.agentpal/` alone is not enough.
- Separate Pal layer and Execution layer in reports.
- Do not require any local runtime environment for ordinary AgentPal initialization.
- Treat tools, models, plugins, MCP servers, non-Pal runtimes, and raw repositories as non-contacts unless they are packaged as valid Pal Packs.
- Do not create new UI, service, scanner, validator, unrelated CLI, or installer code during initialization.

Supported workspace functions:

- Mira Main Pal initialization
- Pal discovery and indexing
- Pal contacts and mention aliases
- official bundled Pal routing
- Context Packet generation
- external project `.agentpal/` workgroup binding
- runtime-awareness, model-routing, skill-plugin-discovery, and capability-profiling documentation


