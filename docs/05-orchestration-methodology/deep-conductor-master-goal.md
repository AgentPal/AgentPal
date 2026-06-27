# Deep Conductor Master Goal

Deep Conductor is AgentPal's no-code coordination methodology for complex work.

Its goal is to improve outcomes inside existing host Agent Runtimes by making planning, allocation, context control, verification, and memory writeback more deliberate.

Deep Conductor is not an executor. It does not call Agents, run commands, write files, start background workers, or perform automatic multi-runtime orchestration. It produces no-code plans, Context Packets, Context Access Lists, and Runtime Skill-aware Task Packages for a host Runtime to execute with evidence.

## Core Goal

Deep Conductor coordinates:

- scheduling;
- task decomposition;
- planning;
- owner and verifier allocation;
- capability composition;
- context access control;
- prompt shaping;
- verification;
- routing and usage memory writeback.

The advantage comes from resource cognition, scheduling, context discipline, verification, and memory, not from AgentPal becoming a program.

## Master Loop

1. Goal Intake.
2. Project / Pal Memory Loading.
3. Deliverable and Stage Judgement.
4. Capability Inventory Read.
5. Runtime Skill / Plugin / MCP Awareness.
6. Workflow Topology Selection.
7. Context Access Planning.
8. Prompt Shaping and Token Budgeting.
9. Runtime Task Package Generation.
10. Verification Planning.
11. Synthesis and User-facing Explanation.
12. Routing Memory Writeback Candidate.

## Candidate Rules

Candidates are never fixed routes.

A Deep Conductor packet may name a candidate Pal, host Runtime, model profile, reasoning profile, Runtime-installed Skill, plugin, or MCP server. That naming means "consider this because the current evidence and goal suggest it may help." It does not mean the candidate is available, authorized, or automatically invoked.

## Runtime Boundary

The host Agent Runtime remains responsible for:

- file reads and writes;
- shell commands;
- tool calls;
- browser or office-document operations;
- external publishing;
- system changes;
- evidence collection.

AgentPal remains responsible for:

- task judgement;
- owner and verifier selection;
- context boundaries;
- task package quality;
- verification requirements;
- routing memory structure;
- explaining what happened and what remains unverified.

## Acceptance

Deep Conductor guidance is acceptable when it:

- improves the host Runtime's chance of completing the user's real task;
- keeps Pal-owned Skills separate from Runtime-installed Skills;
- states evidence requirements;
- reports not-run and unavailable states honestly;
- avoids keyword routes and fixed owner maps;
- keeps private memory out of public examples;
- never claims automatic execution.
