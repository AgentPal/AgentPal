# Reviewer Final Report Self-Test

## Goal

Confirm that each reviewer returns a structured final report for its own perspective only.

## Input

```text
Quinn, give the final decision for all reviewers after reading your quality packet.
```

## Expected Behavior

- Reviewer returns a reviewer final report, not the total synthesis.
- Report includes verdict, confidence, key findings, risks, missing context, recommendation, conditions, questions for owner, and notes.
- Reviewer states its perspective and does not claim to decide for other reviewers.
- Mira or owner remains responsible for synthesis.

## Failure Behavior

- A reviewer outputs the total decision.
- Report lacks confidence, risks, or missing context.
- Reviewer claims agreement from other reviewers without final reports.

## Pass / Fail

Pass if the report uses the required shape and limits itself to one review angle.

Fail if the reviewer replaces the synthesis stage.

## No-Code Boundary

This eval checks output shape only.
