# Atlas Parallel Review Implementation Final Report Example

## Task

Provide the implementation perspective in an independent parallel review.

## Output Shape

```yaml
schema: agentpal.reviewer-final-report.v0.3
reviewer_candidate: Atlas
review_angle: implementation
verdict: "not ready for build"
confidence: medium
key_findings:
  - "Implementation scope cannot be estimated without architecture context."
risks:
  - "Runtime execution may infer too broad a change."
missing_context:
  - "allowed files"
  - "acceptance criteria"
recommendation: "Create a scoped technical spike package."
conditions:
  - "Keep runtime as execution layer only."
questions_for_owner:
  - "Which integration boundary changes?"
notes: "This report does not decide product value or release readiness."
```
