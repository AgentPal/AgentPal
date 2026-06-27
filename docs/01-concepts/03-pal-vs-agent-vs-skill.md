# Pal Vs Agent Vs Skill

## Summary

| Concept | What it is | In AgentPal v0.1.0-rc.1 |
| --- | --- | --- |
| Agent runtime | The system that runs models, reads files, calls tools, and performs actions | External to AgentPal |
| Pal | A portable working companion used by the runtime | Stored as a Pal Pack |
| Pal Pack | Directory package for one Pal | Lives under `official/pals/<Pal>/` |
| Skill | A focused capability or reusable method | Can belong to a Pal, but is not a Pal |
| Workflow | A repeatable process | Can be used by a Pal |
| Tool/plugin/model/MCP | Runtime capability or external integration | Not a Pal contact by itself |

## Why This Boundary Matters

AgentPal should not claim runtime actions that it did not perform. A Pal can guide, review, summarize, and structure work; the host runtime executes actions and provides evidence.

The boundary also keeps contacts clean. A Skill, plugin, model, or raw repository can be useful, but it does not become a Pal unless it is packaged as a valid Pal Pack.

## Related

- [What is a Pal?](01-what-is-a-pal.md)
- [What is a Pal Pack?](02-what-is-a-pal-pack.md)
- [AgentPal vs agent runtime](../00-overview/03-agentpal-vs-agent-runtime.md)
