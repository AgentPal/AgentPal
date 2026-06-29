# Default Pals P2 Sync Plan

Status: R-DefaultPal-11 official P2 sync plan.
Date: 2026-06-26.
Scope: official AgentPal workspace P2 schema and source-lineage sync-back from R10 evidence.

## R10 Test Conclusion Summary

R10 functional-depth testing in an internal test workspace found no P0 or P1 blockers for the 9 default Pals. The default Pal set passed Level 2 role-task simulation, content-depth sampling, multi-Pal collaboration judgement, PalSmith-style job fitness review, source coverage sampling where present, JSON parsing, and no-code boundary checks.

Remaining issues were P2:

- PalSmith and Atlas contacts entries in the official directory lacked explicit `no_runtime_code: true`.
- Mira official `pal.json` lacked `formal_skill_count` and a complete `formal_skills` list.
- Morgan, Harper, and Nova official `formal_skills` lists did not exactly match their actual `*-skill.md` assets.
- PalSmith lacked formal source lineage files under `pals/PalSmith-pal-governor/research/`.
- Some older knowledge, workflow, and eval files remain compact but usable.
- Native `/pal` runtime API and live web fetch were not tested.

## This Round Fix Scope

This round may edit official Markdown and JSON assets only:

- `contacts/pals.json`
- `pals/Mira-main/pal.json`
- `pals/Morgan-document/pal.json`
- `pals/Harper-writing/pal.json`
- `pals/Nova-product/pal.json`
- `pals/PalSmith-pal-governor/research/source-inventory.md`
- `pals/PalSmith-pal-governor/research/source-coverage-matrix.md`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/14-default-pals-p2-sync-verification-report.md`

## Out Of Scope

This round must not:

- deepen a single Pal beyond the R10 P2 sync-back scope;
- copy test-only Pals, test teams, `_test*` directories, or test registry entries into the official workspace;
- copy all R10 test reports into official release content;
- add tools, scripts, scanners, validators, CLIs, installers, daemons, package manifests, or UI;
- stage, commit, tag, push, publish, or create a release.

## JSON Changes Needed

1. Add explicit `no_runtime_code: true` to PalSmith and Atlas in `contacts/pals.json`.
2. Add Mira `formal_skill_count` and `formal_skills` from the official `pals/Mira-main/skills/` directory.
3. Align Morgan, Harper, and Nova `formal_skills` entries to the actual official skill asset names.

All JSON must parse after edits and must avoid test-only entries.

## PalSmith Research Files Needed

Add formal source-lineage files:

- `pals/PalSmith-pal-governor/research/source-inventory.md`
- `pals/PalSmith-pal-governor/research/source-coverage-matrix.md`

These are documentation assets only. They record internal standards, PalSmith protocols, task package contracts, and R10 test evidence. They do not claim live web research.

## Test Artifacts Never To Copy

Do not copy:

- internal test-only `_test*` Pal directories
- internal test-only `Mary-design` Pal directory
- test-only contacts or registry entries
- `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/test-reports/all-pals-functional-depth/` as official release content
- temporary simulation outputs

## Acceptance Criteria

- 9 contacts entries clearly express no-code boundary or documented project policy.
- Mira, PalSmith, Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova have matching `formal_skill_count`, `formal_skills`, and actual skill assets.
- PalSmith source inventory and source coverage matrix exist, are non-empty, and cover at least 6 source records.
- contacts, registry, agentpal, and relevant `pal.json` files parse.
- contacts / registry / agentpal still describe the 9 default Pals without test-only pollution.
- no-code boundary remains intact.
- `git diff --check` passes.
- R11 verification report is generated.
