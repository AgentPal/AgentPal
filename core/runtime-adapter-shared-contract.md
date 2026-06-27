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
- follow `docs/05-orchestration-methodology/cross-runtime-pal-memory.md` and `orchestration/memory-boundary-protocol.md` when a task continues across host Runtimes or uses memory snapshots
- read Pal Project Memory Snapshot, Routing Memory summary, Runtime Skill Usage Memory, and Verification Memory when a task package names them and access is available
- treat Runtime Skill-aware packages as host Runtime instructions that still require current availability and permission evidence
- when a Runtime Skill-aware package names Skill, plugin, or MCP candidates, check the current host Runtime's available capabilities only within the package scope and report available / unavailable / unknown / blocked
- if a named Runtime Skill, plugin, or MCP tool is unavailable, follow the package fallback instead of silently substituting or claiming success
- keep Runtime-installed Skills as host Runtime capabilities, not AgentPal or Pal-owned Skills
- treat memory writeback as a no-code file update task that requires explicit package scope and execution evidence

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
- present Cross-Runtime Pal Memory as an automatic memory sync service, database, daemon, or background Runtime feature
- treat the host Runtime as the owner of Pal memory
- claim Runtime Skill candidates were used before the host Runtime verifies and reports evidence
- auto-scan local Runtime Skills outside a bounded package
- auto-install or auto-enable Runtime Skills, plugins, or MCP tools
- treat Runtime Skill candidates as fixed routes
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

## Cross-Runtime Pal Memory Handling

If a project continues from a previous host Runtime, the adapter should help the host Runtime follow the memory package:

1. read the Pal Project Memory Snapshot or report it missing;
2. read Routing Memory, Runtime Skill Usage Memory, and Verification Memory summaries only when the package allows them;
3. separate previous Runtime history from current Runtime capability evidence;
4. confirm current file, command, Skill, plugin, MCP, and permission availability before use;
5. follow `templates/orchestration/cross-runtime-continuation-task-package.md` when present;
6. write back no-code memory candidates only when the task package asks for it and current Runtime evidence supports the update.

The host Runtime changes, but Pal memory continuity belongs to the Pal layer. The Runtime is an execution carrier, not the owner of Pal memory.

## Runtime Skill-aware Package Handling

If a task package includes `runtime_skill_candidates`, `plugin_candidates`, or `mcp_tool_candidates`, the adapter should help the host Runtime:

1. confirm the named candidates are available in the current host Runtime, when the package asks for it;
2. keep availability evidence separate from execution evidence;
3. execute only if available, allowed, and within the package scope;
4. use `if_unavailable_fallback` when unavailable, unknown, disabled, unsafe, or blocked;
5. return final evidence including availability result, capability used or not-run, outputs, verification evidence, and blockers;
6. record Runtime Skill Usage Memory only when the package asks for writeback and privacy boundaries allow it.

Runtime Skill-aware package handling does not authorize broad local Skill scanning, automatic installs, background services, or fixed Skill routes.

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
