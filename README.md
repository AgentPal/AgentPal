# AgentPal

AgentPal is a Pal Team and Pal Pack standard practice for agent runtimes.

AgentPal gives every agent a Pal.

AgentPal v0.1.0-rc.1 is a Markdown / JSON / protocol workspace for runtimes such as Codex, Claude Code, and other CLI agents that can read structured workspace files. It is not an Agent runtime, not a multi-agent runtime, not an execution layer, not a desktop app, not a web app, and not an installer.

## Why AgentPal?

When users want agents to work better, they usually try one of two paths:

- add more Skills
- build Agent teams

Skills are lightweight, but they can become fragmented. A Skill is often single-purpose, easy to forget, hard to combine, and usually does not own memory, workflow, verification, or long-term context.

Agent teams can be powerful, but they are often heavy. They may require complex configuration, repeated context, more token cost, role coordination, result merging, and stronger permission boundaries.

AgentPal adds the missing middle layer: Pal. A Pal turns many skills, knowledge cards, workflows, memories, and verification rules into a few memorable working companions.

Users should not need to remember hundreds of skills. They should be able to remember a few Pals and what each Pal is responsible for.

## What Is A Pal?

A Pal is not a single Skill.

A Pal is not a new Agent runtime.

A Pal is a portable working companion made of identity, knowledge, skills, memory rules, workflows, context rules, output contracts, verification habits, and collaboration protocols.

The name Pal means a memorable working companion, not a tool name. In AgentPal, a Pal helps the current runtime understand the user's goal, load the right context, shape a Task Package, use relevant Skills or fallback methods, and check whether the result is actually complete.

Learn more about Pal:

- [Why Pal?](docs/01-concepts/07-why-pal.md)
- [Pal Teams and Deep Conductor](docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md)

## What Works Today

AgentPal v0.1.0-rc.1 currently provides:

- Markdown / JSON / protocol workspace assets
- Simple Pal Mode only
- Mira as the default Main Pal / Leader / Conductor
- 8 official bundled Pals
- `/pal Name` explicit Pal calls
- Fast Route for clear owner-Pal handoff
- Task Package rules
- Context Slicing
- Asset Loading Budget
- Codex, Claude Code, and Generic CLI Agent usage guides
- PalBench small-sample validation

## Quick Start

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
3. Find this line:

   ```text
   AGENTPAL_HOME = <replace-with-your-AgentPal-path>
   ```

4. Replace `<replace-with-your-AgentPal-path>` with your local AgentPal repository path, for example:

   ```text
   AGENTPAL_HOME = D:/Tools/AgentPal
   AGENTPAL_HOME = /Users/you/AgentPal
   ```

5. Copy the whole prompt file.
6. Paste it into Claude Code.

The Claude Code path updates project-local binding files and may update `.claude/settings.local.json`. That file is local machine configuration and should not be committed.

More: [`docs/04-runtime-guides/02-use-with-claude-code.md`](docs/04-runtime-guides/02-use-with-claude-code.md)

### Generic CLI Agent

Use this with a CLI agent that can read project files, follow Markdown / JSON instructions, keep context, and report execution evidence.

1. Start in your real project:

   ```text
   cd <your-project>
   <your-cli-agent>
   ```

2. Open [`prompts/generic-cli-agent/install-agentpal-current-project.md`](prompts/generic-cli-agent/install-agentpal-current-project.md).
3. Find this line and replace `<replace-with-your-AgentPal-path>` with your local AgentPal repository path:

   ```text
   AGENTPAL_HOME = <replace-with-your-AgentPal-path>
   ```

4. Copy the whole prompt into the CLI Agent.

This is a generic compatibility path. AgentPal does not claim every CLI Agent has been fully validated.

More: [`docs/04-runtime-guides/03-use-with-generic-cli-agent.md`](docs/04-runtime-guides/03-use-with-generic-cli-agent.md)

## Create Your Own Pal

AgentPal includes standard Pal Pack templates under [`templates/Pal Pack/`](<templates/Pal Pack/>). Copy a template, rename it for your Pal, fill in the identity, output contract, knowledge, Skills, examples, and public-safe placeholders, then place the finished Pal Pack under [`pals/`](pals/). After the Pal is registered through AgentPal contacts and registry, you can use it like the bundled Pals.

Available template sets:

- [`templates/Pal Pack/zh-CN/`](<templates/Pal Pack/zh-CN/>)
- [`templates/Pal Pack/en-US/`](<templates/Pal Pack/en-US/>)

To register a copied Pal Pack, run [`prompts/add-pal-to-agentpal.md`](prompts/add-pal-to-agentpal.md) from the AgentPal Workspace:

- Codex: open the AgentPal directory as its own Codex project, then paste the prompt into the AgentPal project conversation.
- Claude Code or another CLI agent: open a terminal in `<path-to-AgentPal>`, start the CLI agent there, then paste the prompt.

Most users run AgentPal from an external project during daily work. Pal registration edits AgentPal's own `contacts/` and `registry/` files, so do the registration step in the AgentPal Workspace, then reinitialize the external project session if it still shows the old Pal list.

## Official Pals

| Pal | Responsibility | Direct call |
| --- | --- | --- |
| Mira | Main Pal / Leader / Conductor | `/pal Mira` |
| Atlas | Development and engineering | `/pal Atlas` |
| Nova | Product and requirements | `/pal Nova` |
| Vega | Research and analysis | `/pal Vega` |
| Rhea | System, environment, and tools | `/pal Rhea` |
| Quinn | Quality, verification, and release checks | `/pal Quinn` |
| Morgan | Documents, Office, PDF, and file work | `/pal Morgan` |
| Harper | Writing, communication, and editing | `/pal Harper` |

Mira is the default entry Pal. Specialist Pals do not listen by default; Mira routes to them when appropriate, or users can call them directly with `/pal Name`.

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

Subagents and multi-agent execution belong to the runtime layer. A Pal Team can prepare and review tasks for runtime agents, but AgentPal v0.1.0-rc.1 is not a multi-agent runtime.

## Deep Conductor

Deep Conductor is AgentPal's future advanced orchestration design for complex tasks. It is not active in v0.1.0-rc.1. For the current release, use Simple Pal Mode, Fast Route, Task Packages, Context Slicing, and bounded Pal collaboration. More: [`docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md`](docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md)

## What AgentPal Is Not

AgentPal is not:

- an Agent Runtime
- a multi-agent runtime
- a desktop app
- a web app
- an installer
- a daemon or service
- a marketplace
- a replacement for Codex, Claude Code, OpenHands, or other runtimes

AgentPal is a Pal layer for existing runtimes. The host runtime performs actual execution and must provide evidence for real actions.

## Documentation

- [Why Pal?](docs/01-concepts/07-why-pal.md)
- [Concepts](docs/01-concepts/)
- [Pal Pack Standard](docs/03-pal-pack-standard/)
- [Runtime Guides](docs/04-runtime-guides/)
- [Orchestration Methodology](docs/05-orchestration-methodology/)
- [Validation and Evidence](docs/06-validation-and-evidence/)
- [Authoring Pals](docs/07-authoring-pals/)
- [Prompts](prompts/)
- [Documentation Home](docs/README.md)

## Contributing

Contributions should preserve the v0.1.0-rc.1 boundary: AgentPal is a Pal Workspace and Pal Pack standard practice for agent runtimes, with Simple Pal Mode as the only active task-handling path.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](LICENSE).
