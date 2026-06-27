# Failure Example: Pal Group Chat Collapse

## Wrong Scenario

Mira asks several Pals to discuss in one shared thread:

```text
Nova, Atlas, and Quinn, talk together and decide whether this feature is worth doing.
```

Nova posts first. Atlas and Quinn read Nova's draft and adjust their answers around it. Mira reports the resulting agreement as independent review.

## Why It Is Wrong

Parallel Independent Review requires isolated reviewer context before synthesis. Shared drafts cause anchoring, copied assumptions, false consensus, and weaker risk discovery.

## Correct Behavior

Mira or the owner should create separate Reviewer Context Packets and collect final reports before synthesis:

```yaml
reviewers:
  - reviewer_candidate: Nova
    cannot_read:
      - Atlas draft
      - Quinn draft
  - reviewer_candidate: Atlas
    cannot_read:
      - Nova draft
      - Quinn draft
  - reviewer_candidate: Quinn
    cannot_read:
      - Nova draft
      - Atlas draft
synthesis_stage:
  can_read:
    - reviewer_final_reports
```

## Corresponding Eval

- `evals/orchestration/no-group-chat-collapse-in-parallel-review-self-test.md`
