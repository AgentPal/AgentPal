# AgentPal v0.1.0-rc.1

AgentPal v0.1.0-rc.1 is the first public release candidate for AgentPal as a Pal layer for Markdown/JSON-capable agent runtimes.

## Highlights

- AgentPal is a Pal layer, not an Agent layer, not a multi-agent runtime, and not an execution layer.
- Current v0.1 task handling uses Simple Pal Mode only.
- Mira is the default Main Pal and secretary coordinator.
- Owner Pals answer in the same response after Mira handoff.
- AI Judgement routing selects owner Pals case-by-case; no hard-coded semantic routing.
- Bundled default Pals: Mira, Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova.
- Clara is not included in the default bundled Pal set for v0.1.0-rc.1.
- Supports Codex, Claude Code, CodeWhale, Gemini CLI, DeepSeek-TUI, and other runtimes that can read Markdown / JSON workspaces.
- No Python, Node.js, Rust, Go, UI, daemon, scanner, validator, installer, or service is required for AgentPal initialization.

## Current Runtime Behavior

AgentPal v0.1.0-rc.1 uses Simple Pal Mode only:

1. Mira receives ordinary messages.
2. Mira judges whether a registered owner Pal should take over.
3. Mira gives a short handoff and stops.
4. The owner Pal answers immediately in the same response.
5. The owner Pal uses its own Pal assets, Output Contract, and fallback rules when needed.

Future child-workflow, non-Pal runtime, remote agent, and MCP-hosted agent orchestration is reserved for later design and is not active in this release candidate.

## Included Pals

- Mira: Main Pal and secretary coordinator
- Atlas: development perspective
- Vega: research and evidence perspective
- Rhea: local system and environment perspective
- Quinn: quality, risk, evidence, and acceptance perspective
- Morgan: document and file workflow perspective
- Harper: writing and communication perspective
- Nova: product and decision perspective

## Installation / Use

1. Add the AgentPal directory as a workspace/project in your agent runtime.
2. Open the AgentPal workspace.
3. Paste or run `INIT_PROMPT.md`.
4. Talk to Mira normally.
5. Use `/pal Name` to directly call a Pal.

## Known Limitations

- This release is file-driven and prompt-driven.
- It does not include a desktop app, web UI, CLI, service, daemon, scanner, installer, or automatic execution layer.
- Runtime execution evidence still comes from the host agent runtime, not from Pal files themselves.
- Future runtime orchestration is documented as design material only.

## License

MIT License.


