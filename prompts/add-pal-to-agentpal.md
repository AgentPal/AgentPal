# Add a Pal to AgentPal

Use this prompt after copying a new Pal Pack directory into `pals/`.

```text
Add newly copied Pal Pack directories to AgentPal.

Read AgentPal root rules:
- AGENTS.md
- SKILL.md
- PAL.md
- agentpal.json
- pals/README.md
- registry/README.md
- contacts/README.md

Scan only pals/. Do not scan the whole disk or external projects.

Keep the official baseline:
- Mira-main
- Atlas-developer
- Vega-research
- Rhea-system
- Quinn-quality
- Morgan-document
- Harper-writing
- Nova-product

For each new directory:
1. Check directory name follows Name-role.
2. Check PAL.md, SKILL.md, AGENTS.md, and pal.json exist.
3. Parse pal.json.
4. Check pal.json.type = pal-pack.
5. Check display_name, aliases, and direct_call.
6. Check discoverable, contactable, and collaboration permissions.
7. Add only valid Pal Packs to contacts and pal index.
8. Put invalid or uncertain candidates into contacts/discovered-candidates.md.

Update:
- registry/pal.index.md
- registry/pal.index.json
- contacts/PAL_CONTACTS.md
- contacts/pals.json
- contacts/mention-aliases.md

Do not modify the Pal's original content unless I explicitly ask you to repair that Pal Pack.
Do not add ordinary Skills, tools, models, MCP servers, plugins, non-Pal runtimes, raw repositories, knowledge packs, or persona packs to contacts.
```


