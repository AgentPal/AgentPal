# Pal Index

This index and `contacts/` are the AgentPal source of truth for Pal discovery. Individual Pal Packs must not maintain their own hard-coded list of other Pals or required collaborators.

## Registered

| Pal | id | Directory | Role | Direct call | Notes |
|---|---|---|---|---|---|
| Mira | `mira-main` | `pals/Mira-main` | main-leader-conductor | `/pal Mira` | Default Main Pal, Leader Pal, Conductor, team-leadership work owner, and ordinary-message receiver |
| Atlas | `atlas-developer` | `pals/Atlas-developer` | developer | `/pal Atlas` | Requirements, code tasks, repository handoff, review |
| Vega | `vega-research` | `pals/Vega-research` | research | `/pal Vega` | Research plans, source quality, evidence tables, comparisons |
| Rhea | `rhea-system` | `pals/Rhea-system` | system | `/pal Rhea` | System setup, app installation planning, permissions, recovery |
| Quinn | `quinn-quality` | `pals/Quinn-quality` | quality | `/pal Quinn` | Quality gates, acceptance, risk, evidence and release checks |
| Morgan | `morgan-document` | `pals/Morgan-document` | document | `/pal Morgan` | Files, documents, spreadsheets, PDFs, naming and archiving |
| Harper | `harper-writing` | `pals/Harper-writing` | writing | `/pal Harper` | Drafts, rewrites, communication and style alignment |
| Nova | `nova-product` | `pals/Nova-product` | product | `/pal Nova` | Idea intake, PRDs, scope, MVP slicing and developer handoffs |

## Scan Status

Mira and the seven official bundled specialist Pals are indexed. Directory naming follows `Name-role`.

The seven specialist Pals are slim embedded AgentPal modules, not standalone repositories. Workspace-level contacts, registry, runtime compatibility notes, project binding, and current Pal-layer orchestration protocols are owned by AgentPal root.

## Routing Rule

Ordinary messages go to Mira. Specialist Pals do not listen by default. Mira may consult, delegate, hand off, or request review from a specialist Pal through a Context Packet. Users may also call a Pal directly with `/pal Name`.

When collaboration is needed, the current AI / Mira / Brain resolves collaborators from current contacts / registry and decides case-by-case. The table above is a registration view, not a route map.

## Boundary

Only Pal Packs enter the Pal index and contacts. Tools, models, plugins, MCP servers, non-Pal runtimes, raw repositories, knowledge packs, and persona packs are not Pal contacts.


