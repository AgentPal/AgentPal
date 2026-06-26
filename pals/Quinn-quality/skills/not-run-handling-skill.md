# Not-run Handling Skill

## Purpose

Handle checks, tests, reviews, or evidence paths that were not executed without converting them into pass or fail incorrectly.

## When to use

Use whenever a report says a check was skipped, unavailable, blocked, not applicable, not attempted, or impossible in the current Runtime.

## Inputs

Not-run item, reason, required evidence, affected acceptance criteria, risk level, blocker status, and proposed follow-up.

## Required context

Read `not-run-partial-blocked-knowledge.md`, acceptance criteria, release gate, and available Runtime capability evidence.

## Process

1. Name the not-run item precisely.
2. Record why it was not run.
3. Determine whether it is required for acceptance.
4. Classify impact as acceptable risk, partial, needs follow-up, or blocker.
5. Assign next action and owner.
6. Keep the not-run item visible in the final report.

## Output

Not-run register with item, reason, impact, blocker status, owner, follow-up, and residual risk.

## Quality bar

not-run is not fail by default, but it is never pass. The report must preserve that distinction.

## User confirmation points

Ask before accepting not-run on release, destructive, privacy, production, or high-risk criteria.

## No-code boundary

Quinn records and triages not-run items. Runtime executes follow-up checks only if approved and available.

## Common mistakes

- Omitting skipped checks from final report.
- Calling blocked checks "not applicable" without evidence.
- Treating no tool available as pass.
- Over-blocking harmless not-run checks.

## Example

Browser preview was not run because the browser binary was unavailable. Quinn records it as not-run, explains visual QA risk, and recommends installing or using another verification path.
