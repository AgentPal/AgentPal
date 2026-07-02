# AgentPal Core Gates

This directory is the shared rule surface for AgentPal runtime adapters and external project bindings.

Runtime adapters such as Codex, Claude Code, and generic CLI agents should read these files from the AgentPal workspace root instead of copying full AgentPal rules into each adapter prompt or external project.

Start here:

1. `agentpal-core-gate.md`
2. `first-pal-gate.md`
3. `deliverable-aware-task-judgement-gate.md`
4. `main-pal-conductor-gate.md`
5. `owner-assignment-integrity-gate.md`
6. `pal-asset-preflight-protocol.md`
7. `team-asset-preflight-protocol.md`
8. `runtime-adapter-shared-contract.md`
9. `project-binding-thin-contract.md`
10. `runtime-response-gate.md`

The detailed orchestration protocols remain under `orchestration/`. Core gates are the thin, shared entry rules that point runtimes to the current source of truth.
