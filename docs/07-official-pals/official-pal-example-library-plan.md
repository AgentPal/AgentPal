# Official Pal Example Library Plan

The official Pal example library makes each bundled Pal understandable through realistic task examples. Examples are learning artifacts and review aids. They are not route maps, dispatch tables, or execution automation.

## Official 9 Pal List

| Pal | Typical task examples | Not-suitable whole-task examples |
| --- | --- | --- |
| Mira | ordinary intake, owner judgement explanation, staged Task Package, evidence-aware summary | specialist professional body after handoff, implementation, independent verification |
| Atlas | implementation packages, file boundaries, development acceptance repair | product strategy, primary research, final quality gate without evidence |
| Vega | source-grounded research, comparison, uncertainty, claim-safe handoff | final implementation, product commitment, unsupported current facts |
| Rhea | runtime boundary review, no-code review, safe binding diagnosis | implementation edits, high-risk operations without approval |
| PalSmith | Pal creation, AI team design, material ingestion, Pal health repair | direct filesystem execution, automatic registration, ordinary Skill contact creation |
| Quinn | evidence review, release readiness, regression acceptance | original implementation, source research, publication |
| Morgan | structured docs, document artifact packages, release-note structure | invented facts, marketing copy, final release readiness judgement |
| Harper | release copy, style rewrite, source-grounded promo draft | primary research, unsupported claims, page implementation |
| Nova | requirement clarification, MVP scope, product-to-dev handoff | implementation, final QA, primary research without evidence |

These descriptions are examples of where a Pal may be a good candidate. Actual owner and stage selection still uses case-specific AI judgement from the current contacts and registry.

## How Users Choose

- If unsure, ask Mira first. Mira can judge the owner candidate, ask focused clarification, or prepare a staged Task Package.
- If the desired specialist is clear, call `/pal Name` directly.
- If the request has multiple deliverables, the first Pal must use deliverable-aware staged judgement before broad clarification or execution.
- Runtime candidates execute file reads, writes, commands, screenshots, or rendering only when permitted and evidenced. Runtime is not a Pal owner.

## Example Library Paths

| Pal | Task examples |
| --- | --- |
| Mira | `official/pals/Mira-main/examples/tasks/` |
| Atlas | `official/pals/Atlas-developer/examples/tasks/` |
| Vega | `official/pals/Vega-research/examples/tasks/` |
| Rhea | `official/pals/Rhea-system/examples/tasks/` |
| PalSmith | `official/pals/PalSmith-pal-governor/examples/tasks/` |
| Quinn | `official/pals/Quinn-quality/examples/tasks/` |
| Morgan | `official/pals/Morgan-document/examples/tasks/` |
| Harper | `official/pals/Harper-writing/examples/tasks/` |
| Nova | `official/pals/Nova-product/examples/tasks/` |

See also `docs/07-official-pals/official-pal-examples-index.md`.

## Current v0.2 Completion Status

Status: started / first implementation / R42.

R40 created the first PalSmith productization examples. R41 created the first Mira-first examples. R42 extends the example library so all 9 official Pals have task-level example directories, per-Pal task indexes, and at least three real task examples. Mira and PalSmith each have four task examples because their R40/R41 foundations were already deeper.

This does not mark the full v0.2 roadmap complete.

## Example Format

Each task example should include:

- User Request
- When this Pal is a good candidate
- When this Pal should not take the whole task
- Task Judgement
- Context Needs
- Suggested Task Package
- Good Response Example
- Bad Response Example
- Verification / Acceptance Criteria
- Notes

Every example should state that candidates are not fixed routes and that current v0.2 does not auto-run Deep Conductor.

## Not-Do List

- Do not turn examples into fixed owner rules.
- Do not create automatic multi-agent execution.
- Do not treat Deep Conductor as current runtime behavior.
- Do not hard-code artifact types to Pal names.
- Do not claim Runtime actions happened without evidence.
- Do not include private user data, credentials, or local absolute paths in public examples.
- Do not create empty placeholder examples.

## R42 First Implementation Coverage

| Pal | Count | Coverage |
| --- | ---: | --- |
| Mira | 4 | intake, composite staged judgement, direct Pal choice, completion summary |
| Atlas | 3 | docs change package, composite implementation stage, development acceptance repair |
| Vega | 3 | research brief, competitor/technical comparison, research-stage handoff |
| Rhea | 3 | runtime boundary, no-code review, project binding troubleshooting |
| PalSmith | 4 | first Pal creation, AI team design, material ingestion, health repair |
| Quinn | 3 | false completion review, release gate, regression acceptance |
| Morgan | 3 | structured docs, Office/PDF package, release-note structure |
| Harper | 3 | release copy, style rewrite, source-grounded promo draft |
| Nova | 3 | requirements clarification, MVP scope, product-to-development handoff |

## Cross-Pal Examples

R42 adds public-safe staged examples under `examples/orchestration/`:

- `cross-pal-product-research-dev-qa-docs.md`
- `cross-pal-palsmith-create-ai-team.md`
- `cross-pal-release-readiness-review.md`

These examples show conductor judgement, Context Access Lists, staged Task Packages, and acceptance checks. They remain written examples in Simple Pal Mode, not automatic Deep Conductor execution.
