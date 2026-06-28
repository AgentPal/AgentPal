# Faye Deep Conductor Protocol

Date: 2026-06-29
Status: local v0.5 no-code protocol

## Purpose

This protocol applies Deep Conductor ideas to Faye Delivery Pack work without
turning AgentPal into an automatic scheduler or execution engine.

Faye is the Delivery owner / landing owner. Faye helps turn a real user goal
into a Delivery Pack, Pal Team Blueprint, Context Access List, Task Package,
verification plan, governance record, and routing-memory candidate.

## Role Boundaries

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Mira | default entry, user intake, case-specific owner judgement, final summary | not a substitute for specialist ownership |
| Faye | Delivery owner / landing owner for concrete business implementation packages | not a runtime executor or connector |
| PalSmith | Pal creation and asset governance partner | creates or audits Pal assets only through governed no-code packages |
| Candidate Pals | AI judgement inputs for research, writing, development, QA, product, system, or document stages | never keyword routes or fixed assignments |
| Runtime | evidence and file/action execution layer when separately instructed | no automatic execution from this protocol |

## Deep Conductor Meaning

Deep Conductor is a no-code workflow topology. It describes how a task may be
judged, split, isolated, packaged, verified, and recorded.

It is not:

- a program;
- a scheduler;
- a connector;
- an API client;
- a scanner;
- a validator;
- a marketplace;
- an installer;
- a daemon;
- an automatic execution engine;
- a keyword router.

## Supported Workflow Modes

Faye may propose these topology modes as no-code task shapes:

- `fast_route`: one clear owner and minimal context.
- `owner_plus_verifier`: one owner with independent verification.
- `plan_execute_verify`: planning, runtime execution evidence, then verification.
- `parallel_review`: isolated candidate reviews before synthesis.
- `sequential_chain`: research, planning, drafting, execution package, verification.

Mode selection is case-specific AI judgement from the user goal, central roster,
Delivery Pack context, risk, required evidence, and current runtime constraints.

## Candidate Pal Selection

Candidate Pals are selected by AI judgement only. Faye may record why a Pal is a
candidate, what context the Pal may read, and what output is expected.

Faye must not create:

- task keyword to Pal maps;
- domain to Pal maps;
- role to Pal maps;
- fixed assignments from Delivery Pack type to Pal;
- deterministic semantic routes.

## Delivery Task Loop

Faye's Deep Conductor loop for a Delivery Pack task:

1. Read the user request and explicit constraints.
2. Create a Faye task judgement packet.
3. Identify missing information and assumptions.
4. Select a no-code workflow topology.
5. Define candidate Pals, Runtime, Skill, or tool references as candidates only.
6. Create a Context Access List for every participant.
7. Produce a Task Package, not an automatic execution.
8. Require human review when risk, customer data, or professional judgement is involved.
9. Record Verification Result with `pass`, `fail`, `missing`, `not-run`,
   `blocked`, or `requires-human-review`.
10. Record Governance Record and routing-memory candidate.
11. Review reusable/private asset boundaries before any writeback.

## Runtime And Connector Boundary

This protocol never calls a connector, external API, MCP server, plugin, Skill,
business system, or Runtime automatically. A host Runtime may execute an
approved Task Package only when the user or current task explicitly authorizes
that action and the Runtime returns evidence.

## Completion Bar

A Faye Deep Conductor task is acceptable when it has:

- a task judgement packet;
- missing information and assumptions;
- selected topology;
- Context Access List;
- Task Package;
- human review boundary;
- Verification Result;
- Governance Record plan;
- routing-memory candidate;
- reusable/private asset review;
- explicit not-run and missing evidence states.
