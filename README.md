# AgentPal

AgentPal is a lightweight framework for building AI teams on top of agent runtimes such as Codex, Claude Code, OpenCode, OpenHands, and other CLI agents.

Create role-based Pals with knowledge, skills, memory, workflows, output contracts, and collaboration rules, then organize them into a working AI team.

AgentPal gives every agent a Pal. AgentPal v0.3.0-rc.1 is a Markdown / JSON / protocol workspace for runtimes that can read structured workspace files. It is not an Agent runtime, not a multi-agent runtime, not an execution layer, not a desktop app, not a web app, and not an installer.

## PalSmith

PalSmith is the AI team builder and Pal asset governance Pal for AgentPal. It helps users create, improve, inspect, import, export, version, and maintain Pals and Pal teams through natural language, without needing to understand the full Pal Pack directory structure.

Learn more about PalSmith: [What is PalSmith, and how can I operate it?](docs/01-concepts/09-What-is-PalSmith-how-can-I-operate-it.md)

v0.2 development now focuses on productizing this path. Start from the [v0.2 development plan](docs/09-roadmap/v0.2-development-plan.md), the [v0.2 task pool](docs/09-roadmap/v0.2-task-pool.md), and the [PalSmith end-to-end productization plan](docs/06-palsmith/palsmith-end-to-end-productization.md). The first implementation slice adds copyable creation packages for a first professional Pal and an AI team goal.

For v0.2 Capability Inventory work, see the [minimal usable design](docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md), [navigation guide](docs/00-overview/capability-inventory-navigation.md), and [capability profile index](standards/capability-inventory/README.md). Capability Inventory assets are split across `standards/capability-inventory/`, `workspace/organization/capability-inventory/`, `examples/capability-inventory/`, and `templates/capability-inventory/`; templates are copyable shapes, while profiles are illustrative judgement inputs, not automatic environment scans.

For v0.2 release regression work, see the [PalBench Light Suite](evals/palbench-light/README.md) and [suite plan](docs/research/palbench-light-suite-plan.md).

For Runtime Adapter troubleshooting and thin binding stability, see the [stability guide](docs/04-runtime-guides/runtime-adapter-stability-guide.md) and [troubleshooting prompt cards](docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md).

For the no-code orchestration prototype line, see the [v0.3 development plan](docs/09-roadmap/v0.3-development-plan.md), [v0.3 task pool](docs/09-roadmap/v0.3-task-pool.md), [v0.3 Deep Conductor readiness](docs/09-roadmap/v0.3-deep-conductor-readiness.md), [v0.3 public capability summary](docs/09-roadmap/v0.3-public-capability-summary.md), [Deep Conductor E2E guide](docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md), [Deep Conductor real runtime replay report](docs/research/deep-conductor-real-runtime-replay-report.md), [Context Packet usage guide](docs/05-orchestration-methodology/context-packet-usage-guide.md), [multi-Pal prompt cards](docs/02-getting-started/multi-pal-collaboration-prompt-cards.md), and [PalBench Collaboration Suite](evals/palbench-collaboration/README.md). v0.3 Deep Conductor is no-code orchestration, not an automatic runtime.

For the local v0.4/v0.5 workspace layout, see the [Repository Structure](docs/00-overview/repository-structure.md) guide. The visible root directories are `standards/`, `official/`, `workspace/`, `templates/`, `examples/`, `evals/`, `release/`, `archive/`, and `docs/`.

## Why AgentPal?

When users want agents to work better, they usually try one of two paths:

- add more Skills
- build Agent teams

Skills are lightweight, but they can become fragmented. A Skill is often single-purpose, easy to forget, hard to combine, and usually does not own memory, workflow, verification, or long-term context.

Agent teams can be powerful, but they are often heavy. They may require complex configuration, repeated context, higher context cost, role coordination, result merging, and stronger permission boundaries.

AgentPal adds the missing middle layer: Pal. A Pal turns many skills, knowledge cards, workflows, memories, and verification rules into a few memorable working companions.

Users should not need to remember hundreds of skills. They should be able to remember a few Pals and what each Pal is responsible for.

## What Is A Pal?

A Pal is not a single Skill.

A Pal is not a new Agent runtime.

A Pal is a portable working companion made of identity, knowledge, skills, memory rules, workflows, context rules, output contracts, verification habits, and collaboration protocols.

The name Pal means a memorable working companion, not a tool name. In AgentPal, a Pal helps the current runtime understand the user's goal, load the right context, shape a Task Package, use relevant Skills or fallback methods, and check whether the result is actually complete.

Learn more about Pal:

- [Why Pal?](docs/01-concepts/07-why-pal.md)
- [Pal Teams, Multi-Pal Collaboration, and Deep Conductor](docs/01-concepts/08-pal-teams-collaboration-and-deep-conductor.md)

## What Works Today

AgentPal v0.3.0-rc.1 currently provides:

- Markdown / JSON / protocol workspace assets with no required runtime dependency
- Standards for no-code boundaries, thin project binding, central assets, host-runtime execution, and no keyword routing under `standards/`
- Central organization workspace foundations under `workspace/`, including the central Pal roster at `workspace/organization/contacts/pals.json` and central project records under `workspace/projects/`
- Official bundled Pal Packs under `official/pals/`
- Simple Pal Mode as the active runtime policy
- Mira as the default Main Pal / Leader / Conductor, with leader knowledge, skills, workflows, runbooks, evals, research inventory, delegation, handoff, context packet, risk approval, and progress reporting assets
- 9 official bundled Pals: Mira, Atlas, Vega, Rhea, PalSmith, Quinn, Morgan, Harper, and Nova
- `/pal Name` explicit Pal calls backed by the central contact roster
- AI owner judgement, Fast Route owner-Pal handoff, and no hard-coded keyword routing
- Task Package rules, Runtime Task Package standards, Context Slicing, and Asset Loading Budget
- PalSmith as the official no-code Pal asset governance Pal for Pal creation, AI team creation, job fitness inspection, user material ingestion, optional web research to knowledge, import, export, health checks, versioning, publish readiness, and Runtime Task Package planning
- PalSmith quickstart path, AI team blueprints, demo script, readiness matrix, task package templates, example packages, governance protocols, and Markdown evals
- Formal Skill asset standard with 219 formal skills mapped to Pal-owned skill assets and 0 missing formal Skill assets under the release standard
- Deepened official Pal assets for Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova, including role knowledge, skills, workflows, runbooks, evals, collaboration boundaries, and research inventories
- Historical release-candidate evidence archived under `archive/migration-from-v0.3/release-candidate-docs/`, with `docs/08-release-candidate/README.md` kept as a pointer
- Codex, Claude Code, and Generic CLI Agent usage guides with thin project binding prompts
- PalBench small-sample validation

## Quick Start

Most day-to-day use can start with Mira. Mira is the default Main Pal / Leader Pal / Conductor: tell her the goal, and she will either answer as team leader, ask a focused question, hand off to a specialist Pal, or prepare a staged Runtime Task Package. Start with [Mira-first usage](docs/02-getting-started/mira-first-usage.md) and [Mira-first prompt cards](docs/02-getting-started/mira-first-prompt-cards.md).

### Codex

Use this when you open the AgentPal Workspace directly in Codex.

1. Create a new Codex project with the AgentPal directory.
2. Open [`prompts/codex/initialize-agentpal-workspace.md`](prompts/codex/initialize-agentpal-workspace.md).
3. Copy the whole prompt.
4. Paste it into the AgentPal project conversation in Codex to initialize AgentPal.
5. Start ordinary messages with Mira, or call a specialist with `/pal Name`.

Codex prompt files now live under [`prompts/codex/`](prompts/codex/). Codex workspace initialization does not require `AGENTPAL_HOME`.

More: [`docs/04-runtime-guides/01-use-with-codex.md`](docs/04-runtime-guides/01-use-with-codex.md)

### Claude Code

Use this when you want to connect AgentPal to an existing user project in Claude Code.

1. Start in your real project:

   ```text
   cd <your-project>
   claude
   ```

2. Open [`prompts/claude-code/install-agentpal-current-project.md`](prompts/claude-code/install-agentpal-current-project.md).
3. Copy the whole prompt file without editing it.
4. Paste it into Claude Code.
5. When Claude Code asks for your AgentPal Workspace path, enter the local path to the AgentPal directory, for example `<path-to-AgentPal>`.
6. Let Claude Code create or update the project-local binding files.

The Claude Code path updates project-local binding files and may update `.claude/settings.local.json`. That file is local machine configuration and should not be committed. Project memory, source maps, derived knowledge, task records, reports, governance notes, and capability inventory belong in the AgentPal Workspace under `workspace/projects/<project-id>/`, not in the external project's `.agentpal/` directory.

More: [`docs/04-runtime-guides/02-use-with-claude-code.md`](docs/04-runtime-guides/02-use-with-claude-code.md)

### Generic CLI Agent

Use this with a CLI agent that can read project files, follow Markdown / JSON instructions, keep context, and report execution evidence.

1. Start in your real project:

   ```text
   cd <your-project>
   <your-cli-agent>
   ```

2. Open [`prompts/generic-cli-agent/install-agentpal-current-project.md`](prompts/generic-cli-agent/install-agentpal-current-project.md).
3. Copy the whole prompt file without editing it.
4. Paste it into the CLI Agent.
5. When the CLI Agent asks for your AgentPal Workspace path, enter the local path to the AgentPal directory, for example `<path-to-AgentPal>`.

This is a generic compatibility path. AgentPal does not claim every CLI Agent has been fully validated.

External projects stay thin-bound: `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and protected root instruction blocks point back to the AgentPal Workspace and its `agentpal_project_record`.

More: [`docs/04-runtime-guides/03-use-with-generic-cli-agent.md`](docs/04-runtime-guides/03-use-with-generic-cli-agent.md)

## Create Your Own Pal

AgentPal includes standard Pal Pack templates under [`templates/Pal Pack/`](<templates/Pal Pack/>). Copy a template, rename it for your Pal, fill in the identity, output contract, knowledge, Skills, examples, and public-safe placeholders, then place the finished Pal Pack under [`official/pals/`](official/pals/) or the selected organization Pal area. After the Pal is registered through AgentPal central contacts, you can use it like the bundled Pals.

Available template sets:

- [`templates/Pal Pack/zh-CN/`](<templates/Pal Pack/zh-CN/>)
- [`templates/Pal Pack/en-US/`](<templates/Pal Pack/en-US/>)

To register a copied Pal Pack, run [`prompts/add-pal-to-agentpal.md`](prompts/add-pal-to-agentpal.md) from the AgentPal Workspace:

- Codex: open the AgentPal directory as its own Codex project, then paste the prompt into the AgentPal project conversation.
- Claude Code or another CLI agent: open a terminal in `<path-to-AgentPal>`, start the CLI agent there, then paste the prompt.

Most users run AgentPal from an external project during daily work. Pal registration edits AgentPal's central roster under `workspace/organization/contacts/`, so do the registration step in the AgentPal Workspace, then reinitialize the external project session if it still shows the old Pal list.

## Official Pals

| Pal | Responsibility | Direct call |
| --- | --- | --- |
| Mira | Main Pal / Leader / Conductor | `/pal Mira` |
| Atlas | Developer / Implementation Lead, Runtime Task Packages, file boundaries, evidence review | `/pal Atlas` |
| Nova | Product / Strategy Lead, product intake, problem framing, user segments, JTBD, value proposition, PRD, prioritization, roadmap, MVP/release scope, metrics, risk, GTM alignment, and product handoff | `/pal Nova` |
| Vega | Research / Intelligence Lead, source inventory, evidence matrix, research synthesis, comparative analysis, uncertainty, and knowledge distillation | `/pal Vega` |
| Rhea | System / Runtime Safety Lead, permission boundaries, no-code boundary, evidence review, release safety, rollback readiness, and incident review | `/pal Rhea` |
| PalSmith | Pal creation, job fitness governance, material ingestion, research-to-knowledge, import/export, health checks, versioning, and Runtime Task Packages | `/pal PalSmith` |
| Quinn | Quality / Verification Lead, acceptance criteria, Definition of Done, evidence review, false completion detection, regression gates, release quality gates, not-run handling, and cross-Pal review | `/pal Quinn` |
| Morgan | Document / File Workflow Lead, information architecture, content preservation, Markdown docs, Office/PDF task packages, release notes, document quality, and safe file workflows | `/pal Morgan` |
| Harper | Writing / Content Craft Lead, audience framing, voice, structure, rewriting, copywriting, narrative, social content, preservation, claim safety, and content self-review | `/pal Harper` |

Mira is the default entry Pal and Leader Pal. She handles first-contact intake, owner judgement, Context Packet shaping, risk approval framing, progress reporting, and final synthesis; specialist Pals still own their professional work and do not listen by default. Mira routes to them when appropriate, or users can call them directly with `/pal Name`.

For realistic official Pal task examples, see the [Official Pal examples index](docs/07-official-pals/official-pal-examples-index.md). These examples are non-binding learning references, not dispatch rules.

PalSmith is registered as `palsmith-pal-governor` at `official/pals/PalSmith-pal-governor` in `agentpal.json` and `workspace/organization/contacts/pals.json`.

Use PalSmith directly with `/pal PalSmith ...`. PalSmith works through Runtime Task Packages and does not require Python, Node.js, Rust, a UI, or an installer.

Start from [`docs/PalSmith.md`](docs/PalSmith.md), then use the [Runtime Task Package standard](docs/03-pal-pack-standard/14-runtime-task-package.md), [PalSmith v0.2 productization](docs/06-palsmith/README.md), [PalSmith end-to-end workflows](docs/07-authoring-pals/13-palsmith-end-to-end-workflows.md), [PalSmith Pal lifecycle](docs/07-authoring-pals/14-palsmith-pal-lifecycle.md), [PalSmith quickstart AI team](docs/07-authoring-pals/15-palsmith-quickstart-ai-team.md), [PalSmith demo script](docs/07-authoring-pals/16-palsmith-demo-script.md), and the historical [PalSmith E2E test summary archive](archive/migration-from-v0.3/release-candidate-docs/11-palsmith-e2e-test-summary.md) when preparing release-safe Pal work.

## How AgentPal Works

1. The user gives a goal.
2. Mira receives ordinary tasks.
3. Mira or the owner Pal loads selected context.
4. The Pal shapes a Task Package.
5. The host runtime executes file reads, writes, commands, tools, or publishing actions.
6. The Pal verifies evidence and reports the result.
7. Reusable experience can become a Skill, Runbook, Workflow, knowledge note, or memory candidate.

## Pal Vs Skill

| Skill | Pal |
| --- | --- |
| A single capability | A working companion |
| Usually focused on one method or task type | Organizes capabilities, context, memory, workflow, and verification |
| User often needs to remember when to use it | User remembers the Pal responsible for the work |

Skill is capability. Pal is a working companion that organizes capabilities.

## Pal Team Vs Agent Team

| Agent Team | Pal Team |
| --- | --- |
| Multiple agents executing work | Multiple Pal Packs organizing work |
| Execution belongs to agent runtimes | Execution still belongs to the host runtime |
| Can add configuration, context, and coordination overhead | Shapes context, Task Packages, collaboration, and verification |
| Useful for heavy multi-agent execution | Useful for professional perspectives without making AgentPal a runtime |

Subagents and multi-agent execution belong to the runtime layer. A Pal Team can prepare and review tasks for runtime agents, but AgentPal v0.3.0-rc.1 is not a multi-agent runtime.

## Deep Conductor

Deep Conductor is AgentPal's no-code orchestration protocol and task-package system for complex tasks. In v0.3.0-rc.1, it is represented through Markdown / JSON protocols, templates, examples, evals, E2E packages, synthesis reports, and replay evidence. It is not an automatic background executor. Host runtimes perform real execution and must return evidence. Start with [`docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md`](docs/05-orchestration-methodology/deep-conductor-e2e-usage-guide.md).

## What AgentPal Is Not

AgentPal is not:

- an Agent Runtime
- a multi-agent runtime
- a desktop app
- a web app
- an installer
- a daemon or service
- a marketplace
- a built-in PalSmith CLI, scanner, validator, importer, or exporter
- a replacement for Codex, Claude Code, OpenHands, or other runtimes

AgentPal is a Pal layer for existing runtimes. It does not require Python, Node.js, or Rust for ordinary use. The host runtime performs actual execution from Runtime Task Packages and must provide evidence for real actions.

## Documentation

- [Why Pal?](docs/01-concepts/07-why-pal.md)
- [Concepts](docs/01-concepts/)
- [Central Project Record](docs/02-concepts/central-project-record.md)
- [Project Memory in AgentPal](docs/02-concepts/project-memory-in-agentpal.md)
- [Source Map and Derived Knowledge](docs/02-concepts/source-map-and-derived-knowledge.md)
- [Repository Structure](docs/00-overview/repository-structure.md)
- [Pal Pack Standard](docs/03-pal-pack-standard/)
- [Runtime Guides](docs/04-runtime-guides/)
- [Orchestration Methodology](docs/05-orchestration-methodology/)
- [v0.2 Roadmap](docs/09-roadmap/v0.2-development-plan.md)
- [v0.3 Roadmap](docs/09-roadmap/v0.3-development-plan.md)
- [v0.3 Deep Conductor Readiness](docs/09-roadmap/v0.3-deep-conductor-readiness.md)
- [v0.3 Release Preparation Audit](docs/09-roadmap/v0.3-release-preparation-audit.md)
- [Validation and Evidence](docs/06-validation-and-evidence/)
- [Authoring Pals](docs/07-authoring-pals/)
- [Prompts](prompts/)
- [Documentation Home](docs/README.md)

## Contributing

Contributions should preserve the v0.3.0-rc.1 boundary: AgentPal is a Pal Workspace and Pal Pack standard practice for agent runtimes, with no-code Deep Conductor protocols and host Runtime execution evidence. It is not an automatic runtime.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](LICENSE).
