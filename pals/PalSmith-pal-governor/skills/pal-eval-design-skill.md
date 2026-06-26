# Pal Eval Design Skill

## Purpose

Design evals that prove a Pal can perform its role and respect boundaries.

## When To Use

Use when creating a Pal, improving job fitness, preparing publish readiness, or checking a team.

## Inputs

- target Pal role and responsibilities
- target workflows and outputs
- risky requests
- expected refusal or escalation behavior

## Required Context

Read target Pal role, output contract, skills, workflows, and `pal-quality-criteria-knowledge.md`.

## Process

1. Identify normal task cases.
2. Identify edge cases and risky cases.
3. Define expected output shape.
4. Define pass/fail criteria with evidence.
5. Include `missing` and `not-run` handling.
6. Add at least one boundary/refusal case.
7. Link evals to job fitness dimensions.

## Output

- eval plan
- Markdown eval files
- definition of done
- readiness implications

## Quality Bar

An eval should expose whether the Pal can do the job, not only whether it can repeat its description.

## User Confirmation Points

- using private user examples
- writing eval files
- marking lifecycle state from eval evidence

## No-Code Boundary

Markdown evals are review assets, not automated test scripts.

## Common Mistakes

- only testing happy path
- omitting risky requests
- lacking expected evidence
- marking pass without running or reviewing

## Example

A legal intake Pal eval includes a normal intake summary, missing facts case, unauthorized legal advice request, confidentiality boundary case, and source uncertainty case.
