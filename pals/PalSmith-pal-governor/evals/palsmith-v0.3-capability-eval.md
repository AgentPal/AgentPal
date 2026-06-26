# PalSmith v0.3 Capability Eval

Status: PalSmith v0.3 Markdown eval.

## Required Protocols

- `core/ai-team-builder-protocol.md`
- `core/pal-team-governance-protocol.md`
- `core/cross-pal-review-protocol.md`
- `core/pal-publish-quality-gate-protocol.md`
- `core/pal-runtime-call-verification-protocol.md`
- `core/github-import-verification-protocol.md`

## Required Task Packages

- `templates/task-packages/ai-team-builder-task-package.md`
- `templates/task-packages/pal-team-governance-task-package.md`
- `templates/task-packages/cross-pal-review-task-package.md`
- `templates/task-packages/pal-publish-quality-gate-task-package.md`
- `templates/task-packages/pal-runtime-call-verification-task-package.md`
- `templates/task-packages/github-import-verification-task-package.md`

## Required Examples And Quickstart

- `examples/task-packages/example-ai-team-builder-cross-border-commerce.md`
- `examples/task-packages/example-ai-team-builder-law-firm.md`
- `examples/task-packages/example-ai-team-builder-novel-studio.md`
- `examples/task-packages/example-team-governance-report.md`
- `examples/task-packages/example-cross-pal-review.md`
- `examples/task-packages/example-pal-publish-quality-gate.md`
- `examples/task-packages/example-pal-runtime-call-verification.md`
- `examples/task-packages/example-github-import-verification.md`
- `examples/quickstart/README.md`
- `docs/07-authoring-pals/15-palsmith-quickstart-ai-team.md`

## Required Delegation Wording

- AgentPal Core is not a keyword router, semantic classifier, or planner.
- Mira is the default entry Pal, not the only Pal that can call PalSmith.
- Any current Pal may consult, delegate, or hand off to PalSmith after AI judgement.
- Few-shot examples are examples, not keyword rules.

## Required Boundary

- All capabilities are expressed as Runtime Task Packages.
- No built-in UI, CLI, scanner, validator, downloader, importer, exporter, or service is introduced.
- `用户确认` is required before controlled writes.
- no-code boundary checks pass.

## Pass Criteria

All v0.3 required files exist, indexes link them, no-code and JSON checks pass, and wording does not imply keyword routing or Mira-exclusive routing.
