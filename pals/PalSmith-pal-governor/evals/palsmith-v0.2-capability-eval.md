# PalSmith v0.2 Capability Eval

Status: PalSmith v0.2 Markdown eval.

## Required Files

- `core/pal-quality-inspection-protocol.md`
- `core/pal-conflict-detection-protocol.md`
- `core/pal-capability-map-protocol.md`
- `core/pal-team-design-protocol.md`
- `core/pal-version-governance-protocol.md`
- `core/pal-eval-lab-protocol.md`
- `workflows/pal-lifecycle-workflow.md`
- `templates/task-packages/pal-quality-inspection-task-package.md`
- `templates/task-packages/pal-conflict-detection-task-package.md`
- `templates/task-packages/pal-capability-map-task-package.md`
- `templates/task-packages/pal-team-design-task-package.md`
- `templates/task-packages/pal-version-upgrade-task-package.md`
- `templates/task-packages/pal-version-rollback-task-package.md`
- `templates/task-packages/pal-eval-lab-task-package.md`

## Required Examples

- `examples/task-packages/example-pal-quality-inspection.md`
- `examples/task-packages/example-pal-conflict-detection.md`
- `examples/task-packages/example-pal-capability-map.md`
- `examples/task-packages/example-design-ai-team-from-user-goal.md`
- `examples/task-packages/example-eval-new-pal.md`
- `examples/task-packages/example-pal-version-upgrade.md`

## Required Routing Coverage

PalSmith delegation and handoff guidance should cover:

- team design from a user goal
- Pal quality inspection
- conflict detection
- capability maps
- release readiness with quality inspection, eval, and export safety

## Required Boundary

- No built-in code tool.
- No UI or service.
- No automatic registry / contacts write.
- Runtime Task Package remains the execution boundary.
- user confirmation remains required before writes.

## Pass Criteria

All required files exist, no-code boundary checks pass, JSON parse checks pass, and required v0.2 anchors are searchable.
