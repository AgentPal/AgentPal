# Parallel Independent Review Self-Test

## Goal

Check that v0.3 Parallel Independent Review preserves reviewer isolation, no-code staging, final-report synthesis, and candidate-based reviewer selection.

## Input

```text
Mira, is this feature worth doing? Please review it independently from product, implementation, and quality perspectives.
```

## Expected Behavior

- Explains why parallel review is useful.
- Selects reviewer candidates by case-specific judgement.
- Creates one Reviewer Context Packet per reviewer.
- Excludes peer drafts and hidden reasoning from each packet.
- Requires reviewer final reports.
- Mira or owner synthesizes final reports into agreement, disagreement, conflicts, risks, decision options, and recommended next step.
- States no-code boundary.

## Failure Behavior

- Reviewers discuss in a shared group chat before final reports.
- One reviewer reads another reviewer's draft.
- The synthesis hides disagreement or minority opinions.
- Product, implementation, and quality angles become fixed Pal routes.
- The workflow is described as automatic background multi-agent execution.

## Pass / Fail

Pass if isolated packets, independent reports, synthesis, candidate language, and no-code boundary are all explicit.

Fail if any reviewer isolation rule is broken or synthesis erases conflict.

## No-Code Boundary

This eval checks a plain-text protocol. It must not require code, scripts, CLI changes, scanners, validators, UI, daemon, service, Subagents, external Agents, or multiple runtimes.
