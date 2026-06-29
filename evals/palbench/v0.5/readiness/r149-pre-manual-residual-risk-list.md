# R149 Pre-Manual Residual Risk List

Status: executed
Date: 2026-06-29

## Residual Risks

| Risk | Severity | Status | Handling |
| --- | --- | --- | --- |
| R150+ manual conversations may still overclaim runtime execution | medium | open until manual execution | record real evidence and fail any unsupported execution claim |
| Faye may be confused with connector/executor behavior by users | medium | mitigated | Faye Pack and manual scripts now include direct boundary checks |
| Historical records still show 9 official Pals | low | intentional | preserve R143-R148 historical evidence; current docs and roster show 10 |
| Older release/current snapshots may still show prior 9-Pal local preflight evidence | low | intentional | treat as historical release evidence unless a later release-refresh task updates them |
| Other half-role references may appear in old behavior logs | low | intentional | current R149 manual/readiness artifacts no longer treat Faye as half-registered |

## Current Blockers

No pre-manual blocker remains after Faye registration.

## Next Round

Proceed to R150+ manual test execution with real conversation records. Keep `not-run`, `missing`, `unknown`, and `blocked` visible.
