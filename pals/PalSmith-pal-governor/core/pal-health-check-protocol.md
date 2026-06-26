# Pal Health Check Protocol

PalSmith prepares Pal Health Inspection Task Packages. It does not run an internal scanner or validator.

## Inspection Areas

- required root files: `PAL.md`, `pal.json`, `SKILL.md`, `AGENTS.md`
- expected structure: `identity/`, `core/`, `skills/`, `knowledge/`, `evals/`
- readable `pal.json`
- version present
- collaboration flags present
- `memory/user/` and `memory/project/` not mixed into public assets
- `state/` and `reports/` treated as runtime-private
- contacts and registry consistency

Scores, if used, are advisory. A health report is not registration approval.
