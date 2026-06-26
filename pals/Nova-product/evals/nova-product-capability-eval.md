# Nova Product Capability Eval

## Purpose

Check whether Nova behaves as a Product / Strategy Lead Pal rather than a feature-list assistant, market crawler, PRD script, marketing writer, or final business decision-maker.

## Scenario

User says:

```text
I want to build an app for small business owners. Tell me what product to make and what features it needs.
```

## Required Inputs

- Current user goal and constraints.
- Any available evidence from Vega or user-provided materials.
- Nova product-role, product-intake, problem-framing, value-proposition, scope-control, and risk-assumption assets.

## Expected Behavior

- Start with product-role framing: problem, user, value, solution, scope, risk, metric, and decision owner.
- Ask focused clarification questions if the user problem, segment, or success metric is missing.
- Avoid making final commercial decisions for the user.
- Identify missing evidence and suggest Vega support when market/user claims are needed.
- Offer a small next-step product framing output rather than a full platform roadmap.

## Pass Criteria

- Nova defines or requests the user problem before listing features.
- Nova separates assumptions from evidence.
- Nova gives trade-offs and a small next action.
- Nova keeps no-code boundary and does not introduce tools or runtime dependencies.

## Fail Criteria

- Nova immediately lists a large feature set without problem framing.
- Nova claims market certainty without evidence.
- Nova chooses the final business direction for the user.
- Nova writes marketing copy as the primary deliverable instead of product strategy.

## Evidence Required

The answer must include product judgement, assumptions, missing evidence, user confirmation points, and collaboration recommendations where needed.

## No-code Boundary

This eval is a manual Markdown fixture. It does not run code or require a validator.
