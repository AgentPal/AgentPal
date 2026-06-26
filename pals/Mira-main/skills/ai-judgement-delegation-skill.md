# AI Judgement Delegation Skill

## Purpose

Help Mira choose the right Pal owner through case-specific AI judgement rather than fixed routing.

## When to use

Use when the request may belong to a specialist Pal, when multiple Pals may contribute, or when the owner boundary is unclear.

## Inputs

- User request and expected deliverable.
- Contacts / registry entries.
- Current Pal capability notes.
- Risk, evidence, and verification needs.
- User preference for direct answer, consult, delegation, or takeover.

## Required context

Read contacts / registry and the minimum owner candidate asset needed to judge fit. Do not load every Pal Pack.

## Process

1. Name the work type and success criteria.
2. Compare Mira-owned leadership work against specialist-owned professional work.
3. Check owner candidates from contacts / registry.
4. Decide one of: Mira answers, Mira consults, Mira delegates, Mira hands off, Mira asks clarification, or Mira reports owner gap.
5. If owner changes, make the handoff visible and let the owner answer immediately.

## Output

An owner judgement with a case-specific reason, followed by the selected action.

## Quality bar

The judgement must be explainable from the current request and available Pal pool. It must not rely on hard-coded topics or a hidden default owner.

## User confirmation points

Ask confirmation when delegation requires sharing private files, long memory, credentials, unpublished material, or system state beyond the user's immediate request.

## No-code boundary

This skill only structures judgement and delegation. It does not implement features, modify files, or create runtime agents.

## Common mistakes

- Routing by keyword instead of the deliverable, risk, and evidence needs.
- Keeping ownership because Mira received the request first.
- Sending work to PalSmith only through Mira when another owner Pal has a valid Pal asset governance need.
- Delegating without a Context Packet.

## Example

User asks for release readiness. Mira judges the work needs quality gate evidence, routes to the release-quality owner if registered, and keeps only progress summary responsibility.
