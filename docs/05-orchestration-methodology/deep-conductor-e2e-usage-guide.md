# Deep Conductor E2E Usage Guide

Deep Conductor E2E is the no-code end-to-end package shape for complex AgentPal work. It composes goal intake, memory continuity, Capability Inventory, Context Budget, workflow topology, Context Packets, Runtime Skill-aware packages, verification, synthesis, Routing Memory, and next-round continuation into one auditable plan.

It is a Markdown/JSON methodology artifact. It is not an executor, scheduler, background workflow, service, database, token meter, cost calculator, native router, UI, CLI, scanner, validator, installer, daemon, or automation runtime.

## What It Combines

Deep Conductor E2E combines the v0.3 building blocks from R52-R59:

- Context Packet and Context Access List for bounded handoff.
- Owner + Verifier for independent evidence review.
- Parallel Independent Review when multiple independent perspectives are useful.
- Plan -> Execute -> Verify when a host Runtime performs real actions.
- Deep Conductor Master Loop and Project Conductor Workflow for project-level task maps.
- Cross-Runtime Pal Memory for bounded continuity across host Runtimes.
- Runtime-installed Skill Orchestration for host Skill/plugin/MCP candidates.
- Context Budget for qualitative read tiers, profile reads, memory reuse, and verification cost protection.
- Routing Memory writeback as a public-safe candidate, not a route rule.

## Suitable Tasks

Use an E2E package when the user goal has several material stages, durable project state, execution evidence needs, or cross-runtime continuity.

Good fits include:

- release preparation with docs, quality, safety, and publishing evidence;
- research that must become a deliverable such as an HTML report or decision brief;
- PalSmith AI team creation with asset governance, readiness review, and registry proposals;
- continuation after switching from one host Runtime to another;
- document, PDF, spreadsheet, or browser tasks that may need host Runtime Skills;
- work where memory reuse, capability profiles, and context limits materially change the outcome.

## Unsuitable Tasks

Do not use Deep Conductor E2E for:

- ordinary chat, one-question answers, or simple owner handoff;
- tasks with one clear owner and no material verification or memory need;
- high-risk actions without explicit user approval;
- hidden background work, automatic multi-runtime execution, or automatic capability probing;
- exact token accounting unless the host Runtime provides exact metering evidence;
- cases where the user explicitly asks for a generic runtime answer or no Pal mode.

## E2E Output Structure

A complete E2E response usually returns:

1. `Deep Conductor E2E Package`
2. `Context Budget Plan`
3. `Context Packets`
4. `Runtime Skill-aware packages`
5. `Verification plan`
6. `E2E Synthesis Report`
7. `Routing Memory candidate`
8. `Next-round recommendation`

For real execution, the host Runtime may follow the packages by stage and return evidence. AgentPal does not execute the package by itself.

## Workflow: Project Release

1. Capture the user release goal, release scope, and publish boundary.
2. Read approved release memory and current release assets inside the Context Budget.
3. Use Capability Inventory for current Pal, Runtime, model, reasoning, and Skill candidates.
4. Select a topology such as Owner + Verifier plus Plan -> Execute -> Verify.
5. Prepare owner, verifier, safety, and Runtime task packages.
6. Require evidence for docs consistency, no-code boundary, JSON validity, public safety, Git state, tag/release actions, and not-run items.
7. Synthesize pass/fail/blocked status and write a Routing Memory candidate.

## Workflow: Research To Deliverable

1. Frame the research question, audience, freshness need, and final deliverable.
2. Reuse approved memory and source inventories before full-source reads.
3. Select research, writing/document, implementation-shaped, and verification stage candidates through case-specific judgement.
4. Use Runtime Skill-aware packages only for host-provided search, browser, document, or repository capabilities.
5. Require source inventory, evidence matrix, deliverable artifact path, and verification notes.
6. Produce a synthesis report that separates fact, inference, recommendation, uncertainty, and user decisions.

## Workflow: AI Team Creation

1. PalSmith frames the team goal, user scenarios, roles, assets, and readiness criteria.
2. Memory and Capability Inventory inform candidate Pal responsibilities without forcing contacts/registry changes.
3. Context Packets separate Pal asset design, knowledge ingestion, readiness review, and quality checks.
4. Runtime task packages may request bounded file edits only after approval.
5. Synthesis reports asset completeness, conflicts, missing evidence, and next registration decision.

## Workflow: Cross-Runtime Continuation

1. Read approved Pal Project Memory Snapshot, Routing Memory summary, Runtime Skill Usage Memory, and Verification Memory.
2. Mark memory as valid, stale, missing, private, or not approved.
3. Re-check current host Runtime capability instead of assuming previous Runtime ability still exists.
4. Prepare continuation packages with already-done work, do-not-repeat items, current verification needs, and writeback candidates.
5. Return a synthesis report with what continued, what changed, and what needs user decision.

## Workflow: Runtime Skill-aware Document Task

1. Morgan or another judged owner frames document purpose, source preservation, output format, and privacy boundary.
2. Capability Inventory names host Runtime Skill/plugin/MCP candidates such as document rendering or extraction only as candidates.
3. Runtime Skill availability is checked by the host Runtime inside the package scope.
4. Fallback instructions handle unavailable Skills.
5. Verification includes source preservation, rendered/exported artifact evidence, accessibility or layout notes when relevant, and not-run items.

## User Quality Check

The user can check an E2E output by asking:

- Does it name the actual user goal and whether this is project-level or single-task?
- Does it state memory used or honestly say memory is missing/not approved?
- Does it use Capability Inventory as input, not as fixed routing?
- Does it include a Context Budget with allowed and forbidden reads?
- Does it select a workflow topology and explain the case-specific reason?
- Does it produce Context Packets and Runtime Skill-aware packages only where needed?
- Does verification survive cost pressure?
- Does the synthesis report preserve conflicts, risks, missing evidence, and not-run items?
- Does Routing Memory remain a candidate, not a rule?
- Does it avoid internal local paths, secrets, and private project facts in public examples?

## No-code Boundary

Deep Conductor E2E is no-code orchestration documentation. It may produce task packages that a host Runtime follows with user approval and evidence. It must not create program files, background jobs, native commands, hidden routing tables, databases, scanners, validators, installers, token meters, cost calculators, services, daemons, or UI.
