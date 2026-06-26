# Acceptance Criteria Design Skill

## Purpose

Create clear, testable acceptance criteria that define what must be true for a user goal, artifact, Pal asset, or release candidate to be accepted.

## When to use

Use before implementation, after a vague request, or during review when acceptance is unclear.

## Inputs

User goal, target user, deliverable type, constraints, risk level, required artifacts, examples, non-goals, and evidence expectations.

## Required context

Read the relevant user request, Quinn output contract, `acceptance-criteria-knowledge.md`, and target Pal or project scope when available.

## Process

1. Restate the goal in verifiable terms.
2. Separate functional, evidence, boundary, privacy, release, and quality criteria.
3. Convert vague wishes into observable conditions.
4. Add negative criteria for forbidden outcomes.
5. Link each criterion to evidence that can prove or disprove it.
6. Mark unknowns and user decisions.

## Output

Acceptance criteria list with criterion, evidence required, pass condition, fail condition, risk if not verified, and owner of next evidence.

## Quality bar

Each criterion must be testable or reviewable. If a criterion cannot be verified, label it as a decision or assumption rather than acceptance.

## User confirmation points

Ask when acceptance depends on user preference, private business rules, release tolerance, or risk acceptance.

## No-code boundary

Acceptance criteria are review instructions, not automated tests or validators.

## Common mistakes

- Writing aspirations instead of observable criteria.
- Omitting forbidden outcomes.
- Ignoring evidence source.
- Making Quinn the final business decision maker.

## Example

For a Quinn upgrade, acceptance criteria include role renamed to Quality / Verification Lead, required skills present, JSON parse passing, no-code boundary intact, and false-completion eval added.
