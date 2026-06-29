# AgentPal Orchestration Methodology

Historical note: this file is archived. Use [Pal Orchestration Methodology](../../05-orchestration-methodology/README.md) as the current public entry.

AgentPal is not a benchmark competitor to foundation models. It does not rank or compare foundation-model capability.

AgentPal defines its own problem space: how to help people use existing Agent runtimes more reliably. The core claim is that a transparent scheduling layer can improve real-world task results by choosing the right Pal, runtime, model profile, reasoning level, Skill, plugin, context slice, and verification path for the current job.

AgentPal v0.1.0-rc.1 does not implement a multi-agent runtime. The active path remains Simple Pal Mode only. The methodology in this document is a design foundation for future versions.

AgentPal does not compete with foundation models. It defines a Pal Layer methodology for using existing Agent runtimes better.

The core split is:

- Fast Route: clear tasks use one suitable Pal / Runtime / Skill with bounded context.
- Deep Conductor: future orchestration for complex tasks with workflow topology, Context Access Lists, Pal isolation, verification, and Routing Reward Memory.

In v0.1, Mira is the default Main Pal, Leader Pal, and Conductor. Users normally start with Mira; Mira judges whether to keep the task, route to an owner Pal, prepare a Task Package, or describe a future workflow design. Users do not need to constantly choose Pals, runtimes, models, Skills, plugins, or future Deep Conductor paths manually.

## Problem

Direct Agent usage often leaves the user responsible for too many coordination decisions:

- which Agent runtime to open
- which model or reasoning strength to use
- which Skill, plugin, or MCP server applies
- which project files to include
- when a specialist perspective is needed
- how to verify completion
- what to remember for next time

The result can be context bloat, false completion, repeated prompt engineering, manual multi-window coordination, and fragile acceptance checks.

## AgentPal's Position

AgentPal is a Pal layer. A Pal is a structured task-facing package of identity, knowledge, skills, context boundaries, output contracts, review habits, and learning rules.

The host runtime still reads files, writes files, runs commands, calls tools, and produces execution evidence. AgentPal organizes the thinking and context around those actions.

## Scheduling As Capability Gain

AgentPal's orchestration thesis is:

```text
same Agent runtime + same model + same project context
+ better task judgement
+ better capability selection
+ tighter context access
+ clearer task package
+ independent verification
+ routing memory
= higher acceptance and lower rework in real tasks
```

The gain is not from claiming a stronger model. It is from using available capabilities more deliberately.

## Design Layers

AgentPal's future orchestration design has seven layers:

1. Single entry through Mira / Main Pal.
2. Task judgement for complexity, risk, budget, context, and verification need.
3. Capability Inventory for runtime, model, reasoning, Skill, plugin, MCP, and Pal profiles.
4. Workflow topology selection.
5. Context Access List and Task Package.
6. Verification and evidence review.
7. Routing Reward Memory and PalBench measurement.

## Difference From Direct Single-Agent Use

Direct use asks one Agent to infer the whole process from a prompt. AgentPal adds structured intermediate decisions:

- who should own the work
- what context is enough
- what should not be read
- what evidence is required
- whether a verifier or independent review is worth the cost
- whether a previous routing path worked

## Difference From Manual Skill Use

Manual Skill use depends on the user remembering the right Skill at the right time. AgentPal treats Skills as capability profiles and judgement inputs. It can recommend a Skill candidate, explain why, and record whether it helped.

In v0.1 this remains mostly documentation and Pal judgement. In future versions, capability inventory can make the process more measurable.

## Difference From Manual Multi-Window Coordination

Manual multi-window work often leaks context from one answer into the next and creates agreement bias. AgentPal's future Deep Conductor design uses Context Access Lists and Pal Isolation to keep independent judgement stages separate until a planned summary step.

## Current v0.1 Scope

Active in v0.1.0-rc.1:

- Mira as the single entry Pal.
- Simple Pal Mode only.
- AI Judgement owner selection.
- selected owner Pal assets.
- Context Slicing.
- Task Packages.
- Claude Code and generic CLI project binding prompts.

Not active in v0.1.0-rc.1:

- automatic runtime probing.
- automatic model selection.
- active external Agent orchestration.
- active Subagent Mode.
- parallel Pal or runtime execution.
- Routing Reward Memory writeback as a runtime feature.

## Future Roadmap

v0.2 design target:

- Capability Inventory as structured profiles.
- Task Judgement Packet.
- Context Access List.
- Routing Decision Record.
- Verification Result Record.
- PalBench small-sample evaluation.

v0.3 design target:

- Deep Conductor topology selection.
- independent review workflows.
- best-of-N runtime experiments.
- routing memory feedback into AI Judgement.
- richer capability profile updates.

## Transparency Rule

AgentPal orchestration must be auditable. Users and maintainers should be able to see:

- why a Pal, runtime, model profile, Skill, plugin, or verification path was considered
- which context was read
- which context was skipped
- what evidence was required
- whether the result passed
- what should be tried next time

AgentPal should not become a black box.
