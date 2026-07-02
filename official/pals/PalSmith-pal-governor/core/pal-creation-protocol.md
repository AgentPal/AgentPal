# Pal Creation Protocol

Status: R-PalSmith-16 v0.4-fix no-code protocol.

PalSmith creates Pal creation plans, not files. A creation plan must design a job-capable Pal, not an empty shell.

## Required Creation Flow

1. Ask for or propose a human-style Pal name.
2. Capture role title separately from the Pal name.
3. Ask for Pal responsibilities, target users, goals, and usage scenarios.
4. Ask what the Pal must not do.
5. Ask whether the user has materials to upload: documents, SOPs, examples, style samples, templates, prior outputs, or domain notes.
6. Build an initial job expertise model from the role.
7. Run naming and import conflict checks.
8. Decide required knowledge.
9. Decide required skills.
10. Decide required workflows / runbooks.
11. Decide required templates and output contract rules.
12. Decide required evals.
13. If useful and allowed, generate a web-research-to-knowledge task package.
14. If user material exists, generate a user-material-ingestion task package.
15. Present a complete creation plan.
16. Ask user confirmation.
17. Generate Pal Creation Runtime Task Package.
18. Runtime creates Pal Pack.
19. PalSmith runs job fitness inspection and suggests `draft` or `testing`.

## Creation Plan Must Include

- Pal name
- human display name
- role title
- contact label
- canonical id
- aliases and optional user custom name
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
- Contact Capability Card placeholder or complete card
- suitable team recommendations
- unsuitable team boundaries
- naming conflict check result
- Pal Asset Preflight inheritance
- quality gate
- user confirmation questions

## Forbidden Empty-Shell Pattern

PalSmith must not create a Pal from one sentence without job modelling. It must not provide only root file drafts and a few skill names while omitting knowledge gaps, material ingestion, research needs, workflows, and evals.

## Forbidden Role-Only Name Pattern

PalSmith must not create Pals named only by role or function, such as `方案定制 Pal`, `外部调研 Pal`, `视频剪辑 Pal`, `产品经理 Pal`, or `测试 Pal`.

These phrases are role intent. PalSmith must propose or generate a human name, store the phrase or normalized job as `role_title`, and record a naming conflict check before proposing contacts or registry changes.

## Boundary

After confirmation, the current Agent Runtime creates files and returns evidence. PalSmith reviews evidence and reports `done`, `missing`, `not-run`, and risks.
