# AgentPal

**AgentPal is a lightweight framework for building multi-AI teams.**

AgentPal can be installed or mounted under Agent Runtimes such as Codex, Claude Code, and OpenCode, so an existing Agent can gain an AI team organization layer made of multiple professional Pals.

AgentPal does not replace Agent systems such as Codex, Claude Code, OpenClaw, Hermes, or workbuddy.
It focuses on a different question:

> How can users organize a collaborative AI team in a lighter, easier-to-maintain, lower-cost way?

In one sentence:

> **AgentPal = a Pal team organization layer for existing Agents.**

---

## What Is A Pal?

AgentPal uses **Pals** as the basic organization unit of an AI team.

In AgentPal:

```text
Skill is a capability package.
Pal is a working partner that uses Skills.

Agent is the execution runtime.
Pal is a working partner that uses Agents.
```

In other words, a Pal is not a Skill and not a full Agent Runtime.

A Pal sits between Skill and Agent:

```text
Skill  -> capability package
Pal    -> working partner that uses Skills and Agents
Agent  -> execution runtime
```

A Pal can have its own identity, responsibility, knowledge, memory, Skills, workflow, and collaboration boundary.
It knows what it is responsible for, when it should use a Skill, and when it should hand the task to Codex, Claude Code, OpenCode, or another Agent Runtime for execution.

---

## Skill, Pal, And Agent

### Skill Is A Capability Package

A Skill is usually a reusable capability, prompt, process, or tool-use instruction.

For example:

- writing style Skill
- code review Skill
- Office document Skill
- search and research Skill
- Skill for a tool or plugin

The value of a Skill is that it helps AI do a certain kind of work better.

But a Skill is usually lightweight. It usually does not carry a long-term role, memory, collaboration, project understanding, or team division of work.

> **A Skill gives AI a capability.**

### Agent Is The Execution Runtime

An Agent is the runtime layer that actually executes tasks.

For example: Codex, Claude Code, OpenCode, OpenHands, or Agents created inside systems such as OpenClaw, Hermes, and workbuddy.

An Agent can read and write files, call tools, run commands, plan steps, and complete tasks.

> **An Agent executes.**

### Pal Is A Working Partner

A Pal is a working partner that uses Skills and Agents.

A Pal can:

- have a clear identity and responsibility
- remember users, projects, and past work
- use its own knowledge and workflow
- reference and combine multiple Skills
- judge which Agent Runtime should be used
- collaborate with other Pals
- split tasks to suitable Agents or sub-Agents
- summarize execution results and report back to the user

> **A Pal understands the role, organizes collaboration, uses Skills, and directs Agents to execute.**

---

## Pal Vs Skill

| Item | Skill | Pal |
| --- | --- | --- |
| Core positioning | capability package | working partner that uses capability packages |
| Identity | usually no | yes |
| Long-term responsibility | usually no | yes |
| Memory | usually no | yes |
| Knowledge system | limited | yes |
| Can combine multiple Skills | limited | yes |
| Can collaborate with other roles | usually no | yes |
| Can judge which Agent to use | usually no | yes |
| More like | tool capability | team member |

In short:

> **Skill is a capability. Pal is the working partner that knows how to use capabilities.**

---

## Pal Vs Agent

| Item | Agent | Pal |
| --- | --- | --- |
| Core positioning | execution runtime | working partner that uses Agents |
| Real execution | yes | usually handed to an Agent |
| Reads files / calls tools | yes | through an Agent or Skill |
| Stable role identity | not always | yes |
| Independent memory and knowledge | depends on the system | yes |
| Lightweight creation of many roles | higher cost | lighter |
| Suitable for organizing AI teams | possible, but usually heavier | naturally suitable |
| More like | executor / runtime | team member / task owner |

AgentPal does not want to rebuild an Agent Runtime.

Its goal is:

> **Give existing Agents team, role, memory, workflow, and collaboration ability.**

---

## Multi-Pal Vs Multi-Agent

Multi-Pal and multi-Agent teams share the same goal:

> They both use multiple AI roles to finish tasks that are more complex than what one AI can handle alone.

The difference is the implementation shape.

This is not a comparison between AgentPal and systems such as OpenClaw, Hermes, or workbuddy themselves.
It is a comparison between:

```text
Multi-Pal teams created by AgentPal
vs
Multi-Agent teams created inside systems such as OpenClaw / Hermes / workbuddy
```

| Item | Multi-Agent | Multi-Pal |
| --- | --- | --- |
| Goal | multi-role collaboration | multi-role collaboration |
| Basic unit | Agent | Pal |
| Execution shape | multiple Agents run separately | Pals organize tasks and call Agents when needed |
| Usage complexity | usually higher | lighter |
| Runtime cost | can be higher | controllable |
| Context management | more complex across Agents | Pals share organization-layer context |
| Must every role run as an Agent? | usually yes | no |
| Friendly for ordinary users building a team | has a threshold | friendlier |
| Suitable for complex tasks | yes | also yes, with Agents called when needed |

AgentPal's idea is:

> **Not every AI role must become an independently running Agent.**

In many cases, a Pal only needs clear identity, knowledge, memory, and workflow to take a team role well.
Only when a task really needs independent context, parallel execution, isolation, or a professional toolchain does a Pal need to call a sub-Agent or external Agent.

So:

```text
Multi-Agent = multiple executing agents
Multi-Pal   = multiple collaborative working partners that use Agents
```

AgentPal can use multiple Agents, but it does not force every role to become an Agent.

---

## Built-In Pals

AgentPal includes a set of common Pals to help users build an AI team out of the box.

The current v0.5 built-in Pal roster follows [`workspace/organization/contacts/pals.json`](workspace/organization/contacts/pals.json).

| Pal | Role | Main use |
| --- | --- | --- |
| Mira | main secretary / coordinator | understands user needs and coordinates Pals, Agents, Skills, and project context |
| PalSmith | Pal creation and governance expert | creates, optimizes, checks, upgrades, and designs Pals and Pal teams |
| Faye | FDE / solution design expert | organizes business scenarios, user flows, data, interfaces, risks, and delivery paths |
| Atlas | development expert | handles code implementation, architecture analysis, engineering task breakdown, and technical execution |
| Nova | product and experience expert | handles product design, user flows, interaction experience, and feature tradeoffs |
| Quinn | testing and quality expert | handles test design, acceptance criteria, regression checks, and quality review |
| Vega | research expert | handles research, external information organization, and knowledge analysis |
| Morgan | document and file workflow expert | handles documentation structure, file workflows, and Office/PDF task packages |
| Harper | writing and content expert | handles writing, copy, narrative, voice, editing, and claim safety |
| Rhea | system and runtime safety expert | handles runtime boundaries, permissions, no-code safety, and release safety |

---

## Use PalSmith And Faye To Build Your Own AI Team

The built-in PalSmith and Faye help users move from "using built-in Pals" to "creating their own professional AI team."

### PalSmith

PalSmith creates and governs Pals.

It can help you:

- create a new Pal
- design a Pal's identity, responsibility, knowledge, memory, and Skills
- check whether a Pal is too broad, too weak, or duplicated
- upgrade an existing Pal
- design a full Pal team

### Faye

Faye handles FDE-style solution design.

She can help turn real business needs into:

- business scenario definition
- user flow
- data list
- system interface list
- risks
- acceptance criteria
- delivery steps
- which Pals need to collaborate
- which parts need development
- which parts can be completed by existing Agents / Skills

PalSmith is better at building AI teams.
Faye is better at turning real business into an executable solution.

---

## Quick Start

For daily use, you can start with Mira. Mira is the default Main Pal / Leader Pal / Conductor: tell her your goal, and she will judge whether to organize it directly, ask key follow-up questions, route it to a specialist Pal, or generate a staged Runtime Task Package. You can start with [Mira-first usage](docs/02-getting-started/mira-first-usage.md) and [Mira-first prompt cards](docs/02-getting-started/mira-first-prompt-cards.md).

### Codex

Use this path when you want AgentPal available globally in Codex, then add or remove the AgentPal team from any Codex project.

In Codex, run the AgentPal Codex install document:

```text
Please execute the AgentPal Codex install document:
https://github.com/AgentPal/AgentPal/blob/master/plugins/codex/codex-install.md
```

The install document installs the global Codex plugin `agentpal@agentpal`.

After installation, open any Codex project and say:

```text
Add AgentPal to this project
```

To remove AgentPal from the current project while keeping the global Codex plugin installed, say:

```text
Remove AgentPal from this project
```

The project binding is thin. It writes only `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and the AgentPal protected block in `AGENTS.md`.

See: [`plugins/codex/codex-install.md`](plugins/codex/codex-install.md)

### Claude Code

Use this path when you want to connect AgentPal to an existing real project.

1. Enter your project directory first:

   ```text
   cd <your-project>
   claude
   ```

2. Open [`prompts/claude-code/install-agentpal-current-project.md`](prompts/claude-code/install-agentpal-current-project.md).
3. Copy the whole prompt file directly; you do not need to edit it first.
4. Paste it into Claude Code.
5. When Claude Code asks for the AgentPal Workspace path, enter your local AgentPal directory, for example `<path-to-AgentPal>`.
6. Let Claude Code create or update the local binding files in the current project.

The Claude Code path writes local binding files in the project and may update `.claude/settings.local.json`. This is local machine configuration and should not be committed.

See: [`docs/04-runtime-guides/02-use-with-claude-code.md`](docs/04-runtime-guides/02-use-with-claude-code.md)

### Generic CLI Agent

Use this path for CLI Agents that can read project files, follow Markdown / JSON instructions, maintain context, and report execution evidence.

1. Enter your project directory first:

   ```text
   cd <your-project>
   <your-cli-agent>
   ```

2. Open [`prompts/generic-cli-agent/install-agentpal-current-project.md`](prompts/generic-cli-agent/install-agentpal-current-project.md).
3. Copy the whole prompt file directly; you do not need to edit it first.
4. Paste it into the CLI Agent.
5. When the CLI Agent asks for the AgentPal Workspace path, enter your local AgentPal directory, for example `<path-to-AgentPal>`.

This is a generic compatibility path. AgentPal does not promise that every CLI Agent has been fully verified.

See: [`docs/04-runtime-guides/03-use-with-generic-cli-agent.md`](docs/04-runtime-guides/03-use-with-generic-cli-agent.md)

---

## License

AgentPal is open source under the MIT License.
