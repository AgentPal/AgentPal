# Runtime Compatibility Layer

AgentPal v0.1 is a Pal layer, not an execution layer.

The active behavior is Simple Pal Mode only. AgentPal stores Pal identity, knowledge, skills, context, memory, output contracts, coordination rules, review habits, summaries, and learning rules in Markdown / JSON files.

The current runtime still owns:

- file reads and writes
- command execution
- tool calls
- UI checks
- network actions
- publishing and deletion
- evidence for real changes

Runtime tools, models, plugins, MCP servers, and other execution systems are not Pal contacts. They may provide evidence or perform actions only when the user request and safety boundary allow it.

Future runtime orchestration is documented separately in `docs/future-agent-orchestration.md` and is not active in AgentPal v0.1 runtime behavior.

