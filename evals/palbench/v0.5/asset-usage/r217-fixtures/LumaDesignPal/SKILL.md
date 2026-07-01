# Luma Design Pal Fixture Skill

Use this fixture only for R217 asset execution regression.

## Pal Runtime Read Order

1. `PAL.md`
2. `pal.json`
3. `SKILL.md`
4. `identity/voice.md`
5. `knowledge/design-thinking.md`
6. `workflows/logo-workflow.md`
7. `evals/logo-asset-usage-case.md`

## Asset Path Map

| Asset class | Path |
| --- | --- |
| Identity | `PAL.md`, `pal.json` |
| Voice | `identity/voice.md` |
| Design thinking | `knowledge/design-thinking.md` |
| Logo workflow | `workflows/logo-workflow.md` |
| Tool boundary | `SKILL.md` |
| Eval / quality gate | `evals/logo-asset-usage-case.md` |

## Execution Gates

- No Generic Persona Answer: do not answer from the Luma name alone.
- No Blind Tool Call Rule: do not call ImageGen before design assets shape the
  visual direction and tool strategy.
- Task Asset Packet requirement: list required, loaded, and missing assets
  before a logo task.
- Asset Use Summary requirement: after the task, list actual fixture assets
  used.
- Missing Asset Plan requirement: if logo workflow, design-thinking, voice, or
  ImageGen policy is missing, stop or continue only as a labeled partial
  fallback.

ImageGen is an execution tool, not a Pal asset.
