# Memory Boundary Protocol

This protocol defines which memory can be stored, shared, committed, or placed into Context Packets.

Memory is a no-code artifact. AgentPal does not provide a database, memory daemon, background sync service, scanner, validator, installer, or automatic memory runtime.

## Memory Classes

### Pack Static Memory

Purpose: public-safe Pal Pack identity, examples, templates, knowledge, workflows, runbooks, and evals.

- Can live in: Pal Pack directories, public docs, templates, examples, evals.
- Can commit to Git: yes, if public-safe and synthetic or maintainer-authored.
- Can share with other Pals: yes, through normal Pal asset loading and Context Packets.
- Can enter Context Packet: yes, as selected asset references or summaries.
- Needs user approval: only when derived from user private content.
- Should desensitize: yes when based on real user or project material.

### Project Runtime Memory

Purpose: project state, goals, blockers, decisions, task ledger, and next steps for a specific external project.

- Can live in: the central `workspace/projects/<project-id>/memory/` record, private runtime state, or user-approved project notes.
- Can commit to Git: only if the project owner approves and content is public-safe for that project.
- Can share with other Pals: only as bounded summaries.
- Can enter Context Packet: yes, as minimal task-relevant summaries.
- Needs user approval: yes when private project facts are involved.
- Should desensitize: yes by default.

### User Private Memory

Purpose: personal preferences, private facts, sensitive constraints, long-term user-specific context.

- Can live in: user-approved private memory locations.
- Can commit to Git: no by default.
- Can share with other Pals: only with user approval and minimal summary.
- Can enter Context Packet: only as explicit, bounded, relevant summary.
- Needs user approval: yes.
- Should desensitize: yes.

### Routing Memory

Purpose: record owner, verifier, Runtime, model/reasoning, topology, context, verification outcome, and next-time recommendations.

- Can live in: `memory/routing/` for synthetic examples; project-private memory for real records.
- Preferred project location: `workspace/projects/<project-id>/memory/routing-memory.md`.
- Can commit to Git: only templates and synthetic examples in public AgentPal.
- Can share with other Pals: yes as judgement input, not as rules.
- Can enter Context Packet: yes as a short evidence summary.
- Needs user approval: yes for real project/user details.
- Should desensitize: yes.

### Runtime Usage Memory

Purpose: observed success, failure, limits, permission issues, or evidence quality for a host Runtime.

- Can live in: private runtime state, central project memory, or synthetic public examples.
- Can commit to Git: only synthetic or public-safe summaries.
- Can share with other Pals: yes as current-risk context.
- Can enter Context Packet: yes as a summary with freshness notes.
- Needs user approval: yes when it includes private environment details.
- Should desensitize: yes.

### Runtime Skill Usage Memory

Purpose: observed result of a host Runtime-installed Skill, plugin, MCP tool, browser, document tool, or repository tool.

- Can live in: private runtime/project memory; synthetic examples in public docs.
- Can commit to Git: only synthetic or public-safe templates/examples.
- Can share with other Pals: yes as candidate evidence, not as availability proof.
- Can enter Context Packet: yes as a brief usage result and limits summary.
- Needs user approval: yes when tool inputs or outputs include private data.
- Should desensitize: yes.

### Verification Memory

Purpose: preserve verification result, evidence checked, missing evidence, not-run items, false completion caught, and repair history.

- Can live in: central project memory, verification records, private runtime notes, or synthetic public examples.
- Can commit to Git: only public-safe verification templates/examples or approved project records.
- Can share with other Pals: yes when needed for acceptance decisions.
- Can enter Context Packet: yes, with evidence references and missing items.
- Needs user approval: yes for private project evidence.
- Should desensitize: yes.

### Decision Memory

Purpose: preserve why a decision was made, alternatives rejected, constraints, risks, and user decisions needed.

- Can live in: conductor decision records, central project notes, private runtime state.
- Can commit to Git: only public-safe or synthetic decision records.
- Can share with other Pals: yes as context for future judgement.
- Can enter Context Packet: yes as a summary.
- Needs user approval: yes for private project/user decisions.
- Should desensitize: yes.

## Context Packet Rule

Only include the smallest memory summary needed for the current recipient and task. A Context Packet must not carry raw private memory, full chat history, secrets, local absolute paths, or unrelated project details.

## Git Rule

Public AgentPal release files may include templates and synthetic examples. Real private user memory, private project memory, local runtime state, credentials, and raw logs must stay out of public Git.

## Runtime Switch Rule

When switching host Runtimes, preserve continuity through memory snapshots and task packages, not through automatic sync. The new Runtime must refresh current capability evidence before acting.
