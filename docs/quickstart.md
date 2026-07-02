# AgentPal v0.6 Quickstart

AgentPal is a no-code Pal / Team orchestration layer for Agent Runtimes. This quickstart shows how to connect AgentPal to a project through thin binding and run a first visible, auditable task.

Current status:

```text
guided user testing ready with notes
```

## Before You Start

Prepare a local AgentPal workspace. In this repository, that is the folder containing `agentpal.json`, `AGENTS.md`, `core/`, `official/`, `templates/`, and `plugins/`.

AgentPal does not copy full Pal assets into your project. It creates a thin project binding that points back to the AgentPal workspace.

## Codex Quickstart

Use this path for a fresh external Codex project.

1. Install the AgentPal Codex plugin from the AgentPal install document or make the local plugin available to Codex.
2. Open a fresh Codex project.
3. Say:

   ```text
   Add AgentPal to this project.
   ```

4. Check status:

   ```text
   Check AgentPal status.
   ```

5. Repair if needed:

   ```text
   Repair AgentPal.
   ```

6. Disable and re-enable when testing binding cleanup:

   ```text
   Remove AgentPal from this project.
   Add AgentPal to this project.
   ```

7. Run a first natural-language test:

   ```text
   Use AgentPal to organize a v0.6 user testing task. Check existing Team Packs first, and do not create a new team unless reuse is insufficient.
   ```

Expected thin-binding files:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- one Codex AgentPal protected block in `AGENTS.md`

Expected output signals:

- Team First Discovery
- selected or rejected team
- Pal Work Plan
- Asset Preflight
- Workflow Execution Contract
- Closure Gate
- Quinn review, or a clear reason why verification was skipped, blocked, or not required

Evidence note: Codex CLI fresh external project smoke has been validated with notes. Codex desktop saved-project screenshots and Codex slash-command surface are not yet complete proof.

## Claude Code Quickstart

Use this path for local Claude Code binder testing.

1. Open a project in Claude Code using the local plugin directory:

   ```text
   claude --plugin-dir <path-to-AgentPal>/integrations/claude-code/agentpal-project-binder
   ```

2. Enable AgentPal:

   ```text
   /agentpal:enable
   ```

3. Check status:

   ```text
   /agentpal:status
   ```

4. Repair if needed:

   ```text
   /agentpal:repair
   ```

5. Disable and re-enable when testing binding cleanup:

   ```text
   /agentpal:disable
   /agentpal:enable
   ```

6. Run a first natural-language task:

   ```text
   Use the existing Team Packs if one fits. Organize a short product research task with visible owners, asset preflight, Workflow Execution Contract, and Closure Gate.
   ```

Expected thin-binding files:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- one Claude Code AgentPal protected block in `CLAUDE.md`

Evidence note: Claude Code has local `--plugin-dir` binder proof. This is not a Marketplace or global plugin publication proof.

## First Task Examples

Try these after binding:

```text
Ask AgentPal to organize a product research task, and reuse an existing Team Pack first.
```

```text
Ask AgentPal to create a beginner coach Pal for cross-border independent store operators.
```

```text
Ask AgentPal to review a product proposal that makes all user custom Pals public by default.
```

## What Good Output Looks Like

For non-trivial work, good AgentPal output should make the work auditable:

- Task Intake
- Team First Discovery
- selected and rejected teams / Pals
- Work Plan
- Team Asset Preflight and Pal Asset Preflight when applicable
- Workflow Execution Contract
- Execution Trace or honest `not-run` / `blocked` / `skipped` status
- Owner Assignment Integrity check
- Closure Gate
- Quinn verification when Quinn is selected or named
- deliverable
- known limits and remaining risks

## What To Avoid Claiming

Do not treat AgentPal v0.6 as:

- production ready
- a fully automated runtime
- a backend service
- a daemon
- a GUI app
- a Marketplace backend
- a one-click install with all host surfaces proven

See [Known limits](known-limits.md) and [v0.6 status](v0.6-status.md).
