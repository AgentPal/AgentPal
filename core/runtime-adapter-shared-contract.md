# Runtime Adapter Shared Contract

Runtime adapters connect AgentPal to a host runtime. They are not the AgentPal rule body.

Applies to:

- Codex
- Claude Code
- generic CLI agents
- future agent CLI adapters

## Adapter Duties

An adapter may:

- help the runtime locate the AgentPal workspace root
- tell the runtime which core gates to read
- create thin project binding files
- write runtime-specific local access configuration
- preserve a short welcome message

An adapter must:

- read `core/agentpal-core-gate.md` from the AgentPal workspace root
- read contacts / registry from the AgentPal workspace root
- load selected Pal assets on demand
- keep Runtime-specific configuration separate from AgentPal rules
- parse `/pal Name` and `@Pal` as AgentPal plain-text protocols when they appear in user input
- resolve named Pals through current contacts / registry instead of copied Pal lists
- follow `orchestration/mention-and-direct-pal-protocol.md` and `orchestration/context-packet-protocol.md` for direct calls, consults, reviews, handoffs, and owner transfers
- follow `orchestration/owner-verifier-workflow-protocol.md` when a task package separates an owner Pal from a verifier Pal candidate
- follow `orchestration/parallel-independent-review-protocol.md` when a task package requests isolated reviewer candidates and synthesis
- follow `orchestration/deep-conductor-protocol.md` and `orchestration/project-conductor-workflow.md` when a task package contains a Deep Conductor plan, project task map, or next-round Runtime task package
- treat Runtime Skill-aware packages as host Runtime instructions that still require current availability and permission evidence

## Adapter Must Not

- copy full AgentPal rules into external projects
- maintain its own independent copy of First Pal Gate
- maintain a stale Pal roster as source of truth
- copy full orchestration protocols into `.agentpal/`
- copy full Mira assets into `.agentpal/`
- turn future design into current behavior
- treat Runtime as a Pal
- treat `/pal` or `@Pal` as required native CLI features
- copy full chat history into Context Packets
- present Context Packet as an automatic message bus
- present Owner + Verifier as automatic background multi-agent execution
- present Parallel Independent Review as automatic background parallel execution
- present Deep Conductor or Project Conductor as an automatic background task system
- claim Runtime Skill candidates were used before the host Runtime verifies and reports evidence
- let verifier work rely only on an owner completion claim when evidence context is missing
- feed one reviewer candidate another reviewer draft during independent review

If a core rule changes, adapter behavior should inherit the change by reading the AgentPal workspace core gates, without rewriting every adapter prompt.

## `/pal` And `@Pal` Handling

If the host runtime has no native slash-command or mention support, it should still treat `/pal Name` and `@Pal` as user text:

- `/pal Name` means direct owner-candidate mode for the named Pal after core gates.
- `@Pal` means consult or review by default and must use a bounded Context Packet.
- explicit handoff or takeover wording may become `handoff` or `owner_transfer`.
- all named Pals are resolved from `contacts/pals.json` and `registry/pal.index.json`.
- Context Packets must use `can_read`, `cannot_read`, `needed_output`, and `verification_requirements`; they must not copy full chat history.

This remains no-code protocol behavior. It does not start background Pals, Subagent Mode, external Agent calls, Deep Conductor automation, or runtime parallelism.

## Deep Conductor / Project Conductor Handling

If a task package includes a Deep Conductor plan, Project Conductor task map, or next-round Runtime task package, the adapter should help the host Runtime follow the package as a no-code plan:

1. confirm the target Runtime and any Runtime Skill candidates are currently available before using them;
2. respect `required_context` and `forbidden_context`;
3. execute only the approved next-round scope;
4. preserve Pal-owned Skill and Runtime-installed Skill separation;
5. return evidence, not-run items, blockers, and changed or read files;
6. leave verification and Routing Memory writeback to the Pal-layer package unless explicitly asked to prepare evidence.

Deep Conductor and Project Conductor are not a background project manager, queue, service, database, scanner, validator, or automatic execution loop.

## Owner + Verifier Handling

If a task package includes Owner + Verifier stages, the adapter should help the host runtime follow the stages sequentially:

1. owner task judgement and owner task package;
2. evidence collection by the execution layer when requested and allowed;
3. bounded Verifier Context Packet;
4. Verification Result Record with verdict `pass`, `fail`, or `blocked`;
5. Mira or owner synthesis.

The verifier context must contain evidence to check, expected criteria, allowed files, missing or not-run checks, and known risks. The runtime must not infer a pass from a completion report alone.

## Parallel Independent Review Handling

If a task package includes Parallel Independent Review stages, the adapter may help the host runtime process Reviewer Context Packets sequentially while preserving isolation:

1. create one Reviewer Context Packet per reviewer candidate;
2. run or simulate each review from its own packet only;
3. keep peer drafts, hidden reasoning, and intermediate notes out of later reviewer packets;
4. collect reviewer final reports;
5. let Mira or the owner synthesize agreement, disagreement, conflicts, risks, decision options, and next step.

This remains no-code staged workflow behavior. It is not automatic parallel runtime execution, Subagent Mode, external Agent orchestration, a message bus, or a background worker.
