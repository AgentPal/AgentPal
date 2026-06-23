# Official Pal Slim Structure Self-Test

Purpose: verify that the seven official specialist Pals are slim embedded AgentPal modules, not standalone repositories.

## Scope

Check:

- `pals/Atlas-developer`
- `pals/Nova-product`
- `pals/Quinn-quality`
- `pals/Rhea-system`
- `pals/Vega-research`
- `pals/Morgan-document`
- `pals/Harper-writing`
- `pals/`

## Expected

Each specialist Pal must have:

- `README.md`
- `PAL.md`
- `AGENTS.md`
- `SKILL.md`
- `pal.json`
- `identity/`
- `core/`
- `knowledge/`
- `skills/`
- `workflows/`
- `runbooks/`
- `learning/`
- `evals/`
- `examples/`
- `memory/`
- `state/`
- `reports/`
- `core/output-contract.md`
- `core/capability-reference.md`

Each specialist Pal must not contain duplicate system-layer directories:

- `.agentpal/`
- `.agents/`
- `.claude/`
- `adapters/`
- `contacts/`
- `coordination/`
- `imports/`
- `models/`
- `orchestration/`
- `plugins/`
- `registry/`
- `runtime/`

Atlas, Nova, Quinn, Rhea, Vega, Morgan, and Harper must not contain placeholder `tools/` folders.

Specialist Pal directories must not contain runtime tool engines by default. Optional Pal-owned tool assets belong in separate Pal Packs or future extension packages, not in the v0.1 bundled Pal set.

## Routing Regression

This self-test does not assert fixed owner Pal names for natural language tasks. It checks AI judgement rationale, real owner assets, output contracts, and absence of hard-coded semantic routing.

