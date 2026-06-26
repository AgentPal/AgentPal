# incident-review

## Purpose

Structure a failure or incident review so Rhea can identify impact, timeline, evidence, root causes, mitigations, and follow-up actions.

## When to use

Use after failed commands, broken releases, unsafe file changes, environment regressions, privacy exposure, or repeated runtime failures.

## Inputs

Incident summary, timeline, observed impact, commands/actions, evidence, affected paths/systems, mitigation status, and open risks.

## Required context

Incident review knowledge, evidence review, risk classification, and collaboration boundaries.

## Process

1. State what happened and what evidence proves it.
2. Classify severity and current status.
3. Build a short timeline.
4. Identify contributing factors and root-cause candidates.
5. Identify mitigations and rollback/recovery actions.
6. Define follow-up owners and due evidence.
7. Distill reusable lessons only if public-safe.

## Output

Incident review with impact, timeline, evidence, root-cause candidates, mitigations, follow-ups, and not-run items.

## Quality bar

The review must be blameless, evidence-based, and action-oriented.

## User confirmation points

Ask before sharing sensitive logs, writing memory, or assigning follow-up changes.

## No-code boundary

This skill creates a review artifact. It does not monitor systems or run recovery.

## Common mistakes

- Blaming a person instead of identifying conditions.
- Omitting what evidence is missing.
- Skipping follow-up actions.
- Writing private incident details into public assets.

## Example

"The release check failed because JSON parse failed in `registry/pal.index.json`; impact limited to release readiness; follow-up is to fix JSON and rerun parse."

