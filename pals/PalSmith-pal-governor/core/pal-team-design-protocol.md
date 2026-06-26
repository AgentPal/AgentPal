# Pal Team Design Protocol

Status: PalSmith v0.2 no-code protocol.

Team design happens before team creation. PalSmith first turns a user's goal into a small, understandable team proposal, then asks whether to generate a Runtime Task Package.

## Team Design Inputs

- user goal
- business scenario
- desired output
- risk boundary
- existing Pals that should be reused
- whether team-local Pals may be created
- whether any Pals should enter global contacts

## Design Output

- suggested team name
- recommended Pal count
- member names and roles
- each Pal's responsibilities and non-responsibilities
- owner Pal
- verifier Pal
- consultant Pals
- collaboration mode
- Context Packet rules
- global contacts candidates
- team-local only candidates
- shared knowledge
- shared workflow
- team eval
- team capability map

## Team Size Control

Default to 3-5 Pals. Do not create 10+ Pals unless the user clearly asks for a complex team. Larger teams require explicit owner, verifier, and handoff rules.

## Beginner-Friendly Flow

1. Give the team proposal first.
2. Ask whether the user accepts it.
3. Generate the Runtime Task Package only after the user accepts.
4. Runtime creates files after confirmation.
5. PalSmith reviews evidence.

## Boundary

Team design is not automatic team creation. File writes, registry updates, and contacts updates remain separate confirmed runtime actions.
