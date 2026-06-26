# Pal Workflow Design Skill

## Purpose

Design multi-step workflows and runbooks that make a Pal's work repeatable.

## When To Use

Use when a Pal needs a sequence such as intake to report, draft to review, import to staging, or publish readiness review.

## Inputs

- target task sequence
- target Pal or team
- expected evidence
- user confirmation points
- failure modes

## Required Context

Read target Pal role, existing workflows, `pal-skill-vs-knowledge-vs-workflow.md`, and relevant protocols/templates.

## Process

1. Identify start condition, end condition, and owner.
2. Break the work into ordered steps.
3. Define inputs, outputs, and evidence for each step.
4. Add decision points and user confirmations.
5. Add `missing`, `not-run`, and blocker handling.
6. Separate workflow from stable runbook when the sequence becomes repeatable.
7. Add eval cases to prove the workflow works.

## Output

- workflow plan or draft
- runbook candidate
- template needs
- eval needs
- Runtime Task Package for approved writes

## Quality Bar

A workflow should be executable by a runtime-readable Pal context without hidden assumptions.

## User Confirmation Points

- file writes
- high-risk actions
- private data reads
- publishing or registry changes

## No-Code Boundary

Workflows do not automate execution. They guide Pal judgement and Runtime Task Packages.

## Common Mistakes

- writing a checklist with no evidence fields
- hiding user confirmation points
- mixing workflow with executable script behavior
- leaving failure paths undefined

## Example

A Pal import workflow starts with source classification, then staging, risk review, install recommendation, user confirmation, install package, and post-install verification.
