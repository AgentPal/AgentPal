# PalSmith Source Coverage Matrix

Status: R11 official source-lineage asset.
Scope: Maps PalSmith source records to existing PalSmith knowledge, skills, workflows, templates, evals, and R11 verification artifacts.

## Coverage Summary

| Area | Coverage | Remaining limitation |
|---|---|---|
| Pal Pack structure and valid asset types | strong | Detailed public authoring examples can keep improving over time. |
| Runtime Task Package planning | strong | Actual Runtime evidence is still required per task. |
| Pal creation and job fitness | strong | Domain-specific Pals may still need user material or live research. |
| Content preservation and material ingestion | strong | Large private sources require explicit user approval before reads/writes. |
| Web research to knowledge | strong as protocol | R11 did not run live web fetch; future current-facts work must run Runtime research. |
| Readiness and publish quality gates | strong | Native `/pal` Level 3 direct-call behavior remains not-run in this environment. |
| R10 test evidence linkage | adequate | Test reports are evidence references, not files to copy into official release content. |

## Matrix

| Source ID | Extracted point | Importance | Should become | Actual file path | Actual section | Coverage status | Notes |
|---|---|---|---|---|---|---|---|
| PS-S01 | A Pal Pack is a structured no-code asset set, not an arbitrary tool or raw skill. | critical | knowledge / eval | `knowledge/pal-skill-vs-knowledge-vs-workflow.md`, `evals/official-registration-eval.md` | Concept / Expected checks | covered | Prevents ordinary tools, plugins, or skills from being registered as Pals. |
| PS-S01 | Pal asset categories should stay distinct: knowledge, skill, workflow, runbook, template, eval, and output contract. | critical | knowledge | `knowledge/pal-skill-vs-knowledge-vs-workflow.md` | Judgement Standards | covered | Used by creation and material ingestion plans. |
| PS-S02 | Runtime Task Packages must define scope, boundaries, evidence, and reporting. | critical | skill / template | `templates/task-packages/README.md`, `core/output-contract.md` | Template index / Output contract | covered | Keeps PalSmith from becoming an execution runtime. |
| PS-S02 | Completion claims require Runtime evidence, not Pal confidence. | critical | skill / eval | `skills/pal-publish-readiness-skill.md`, `evals/pal-readiness-matrix-eval.md` | Quality / Expected behavior | covered | Aligns with Quinn-style evidence discipline. |
| PS-S03 | Pal creation must begin with job fitness modelling, not file scaffolding alone. | critical | skill / workflow | `skills/pal-creation-skill.md`, `workflows/pal-creation-with-research-workflow.md` | Process / Flow | covered | Prevents empty-shell Pal creation. |
| PS-S03 | Creation plans must include knowledge, skills, workflows, evals, risks, and collaboration boundaries. | critical | skill / eval | `skills/pal-creation-skill.md`, `evals/pal-quality-inspection-eval.md` | Output / Expected behavior | covered | Supports real job usability. |
| PS-S04 | Long materials must preserve source anchors, examples, steps, boundaries, and uncertainty. | critical | knowledge / skill / eval | `knowledge/pal-content-preservation-principles.md`, `skills/user-material-ingestion-skill.md`, `evals/content-preservation-eval.md` | Judgement Standards / Process | covered | Prevents over-compressed knowledge cards. |
| PS-S05 | User material ingestion requires approved source reads, source inventory, classification, privacy boundary, and confirmation before writes. | critical | skill / workflow / template | `skills/user-material-ingestion-skill.md`, `workflows/user-material-ingestion-workflow.md`, `templates/task-packages/user-material-ingestion-task-package.md` | Process / Flow | covered | Protects user materials and source traceability. |
| PS-S06 | Web research to knowledge must separate live research, local inference, candidate knowledge, uncertainty, and stable writes. | critical | skill / workflow / eval | `skills/web-research-to-knowledge-skill.md`, `workflows/web-research-to-knowledge-workflow.md`, `evals/web-research-to-knowledge-eval.md` | Process / Acceptance | covered | R11 did not run live web fetch; future use must label that honestly. |
| PS-S07 | Job fitness review checks role fit, expertise depth, coverage, research gaps, user material gaps, and collaboration fit. | critical | skill / knowledge / eval | `skills/pal-quality-inspection-skill.md`, `knowledge/pal-quality-criteria-knowledge.md`, `evals/pal-quality-inspection-eval.md` | Process / Criteria | covered | Used for R10 all-Pal fitness review and future Pal health checks. |
| PS-S08 | Readiness status must use the lowest state proven by evidence. | important | skill / eval | `skills/pal-publish-readiness-skill.md`, `evals/pal-readiness-matrix-eval.md` | Quality bar / Expected behavior | covered | Prevents unsupported publish-ready claims. |
| PS-S09 | PalSmith templates define owner Pal, Runtime role, context limits, write boundaries, and confirmation needs. | important | template / workflow | `templates/task-packages/README.md` | Template index / Routing note | covered | Supports consistent no-code planning across PalSmith work types. |
| PS-S10 | R10 found PalSmith source lineage missing while PalSmith remained functionally usable. | important | research asset / verification report | `research/source-inventory.md`, `research/source-coverage-matrix.md`, `docs/08-release-candidate/14-default-pals-p2-sync-verification-report.md` | R11 additions | covered by R11 | This is a P2 source-depth repair, not a new feature. |
| PS-S11 | R10 verified no-code boundary and schema consistency after normalization in the test directory. | important | sync plan / verification report | `docs/08-release-candidate/13-default-pals-p2-sync-plan.md`, `docs/08-release-candidate/14-default-pals-p2-sync-verification-report.md` | Acceptance criteria / Results | covered by R11 | R11 syncs the verified schema repairs back to official files. |
| PS-S12 | Formal skills may be represented by mapped Flat Skill Cards or Directory Skill Packages, but every formal skill needs an actual asset. | critical | standard / skill map / release report | `docs/03-pal-pack-standard/15-formal-skill-assets.md`, `skills/skill-asset-map.md`, `docs/08-release-candidate/20-formal-skill-assets-audit.md` | Valid representations / Skill Asset Map | covered by R13 | Fixes the old checker gap without creating empty skill directories. |

## Remaining Gaps

- Native `/pal` runtime API verification remains not-run in this Codex environment.
- Live web fetch was not run for PalSmith in R11.
- Future domain-specific Pal creation still needs source inventories tied to that domain, not only PalSmith governance protocols.
- Formal Skill asset representation is mapped under the R13 standard; future stricter checks should accept both Flat Skill Cards and Directory Skill Packages.
