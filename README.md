# AgentPal

**AgentPal is a no-code Pal / Team orchestration layer for Agent Runtimes such as Codex and Claude Code.**

AgentPal does not replace Codex, Claude Code, OpenCode, OpenHands, or other Agent Runtimes. It gives those runtimes a structured Pal layer: identity, responsibilities, Team Packs, workflows, asset preflight, assignment integrity, and closure checks.

Current public status:

```text
AgentPal v0.6 is ready for guided user testing with notes.
```

It is not production ready, not a backend, not a daemon, not a GUI app, not an independent CLI product, and not an automatic multi-agent runtime. Real file edits, commands, tool calls, and external actions remain owned by the host Agent Runtime.

## What AgentPal Provides

AgentPal helps a runtime answer these questions before work begins:

- Which Pal or Team should own this task?
- Which assets should be loaded before answering?
- Which workflow steps, participants, and verifiers are required?
- What output contract must be satisfied?
- What has really happened, and what is still skipped, blocked, or not run?

The current v0.6 focus is visible, auditable no-code orchestration:

- Pal and Team identity.
- Team Pack First Discovery.
- DeepConductor no-code planning.
- Pal Asset Preflight and Team Asset Preflight.
- Workflow Execution Contract.
- Closure Gate.
- Owner Assignment Integrity.
- Thin binding for Codex and Claude Code.

## Pal

A **Pal** is a working partner with identity, role, knowledge, Skills, workflow, memory, evals, boundaries, and collaboration rules.

A Pal is not a plain Skill. A Skill is a capability package. A Pal is the role-aware partner that decides how and when to use capabilities.

A Pal is also not the runtime. The host Agent Runtime performs execution-layer actions such as file edits, command runs, browser use, and tool calls.

For substantive work, a Pal should use its own relevant assets instead of answering from only its name, persona, or general model knowledge. When assets are missing, it should report a missing-asset plan or an honest fallback.

## Team Pack

A **Team Pack** is a reusable AI team asset. A Team Pack can contain:

- `TEAM.md`
- `team.json`
- `roster.json`
- shared knowledge, Skills, workflows, runbooks, memory, evals, and routing notes

Team Pack First Discovery is a v0.6 rule:

```text
When a user asks to form, build, find, or use a team, AgentPal checks existing Team Packs before creating or redesigning a team.
```

If a fitting Team Pack exists, the runtime should reuse it, state `selected_team`, record missing roles as `open_roles`, and produce a Workflow Execution Contract plus Closure Gate. If no fitting team exists or the team needs durable governance, PalSmith may plan or create the Team Pack.

## DeepConductor

DeepConductor is AgentPal's no-code mechanism for understanding a composite task, selecting a Team or Pal, planning work, recording an execution graph, running asset preflight, and closing the workflow.

It is not a background scheduler, not a backend service, and not an automatic execution engine.

DeepConductor requires selected owners, participants, verifiers, tools, and promised outputs to have actual output, evidence, skip reason, blocker, failure, cancellation, or replan records before work can be reported as complete.

## Workflow Execution Contract And Closure Gate

A **Workflow Execution Contract** records the work before completion is claimed:

- owner
- steps
- assignees
- expected outputs
- status
- verifier
- skipped, blocked, failed, cancelled, or replanned records

The **Closure Gate** checks that the workflow really closed. A named verifier such as Quinn cannot appear only as a name. Quinn must produce a review or be legally skipped, blocked, failed, cancelled, or replanned.

## Assignment Integrity

AgentPal does not use keyword routing.

Owner selection is case-by-case AI judgement using the user goal, current context, Team Pack roster, Pal assets, Contact Capability Cards, task risk, and host runtime capability.

Important boundaries:

- Mira is the default entry and coordinator, not a substitute for every specialist.
- PalSmith owns durable Pal / Team Pack creation, repair, governance, roster design, and workflow package design after Team Pack discovery shows reuse is insufficient.
- Faye helps with business flow discovery and team setup, not established-team daily execution by default.
- Quinn is not the fixed verifier for every task, but if Quinn is named, Quinn must actually close the verification step.
- Atlas is a development Pal candidate only when the current task really needs development ownership.
- A Team label is an anchor, not a participant.
- An `open_role` is a gap, not a contributor.

## Thin Binding

AgentPal connects to external projects through thin binding. A bound project points back to the AgentPal workspace instead of copying the full Pal library into the project.

The project binding may create only small files such as:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- an AgentPal protected block in `AGENTS.md` for Codex
- an AgentPal protected block in `CLAUDE.md` for Claude Code

It must not copy full `official/pals`, contacts, evals, release history, memory, or Team Pack bodies into the external project.

## Quickstart

Start here:

- [Quickstart](docs/quickstart.md)
- [Known limits](docs/known-limits.md)
- [v0.6 status](docs/v0.6-status.md)
- [v0.6 user testing package](docs/user-tests/v0.6/README.md)

Example first prompt after binding AgentPal:

```text
Use AgentPal to organize a v0.6 user testing task. Check existing Team Packs first, and do not create a new team unless reuse is insufficient.
```

Good output should show Team First Discovery, selected or rejected teams, a Pal Work Plan, Asset Preflight, a Workflow Execution Contract, Closure Gate, and any verifier result or skip/block reason.

## Tested Status

Current evidence supports guided user testing with notes:

- Codex CLI fresh external project thin-binding smoke: `pass_with_notes`.
- Claude Code local `--plugin-dir` binder smoke: `pass_with_notes`.
- Team Pack First Discovery: `pass_with_notes`.
- DeepConductor: `pass_with_notes`.
- PalSmith create-Pal flow: `pass_with_notes`.
- Pal Asset Preflight: `pass_with_notes`.
- Workflow Execution Contract: `pass_with_notes`.
- Closure Gate: `pass_with_notes`.

Notes still preserved:

- Codex desktop saved-project screenshot coverage is not complete.
- Codex slash-command surface is not separately proven.
- Claude Code evidence is local `--plugin-dir`, not Marketplace or global plugin proof.
- Live external validation is not complete.
- Some legacy v0.1 / Simple Pal Mode wording remains in non-default historical knowledge or examples; it is cleanup debt, not the active v0.6 fresh binding mode.

## License

AgentPal is open source under the MIT License.
