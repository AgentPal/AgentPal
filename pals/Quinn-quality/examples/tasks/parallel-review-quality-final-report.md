# Quinn Parallel Review Quality Final Report Example

## Task

Provide the quality or release-risk perspective in an independent parallel review.

## Output Shape

```yaml
schema: agentpal.reviewer-final-report.v0.3
reviewer_candidate: Quinn
review_angle: quality
verdict: "blocked"
confidence: high
key_findings:
  - "Acceptance criteria and evidence requirements are missing."
risks:
  - "False readiness"
missing_context:
  - "Definition of Done"
  - "test evidence or not-run labels"
recommendation: "Define evidence criteria before accepting the work."
conditions:
  - "No pass without evidence."
questions_for_owner:
  - "What proof would satisfy the user goal?"
notes: "This is a quality report, not the final synthesis."
```
