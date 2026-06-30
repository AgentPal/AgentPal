# AgentPal Documentation

This is the user documentation entry for AgentPal v0.5.

AgentPal is a no-code Pal organization layer for existing agent runtimes. It is not an Agent runtime, multi-agent runtime, app runtime, installer, scanner, daemon, connector layer, or marketplace.

## Start Here

| Need | Read |
| --- | --- |
| Understand AgentPal in 5 minutes | [`00-overview/00-what-is-agentpal.md`](00-overview/00-what-is-agentpal.md) |
| Learn why AgentPal uses Pals | [`01-concepts/07-why-pal.md`](01-concepts/07-why-pal.md) |
| Initialize AgentPal in Codex | [`04-runtime-guides/01-use-with-codex.md`](04-runtime-guides/01-use-with-codex.md) |
| See runtime support boundaries | [`04-runtime-guides/00-runtime-compatibility.md`](04-runtime-guides/00-runtime-compatibility.md) |
| Use Mira first | [`02-getting-started/mira-first-usage.md`](02-getting-started/mira-first-usage.md) |
| Call a specialist Pal | [`02-getting-started/mira-first-prompt-cards.md`](02-getting-started/mira-first-prompt-cards.md) |
| Bind an external project | [`01-getting-started/bind-external-project.md`](01-getting-started/bind-external-project.md) |

## Core Concepts

- Skill is a capability package.
- Pal is a working partner that knows how to use Skills and Agents.
- Agent is the execution runtime.
- Multi-Pal and multi-Agent teams share the same goal, but AgentPal uses a lighter organization layer to reduce complexity and cost.

Useful concept docs:

- [`01-concepts/01-what-is-a-pal.md`](01-concepts/01-what-is-a-pal.md)
- [`01-concepts/05-simple-pal-mode.md`](01-concepts/05-simple-pal-mode.md)
- [`01-concepts/08-pal-teams-collaboration-and-deep-conductor.md`](01-concepts/08-pal-teams-collaboration-and-deep-conductor.md)
- [`02-concepts/central-project-record.md`](02-concepts/central-project-record.md)
- [`02-concepts/project-memory-in-agentpal.md`](02-concepts/project-memory-in-agentpal.md)

## Codex Setup

Codex is the current verified first path for AgentPal v0.5.

1. Open the AgentPal directory as a Codex project.
2. Copy [`../prompts/codex/initialize-agentpal-workspace.md`](../prompts/codex/initialize-agentpal-workspace.md).
3. Paste it into a fresh Codex conversation.
4. Confirm Mira appears and the 10 official Pals are listed.

More setup links:

- [`../START_HERE.md`](../START_HERE.md)
- [`../prompts/codex/README.md`](../prompts/codex/README.md)
- [`04-runtime-guides/01-use-with-codex.md`](04-runtime-guides/01-use-with-codex.md)

## Built-In Pals

The current official roster is Mira, Atlas, Nova, Faye, Vega, Quinn, Morgan, Harper, Rhea, and PalSmith.

| Pal | Primary role |
| --- | --- |
| Mira | main entry, leader, conductor |
| Atlas | development and implementation |
| Nova | product and strategy |
| Faye | AI delivery and business landing |
| Vega | research and intelligence |
| Quinn | quality and verification |
| Morgan | documents and file workflows |
| Harper | writing and content craft |
| Rhea | system and runtime safety |
| PalSmith | Pal creation and asset governance |

Source of truth: [`../workspace/organization/contacts/pals.json`](../workspace/organization/contacts/pals.json).

## Create A Pal Team

Use these docs when you want your own AI team:

- [`PalSmith.md`](PalSmith.md)
- [`03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md`](03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md)
- [`../examples/palsmith/composite-pal-creation-examples.md`](../examples/palsmith/composite-pal-creation-examples.md)
- [`../prompts/palsmith/create-composite-pal.md`](../prompts/palsmith/create-composite-pal.md)
- [`07-authoring-pals/README.md`](07-authoring-pals/README.md)
- [`03-pal-pack-standard/README.md`](03-pal-pack-standard/README.md)

Use Faye for business landing and delivery-shape work. Use PalSmith to design, inspect, and govern Pals and Pal teams.

## Agent-Use Decision

AgentPal can help decide when a task should stay in a simple Pal route, use owner + verifier, prepare a Runtime Task Package, or ask the host runtime for more capability evidence.

Start with:

- [`05-orchestration-methodology/README.md`](05-orchestration-methodology/README.md)
- [`05-orchestration-methodology/deep-conductor-e2e-usage-guide.md`](05-orchestration-methodology/deep-conductor-e2e-usage-guide.md)
- [`../standards/agent-use/`](../standards/agent-use/)
- [`../standards/capability-inventory/host-capability-snapshot.md`](../standards/capability-inventory/host-capability-snapshot.md)

Deep Conductor is a no-code collaboration and mode-decision protocol. It is not automatic background execution.

## Examples

- [`../examples/walkthroughs/first-agentpal-team/`](../examples/walkthroughs/first-agentpal-team/)
- [`../examples/palsmith/composite-pal-creation-examples.md`](../examples/palsmith/composite-pal-creation-examples.md)
- [`07-official-pals/official-pal-examples-index.md`](07-official-pals/official-pal-examples-index.md)
- [`../examples/orchestration/cross-pal-palsmith-create-ai-team.md`](../examples/orchestration/cross-pal-palsmith-create-ai-team.md)
- [`../examples/delivery-packs/sales-crm-delivery-pack/`](../examples/delivery-packs/sales-crm-delivery-pack/)

Examples are public-safe demonstrations, not customer data and not dispatch rules.

## Limitations

- Codex is the current verified first path.
- Claude Code has minimal handoff evidence, not full host acceptance.
- Generic CLI agents have a compatibility prompt path, not broad validation.
- OpenCode and Gemini are unavailable in current evidence.
- DeepSeek / DeepSeek-TUI are experimental or version-help level only.
- Plan Mode UI evidence is unavailable.
- Goal Mode evidence is limited.
- External writeback to GitHub, Notion, Lark, Cloudflare, CRM, or customer systems is not generally validated.

## Evidence / Validation Archive

Evidence records are useful for maintainers and release checks, but they are not the first user path.

- [`release/v0.5-release-candidate-preflight.md`](release/v0.5-release-candidate-preflight.md)
- [`../evals/palbench/v0.5/`](../evals/palbench/v0.5/)
- [`../evals/palbench/v0.5/documentation/archive/docs/`](../evals/palbench/v0.5/documentation/archive/docs/)
- [`../release/fresh-clone-checks/`](../release/fresh-clone-checks/)
- [`../release/integration-notes/`](../release/integration-notes/)

## Public-Safe Rule

Do not publish private user memory, private project state, internal development notes, credentials, local absolute paths, real customer data, or unauthorized third-party full text.
