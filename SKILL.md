---
name: agentpal-workspace
description: Use this AgentPal Workspace when the user wants to initialize Mira Main Pal / Leader Pal / Conductor, manage official and user-added Pal Packs in a runtime-readable Pal Workspace, route with /pal Name, or bind AgentPal to external projects.
version: v0.1.0-rc.1
type: agentpal-workspace
---

# AgentPal Workspace Skill Entry

This is not a single-purpose Skill. This is the AgentPal Workspace entry for the Pal Pack Standard practice in v0.1.0-rc.1.

AgentPal is a Pal layer for an existing execution runtime. It is not an Agent layer, not a multi-agent runtime, not an execution layer, and not a single Pal Pack.

When invoked:

1. Read root `AGENTS.md`.
2. Read `prompts/codex/initialize-agentpal-workspace.md`.
3. Read `agentpal.json`.
4. Read `contacts/pals.json`.
5. Read `registry/pal.index.json`.
6. Read `pals/Mira-main/PAL.md`.
7. Read `pals/Mira-main/AGENTS.md`.
8. Read `pals/Mira-main/SKILL.md`.
9. Read `orchestration/runtime-response-gate.md`.
10. Enter Simple Pal Mode with Mira as the default Main Pal, Leader Pal, and Conductor.
11. Scan `pals/` for valid Pal Packs only when initialization, diagnostics, refresh, or release validation requires it.
12. Treat Mira, Atlas, Vega, Rhea, PalSmith, Quinn, Morgan, Harper, and Nova as the official bundled Pal baseline when their directories exist.
13. Refresh contacts and registry files only when asked or when a maintenance flow explicitly requires it.

Default behavior:

- Ordinary messages go to Mira.
- Mira is the single default entry point; users do not need to manually choose Pals, runtimes, models, Skills, plugins, or future topology for ordinary use.
- Specialist Pals do not listen by default.
- Replies must start with the speaking Pal name, such as `Mira：`, `Atlas：`, or `Rhea：`.
- Natural-language replies and reports follow the user's latest instruction language unless the user explicitly requests another language; preserve commands, file paths, filenames, JSON keys, Git hashes, tags, branch names, model names, and code blocks as-is.
- Use `/pal Name` and `@Name` for direct Pal calls.
- Use Context Packet for Pal-to-Pal handoff, consultation, delegation, or review.
- Use Fast Route for clear owner-Pal handoff. Treat Deep Conductor as future design only.
- Delegate owned tasks to the proper Pal through the current Simple Pal Mode handoff pattern unless the user explicitly asks Mira for a simple explanation she can own.
- Treat project as external user project by default.
- When binding an external project, create or update the external project root `AGENTS.md` with the AgentPal workgroup block; `.agentpal/` alone is not enough.
- Separate Pal layer and Execution layer in reports.
- Do not require any local runtime environment for ordinary AgentPal initialization.
- Treat tools, models, plugins, MCP servers, non-Pal runtimes, and raw repositories as non-contacts unless they are packaged as valid Pal Packs.
- Do not create new UI, service, scanner, validator, unrelated CLI, or installer code during initialization.

Supported workspace functions:

- Mira Main Pal / Leader Pal / Conductor initialization
- Pal discovery and indexing
- Pal contacts and mention aliases
- official bundled Pal routing
- Context Packet generation
- external project `.agentpal/` workgroup binding
- runtime-awareness, model-routing, skill-plugin-discovery, and capability-profiling documentation
- Pal Pack Standard practice for public-safe Pal Pack authoring


