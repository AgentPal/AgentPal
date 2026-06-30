# R198 - Pal Asset Execution Contract Eval

Date: 2026-07-01

Status: pass

## Purpose

This eval checks whether the R198 Pal Asset Execution Contract addresses the
root failure: Pal assets exist, but the runtime or Pal answers from name,
persona, model common sense, or direct tool calls without using task-relevant
assets.

## Required Evidence

| Check | Expected | Result |
| --- | --- | --- |
| Global contract exists | `core/pal-asset-execution-contract.md` | pass |
| Asset Loading Gate exists | `core/asset-loading-gate.md` | pass |
| Task Asset Packet template exists | `templates/pal/task-asset-packet.md` | pass |
| Asset Use Summary template exists | `templates/pal/asset-use-summary.md` | pass |
| Missing Asset Plan template exists | `templates/pal/missing-asset-plan.md` | pass |
| Tools are not Pal assets | contract states tool boundary | pass |
| Lightweight loading allowed | contract avoids mandatory full-load for small tasks | pass |
| Regression failure label exists | `fail_asset_usage_regression` | pass |

## Acceptance Cases

### Case 1: Substantive Pal Task

Expected:

- Pal identifies target Pal and task type.
- Pal identifies required identity, voice, thinking, knowledge, Skill,
  workflow, runtime policy, memory, and eval assets as applicable.
- Pal reports loaded and missing assets.
- Pal gives go / no-go decision.

Result: pass.

### Case 2: Tool-Backed Task

Expected:

- Pal forms direction, constraints, workflow, and verification from assets
  before selecting a tool.
- Tool is recorded as execution tool, not Pal asset.
- Pal reviews tool output with Pal eval or quality gate.

Result: pass.

### Case 3: Missing Core Asset

Expected:

- Pal does not pretend the asset exists.
- Pal uses `go_with_limited_fallback`, `partial_then_missing_asset_plan`, or
  `blocked_missing_core_asset`.
- Pal may output a Missing Asset Plan.

Result: pass.

### Case 4: Blind Tool Call

Expected fail:

```text
User asks design task
-> Runtime directly calls ImageGen
-> Pal claims design work completed
-> no Pal assets are loaded or summarized
```

Required result: `fail_asset_usage_regression`.

Result: pass.

### Case 5: Lightweight Typo

Expected:

- A narrow typo or one-line clarification may use `go_lightweight`.
- It should not require all Pal assets.
- It must still avoid unsupported claims.

Result: pass.

## Decision

`pal_asset_execution_contract_eval_pass`

R198 establishes a no-code execution contract and does not add runtime code,
scanner behavior, daemon behavior, connector behavior, backend service, or
Marketplace backend.
