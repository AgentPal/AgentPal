# product-feedback-synthesis

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：反馈整理

## Purpose

Turn raw feedback, user comments, bug-like complaints, feature requests, and stakeholder opinions into themes, product signals, decisions, and next actions.

## Good Fit

- Multiple feedback items conflict.
- User wants to know what feedback means for product direction.
- Need to update PRD, scope, or roadmap.

## Poor Fit

- Feedback contains private customer data that cannot be summarized safely.
- User asks for sentiment mining without source permission.

## Input Information

- Feedback items or summaries.
- Source type and recency.
- User segment.
- Product version.
- Current scope and goals.

## Process

1. Normalize feedback into themes.
2. Separate bugs, usability issues, feature requests, and strategic signals.
3. Check frequency, severity, and target-user fit.
4. Recommend product actions: fix, investigate, prioritize, icebox, reject.
5. Update decision or handoff artifacts when needed.

## Output Format

```text
# Feedback Synthesis
## Themes
## Product Signals
## Recommended Actions
## PRD / Scope Changes
## Evidence Gaps
```

## Acceptance Standard

The output helps decide what to change, not just what users said.

## Risk Boundary

Do not store raw private feedback by default. Summarize and anonymize.

## Related Skills / Runbooks

Feeds `feature-prioritization`, `decision-log-writer`, and `prd-writer`.

