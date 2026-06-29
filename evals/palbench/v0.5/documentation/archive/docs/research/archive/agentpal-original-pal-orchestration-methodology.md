# AgentPal Original Pal Orchestration Methodology

Historical note: this file is archived. Use [Pal Orchestration Methodology](../../05-orchestration-methodology/README.md) as the current public entry.

AgentPal defines its own Pal Layer methodology for practical agent runtimes.

The core idea is that a transparent Pal layer can improve practical agent work by selecting the right Pal, runtime, model profile, reasoning level, Skill, plugin, context slice, verification path, and memory boundary for the current task.

AgentPal does not rank or compare foundation-model capability. It is not a model benchmark target and does not compete with foundation models.

AgentPal transparent Pal orchestration separates:

- Fast Route: use one suitable Pal / Runtime / Skill for clear tasks.
- Deep Conductor: future orchestration for complex tasks using workflow topology, Context Access Lists, isolation, verification, and routing memory.

AgentPal v0.1 keeps the active path simple: Mira as the default Main Pal, Leader Pal, and Conductor; Simple Pal Mode; Context Slicing; Task Package; and one-prompt project install. Deep Conductor remains future design and is not active in v0.1.0-rc.1.

## AgentPal Method Map

| AgentPal term | Meaning |
| --- | --- |
| Single Entry via Mira | Ordinary users start with Mira instead of manually choosing every Pal, runtime, Skill, or plugin. |
| Fast Route | Clear tasks are routed to one suitable owner Pal or handled by Mira when the work is Mira-owned. |
| Task Package | A compact handoff shape with goal, context, constraints, steps, acceptance criteria, risks, and evidence requirements. |
| Context Slicing | Read the smallest useful file and memory slice instead of loading all assets. |
| Asset Loading Budget | A bounded loading policy for Pal files, project files, memory summaries, examples, evals, and reports. |
| Context Access List | A future design asset for declaring what a workflow step may read, receive, and output. |
| Routing Decision Record | A future design asset for recording why a route was selected and whether it worked. |
| Verification Result Record | A future design asset for separating completion claims from evidence. |
| Runtime Capability Awareness | Runtime, model, Skill, plugin, MCP, and Pal capability profiles used as judgement inputs. |
| Model and Reasoning Routing | Choosing model and reasoning strength by task risk, complexity, cost, and verification needs. |
| Pal Isolation and Shared Memory | Future design for keeping independent judgement separate while sharing cleaned, safe learning across workflows. |
| PalBench small-sample validation | Qualitative smoke validation for AgentPal usage methods, not a foundation-model leaderboard. |

## Current v0.1 Practice

Current in v0.1.0-rc.1:

- Simple Pal Mode only.
- Mira as the single entry Pal.
- AI Judgement owner selection.
- selected owner Pal assets.
- Context Slicing.
- Asset Loading Budget.
- Task Packages.
- PalBench small-sample smoke validation.
- Claude Code and generic CLI project binding prompts.

Future design only in v0.1.0-rc.1:

- Deep Conductor.
- active Subagent Mode.
- parallel child workflows.
- active external Agent orchestration.
- automatic runtime probing.
- automatic model selection.
- Routing Reward Memory writeback as a runtime feature.
- Pal Isolation and Shared Memory as active runtime behavior.

Subagent behavior belongs to the Runtime layer, not to the Pal itself.

## What AgentPal Uses

AgentPal uses:

- single entry for ordinary users
- capability inventory instead of manual tool hunting
- task judgement before execution
- context access boundaries
- independent review stages when useful and available
- verification records
- routing memory as future design
- transparent explanations

## What AgentPal Does Not Claim

AgentPal does not claim:

- to be a stronger model
- to make foundation-model capability claims
- to be a full multi-agent runtime
- to run hidden multi-Agent execution in v0.1
- to make automatic external Agent calls
- to improve every task automatically
- to replace Codex, Claude Code, OpenClaw, Hermes, or other runtimes

External runtimes and products may be compared neutrally as runtime categories or future compatibility targets. They are not described as the source of AgentPal's Pal methodology.

## Capability Candidate Types

In AgentPal, a capability candidate can mean:

- a Pal Pack
- an Agent runtime
- a model profile
- a reasoning strength
- a Skill
- a plugin
- an MCP server
- a verification method

These are judgement inputs. They do not become hard-coded routes.

## Context Access

AgentPal's Context Access List design extends existing Context Slicing and Task Package protocols:

- `can_read_paths`
- `can_read_summaries`
- `can_receive_outputs_from`
- `cannot_read`
- content-read budget
- sensitive context boundary
- output contract
- verification requirement

## Isolation

If future AgentPal workflows use multiple Pal perspectives, independent judgement should happen before cross-reading other drafts. Otherwise the workflow collapses into group-chat agreement.

Isolation prevents:

- first-answer anchoring
- copied mistakes
- redundant opinions
- noisy context expansion
- false consensus

## Shared Memory

AgentPal should share only cleaned, task-safe learning across workflows:

- routing success and failure
- runtime fit
- model/reasoning fit
- Skill usefulness
- verification outcome
- user acceptance
- rework reason

It should not share raw private content, credentials, unrelated user memory, or full project files by default.

## Transparency

AgentPal should remain transparent and inspectable:

- users can ask why a route was selected
- maintainers can review routing records
- capability profiles are readable files
- Context Access Lists are explicit design assets
- PalBench records small-sample evidence instead of slogans

The goal is not hidden orchestration. The goal is better practical agent use through AgentPal's own Pal Workspace methodology.
