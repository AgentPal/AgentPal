<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Pal To Subagent Map

This map describes which official AgentPal Pals are suitable for Codex Subagent Mode.

This map is part of the AgentPal registry view, not a task routing table. It describes selected-Pal subagent assets and boundaries. It must not be used as a hard-coded semantic route map.

Codex Subagent Mode uses Codex subagent threads, not OS-level background processes. Mira is coordinator and summarizer; specialist Pals may run as bounded subagents.

| Pal | Role | Default subagent role | Suitable | Permission boundary |
|---|---|---|---|---|
| Mira | main-secretary | coordinator / secretary summarizer | coordinator only | read-only coordination |
| Atlas | developer | owner / consultant | yes | workspace-scoped, no edits unless allowed |
| Nova | product | owner / consultant | yes | read-only planning |
| Quinn | quality | reviewer | yes | read-only evidence review |
| Rhea | system | owner / consultant | yes | read-only by default |
| Vega | research | consultant | yes | no external network unless approved |
| Morgan | document | owner / consultant | yes | no file moves or deletes unless approved |
| Harper | writing | consultant | yes | no external sending unless approved |

Use `registry/pal-subagent-map.json` as the structured source.

Official specialist subagents read slim embedded Pal assets such as `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`, `core/output-contract.md`, `core/capability-reference.md`, `knowledge/`, `skills/`, `workflows/`, `runbooks/`, and `learning/`. They do not rely on per-Pal standalone contacts, registry, runtime, models, plugins, or orchestration directories.


