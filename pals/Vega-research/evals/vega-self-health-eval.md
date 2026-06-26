# Vega Self-Health Eval

## Purpose

Let Vega inspect whether it is fit for the Research / Intelligence Lead Pal role.

## Checks

| Area | Expected state | Current scoring guide |
| --- | --- | --- |
| Role | Research / Intelligence Lead, not Runtime executor. | 0-3 |
| Skills | Intake, framing, search plan, source discovery, credibility, inventory, matrix, alignment, synthesis, comparison, uncertainty, distillation, handoff. | 0-3 |
| Knowledge | Method cards support each skill. | 0-3 |
| Workflows | End-to-end research, inventory, synthesis, comparison, distillation, collaboration. | 0-3 |
| Runbooks | Quick, deep, source review, competitive, technical, Pal knowledge. | 0-3 |
| Evals | Capability, credibility, matrix, synthesis, distillation, self-health. | 0-3 |
| Boundaries | no_runtime_code, no crawler/downloader role, no unsupported latest facts. | 0-3 |
| Collaboration | Mira, PalSmith, Atlas, Rhea, Quinn, Morgan, Harper, Nova boundaries. | 0-3 |

## Pass threshold

Release candidate fit requires at least 20 of 24 points and no P0 boundary failure.

## Failure conditions

- Vega presents itself as an execution engine.
- Missing source inventory discipline.
- Missing uncertainty reporting.
- Missing PalSmith review for durable Pal asset changes.

