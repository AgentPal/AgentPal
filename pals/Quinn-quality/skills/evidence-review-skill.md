# Evidence Review Skill

## Purpose

Judge whether returned evidence proves, contradicts, weakly supports, or fails to support a completion claim.

## When to use

Use whenever a Runtime, Pal, or agent claims completion, readiness, test pass, release safety, or quality acceptance.

## Inputs

Completion claim, changed files, diff summary, commands run, test/check outputs, manual verification, artifacts, failures, skipped checks, not-run items, risk notes, and executor identity.

## Required context

Read `evidence-review-knowledge.md`, target acceptance criteria, Definition of Done, and raw evidence snippets or file paths.

## Process

1. Map each claim to evidence.
2. Confirm who or what executed each check and where it ran.
3. Identify changed files and whether the evidence covers them.
4. Separate pass, fail, partial, not-run, blocked, and unknown.
5. Downgrade unsupported claims.
6. State whether the evidence supports acceptance.

## Output

Evidence review table with claim, evidence source, coverage, result, confidence, missing proof, and next action.

## Quality bar

The review must be stricter than a summary. It should prove the claim or clearly say that proof is missing.

## User confirmation points

Ask before reading private logs, screenshots, production output, credentials, or broad system data.

## No-code boundary

Quinn reviews evidence returned by Runtime. Quinn does not execute commands, inspect environments directly, or create validators.

## Common mistakes

- Treating a green statement as a green check.
- Ignoring changed files.
- Ignoring who executed a command.
- Calling not-run checks successful.

## Example

A report says tests passed but includes no command output. Quinn marks test evidence missing and the completion claim as needs-more-evidence.
