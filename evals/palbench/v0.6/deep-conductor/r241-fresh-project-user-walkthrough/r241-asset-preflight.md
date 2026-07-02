# R241 Asset Preflight

## Verdict

`asset_preflight_pass`

## Fresh Project Binding Assets

| Asset | Status | Use |
| --- | --- | --- |
| fresh `.agentpal/project.json` | present | Confirms active project root and AgentPal workspace root. |
| fresh `.agentpal/AGENTPAL.md` | present | Confirms thin binding, v0.6 Team Pack guardrails, WEC and Closure Gate requirements. |
| fresh `AGENTS.md` protected block | present | Confirms Codex binding marker and natural-language Team Pack first behavior. |

## Team Assets

| Asset | Status | Use |
| --- | --- | --- |
| `examples/team-packs/marketing-growth-team/TEAM.md` | used | Mission, suitable tasks, unsuitable tasks. |
| `examples/team-packs/marketing-growth-team/team.json` | used | Team policy and supported task types. |
| `examples/team-packs/marketing-growth-team/roster.json` | used | Existing members and open roles. |
| `examples/team-packs/marketing-growth-team/workflows/weekly-agentpal-promotion-content.md` | used | Promotion planning workflow shape. |
| `examples/team-packs/marketing-growth-team/evals/definition-of-done.md` | used | Acceptance expectations. |
| `examples/team-packs/marketing-growth-team/routing/team-routing-card.json` | used | Faye / PalSmith / Quinn routing cautions. |

## Pal Assets

| Pal | Asset status |
| --- | --- |
| Mira | central contact and default Main Pal role used |
| Nova | capability card used for product / target-user framing |
| Vega | capability card used for research / channel boundary |
| Harper | capability card used for user-facing writing |
| Rhea | capability card used for no-code and runtime boundary |
| Quinn | capability card used for final verification |

## Missing / Not-Run Assets

| Item | Handling |
| --- | --- |
| live GitHub channel research | not-run; not needed for local walkthrough |
| live tester list | future user-provided input |
| actual publication credentials | not-run; open role |
| external sub-agent results | not-run; no sub-agent used |
