# R108-C Mira Root Entry `.agentpal` Wording Audit

## Status

Audit complete. No Mira root entry file was modified in this thread.

## Mira actual path

`official/pals/Mira-main`

Central roster evidence:

- `id`: `mira-main`
- `display_name`: `Mira`
- `role`: `main-leader-conductor`
- `pack_path`: `official/pals/Mira-main`

## Audited files

Mira root entry files:

- `official/pals/Mira-main/README.md`
- `official/pals/Mira-main/PAL.md`
- `official/pals/Mira-main/AGENTS.md`
- `official/pals/Mira-main/SKILL.md`
- `official/pals/Mira-main/pal.json`

Mira related README files:

- `official/pals/Mira-main/memory/README.md`
- `official/pals/Mira-main/research/README.md`

Related thin-binding references:

- `templates/project-binding/`
- `docs/01-getting-started/bind-external-project.md`
- `workspace/organization/contacts/pals.json`
- `J:\开发\AgentPal_dcos\开发记录\R105-Mira-specific-PalAssetReview与memory-research-index补齐完成报告.md`

## Audit criteria

Checked whether wording could imply:

- external projects should copy Pal assets or Pal Packs
- external projects should create `.agentpal/memory`
- external projects should create `.agentpal/reports`
- external projects should create `.agentpal/pals`
- Mira should read a local Pal roster from an external project's `.agentpal/`
- keyword routing or Core keyword assignment
- connector, scanner, or auto-execution behavior

Expected retained semantics:

- external projects use thin binding only
- allowed binding files are `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and protected host-runtime instruction blocks
- central Pal roster stays at `workspace/organization/contacts/pals.json`
- project records stay in the AgentPal central workspace
- Mira is the default entry Pal but not a keyword router
- Brain / AI judgement performs case-specific owner selection

## Suspicious wording table

| File | Lines | Current wording summary | Risk | Severity | Recommended replacement wording | safe_to_fix_in_R109 | requires_human_review |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| `official/pals/Mira-main/PAL.md` | 230-235 | The memory destination list says external project facts go to the external project's `.agentpal/`. | Could be read as permission to store project facts or memory directly under an external project's `.agentpal/`, conflicting with current thin-binding policy and central `agentpal_project_record` storage. | Medium | Replace the external-project bullet with: `external project facts: the central AgentPal project record under workspace/projects/<project-id>/, referenced by agentpal_project_record; do not write project memory into the external project's .agentpal/ by default.` | yes | no |

## Confirmed non-issues

| File or area | Evidence summary | Result |
| --- | --- | --- |
| `official/pals/Mira-main/README.md` | States Mira does not hard-code semantic routing and that Pal capability descriptions are orientation only. | ok |
| `official/pals/Mira-main/AGENTS.md` | States no hard-coded semantic routing, no Core semantic router, and current project means external project by default. | ok |
| `official/pals/Mira-main/SKILL.md` | States AI judgement is used instead of fixed word matching and that Core files must not be presented as an active semantic router. | ok |
| `official/pals/Mira-main/pal.json` | `routing_policy` says AI judgement case-by-case, no fixed word table, no Core semantic router. | ok |
| `official/pals/Mira-main/memory/README.md` | Explicitly says external project `.agentpal/memory/` is not a default target and project-private memory belongs in the central AgentPal project record. | ok |
| `official/pals/Mira-main/research/README.md` | Explicitly says not to copy Mira research into external project `.agentpal/` by default. | ok |
| `templates/project-binding/` | Current templates describe thin binding, central project records, central contacts, and forbidden thick `.agentpal/` directories. | ok |
| `docs/01-getting-started/bind-external-project.md` | States AgentPal stores project memory, task records, reports, governance records, and capability inventory in the central project record, not the external project's `.agentpal/` directory. | ok |

## Safe-fix candidate for R109

Candidate: update only `official/pals/Mira-main/PAL.md` memory destination wording around lines 230-235.

R109 status:

- `fixed_in`: `R109`
- `fixed_path`: `official/pals/Mira-main/PAL.md`
- `fixed_scope`: one bullet in the Memory and Knowledge destination list
- `remaining_risk`: none currently known; verify with the R109 integrated gate and clean-copy validation

Suggested replacement block:

```md
Mira can suggest memory candidates and knowledge candidates. She must choose the right destination:

- user preference: `memory/user/`
- system knowledge: `memory/system/` or public docs
- external project facts: the central AgentPal project record under `workspace/projects/<project-id>/`, referenced by `agentpal_project_record`; do not write project memory into the external project's `.agentpal/` by default
- Mira team-leadership lessons: `official/pals/Mira-main/learning/`
```

Risk: low, if handled in R109 with root-entry sync scope only.

Reason not fixed in R108-C: this thread is audit-only by design and must avoid direct Mira root entry modifications while R108-A / R108-B may run in parallel.

## Boundary conclusion

The audit found one medium-severity stale wording candidate in Mira `PAL.md`. The rest of the audited Mira entry and thin-binding reference files support the current thin-binding model and do not recommend keyword routing, copied Pal Packs, project-local Pal rosters, scanners, connectors, or auto execution.
