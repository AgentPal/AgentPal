# Web Research To Knowledge Workflow

Status: R16 v0.4-fix no-code workflow.

Use this workflow when PalSmith judges that a Pal needs current, source-backed, or domain-specific expertise beyond the user's own materials.

## Flow

1. Define research questions from the Pal's responsibilities and job expertise model.
2. Ask whether network access is allowed and which source classes are acceptable.
3. Separate stable background knowledge from time-sensitive claims.
4. Ask the Runtime to gather approved sources only after confirmation.
5. Convert source evidence into knowledge cards, workflow updates, skill requirements, templates, eval cases, and uncertainty notes.
6. Preserve citations, dates, and source quality notes for facts that depend on external evidence.
7. Review the resulting Pal assets through job fitness inspection.

## Acceptance

- The research plan names source scope, freshness needs, and excluded source types.
- Facts, inference, recommendation, and uncertainty are separated.
- Derived Pal knowledge includes enough source traceability for later review.
- The workflow reports `not-run` if no network evidence was gathered.

## Boundary

PalSmith does not browse or download sources by itself. The current Runtime performs approved network access and must report source evidence.
