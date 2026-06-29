# R148 Legacy Entry / Wording / File Residual Review List

Status: executed
Date: 2026-06-29

## Summary

Residual review items do not block R149 manual test plan preparation. They are preserved because their legacy wording appears in historical evidence, older roadmap material, archive content, or examples whose current value is ambiguous.

## Residual Groups

| Group | Example paths | Why ambiguous | Suggested future action | Blocks R149 |
| --- | --- | --- | --- | --- |
| Older roadmap docs | `docs/09-roadmap/v0.2-development-plan.md`, `docs/09-roadmap/v0.3-development-plan.md`, `docs/09-roadmap/v0.3-release-preparation-audit.md` | These contain old version/stage language but may still explain project evolution. | Add archive banner or move to explicit history section in a future documentation archive pass. | no |
| Release history and local completion records | `release/current/v0.4-local-completion-report.md`, `release/history/`, `release/v0.1.0-rc.1/` | They are historical evidence and should not be rewritten as current state. | Keep as history; optionally add stronger historical labels. | no |
| Archived migration files | `archive/migration-from-v0.3/` | Archive content intentionally preserves old wording and migration context. | Keep unless a future archive pruning task explicitly decides otherwise. | no |
| Historical eval and validation records | `evals/`, `release/fresh-clone-checks/`, `release/integration-notes/` | They preserve the exact evidence chain and often mention old versions or old forbidden patterns. | Keep; do not delete for keyword matches. | no |
| Example packs with boundary terms | `examples/`, `templates/` | Many hits are "not a connector / not a scanner / no real customer data" boundary text. | Keep; review only if an example becomes a current entry point. | no |
| Duplicate-era docs directories | `docs/01-getting-started/` and `docs/02-getting-started/` | Both appear useful; deleting either would need a separate navigation and link audit. | Consider a future information-architecture cleanup round. | no |

## R149 Impact

No residual review item blocks R149 manual test plan preparation. R149 should test current entry points and current v0.5 behavior, not historical archive wording.
