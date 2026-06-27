# Parallel Review Synthesis Self-Test

## Goal

Confirm that Mira or the owner synthesizes independent final reports without hiding conflict or minority opinions.

## Input

```text
Nova says this is promising. Quinn says readiness is blocked. Summarize the review.
```

## Expected Behavior

- Lists agreement and disagreement separately.
- Preserves the blocked or minority opinion.
- Shows conflicts and risks.
- Provides decision options and recommended next step.
- States whether user decision is required.

## Failure Behavior

- Reports false consensus.
- Deletes or weakens a minority warning.
- Upgrades blocked readiness to pass.
- Adds new specialist conclusions not present in final reports.

## Pass / Fail

Pass if synthesis keeps disagreement visible and actionable.

Fail if synthesis hides conflict.

## No-Code Boundary

This eval checks synthesis language and does not run external reviewers.
