# Derived Knowledge Standard

Derived knowledge is structured AgentPal knowledge produced from user project materials.

## Location

Default location:

`workspace/projects/<project-id>/derived-knowledge/`

## Inputs

Inputs may include user project docs, design files, requirements, issue notes, source files, assets, and user-provided explanations.

## Outputs

Derived knowledge may include:

- Project summary.
- User-provided docs summary.
- Business rules.
- Product constraints.
- Architecture notes.
- Glossary and domain concepts.

## Boundary

Derived knowledge is not a replacement for current source files. When current facts matter, the runtime must re-check the active project or clearly report that the knowledge is memory-derived and may be stale.

