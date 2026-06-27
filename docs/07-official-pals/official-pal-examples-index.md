# Official Pal Examples Index

This index points to the v0.2 first implementation of the official 9 Pal real task example library.

## How To Use

- Start with Mira when you are unsure which Pal should own the work.
- Use `/pal Name` when the intended specialist is clear.
- For composite deliverables, expect a staged judgement with Pal, Runtime, Skill, and verification candidates.
- Treat examples as learning references, not fixed routes.

## Pal Task Libraries

| Pal | Role | Task examples |
| --- | --- | --- |
| Mira | Main Pal / Leader / Conductor | `official/pals/Mira-main/examples/tasks/` |
| Atlas | Developer / Implementation Lead | `official/pals/Atlas-developer/examples/tasks/` |
| Vega | Research / Intelligence Lead | `official/pals/Vega-research/examples/tasks/` |
| Rhea | System / Runtime Safety Lead | `official/pals/Rhea-system/examples/tasks/` |
| PalSmith | Pal Asset Governor | `official/pals/PalSmith-pal-governor/examples/tasks/` |
| Quinn | Quality / Verification Lead | `official/pals/Quinn-quality/examples/tasks/` |
| Morgan | Document / File Workflow Lead | `official/pals/Morgan-document/examples/tasks/` |
| Harper | Writing / Content Craft Lead | `official/pals/Harper-writing/examples/tasks/` |
| Nova | Product / Strategy Lead | `official/pals/Nova-product/examples/tasks/` |

## Cross-Pal Examples

- `examples/orchestration/cross-pal-product-research-dev-qa-docs.md`
- `examples/orchestration/cross-pal-palsmith-create-ai-team.md`
- `examples/orchestration/cross-pal-release-readiness-review.md`

Cross-Pal examples show staged written Task Packages and Context Access Lists. They do not start automatic multi-Pal execution.

## Status

Status: started / first implementation / R42.

R42 provides at least three task examples for each official Pal. Mira and PalSmith each have four. The library remains open for later expansion with more domain-specific examples and PalBench cases.

## Review Rules

- Every task example should include User Request, Task Judgement, Context Needs, Good Response Example, Bad Response Example, and Verification / Acceptance Criteria.
- Every example should state that candidates are not fixed routes.
- Public examples must not contain private user data, credentials, or local absolute paths.
- Current v0.2 examples are written guidance and do not activate Deep Conductor.
