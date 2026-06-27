# Deep Conductor E2E Context Budget Self-Test

## Purpose

Verify that an E2E package controls context reads and reports usage qualitatively.

## Passing criteria

- `context_budget_plan` includes read tier, allowed context, forbidden context, escalation reasons, stop conditions, and ask-user conditions when needed.
- `context_usage_report_required: true` is present for E2E packages.
- Index-known paths are not counted as content-read files.
- Verification reads are preserved as quality cost.
- The package does not ask the Runtime to load all Pals, all examples, all evals, all memory, all docs, or all project files by default.
- Exact token or cost claims require host-provided metering evidence; otherwise they are not claimed.
- Public examples contain no internal local paths.

## Failing patterns

- Full-workspace read is treated as the default for complex tasks.
- Verification is skipped to reduce context.
- The synthesis report claims exact token totals without evidence.

## Related failure example

- `examples/failures/deep-conductor-e2e-no-context-budget.md`

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
