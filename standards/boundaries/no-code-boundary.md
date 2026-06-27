# No-Code Boundary

AgentPal is a Markdown / JSON / protocol workspace. It organizes Pal identity, contacts, knowledge, skills, context, task packages, verification records, release governance, and project binding instructions for a host runtime.

AgentPal must not be represented as:

- a CLI or required command-line tool
- an app, web UI, desktop UI, daemon, service, or database
- an automatic scanner, validator, installer, or background monitor
- a multi-agent runtime or execution layer
- a hidden router that invokes other agents without user-visible evidence

Host runtimes such as Codex, Claude Code, CodeWhale, or other Markdown/JSON-capable agents may read AgentPal files and execute work. The runtime is the execution layer; AgentPal remains the organization layer.

Optional helper tools may exist only as explicitly optional assets owned by a Pal or by an external host runtime. They must not be required for workspace initialization or external project binding.
