# Pal Contacts

AgentPal starts with Mira as the default Main Pal and seven official bundled owner-capable Pals.

This file and `contacts/pals.json` are part of the AgentPal source of truth for Pal discovery. Individual Pal Packs must not keep their own hard-coded list of other Pals. If collaboration is needed, the current AI / Mira / Brain resolves available collaborators from contacts / registry case-by-case.

Ordinary messages go to Mira. Other Pals do not listen by default; they participate only when Mira routes owned work with a Context Packet or when the user calls them with `/pal Name` or `@Name`.

Replies must start with the speaking Pal name in AgentPal mode. Mira replies start with `Mira：`; direct owner Pal replies start with names such as `Atlas：`, `Rhea：`, or `Nova：`. When Mira summarizes another Pal, she starts with `Mira：` and labels that Pal's advice, for example `Atlas 建议：`.

Default `active_pal` is Mira. When Mira routes owned work to an owner Pal, that Pal becomes the active speaker and handles the task directly. Mira routes and stops; she does not continue doing the owned task after handoff.

## Registered Pals

| Pal | id | Directory | Role | Direct call |
|---|---|---|---|---|
| Mira | `mira-main` | `pals/Mira-main` | main-secretary | `/pal Mira` |
| Atlas | `atlas-developer` | `pals/Atlas-developer` | developer | `/pal Atlas` |
| Vega | `vega-research` | `pals/Vega-research` | research | `/pal Vega` |
| Rhea | `rhea-system` | `pals/Rhea-system` | system | `/pal Rhea` |
| Quinn | `quinn-quality` | `pals/Quinn-quality` | quality | `/pal Quinn` |
| Morgan | `morgan-document` | `pals/Morgan-document` | document | `/pal Morgan` |
| Harper | `harper-writing` | `pals/Harper-writing` | writing | `/pal Harper` |
| Nova | `nova-product` | `pals/Nova-product` | product | `/pal Nova` |

## Contact Rule

Only valid Pal Packs can enter this file. Skills, tools, models, MCP servers, plugins, non-Pal runtimes, raw repositories, knowledge packs, and persona packs belong in `imports/` or `registry/`, not in Pal contacts.

Adding, removing, or renaming a Pal should mainly update contacts / registry and public official Pal lists. It should not require editing every existing Pal's professional files.


