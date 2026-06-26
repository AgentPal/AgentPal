# Pal Creation Skill

## Purpose

Design a Pal Pack that can actually work in its intended role, not just a directory with required files.

## When To Use

Use when the user wants to create a new Pal, create a personal work companion, turn a role into a Pal, or convert a user goal into a Pal Pack plan.

## Inputs

- desired Pal name or naming preference
- target responsibility and usage scenarios
- target language and audience
- user-provided materials or statement that none are available
- release intent: private, team-local, global contact, or public-share candidate
- optional reference Pals approved by the user

## Required Context

Read PalSmith identity files, Pal Pack standard docs, `pal-role-design-knowledge.md`, `pal-skill-vs-knowledge-vs-workflow.md`, `pal-content-preservation-principles.md`, and the Pal creation protocol/template.

## Process

1. Ask for Pal name if missing.
2. Ask for responsibilities, target users, usage scenes, and non-responsibilities.
3. Ask whether the user has documents, examples, SOPs, tone samples, domain notes, or prior outputs to upload.
4. Build an initial job fitness model: role fit, required knowledge, required skills, common workflows, output contracts, eval cases, risks, and collaboration boundaries.
5. Decide whether web research is useful. If yes, prepare a web-research-to-knowledge Runtime Task Package; if it is not run, label it `web research not run`.
6. Decide whether user material ingestion is useful. If yes, prepare a user-material-ingestion Runtime Task Package.
7. Propose a complete file plan: root files, output contract, skills, knowledge, workflows, runbooks, templates, examples, evals, memory/state/report placeholders, registry suggestion, contacts suggestion.
8. Ask for user confirmation before any Runtime write.
9. After Runtime creates files, review evidence and run job fitness inspection.

## Output

- Pal design plan
- job fitness model
- required knowledge/skills/workflows/evals
- user upload request
- optional web research task package
- Pal Creation Runtime Task Package
- post-creation quality report

## Quality Bar

A good creation plan explains what the Pal can do, what it cannot do, what knowledge it needs, what skills it needs, how it works, how it is tested, and what evidence is missing. It never creates an empty shell from one sentence.

## User Confirmation Points

- target name/id/directory
- whether to read user materials
- whether web research should run
- exact write paths
- whether registry/contacts updates remain suggestions only

## No-Code Boundary

PalSmith does not create files directly. The current Agent Runtime writes only after a confirmed Runtime Task Package and returns evidence.

## Common Mistakes

- generating only root files without role expertise
- omitting user material intake
- skipping research gap analysis
- treating registry/contacts writes as part of creation
- flattening all knowledge into one short card

## Example

User asks for a Xiaohongshu operations Pal. PalSmith asks the name, target content niche, posting goals, examples of preferred posts, forbidden claims, and whether web research on current platform content practices should run. Only then does it propose knowledge files, content planning skills, review workflows, eval cases, and a Pal Creation Task Package.
