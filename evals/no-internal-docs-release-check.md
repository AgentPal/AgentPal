# No Internal Docs Release Check

## Purpose

Verify that public release files do not reference private maintainer paths, internal reports, or copied internal documents.

## Preconditions

- Work from the public AgentPal repository root.
- Do not read or copy private maintainer directories.

## Manual Steps

1. Search for private maintainer directory names.
2. Search for local absolute development paths.
3. Search for internal report names.
4. Search for private memory, project state, screenshots, chat logs, or temporary task reports.
5. Replace any hit with a public placeholder or remove it.

## Expected Result

No public release file requires, references, or exposes private maintainer material.

## Failure Signs

- A public file asks users to read a maintainer-local path.
- A public file contains internal report titles or task-mode records.
- A public file contains private user memory or project state.

## Notes

Use placeholders such as `<path-to-AgentPal>`, `<your-project-path>`, or `C:/Projects/MyProject` when examples need paths.

