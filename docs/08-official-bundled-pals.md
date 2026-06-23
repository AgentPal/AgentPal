# Official Bundled Pals

AgentPal v0.1 includes Mira plus seven official bundled specialist Pals.

The seven specialist Pals are embedded Pal modules, not standalone repositories. AgentPal root owns workspace-level contacts, registry, runtime compatibility notes, project binding, and current Pal-layer orchestration protocols. Each Pal keeps only its identity, professional knowledge, skills, workflows, runbooks, learning records, examples, evals, public-safe memory/state/report placeholders, and output contract.

The official list below is a contacts / registry display, not a route map. Individual Pal Packs do not maintain hard-coded lists of other Pals. If collaboration is needed, the current AI / Mira / Brain resolves available collaborators from contacts / registry and decides case-by-case.

This slim structure reduces token cost, keeps Pal creation easier to understand, and prevents each Pal from carrying duplicate system-layer routing or runtime folders. A separate standalone Pal Pack standard can still exist outside the bundled official Pals.

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

## Default Behavior

Ordinary messages go to Mira. Specialist Pals do not listen by default.

Mira routes to a specialist Pal with a Context Packet when the task calls for specialist judgment, or when the user directly names a Pal.

Replies must start with the speaking Pal name. Mira uses `Mira：`; direct specialist replies use names such as `Atlas：`, `Rhea：`, or `Quinn：`.

Owned work may be delegated after case-by-case AI judgement. The role descriptions above are capability orientation only, not task-domain routing rules.

## Valid Specialist Output

AgentPal v0.1 is a Markdown/protocol-driven Pal work mode. Current task handling uses Simple Pal Mode only.

A valid specialist Pal response must:

- use the Pal's Response Fingerprint
- use the Pal's Output Contract
- use at least one Pal asset or fallback method
- include Asset Usage Proof for complex, audited, or release-gated work

If no Pal asset or fallback method was used, label it `Codex generic answer`, not a Pal answer.

如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。Pal 不是换名字回答。

