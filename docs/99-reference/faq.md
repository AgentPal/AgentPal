# FAQ

## Is AgentPal an agent runtime?

No. AgentPal is a Pal layer and Pal Pack Standard practice. The host runtime still performs model execution, file operations, commands, tool calls, publishing, deletion, and other actions.

## Is a Pal an agent?

No. A Pal is a portable working companion loaded by an agent runtime. It is not an independent process.

## Is AgentPal a multi-agent system?

No. AgentPal v0.1.0-rc.1 uses Simple Pal Mode only. Future runtime orchestration material is not active current behavior.

## Where do Pals live?

Single Pal Packs live under `official/pals/<Pal-Directory>/`.

## Is the AgentPal root one Pal Pack?

No. The AgentPal root is the AgentPal Workspace. It contains multiple Pal Packs and shared workspace assets.

## How does AgentPal discover Pals?

Through `workspace/organization/contacts/`. Legacy `contacts/` and `registry/` directories are compatibility references, not the current source of truth.

## Can a Skill or plugin be a Pal contact?

No. Skills, tools, plugins, models, MCP servers, raw repositories, and runtime adapters do not become Pal contacts unless they are packaged as valid Pal Packs.

## What is active in v0.1.0-rc.1?

Simple Pal Mode, Mira as default Main Pal, official bundled Pal Packs, runtime-readable Markdown/JSON assets, direct `/pal Name` calls, and public Pal Pack Standard documentation.

## Related

- [Current status](../00-overview/01-current-status.md)
- [Known limitations](known-limitations.md)
- [What is AgentPal?](../00-overview/00-what-is-agentpal.md)
