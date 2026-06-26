# Pal Conflict Detection Protocol

Status: PalSmith v0.2 no-code protocol.

Conflict detection identifies overlap, gaps, and unsafe registration choices across Pals and Pal teams. It gives recommendations only; it does not modify contacts or registry.

## Conflict Types

- Pal id conflict
- direct call or alias conflict
- responsibility overlap
- responsibility gap
- owner / verifier duplicate or missing
- Mira responsibility confused with a business Pal
- PalSmith responsibility confused with a business Pal
- too many team Pals owning the same task
- one Pal owning too broad a scope
- missing non-responsibility boundary
- ordinary Skill treated as a Pal

## Severity

- P0: registry / contacts breakage, duplicate ids, or ordinary Skill registered as Pal
- P1: direct-call collision, unclear owner, unsafe public/private boundary
- P2: role overlap, vague boundary, weak naming
- P3: style or documentation clarity

## Output

`Conflict Report`:

- conflict type
- involved Pals
- severity
- evidence paths
- recommendation: keep overlap, clarify boundary, merge, split, rename alias, update contacts, or ask user
- required user decisions

## Boundary

Conflict detection never auto-edits Pal files, registry, or contacts.
