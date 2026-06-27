# Official Bundled Pals

AgentPal v0.1.0-rc.1 includes nine official bundled Pal Packs: Mira plus eight specialists.

The official list below is a central contacts display, not a route map. Owner selection is case-by-case AI judgement. Individual Pal Packs should not maintain hard-coded route maps for other Pals.

| Pal | ID | Directory | Role | Direct call |
| --- | --- | --- | --- | --- |
| Mira | `mira-main` | `official/pals/Mira-main` | Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator | `/pal Mira` |
| Atlas | `atlas-developer` | `official/pals/Atlas-developer` | Development perspective | `/pal Atlas` |
| Vega | `vega-research` | `official/pals/Vega-research` | Research and evidence perspective | `/pal Vega` |
| Rhea | `rhea-system` | `official/pals/Rhea-system` | Local system and environment perspective | `/pal Rhea` |
| PalSmith | `palsmith-pal-governor` | `official/pals/PalSmith-pal-governor` | Pal asset governance, creation, health, import/export, versioning and privacy perspective | `/pal PalSmith` |
| Quinn | `quinn-quality` | `official/pals/Quinn-quality` | Quality, risk, evidence, and acceptance perspective | `/pal Quinn` |
| Morgan | `morgan-document` | `official/pals/Morgan-document` | Document and file workflow perspective | `/pal Morgan` |
| Harper | `harper-writing` | `official/pals/Harper-writing` | Writing and communication perspective | `/pal Harper` |
| Nova | `nova-product` | `official/pals/Nova-product` | Product and decision perspective | `/pal Nova` |

## Default Behavior

Ordinary messages go to Mira. Specialist Pals do not listen by default.

Direct calls use display names or aliases, not directory names.

## Context Loading

Mira does not load every bundled Pal before routing. Mira reads central contacts summaries, then hands off to the selected owner Pal.

The selected Pal reads its own minimum files and a small number of relevant assets. Pal `index.md` files are navigation aids, not permission to load every skill, knowledge card, runbook, workflow, example, or eval.

## Related

- [Call your first Pal](../02-getting-started/05-call-your-first-pal.md)
- [Simple Pal Mode](../01-concepts/05-simple-pal-mode.md)
- [Contacts and registry](../03-pal-pack-standard/10-contacts-and-registry.md)
