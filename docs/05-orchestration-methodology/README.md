# Pal Orchestration Methodology

This directory is the public entry point for AgentPal's Pal Orchestration Methodology.

AgentPal's scheduling goal is practical: in the same agent runtime, with the same model, Skills, plugins, and project context, AgentPal organizes task ownership, context, reasoning strength, runtime awareness, verification, and reusable records so users get more stable results with less context waste and less rework.

AgentPal v0.1.0-rc.1 is not a multi-agent runtime and not an execution layer. The current runtime path is Simple Pal Mode.

## Status

- Current: Simple Pal Mode, Fast Route, Task Package, Context Slicing, Asset Loading Budget, Verification Result Record templates, and Routing Decision Record templates.
- Future: Deep Conductor, richer Capability Inventory, Context Access Lists as enforceable workflow contracts, Pal Isolation and Shared Memory, Routing Reward Memory, and external runtime orchestration.
- Research: PalBench evaluates AgentPal usage methods, not model capability or model superiority.

## Why it exists

Users should not have to choose every Pal, runtime, model, Skill, plugin, context file, and verification path by hand for every task.

This methodology gives AgentPal a readable way to decide:

- who owns the work
- what context is enough
- what evidence is required
- which capability candidates may help
- what should be remembered for next time

## How it works

Start with the active v0.1 path:

1. Mira receives ordinary work.
2. Mira judges ownership case by case.
3. Clear owned work uses Fast Route to one owner Pal.
4. The owner Pal reads a bounded slice of assets and answers through its Output Contract.
5. When work must be executed or checked, the result is compressed into a Task Package with acceptance criteria and evidence requirements.

Future methodology extends this with workflow topology, Context Access Lists, isolated review, verification records, and routing memory.

## What it is not

- Not a claim that AgentPal is a stronger model.
- Not a hidden multi-agent runtime.
- Not a source-based comparison with outside projects.
- Not permission to run external agents, probes, commands, or tools without runtime evidence and user approval where needed.
- Not a reason to load the full workspace by default.

## Documents

- [00 Methodology Overview](00-methodology-overview.md)
- [01 Fast Route](01-fast-route.md)
- [02 Task Package](02-task-package.md)
- [03 Context Slicing](03-context-slicing.md)
- [04 Asset Loading Budget](04-asset-loading-budget.md)
- [05 Capability Inventory](05-capability-inventory.md)
- [Capability Inventory Minimal Usable Design](capability-inventory-minimal-usable-design.md)
- [06 Runtime / Model / Skill Awareness](06-runtime-model-skill-awareness.md)
- [07 Verification Result Record](07-verification-result-record.md)
- [08 Routing Decision Record](08-routing-decision-record.md)
- [09 Deep Conductor Future](09-deep-conductor-future.md)
- [10 Pal Isolation And Shared Memory Future](10-pal-isolation-and-shared-memory-future.md)
- [11 Pal Teams And Deep Conductor](11-pal-teams-and-deep-conductor.md)
