# Standard Pal Generation Checklist

Use this checklist when PalSmith prepares a Standard Pal creation or upgrade package.

A Standard Pal must satisfy the Minimal Pal checklist first, then add the files and depth checks below.

## Target

- target Pal name:
- target human display name:
- role title:
- contact label:
- canonical id:
- target Pal id:
- target path:
- intended users:
- privacy / publication status:
- Runtime evidence source:

## Minimal Checklist Reference

- Minimal checklist status:
- Minimal checklist evidence path:
- unresolved Minimal gaps:

## Additional Standard Files

| File | Status | Evidence / note |
| --- | --- | --- |
| `research/index.md` | missing | |
| `learning/index.md` | missing | |
| `examples/index.md` | missing | |
| `core/collaboration-protocol.md` | missing | |
| `core/handoff-protocol.md` | missing | |
| `core/reporting-protocol.md` | missing | |
| `core/skill-growth-protocol.md` | missing | |

## Depth Checks

| Check | Status | Evidence / note |
| --- | --- | --- |
| Minimal asset execution inheritance checks passed | not-run | Runtime Read Order, Asset Path Map, Task Asset Packet, Asset Use Summary, Missing Asset Plan, No Blind Tool Call Rule, and `tool_vs_pal_asset_boundary`. |
| job expertise model present | not-run | |
| role-specific knowledge exists beyond placeholder index | not-run | |
| Pal-owned Skills are no-code methods | not-run | |
| workflows or runbooks cover recurring real tasks | not-run | |
| examples include public-safe usage scenarios | not-run | |
| evals include normal, edge, and risky cases | not-run | |
| research gap is explicit | not-run | |
| user material gap is explicit | not-run | |
| collaboration / handoff boundaries are explicit | not-run | |
| suitable team recommendations are explicit | not-run | |
| unsuitable team boundaries are explicit | not-run | |
| Contact Capability Card is complete or intentionally placeholder | not-run | |
| Pal Asset Preflight inheritance is explicit | not-run | |

## Boundary Checks

| Check | Status | Evidence / note |
| --- | --- | --- |
| no Agent Skill stored in Pal `skills/` | not-run | |
| Runtime / Agent Skill candidates only appear as task-package references | not-run | |
| no keyword routing map | not-run | |
| no connector / scanner / auto execution asset | not-run | |
| no credentials / tokens / secrets | not-run | |
| no private memory in public assets | not-run | |
| no central Pal assets written into external project `.agentpal/` | not-run | |

## Decision

Use one:

- `pass`
- `partial`
- `missing`
- `not-run`
- `blocked`

Decision:

Required fixes:

Next Runtime Task Package:
