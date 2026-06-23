# Pal Pool

`pals/` is the AgentPal Pal pool.

The default workspace includes:

```text
Mira-main
Atlas-developer
Vega-research
Rhea-system
Quinn-quality
Morgan-document
Harper-writing
Nova-product
```

Directory names use:

```text
Name-role
```

Users call Pals by display name only:

```text
/pal Mira
/pal Atlas

@Nova
```

Do not expose old internal package names such as `developer-pal` or `pal-developer` as the preferred user command.

Only valid Pal Packs can enter contacts. A valid Pal Pack should include `PAL.md`, `SKILL.md`, `AGENTS.md`, `pal.json`, a display name, aliases, and collaboration permissions.

Ordinary Skills, tools, models, MCP servers, plugins, non-Pal runtimes, raw repositories, knowledge packs, and persona packs do not enter contacts.

After copying a new Pal into this directory, ask Mira to refresh the Pal index and contacts.


