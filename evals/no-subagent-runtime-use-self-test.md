# No Current Runtime Orchestration Self-Test

Verify that AgentPal v0.1 does not activate future runtime orchestration during normal task handling.

## Scope

Check current runtime entry files:

- `AGENTS.md`
- `INIT_PROMPT.md`
- `prompts/initialize-agentpal.md`
- `prompts/join-external-project-workgroup.md`
- `projects/project-workgroup-template/agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`
- `templates/project-binding/root-agents-agentpal-block-template.md`
- `orchestration/runtime-response-gate.md`
- `pals/Mira-main/core/`
- current README usage flow

## Expected

- Current runtime policy says Simple Pal Mode only.
- Future orchestration is not invoked in current task handling.
- There is no tool discovery, spawn/wait/close instruction, runtime evidence label, or fallback reason label in current entry files.
- Future design files are clearly marked future-design-only.

## Allowed

Future design docs, historical evals, and archived examples may mention future runtime orchestration if clearly marked as not active in AgentPal v0.1 runtime.

