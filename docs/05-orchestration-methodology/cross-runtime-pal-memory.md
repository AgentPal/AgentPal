# Cross-Runtime Pal Memory

Cross-Runtime Pal Memory is AgentPal's no-code continuity pattern for keeping a Pal useful when the host Runtime changes.

```text
A Pal is not tied to a single host Runtime.
The same Pal may work in Codex today and continue in Claude Code tomorrow.
The host Runtime changes, but Pal memory, project memory, routing memory, and verification memory should preserve continuity.
```

中文：

```text
Pal 不绑定某一个宿主 Runtime。
同一个 Pal 可以今天在 Codex 中参与项目，明天在 Claude Code 中继续项目。
Runtime 可以变，Pal 记忆不能断。
```

## What It Is

Cross-Runtime Pal Memory is a set of Markdown, JSONL-style records, task packages, memory snapshots, and routing records that help the same Pal continue the same project across Codex, Claude Code, generic CLI agents, or another Markdown/JSON-capable host Runtime.

It is a Pal-layer continuity method. It is not a database, synchronization daemon, background service, memory server, scanner, validator, installer, desktop app, web app, or automatic Runtime switcher.

## Why It Matters

The user may change the host Runtime because one environment has better file access, a stronger document Skill, a different permission model, or a better fit for the next task. That switch should not force AgentPal to forget:

- the project goal;
- the Pal that handled the last stage;
- important decisions and blockers;
- what was verified;
- what failed;
- which Runtime Skill candidate helped;
- what should be avoided next time.

The current Runtime still needs fresh evidence for its own tools, permissions, model, working directory, and installed Skills.

## Codex To Claude Code To Generic CLI

Continuity is preserved by portable no-code artifacts:

1. Before switching Runtime, prepare or update a Pal Project Memory Snapshot.
2. Include recent Routing Memory and Runtime Skill Usage Memory summaries when they are public-safe or user-approved.
3. In the new Runtime, read the snapshot before treating the task as new.
4. Separate previous Runtime evidence from current Runtime capability.
5. Generate a Cross-Runtime Continuation Task Package for the current Runtime candidate.
6. After the new Runtime finishes, write back memory candidates through the host Runtime, not by AgentPal automatic sync.

## Memory Types

| Memory type | Purpose | Typical location |
| --- | --- | --- |
| Pal Memory | Pal-owned lessons, preferences, and professional continuity | Pal `learning/` or user-approved private memory |
| Project Memory | current project goal, state, blockers, decisions, and next steps | central `workspace/projects/` records or private runtime state |
| Routing Memory | routing decisions, candidates, outcomes, and verifier results | `memory/routing/` for synthetic public examples; private project memory for real records |
| Runtime Skill Usage Memory | observed result of a host Runtime Skill, plugin, MCP, or tool candidate | private runtime/project memory or synthetic public examples |
| Verification Memory | evidence, pass/fail/blocked, not-run, and rework history | project-local memory or verification records |

## Public And Private Boundary

Public AgentPal release files may contain:

- empty templates;
- synthetic examples;
- public-safe field definitions;
- no-code protocols;
- privacy-safe evals.

Public AgentPal release files must not contain:

- real private user memory;
- private project facts;
- raw chat history;
- local absolute paths;
- credentials, tokens, secrets, or API keys;
- private runtime settings;
- unauthorized third-party material.

## Before Switching Runtime

Read or prepare:

- Pal Project Memory Snapshot;
- Routing Memory summary;
- Runtime Skill Usage Memory summary;
- Verification Memory summary;
- current Project Conductor task map when available;
- next-round Runtime Task Package when available.

Do not copy full private history into the new Runtime. Use summaries and Context Packets.

## After Switching Runtime

The new host Runtime should:

- confirm its current file, command, Skill, plugin, MCP, and permission evidence;
- read the Pal Project Memory Snapshot before planning from scratch;
- treat previous Runtime success as history, not current capability proof;
- produce a Cross-Runtime Continuation Task Package;
- report evidence, not-run items, blockers, and changed or read files;
- prepare memory writeback candidates after verification.

## Avoid Fixed Routing

Routing Memory is AI Judgement input, not a rule table.

Correct:

```text
In similar tasks, Quinn worked well as a verifier candidate, so Quinn may be considered again if current evidence and goal fit.
```

Incorrect:

```text
All verification tasks must use Quinn.
```

Every routing record that recommends future reuse must include `not_a_fixed_route: true`.

## Privacy Guardrails

- Summarize preferences and decisions instead of copying raw messages.
- Redact names, paths, secrets, customer details, and private project content unless the user explicitly approves private local storage.
- Keep public examples synthetic.
- Mark freshness and uncertainty.
- Do not share one Pal's private memory with another Pal unless the user-approved context package allows it.

## No-Code Boundary

Cross-Runtime Pal Memory is maintained through memory snapshots, routing records, verification records, task ledgers, and Runtime Task Packages.

AgentPal does not automatically write a database, run a memory sync program, scan host Runtimes, or execute memory updates. The host Runtime updates no-code files only when the user allows the task package and the Runtime reports evidence.
