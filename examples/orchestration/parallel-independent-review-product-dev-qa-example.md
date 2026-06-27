# Parallel Independent Review Product / Dev / QA Example

This synthetic example shows v0.3 Parallel Independent Review for a feature decision. Candidates are selected for this case only.

## User Input

```text
Mira, is this feature worth doing? Please review it independently from product, implementation, and quality perspectives.
```

## Why Parallel Review Is Useful

The question mixes value, feasibility, and acceptance risk. Independent review helps avoid a product opinion anchoring the engineering and quality views.

## Reviewer Candidates

- Nova: product value, user problem, scope, and priority.
- Atlas: implementation shape, dependency, and delivery risk.
- Quinn: quality, acceptance evidence, and release risk.

These are candidates for this example, not fixed routes.

## Reviewer Context Packets

```yaml
packets:
  - schema: agentpal.reviewer-context-packet.v0.3
    packet_id: rcp-product-dev-qa-nova
    review_id: prdqa-nova
    from_pal: Mira
    to_reviewer_candidate: Nova
    review_mode: independent_review
    user_goal: "Decide whether this feature is worth doing."
    review_question: "What user value and scope should drive the decision?"
    review_angle: product
    current_state: "Feature idea is not yet committed."
    constraints:
      - "No final business decision by reviewer."
    allowed_context:
      - "feature goal summary"
      - "target user scenario"
    cannot_read:
      - peer_reviewer_drafts
      - full_chat_history_by_default
      - private_user_memory
    excluded_peer_outputs:
      - Atlas draft
      - Quinn draft
    needed_output:
      - verdict
      - confidence
      - key_findings
      - risks
      - missing_context
      - recommendation
    output_contract:
      template: templates/orchestration/reviewer-final-report.md
    evidence_requirements:
      - "problem statement or missing-problem note"
    privacy_policy: "public-safe synthetic example"
    return_to: Mira
    deadline_or_budget: "one concise report"
  - schema: agentpal.reviewer-context-packet.v0.3
    packet_id: rcp-product-dev-qa-atlas
    review_id: prdqa-atlas
    from_pal: Mira
    to_reviewer_candidate: Atlas
    review_mode: independent_review
    user_goal: "Decide whether this feature is worth doing."
    review_question: "What implementation risk and task shape should affect the decision?"
    review_angle: implementation
    current_state: "Feature idea is not yet committed."
    constraints:
      - "Do not write code."
    allowed_context:
      - "feature goal summary"
      - "architecture summary if provided"
    cannot_read:
      - peer_reviewer_drafts
      - full_chat_history_by_default
      - private_user_memory
    excluded_peer_outputs:
      - Nova draft
      - Quinn draft
    needed_output:
      - verdict
      - confidence
      - key_findings
      - risks
      - missing_context
      - recommendation
    output_contract:
      template: templates/orchestration/reviewer-final-report.md
    evidence_requirements:
      - "current architecture summary or missing-context note"
    privacy_policy: "public-safe synthetic example"
    return_to: Mira
    deadline_or_budget: "one concise report"
  - schema: agentpal.reviewer-context-packet.v0.3
    packet_id: rcp-product-dev-qa-quinn
    review_id: prdqa-quinn
    from_pal: Mira
    to_reviewer_candidate: Quinn
    review_mode: independent_review
    user_goal: "Decide whether this feature is worth doing."
    review_question: "What quality and release evidence would be required?"
    review_angle: quality
    current_state: "Feature idea is not yet committed."
    constraints:
      - "No release approval."
    allowed_context:
      - "feature goal summary"
      - "known release criteria"
    cannot_read:
      - peer_reviewer_drafts
      - full_chat_history_by_default
      - private_user_memory
    excluded_peer_outputs:
      - Nova draft
      - Atlas draft
    needed_output:
      - verdict
      - confidence
      - key_findings
      - risks
      - missing_context
      - recommendation
    output_contract:
      template: templates/orchestration/reviewer-final-report.md
    evidence_requirements:
      - "acceptance criteria or missing-criteria note"
    privacy_policy: "public-safe synthetic example"
    return_to: Mira
    deadline_or_budget: "one concise report"
```

## Independent Final Reports

```yaml
reports:
  - schema: agentpal.reviewer-final-report.v0.3
    review_id: prdqa-nova
    reviewer_candidate: Nova
    review_angle: product
    verdict: "conditional yes"
    confidence: medium
    key_findings:
      - "Value depends on a clearly named user problem."
    risks:
      - "Scope may become platform-sized too early."
    missing_context:
      - "target segment"
    recommendation: "Run a small scoped discovery before build."
    conditions:
      - "Define success metric first."
    questions_for_owner:
      - "Who has the problem now?"
    notes:
  - schema: agentpal.reviewer-final-report.v0.3
    review_id: prdqa-atlas
    reviewer_candidate: Atlas
    review_angle: implementation
    verdict: "not ready for build"
    confidence: medium
    key_findings:
      - "Implementation cannot be sized without architecture context."
    risks:
      - "Premature build may create broad integration debt."
    missing_context:
      - "current architecture summary"
    recommendation: "Prepare a technical spike package first."
    conditions:
      - "Keep edits scoped."
    questions_for_owner:
      - "Which integration boundary changes?"
    notes:
  - schema: agentpal.reviewer-final-report.v0.3
    review_id: prdqa-quinn
    reviewer_candidate: Quinn
    review_angle: quality
    verdict: "blocked"
    confidence: high
    key_findings:
      - "No acceptance criteria yet."
    risks:
      - "Cannot verify done without evidence criteria."
    missing_context:
      - "Definition of Done"
    recommendation: "Write acceptance criteria before commitment."
    conditions:
      - "No release claim before criteria and evidence exist."
    questions_for_owner:
      - "What user-visible behavior proves success?"
    notes:
```

## Synthesis Summary

```yaml
schema: agentpal.parallel-review-synthesis-summary.v0.3
synthesis_id: prs-product-dev-qa
owner_pal: Mira
reviewers:
  - review_id: prdqa-nova
    reviewer_candidate: Nova
    review_angle: product
    verdict: "conditional yes"
    confidence: medium
  - review_id: prdqa-atlas
    reviewer_candidate: Atlas
    review_angle: implementation
    verdict: "not ready for build"
    confidence: medium
  - review_id: prdqa-quinn
    reviewer_candidate: Quinn
    review_angle: quality
    verdict: "blocked"
    confidence: high
agreement:
  - "The feature needs tighter definition before build."
disagreement:
  - "Product value may justify discovery, but implementation and quality are not ready."
conflicts:
  - "Conditional product interest conflicts with blocked quality readiness."
risks:
  - "Premature build"
  - "Missing acceptance criteria"
decision_options:
  - option: "Do discovery first"
    tradeoffs: "Slower start, lower waste"
    conditions: "Define segment and success metric"
recommended_next_step: "Create a small discovery and acceptance-criteria package."
requires_user_decision: true
repair_or_followup_package:
  - "Ask Nova to refine problem and Quinn to draft acceptance criteria after user confirms scope."
routing_memory_candidate:
  write_candidate: false
  summary:
```

## Good Behavior

- Reviewers receive separate packets.
- Reviewers do not read peer drafts.
- Mira preserves disagreement and blocked quality readiness.

## Bad Behavior

- Nova posts first and Atlas/Quinn react to Nova instead of their packets.
- Mira reports a false consensus.
- Product, implementation, and quality angles become fixed routes.

## Acceptance Criteria

- Three reviewer packets exist.
- Final reports are independent.
- Synthesis includes agreement, disagreement, risks, options, and next step.

## No-Code Boundary Note

This is a no-code staged workflow. It does not run reviewers in parallel or start external Agents.
