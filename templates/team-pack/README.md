# Team Pack Templates

Team Pack templates are no-code organization asset templates for AgentPal v0.6.

Use `standard-team-pack/` when creating a reusable team asset that references
Pals, stores team-level knowledge and workflows, and keeps external projects
thin-bound.

Team Packs are not Pal Packs. They should reference Pals through `roster.json`
and central contacts; they must not copy full Pal assets into the team folder.

## Related v0.6 Protocols

- Team schema: `standards/schemas/team.schema.json`
- Roster schema: `standards/schemas/roster.schema.json`
- Team Asset Preflight: `core/team-asset-preflight-protocol.md`
- Pal Asset Preflight: `core/pal-asset-preflight-protocol.md`
- Workflow Execution Contract: `orchestration/workflow-execution-contract-protocol.md`
- Canonical contract template: `templates/orchestration/workflow-execution-contract.md`
- Closure Gate: `orchestration/workflow-closure-gate-protocol.md`
