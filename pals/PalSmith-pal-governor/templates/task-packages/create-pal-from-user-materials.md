# Create Pal From User Materials Task Package

task_name: Create Pal From User Materials
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## Goal

Create a draft Pal Pack from a user goal and approved user materials while preserving source content and public/private boundaries.

## Required Inputs

- user goal;
- Pal name, id, and directory proposal;
- responsibilities and non-responsibilities;
- approved source materials;
- privacy classification;
- target language and tone;
- optional research approval;
- confirmation of allowed write path.

## Allowed Reads

- Pal Pack templates;
- Pal Pack standard docs;
- approved user materials;
- approved research reports;
- approved reference Pal Packs.

## Allowed Writes

- approved new `pals/<Pal-Directory>/` only.

## Forbidden Writes

- `contacts/`;
- `registry/`;
- existing unrelated Pal directories;
- private `memory/user/` or `memory/project/`;
- runtime `state/`;
- private `reports/`;
- executable files.

## Execution Steps

1. Create root Pal files.
2. Create an output contract.
3. Classify source materials into knowledge, Skills, workflows, runbooks, templates, examples, and evals.
4. Preserve important source details with traceability.
5. Add job-specific evals and failure cases.
6. Produce a creation report.
7. Parse `pal.json`.

## Expected Evidence

- created path list;
- skipped path list;
- `pal.json` parse result;
- source coverage note;
- eval coverage note;
- not-run checks;
- risks and missing assets.

## Acceptance

PalSmith accepts the result only when the Pal has enough job-specific assets to try a real task and no private material was copied into public files without approval.
