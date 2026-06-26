# Quality Report Writing Skill

## Purpose

Write concise, evidence-backed quality reports that show decision, evidence, risks, gaps, not-run items, and next actions.

## When to use

Use after evidence review, release gate, regression planning, completion audit, or cross-Pal review.

## Inputs

Review target, acceptance criteria, evidence table, risk table, not-run register, blockers, residual gaps, and recommended next owner.

## Required context

Read `quality-reporting-knowledge.md`, Quinn output contract, and the evidence/risk outputs from the current review.

## Process

1. Start with the decision.
2. Summarize evidence actually reviewed.
3. List risks by severity.
4. List gaps and not-run items separately.
5. State next action and owner.
6. Avoid unsupported reassurance.

## Output

Quality report with decision, evidence, risk, gaps, not-run, next action, and residual uncertainty.

## Quality bar

The report should be short enough for a user to act on and specific enough for a Runtime or Pal to continue.

## User confirmation points

Ask before recommending release, risk waiver, privacy-sensitive sharing, or high-risk acceptance.

## No-code boundary

The report is a Markdown judgement artifact. It does not execute, publish, or validate automatically.

## Common mistakes

- Hiding failure behind a positive summary.
- Mixing evidence and inference.
- Omitting not-run.
- Ending with no next action.

## Example

Final decision: partial. Evidence proves JSON parse and no-code boundary; browser preview is not-run; release remains blocked until visual QA or accepted risk.
