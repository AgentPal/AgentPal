# AgentPal v0.1.0-rc.1 Release Notes

AgentPal v0.1.0-rc.1 is a public release candidate for the AgentPal Pal Workspace.

## What Is Included

- A Markdown / JSON AgentPal workspace for supported agent runtimes.
- Mira as the default Main Pal and secretary coordinator.
- Seven bundled specialist Pals: Atlas, Nova, Vega, Rhea, Quinn, Morgan, and Harper.
- Clara was removed from the default bundled Pal set and may return later as a separate Pal package.
- Bundled specialist Pals are slim embedded AgentPal modules, not standalone repositories.
- `/pal Name` direct call protocol.
- Simple Pal Mode as the only active v0.1 task-handling path.
- AI Judgement routing governance.
- Pal discovery source-of-truth: contacts / registry are the source for Pal names, aliases, paths, and collaboration availability.
- Runtime Response Gate and Pal Mode validity rules.
- External project workgroup templates.
- Release-safe examples, evals, prompts, and failure examples.

## What Is Not Included

- No desktop app.
- No web UI.
- No Tauri / React app.
- No background daemon.
- No scanner, validator, installer, or workspace service.
- No required Python, Node.js, Rust, or Go dependency for AgentPal initialization.
- No automatic execution layer.
- No active subagent or non-Pal runtime orchestration in v0.1.

## How To Use

1. Add the AgentPal directory as a project/workspace in a supported runtime.
2. Open the AgentPal Workspace.
3. Copy the full contents of `INIT_PROMPT.md`.
4. Start with Mira.
5. Use `/pal Name` to call a specialist Pal directly when needed.

## Built-In Pals

- Mira: Main Pal, triage, context, project workgroups, and summaries.
- Atlas: development-oriented planning and evidence review.
- Nova: product thinking, PRDs, scope, and decisions.
- Vega: research, sources, comparisons, and uncertainty.
- Rhea: system setup planning, permissions, and recovery.
- Quinn: quality, risk, evidence, and release gates.
- Morgan: files, documents, PDFs, spreadsheets, and organization.
- Harper: writing, rewriting, communication, and style.

Capability descriptions are non-binding orientation. They are not task-domain route rules.

Contacts / registry are the source of truth for Pal discovery. Individual Pal Packs do not maintain hard-coded lists of other Pals, so adding or removing a Pal should mainly update contacts / registry and public bundled lists.

## Simple Pal Mode

Simple Pal Mode is the active AgentPal v0.1 behavior.

Mira receives ordinary messages. When Mira judges that a registered Pal owns a substantive request, Mira gives only a short ownership judgement and handoff. The owner Pal answers immediately in the same response, using its own Pal assets, Output Contract, and honest fallback if relevant assets are missing.

AgentPal does not show runtime-mode metadata in normal answers.

## Future Runtime Orchestration

Future subagent / non-Pal runtime / remote agent / MCP-hosted agent orchestration is documented in `docs/future-agent-orchestration.md`. It is not active in AgentPal v0.1 runtime behavior.

## AI Judgement Routing Governance

AgentPal does not use hard-coded semantic routing. Mira judges owner Pal selection case-by-case from user goal, context, current registered Pal ownership scopes, risk, available Pal assets, user constraints, and expected output.

Explicit commands such as `/pal Atlas`, Codex generic requests, safety boundaries, and availability guardrails remain deterministic.

## External Project Workgroup

AgentPal can be bound to an external project using `.agentpal/` and a protected root `AGENTS.md` block. In project-bound mode, the external project is `active_project_root`; the AgentPal workspace remains only a Pal source and routing reference.

Removal deletes only the AgentPal binding files and protected block. It must not delete user project source or user-authored `AGENTS.md` content.

## Known Limitations

- AgentPal v0.1 is file-driven and prompt-driven.
- AgentPal does not execute real filesystem, system, or publishing actions by itself.
- Pal responses require assets, output contracts, or explicit fallback methods to be valid.
- Future runtime orchestration requires a separate design before activation.

## License

AgentPal is released under the MIT License. See `LICENSE`.

