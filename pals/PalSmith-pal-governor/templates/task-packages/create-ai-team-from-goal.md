# Create AI Team From Goal Task Package

task_name: Create AI Team From Goal
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## Goal

Create a small, bounded Pal team design and optional draft team assets from a plain-language user goal.

## Required Inputs

- user goal;
- target domain and scenarios;
- preferred team size;
- owner/verifier expectation;
- team-local vs global-contact preference;
- approved source materials;
- target write path;
- explicit confirmation before writes.

## Allowed Reads

- PalSmith AI team examples;
- Pal team templates;
- approved reference Pal Packs;
- approved user materials.

## Allowed Writes

- approved team directory;
- approved new member Pal directories when explicitly confirmed.

## Forbidden Writes

- `contacts/`;
- `registry/`;
- unrelated Pal directories;
- private memory, state, reports, credentials, and executable files.

## Execution Steps

1. Write team purpose and scope.
2. Create member Pal design cards.
3. Define owner, verifier, and consultant boundaries.
4. Define Context Packet and context-sharing rules.
5. Add conflict risks and eval outline.
6. Produce team creation report.

## Expected Evidence

- team directory path;
- member list;
- created/skipped paths;
- parse results for any created `pal.json`;
- not-run checks;
- registration recommendations only, not actual contacts/registry writes.

## Acceptance

PalSmith accepts the result only when every member has a clear job, non-responsibility boundary, and evidence-backed creation report.
