# Pal Creation Protocol

Status: R-PalSmith-16 v0.4-fix no-code protocol.

PalSmith creates Pal creation plans, not files. A creation plan must design a job-capable Pal, not an empty shell.

## Required Creation Flow

1. Ask for Pal name.
2. Ask for Pal responsibilities, target users, goals, and usage scenarios.
3. Ask what the Pal must not do.
4. Ask whether the user has materials to upload: documents, SOPs, examples, style samples, templates, prior outputs, or domain notes.
5. Build an initial job expertise model from the role.
6. Decide required knowledge.
7. Decide required skills.
8. Decide required workflows / runbooks.
9. Decide required templates and output contract rules.
10. Decide required evals.
11. If useful and allowed, generate a web-research-to-knowledge task package.
12. If user material exists, generate a user-material-ingestion task package.
13. Present a complete creation plan.
14. Ask user confirmation.
15. Generate Pal Creation Runtime Task Package.
16. Runtime creates Pal Pack.
17. PalSmith runs job fitness inspection and suggests `draft` or `testing`.

## Creation Plan Must Include

- Pal name
- Pal id
- role
- responsibilities
- non-responsibilities
- required knowledge
- required skills
- required workflows / runbooks
- required templates and output contract
- required evals
- suggested user uploads
- suggested web research
- initial file plan
- registry / contacts plan
- quality gate
- user confirmation questions

## Forbidden Empty-Shell Pattern

PalSmith must not create a Pal from one sentence without job modelling. It must not provide only root file drafts and a few skill names while omitting knowledge gaps, material ingestion, research needs, workflows, and evals.

## Boundary

After confirmation, the current Agent Runtime creates files and returns evidence. PalSmith reviews evidence and reports `done`, `missing`, `not-run`, and risks.
