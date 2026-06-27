# Cross-Runtime Pal Memory Protocol

Runtime can change, Pal memory must not break.

The same Pal may continue the same project in Codex, Claude Code, OpenCode, OpenHands, Gemini CLI, or another Markdown/JSON-capable host Runtime. AgentPal memory therefore belongs to the Pal layer, not to one Runtime process.

## What Pal Memory Records

Pal memory may record public-safe or user-approved summaries of:

- project goals;
- user preferences;
- historical tasks;
- routing decisions;
- Runtime usage results;
- Runtime Skill usage results;
- verification history;
- repeated blockers;
- accepted output preferences.

Memory should record what helps future judgement without copying private source content, secrets, credentials, raw chat logs, or unrelated project data.

## Runtime Switch Rule

When the Runtime changes, the Pal should read its own relevant memory and project state before assuming context is lost.

The Pal should also separate:

- Runtime-specific state, such as session availability, installed tools, permissions, current model, and current working directory;
- Pal-owned memory, such as project goals, user preferences, prior verification outcomes, and learned task patterns.

Runtime-specific state must be refreshed by the current host Runtime. Pal-owned memory may continue across Runtimes when it is public-safe or user-approved.

## Continuation Artifacts

Use no-code artifacts to keep continuity:

- `templates/memory/pal-project-memory-snapshot.md`
- `templates/memory/routing-memory-record.md`
- `templates/memory/runtime-skill-usage-memory-record.md`
- `templates/orchestration/cross-runtime-continuation-task-package.md`
- `templates/orchestration/routing-decision-record.md`
- `templates/orchestration/routing-result-record.md`

These artifacts are summaries and task packages. They are not a database or automatic sync system.

## Skill Usage Memory

Runtime Skill usage results should name:

- the host Runtime;
- the Skill, plugin, MCP, or tool candidate;
- whether it was actually available;
- whether it was used;
- what evidence it produced;
- whether the result passed verification.

This memory helps future judgement. It does not create a fixed route.

## Privacy Boundary

Private sensitive content is not written into public AgentPal docs, examples, evals, or shared templates by default.

If a project needs private memory, keep it in the project-side or user-approved private memory location for that environment. Public examples should use synthetic data only.

## Acceptance

Cross-runtime memory is acceptable when:

- Pal identity and project continuity survive a Runtime switch;
- current Runtime capability is still verified fresh;
- Runtime Skill results and Pal-owned Skill usage are recorded separately;
- verification history remains available;
- private content is not leaked into public files.
