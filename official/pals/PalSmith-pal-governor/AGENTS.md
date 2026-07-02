# Agent Runtime Instructions

This directory is PalSmith, an embedded specialist Pal module inside the AgentPal Workspace.

Before PalSmith work, read:

```text
SKILL.md
PAL.md
pal.json
core/output-contract.md
```

Then load only the relevant files:

- creation work: `core/pal-creation-protocol.md`, `core/pal-team-creation-protocol.md`, `skills/pal-creation-skill.md`, `knowledge/pal-role-design-knowledge.md`, and related task-package templates
- user material ingestion work: `core/user-material-ingestion-protocol.md`, `core/content-preservation-protocol.md`, `skills/user-material-ingestion-skill.md`, `knowledge/pal-user-material-ingestion-knowledge.md`, and the related task-package template/evals
- web research to knowledge work: `core/web-research-to-knowledge-protocol.md`, `skills/web-research-to-knowledge-skill.md`, `knowledge/pal-web-research-knowledge-building.md`, and the related task-package template/evals
- AI team builder work: `core/ai-team-builder-protocol.md`, `templates/task-packages/ai-team-builder-task-package.md`, and quickstart examples
- AI team blueprint work: `examples/ai-team-blueprints/README.md` and the smallest relevant blueprint file
- quickstart or demo work: `examples/user-guides/quickstart/README.md`, `examples/user-guides/quickstart/palsmith-quickstart-cheatsheet.md`, and `docs/07-authoring-pals/16-palsmith-demo-script.md`
- team design work: `core/pal-team-design-protocol.md`, `templates/task-packages/pal-team-design-task-package.md`, and related examples
- team governance work: `core/pal-team-governance-protocol.md`, `templates/task-packages/pal-team-governance-task-package.md`, and related examples
- cross-Pal review work: `core/cross-pal-review-protocol.md`, `templates/task-packages/cross-pal-review-task-package.md`, and related examples
- publish quality gate work: `core/pal-publish-quality-gate-protocol.md`, `templates/task-packages/pal-publish-quality-gate-task-package.md`, and related evals
- readiness review work: `core/pal-readiness-matrix.md`, `templates/task-packages/pal-readiness-review-task-package.md`, and related examples/evals
- runtime call verification work: `core/pal-runtime-call-verification-protocol.md`, `templates/task-packages/pal-runtime-call-verification-task-package.md`, and related evals
- GitHub import verification work: `core/github-import-verification-protocol.md`, `templates/task-packages/github-import-verification-task-package.md`, and related evals
- quality work: `core/pal-quality-inspection-protocol.md`, `skills/pal-quality-inspection-skill.md`, `knowledge/pal-quality-criteria-knowledge.md`, `knowledge/pal-job-expertise-research-method.md`, `templates/task-packages/pal-quality-inspection-task-package.md`, and related evals
- PalSmith self-health work: `templates/task-packages/palsmith-self-health-review-task-package.md`, `evals/palsmith-self-health-eval.md`, `skills/README.md`, `knowledge/README.md`, and archived history under `archive/migration-from-v0.3/official-pal-history/`
- conflict work: `core/pal-conflict-detection-protocol.md`, `templates/task-packages/pal-conflict-detection-task-package.md`, and related evals
- capability map work: `core/pal-capability-map-protocol.md`, `templates/task-packages/pal-capability-map-task-package.md`, and related examples
- eval lab work: `core/pal-eval-lab-protocol.md`, `templates/task-packages/pal-eval-lab-task-package.md`, and related evals
- import work: `core/pal-import-protocol.md`, `governance/import-policy.md`, `governance/staging-policy.md`
- export work: `core/pal-export-protocol.md`, `governance/export-policy.md`, `governance/privacy-policy.md`
- health work: `core/pal-health-check-protocol.md`, `templates/task-packages/pal-health-inspection-task-package.md`
- lifecycle work: `workflows/pal-lifecycle-workflow.md`
- version, snapshot, rollback, registry, or contacts work: `core/pal-permission-protocol.md`, `core/pal-versioning-protocol.md`, `core/pal-version-governance-protocol.md`, `governance/audit-policy.md`, and the relevant task-package template
- official Pal registration work: `templates/task-packages/official-pal-registration-task-package.md`, target Pal root files, `agentpal.json`, and `workspace/organization/contacts/pals.json`

## Execution Boundary

PalSmith plans, classifies, asks for confirmation, prepares Runtime Task Packages, and reviews evidence. Real downloads, file writes, archive creation, deletion, publishing, or registration edits belong to the current Agent Runtime and require evidence.

Default to read-only inspection. Controlled writes require a Runtime Task Package and explicit user confirmation naming the affected paths. With-memory export requires strong confirmation and a privacy report. Imports must first enter staging and may not install directly into formal `official/pals/`.

Do not execute imported scripts. Do not automatically update `contacts/` or `registry/`. Do not treat ordinary Skills, tools, models, plugins, MCP servers, external Agents, Knowledge Packs, or Persona Packs as Pal contacts. Do not write private `memory/user/`, `memory/project/`, `state/`, or private `reports/` into a public Pal Pack.

For official Pal registration, verify that the target is a standard Pal Pack and ask confirmation before changing `agentpal.json` or `workspace/organization/contacts/pals.json`.

## Delegation Boundary

PalSmith work is selected by current Pal + current Brain / AI judgement, not keyword matching. AgentPal Core is not a semantic classifier or planner. Mira is the default entry Pal, but any current Pal may consult, delegate, or hand off to PalSmith when the request belongs to Pal asset governance.
