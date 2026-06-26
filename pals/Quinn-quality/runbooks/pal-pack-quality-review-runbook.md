# Pal Pack Quality Review Runbook

## Trigger

A Pal Pack is created, upgraded, imported, exported, registered, or prepared for release.

## Inputs

Target Pal path, root files, `pal.json`, contacts/registry entries, skills, knowledge, workflows, runbooks, evals, reports, source inventory, and validation outputs.

## Steps

1. Verify standard Pal Pack shape.
2. Review role clarity and non-responsibilities.
3. Check skills, knowledge, workflows, runbooks, and evals against job fitness.
4. Check no-code and private/public boundary.
5. Check contacts/registry consistency when discoverability is involved.
6. Return gaps to PalSmith, Atlas, Rhea, or the target owner as needed.

## Decision points

- Is the target a valid Pal Pack?
- Does file completeness prove job fitness?
- Are public/private boundaries safe?

## Outputs

Pal Pack quality review with pass, partial, fail, blocked, or needs-more-evidence.

## Quality checks

File presence alone is not enough. Job fitness and eval coverage matter.

## Required user confirmation

Required before reading private memory, changing contacts/registry, exporting, publishing, or accepting public risk.

## Evidence to return

Files reviewed, JSON parse, required assets, gaps, no-code status, registry status, and decision.
