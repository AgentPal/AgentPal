# Nova PRD Quality Eval

## Purpose

Check whether Nova can produce or review a PRD / Product Brief that is product-complete and collaboration-safe.

## Scenario

User says:

```text
Write a PRD for a customer feedback feature.
```

## Required Inputs

- User request and known product context.
- Nova PRD/product brief, requirements discovery, metrics feedback, product handoff, and collaboration boundary assets.

## Expected Behavior

- Clarify or explicitly mark missing product goal, target users, problem, constraints, evidence, metric, release scope, and risks.
- Produce a PRD or product brief structure with problem, users, value, non-goals, requirements, acceptance criteria candidates, metrics, risks, open questions, and handoff needs.
- Suggest Harper only for final wording, Morgan for document packaging, Atlas for technical implementation package, Quinn for acceptance-quality review, and Vega for missing evidence.

## Pass Criteria

- PRD structure is complete enough to guide product discussion.
- Missing inputs are not invented.
- Acceptance criteria are product-level candidates, not a claim that implementation is ready.
- Collaboration boundaries are explicit.

## Fail Criteria

- Nova outputs only a feature list.
- Nova invents user research or market data.
- Nova writes polished marketing copy instead of product requirements.
- Nova claims engineering feasibility without Atlas input.

## Evidence Required

The response must include PRD sections, assumptions, evidence needs, user confirmations, and handoff notes.

## No-code Boundary

This eval is a documentation-quality fixture only.
