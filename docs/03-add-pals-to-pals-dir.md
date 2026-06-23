# Add Pals to `pals/`

`pals/` is the AgentPal Pal pool. The default workspace already includes Mira and seven official bundled specialist Pals:

- `Mira-main`
- `Atlas-developer`
- `Vega-research`
- `Rhea-system`
- `Quinn-quality`
- `Morgan-document`
- `Harper-writing`
- `Nova-product`


## Add Another Pal

Copy a valid Pal Pack directory into `pals/`.

Use `Name-role` names such as:

```text
Atlas-developer
Nova-product
Vega-research
```

The Pal Pack should include `PAL.md`, `SKILL.md`, `AGENTS.md`, and `pal.json`.

After adding a Pal, ask Mira to refresh the Pal index and contacts with `prompts/refresh-pal-index.md`.

## Boundary

Only Pal Packs enter contacts. Skills, tools, models, MCP servers, plugins, non-Pal runtimes, raw repositories, knowledge packs, persona packs, and Pal-owned tool engines do not enter contacts.




