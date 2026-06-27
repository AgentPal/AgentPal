# What Is A Pal Pack?

A Pal Pack is the directory package for one Pal.

In the AgentPal Workspace, Pal Packs live under:

```text
official/pals/<Pal-Directory>/
```

Each directory is one Pal Pack. The AgentPal Workspace itself is not a single Pal Pack.

## Minimum Useful Files

A contributed Pal Pack should include:

- `PAL.md`
- `pal.json`
- `SKILL.md`
- `README.md`
- `AGENTS.md`
- `core/output-contract.md`

## Common Pal Pack Directories

- `identity/`
- `knowledge/`
- `skills/`
- `runbooks/`
- `workflows/`
- `learning/`
- `memory/`
- `state/`
- `reports/`
- `examples/`
- `evals/`

## Contacts Boundary

Only valid Pal Packs should enter `workspace/organization/contacts/`. Skills, tools, plugins, models, MCP servers, and runtime adapters do not become Pals because they are indexed.

## Related

- [Pal Pack structure](../03-pal-pack-standard/01-pal-pack-structure.md)
- [Root files](../03-pal-pack-standard/02-root-files.md)
- [Public/private boundary](../03-pal-pack-standard/11-public-private-boundary.md)
