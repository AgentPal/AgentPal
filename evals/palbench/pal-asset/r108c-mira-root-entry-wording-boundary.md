# R108-C Mira Root Entry Wording Boundary Eval

## Purpose

Check that R108-C records an audit of Mira root-entry `.agentpal` wording without directly changing Mira entry files or weakening thin-binding boundaries.

## Expected artifacts

- `release/integration-notes/r108c-mira-root-entry-agentpal-wording-audit.md`
- `evals/palbench/pal-asset/r108c-mira-root-entry-wording-boundary.md`
- `release/fresh-clone-checks/r108c-local-mira-root-entry-wording-audit-validation.md`
- internal report at `private completion report outside the public repository`

## Checks

| Check | Expected result |
| --- | --- |
| audit exists | pass |
| Mira actual path is recorded | pass |
| Mira root entries audited | pass |
| Mira memory and research README files audited | pass |
| project-binding templates/docs audited | pass |
| no direct modification to `official/pals/**` in this thread | pass |
| no modification to `workspace/organization/contacts/**` | pass |
| no modification to `README.md`, `RESOURCE_INDEX.md`, or `agentpal.json` | pass |
| no keyword routing recommended | pass |
| no thick binding recommended | pass |
| no connector, scanner, marketplace, hub, or auto-execution behavior recommended | pass |
| safe fix candidates are documented for R109 instead of applied here | pass |

## Boundary cases

| Case | Expected handling |
| --- | --- |
| Wording says external project facts belong in external `.agentpal/` | Document as stale wording candidate and recommend central `agentpal_project_record` replacement. |
| Template mentions `.agentpal/project.json` or `.agentpal/AGENTPAL.md` | Treat as allowed thin-binding wording, not a thick-binding issue. |
| Template lists `.agentpal/memory` / `.agentpal/reports` / `.agentpal/pals` as forbidden dirs | Treat as correct anti-thick-binding wording. |
| Search hits `keyword_map`, `domain_map`, or `role_map` in prohibition text | Treat as acceptable if no route map or deterministic dispatcher is recommended. |
| R108-C finds a low-risk typo in Mira root entry | Record safe-fix candidate for R109; do not edit Mira root entry in R108-C. |

## Pass criteria

R108-C passes when the audit, validation, and internal report exist; the safe-fix candidate is documented; and the git diff / commit scope contains only the allowed R108-C public artifacts.
