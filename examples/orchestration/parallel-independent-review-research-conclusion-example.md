# Parallel Independent Review Research Conclusion Example

## User Input

```text
Mira, independently review whether this research conclusion is strong enough to use in a public report.
```

## Why Parallel Review Is Useful

Research conclusions can fail through weak sources, product overclaiming, writing ambiguity, or quality evidence gaps. Independent review preserves those differences.

## Reviewer Candidates

- Vega: source quality and evidence strength.
- Nova: product decision relevance.
- Harper: public-facing wording risk.
- Quinn: evidence acceptance risk.

These are reviewer candidates for this case, not fixed routes.

## Reviewer Context Packets

```yaml
packets:
  - review_id: research-vega
    to_reviewer_candidate: Vega
    review_angle: research
    allowed_context:
      - "claim summary"
      - "source inventory"
    excluded_peer_outputs:
      - Nova draft
      - Harper draft
      - Quinn draft
  - review_id: research-nova
    to_reviewer_candidate: Nova
    review_angle: product
    allowed_context:
      - "claim summary"
      - "decision context"
    excluded_peer_outputs:
      - Vega draft
      - Harper draft
      - Quinn draft
  - review_id: research-harper
    to_reviewer_candidate: Harper
    review_angle: writing
    allowed_context:
      - "claim summary"
      - "intended audience"
    excluded_peer_outputs:
      - Vega draft
      - Nova draft
      - Quinn draft
  - review_id: research-quinn
    to_reviewer_candidate: Quinn
    review_angle: quality
    allowed_context:
      - "claim summary"
      - "evidence matrix"
    excluded_peer_outputs:
      - Vega draft
      - Nova draft
      - Harper draft
```

## Independent Final Reports

```yaml
reports:
  - review_id: research-vega
    reviewer_candidate: Vega
    review_angle: research
    verdict: "weak support"
    confidence: medium
    key_findings:
      - "Sources support a trend, not a universal claim."
    risks:
      - "Overgeneralization"
    missing_context:
      - "primary source for the strongest claim"
    recommendation: "Downgrade wording."
  - review_id: research-nova
    reviewer_candidate: Nova
    review_angle: product
    verdict: "usable with caveat"
    confidence: medium
    key_findings:
      - "Conclusion can guide prioritization if uncertainty is visible."
    risks:
      - "Product roadmap may overfit weak evidence."
    missing_context:
      - "user segment relevance"
    recommendation: "Use as directional input only."
  - review_id: research-harper
    reviewer_candidate: Harper
    review_angle: writing
    verdict: "rewrite needed"
    confidence: high
    key_findings:
      - "Current wording sounds stronger than evidence."
    risks:
      - "Reader may treat inference as fact."
    missing_context: []
    recommendation: "Add uncertainty markers."
  - review_id: research-quinn
    reviewer_candidate: Quinn
    review_angle: quality
    verdict: "blocked for public report"
    confidence: high
    key_findings:
      - "Evidence matrix has unproven claim."
    risks:
      - "False authority"
    missing_context:
      - "source for key claim"
    recommendation: "Block public use until claim is downgraded or sourced."
```

## Synthesis Summary

```yaml
agreement:
  - "The conclusion should be weakened or caveated."
disagreement:
  - "Nova finds directional value, while Quinn blocks public report use."
conflicts:
  - "Decision usefulness does not equal publication readiness."
risks:
  - "Overclaiming"
decision_options:
  - option: "Use internally only"
    tradeoffs: "Useful for planning, not public proof"
    conditions: "Label as directional"
  - option: "Publish after repair"
    tradeoffs: "Needs source repair and rewrite"
    conditions: "Add source or downgrade claim"
recommended_next_step: "Return to Vega and Harper for claim downgrade and wording repair."
requires_user_decision: true
```

## Good Behavior

- Source quality and public wording are reviewed separately.
- Minority/product value view is preserved without overriding quality block.

## Bad Behavior

- Vega's source concern is hidden because Nova says it is directionally useful.
- Harper reads Vega's draft and only copies its wording.

## Acceptance Criteria

- Reviewer reports stay independent.
- Synthesis shows the conflict between internal usefulness and public readiness.

## No-Code Boundary Note

This example does not browse, download, or validate sources automatically.
