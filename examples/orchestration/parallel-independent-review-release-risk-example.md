# Parallel Independent Review Release Risk Example

## User Input

```text
Mira, please independently evaluate this version's release risk from different angles.
```

## Why Parallel Review Is Useful

Release risk can hide in quality evidence, runtime safety, documentation, and product scope. Independent review prevents one optimistic release narrative from anchoring every reviewer.

## Reviewer Candidates

- Quinn: acceptance evidence and release quality.
- Rhea: runtime, permission, rollback, and safety boundary.
- Morgan: documentation and release-note completeness.

These are case-specific candidates, not fixed release routes.

## Reviewer Context Packets

```yaml
packets:
  - packet_id: rcp-release-risk-quinn
    review_id: relrisk-quinn
    to_reviewer_candidate: Quinn
    review_angle: quality
    allowed_context:
      - "release scope summary"
      - "test results or not-run labels"
    excluded_peer_outputs:
      - Rhea draft
      - Morgan draft
    output_contract:
      template: templates/orchestration/reviewer-final-report.md
  - packet_id: rcp-release-risk-rhea
    review_id: relrisk-rhea
    to_reviewer_candidate: Rhea
    review_angle: system
    allowed_context:
      - "release action list"
      - "rollback notes"
    excluded_peer_outputs:
      - Quinn draft
      - Morgan draft
    output_contract:
      template: templates/orchestration/reviewer-final-report.md
  - packet_id: rcp-release-risk-morgan
    review_id: relrisk-morgan
    to_reviewer_candidate: Morgan
    review_angle: document
    allowed_context:
      - "release notes"
      - "public docs summary"
    excluded_peer_outputs:
      - Quinn draft
      - Rhea draft
    output_contract:
      template: templates/orchestration/reviewer-final-report.md
```

## Independent Final Reports

```yaml
reports:
  - review_id: relrisk-quinn
    reviewer_candidate: Quinn
    review_angle: quality
    verdict: "blocked"
    confidence: high
    key_findings:
      - "Missing test output prevents release quality pass."
    risks:
      - "False completion"
    missing_context:
      - "current test evidence"
    recommendation: "Collect test evidence or mark checks not-run."
  - review_id: relrisk-rhea
    reviewer_candidate: Rhea
    review_angle: system
    verdict: "risk medium"
    confidence: medium
    key_findings:
      - "Rollback path exists but publish action must be explicit."
    risks:
      - "High-risk release action without confirmation"
    missing_context:
      - "exact release target"
    recommendation: "Require user confirmation before push/tag/release."
  - review_id: relrisk-morgan
    reviewer_candidate: Morgan
    review_angle: document
    verdict: "needs repair"
    confidence: medium
    key_findings:
      - "Release notes omit one user-facing limitation."
    risks:
      - "Users may overread current capability."
    missing_context:
      - "known limitations list"
    recommendation: "Patch release notes before release."
```

## Synthesis Summary

```yaml
agreement:
  - "Release should not proceed until missing evidence is resolved."
disagreement:
  - "Rhea sees medium system risk, while Quinn blocks quality pass."
conflicts:
  - "Rollback readiness does not compensate for missing test evidence."
risks:
  - "Unsupported release readiness"
decision_options:
  - option: "Do not release yet"
    tradeoffs: "Safer, requires more evidence"
    conditions: "Collect tests and update docs"
recommended_next_step: "Return to owner for release evidence and doc repair package."
requires_user_decision: true
```

## Good Behavior

- Quality, system, and document reviews are isolated.
- Missing evidence blocks release readiness.
- Synthesis preserves the stronger Quinn block.

## Bad Behavior

- Rhea's medium risk summary is used to override Quinn's blocked result.
- Reviewers see each other's drafts and converge too early.

## Acceptance Criteria

- Release risk uses multiple independent reports.
- Synthesis does not hide blocked quality evidence.
- No release action occurs.

## No-Code Boundary Note

This is a review protocol only. It does not push, tag, publish, or run an automatic release robot.
