# Release Quality Gate Skill

## Purpose

Decide whether a release candidate has enough evidence, risk handling, documentation, rollback readiness, and user confirmation to proceed.

## When to use

Use before publishing, tagging, shipping a package, exporting a Pal, announcing readiness, or sending a user-facing deliverable.

## Inputs

Release scope, version or artifact, changed files, test results, documentation, source inventory, privacy review, rollback plan, known issues, and user decision needs.

## Required context

Read `release-quality-gate-knowledge.md`, relevant release checklist, Rhea safety evidence when available, and PalSmith publish gate evidence for Pal assets.

## Process

1. Confirm release scope and intended audience.
2. Check functional completion and acceptance evidence.
3. Check regression, privacy, security, license, source, and rollback evidence.
4. Identify not-run checks and whether they block.
5. Classify release risk.
6. Recommend pass, conditional pass, fail, blocked, or needs-more-evidence.

## Output

Release quality gate report with decision, evidence, blockers, conditional risks, not-run items, rollback readiness, and user confirmations.

## Quality bar

A release pass requires evidence. Local completeness does not prove public release readiness.

## User confirmation points

Required before publish, tag, push, external send, public announcement, export with memory, or risk waiver.

## No-code boundary

Quinn does not publish, tag, push, package, or release. Runtime or user performs approved actions.

## Common mistakes

- Treating local files as published release.
- Ignoring rollback evidence.
- Hiding not-run release checks.
- Letting urgency waive privacy review.

## Example

Before AgentPal RC release, Quinn requires no-code boundary evidence, JSON parse, docs consistency, source inventory for research-backed claims, clean export safety, and known not-run items.
