# Central Pal Contacts

This file is the human-readable companion to `pals.json`.

Source of truth:

- `source_of_truth`: true
- routing policy: AI judgement only
- keyword routing allowed: false

| Pal | Status | Pack Path | Direct Call | Role |
| --- | --- | --- | --- | --- |
| Mira | active | `official/pals/Mira-main` | `/pal Mira` | Main Pal, leader, conductor |
| Atlas | active | `official/pals/Atlas-developer` | `/pal Atlas` | Developer / implementation lead |
| Nova | active | `official/pals/Nova-product` | `/pal Nova` | Product / strategy lead |
| Faye | active | `official/pals/Faye-delivery` | `/pal Faye` | FDE business flow architect / AI delivery planning |
| Vega | active | `official/pals/Vega-research` | `/pal Vega` | Research / intelligence lead |
| Quinn | active | `official/pals/Quinn-quality` | `/pal Quinn` | Quality / verification lead |
| Morgan | active | `official/pals/Morgan-document` | `/pal Morgan` | Document / file workflow lead |
| Harper | active | `official/pals/Harper-writing` | `/pal Harper` | Writing / content craft lead |
| Rhea | active | `official/pals/Rhea-system` | `/pal Rhea` | System / runtime safety lead |
| PalSmith | active | `official/pals/PalSmith-pal-governor` | `/pal PalSmith` | Pal asset governor |

Capability summaries are judgement inputs only. They are not keyword routes.

## Capability Cards

Structured capability cards live under
`workspace/organization/contacts/capability-cards/`.

When Mira or an owner Pal selects a candidate Pal, the candidate's capability
card should be checked before assignment. If `forbidden_task_types`,
`team_roles_forbidden`, or `do_not_use_when` clearly conflicts with the current
task, use the [Routing Veto Protocol](routing-veto.md).

Routing Veto is a boundary check after AI judgement. It is not keyword routing.
