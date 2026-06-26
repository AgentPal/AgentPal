# User Material Ingestion Protocol

Status: R-PalSmith-16 v0.4-fix protocol.

PalSmith uses this protocol when the user provides documents, notes, examples, SOPs, templates, transcripts, or prior outputs for a Pal.

## Classification Types

- Knowledge
- Skill
- Workflow
- Runbook
- Template
- Eval
- Example
- Reference
- Persona / Voice
- Boundary
- Decision

## Process

1. Ask user approval for each source.
2. Inventory source name, path, section, date, privacy level, and intended use.
3. Classify each section.
4. Preserve examples, steps, exceptions, limits, source anchors, and decision rules.
5. Split long material into multiple files when needed.
6. Put uncertain sections into review/unclassified.
7. Prepare target files and Runtime Task Package.
8. Review output against content preservation checklist.

## Output

- Material Ingestion Plan
- Source Inventory
- Classification Table
- Knowledge Files Plan
- Skill Files Plan
- Workflow / Runbook Plan
- Template Plan
- Eval Plan
- Unclassified / Need User Decision
- Content Preservation Checklist

## Boundary

User material is private unless the user explicitly says otherwise. Runtime reads/writes only approved paths.
