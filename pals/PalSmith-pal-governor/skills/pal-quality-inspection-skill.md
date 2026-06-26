# Pal Quality Inspection Skill

## Purpose

Inspect whether a Pal can perform its real job, not only whether its files exist.

## When To Use

Use when the user says a Pal feels weak, asks whether it can work, asks for health inspection, or requests publish readiness.

## Inputs

- target Pal path or id
- role and intended usage
- release intent
- approved read paths
- whether registry/contacts checks are allowed
- whether web research or user materials are in scope

## Required Context

Read target root files, indexes, `pal-quality-criteria-knowledge.md`, `pal-job-expertise-research-method.md`, quality protocol/template/eval, and registry/contacts only when relevant.

## Process

1. Verify Pal Pack shape and parse `pal.json`.
2. Build a job fitness model for the role.
3. Compare existing knowledge, skills, workflows, output contract, examples, and evals against the model.
4. Score role fit, job expertise depth, skill coverage, knowledge coverage, workflow coverage, output contracts, eval coverage, research gap, user material gap, and collaboration fit.
5. Identify missing knowledge, skills, workflows, templates, and evals.
6. Recommend web research only when it would improve role expertise; mark it `web research not run` unless Runtime actually ran it.
7. Recommend user uploads when personalization or domain-specific context is needed.
8. Produce a Pal Job Fitness Report.

## Output

- Pal Job Fitness Report
- dimension scores
- missing knowledge/skills/workflows/evals
- suggested web research
- suggested user uploads
- next Runtime Task Package

## Quality Bar

The report must explain whether the Pal can do the job. A structurally complete but shallow Pal should not receive a high job fitness judgement.

## User Confirmation Points

- reading private materials
- writing report files
- running web research
- applying fixes

## No-Code Boundary

Inspection is read-first. Fixes require separate confirmed Runtime Task Packages.

## Common Mistakes

- treating file completeness as role competence
- giving only a total score
- ignoring missing domain knowledge
- failing to recommend user materials
- claiming research was done without evidence

## Example

A website operator Pal with root files but no SEO knowledge, content workflow, analytics interpretation skill, or eval cases may pass structure but fail job expertise depth and workflow coverage.
