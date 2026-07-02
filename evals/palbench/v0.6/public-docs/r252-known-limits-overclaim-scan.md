# R252 Known Limits / Overclaim Scan

## Scope

Checked active public docs created or updated in R252:

- `README.md`
- `docs/README.md`
- `docs/quickstart.md`
- `docs/known-limits.md`
- `docs/v0.6-status.md`
- `RESOURCE_INDEX.md`

## Forbidden Claim Scan

| Term | Result | Notes |
| --- | --- | --- |
| `production ready` | allowed negative context only | Docs say v0.6 is not production ready. |
| `fully automated` | allowed negative context only | Docs say AgentPal is not a fully automated runtime. |
| `autonomous backend` | no positive claim | No completed backend claim. |
| `one-click install completed` | no claim | No one-click install completion claim. |
| `marketplace published` | allowed negative context only | Docs say Marketplace publication is not proven. |
| `all runtime integrations verified` | allowed negative context only | Docs say this is not claimed. |
| `live external validation completed` | allowed negative context only | Docs say live external validation is not complete. |
| `all Pal tasks fully certified` | allowed negative context only | Docs avoid full certification language. |
| `Simple Pal Mode is current` | no claim | Docs name v0.6 no-code Pal / Team orchestration as current mode. |
| `v0.1 is current` | no claim | Legacy v0.1 text is described only as cleanup debt. |

## Active Blocker

active_public_doc_overclaim_blocker: false

## Result

known_limits_overclaim_scan: pass_with_notes

Note: R251 still identified legacy wording in non-default historical knowledge/examples. R252 public docs do not present that legacy wording as the current mode.
