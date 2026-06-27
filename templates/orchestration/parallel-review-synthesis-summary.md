# Parallel Review Synthesis Summary Template

Use this after independent reviewer final reports exist.

```yaml
schema: agentpal.parallel-review-synthesis-summary.v0.3
synthesis_id:
owner_pal:
reviewers:
  - review_id:
    reviewer_candidate:
    review_angle:
    verdict:
    confidence:
agreement:
  - <shared-finding>
disagreement:
  - <difference>
conflicts:
  - <conflict>
risks:
  - <risk>
decision_options:
  - option:
    tradeoffs:
    conditions:
recommended_next_step:
requires_user_decision: true
repair_or_followup_package:
  - <follow-up>
routing_memory_candidate:
  write_candidate: false
  summary:
```

Rules:

- Synthesis cannot smooth away conflict.
- If reviewers disagree, show the disagreement to the user or create a follow-up package.
- Do not delete minority opinions.
- Do not read reviewer drafts or hidden reasoning unless explicitly authorized by a separate packet.
