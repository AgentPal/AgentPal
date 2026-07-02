# PalSmith Templates

These templates are no-code planning and reporting aids. They are not scripts, scanners, validators, importers, exporters, or UI assets.

| Template | Purpose |
| --- | --- |
| `change-proposal.md` | propose safe asset changes |
| `export-plan.md` | plan clean or with-memory export |
| `health-report.md` | summarize health findings |
| `import-plan.md` | plan staged import |
| `pal-creation-plan.md` | auxiliary / legacy Pal creation planning reference; do not use as the main R217 implementation path |
| `composite-pal-creation-plan.md` | plan composite Pal creation across role, thinking style, voice, knowledge, Skill, plugin, Agent, memory, collaboration, eval, and Marketplace metadata assets |
| `existing-pal-composite-upgrade-plan.md` | plan existing Pal composite upgrades through AI judgement, target file maps, source boundaries, evals, and confirmation |
| `pal-team-plan.md` | plan Pal team creation |
| `source-coverage-report-template.md` | prove source material became concrete knowledge, skill, workflow, runbook, template, or eval assets |

Use `source-coverage-report-template.md` after user material ingestion or web research whenever content completeness matters. It should not be replaced by a one-paragraph summary.

## v0.6 Additions

Pal creation plans must separate human `display_name` from `role_title`, record
`canonical_id`, `contact_label`, aliases, user custom name handling, and naming
conflict checks. Role-only names such as `方案定制 Pal` are role intent, not valid
Pal display names.

Team creation plans must include Team Asset Preflight, a Workflow Execution
Contract placeholder, and member Pal Asset Preflight requirements. These are
protocol records only; they do not implement a Team Pack runtime or Workflow
state machine.
