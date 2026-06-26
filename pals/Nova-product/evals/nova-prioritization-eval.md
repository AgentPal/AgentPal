# Nova Prioritization Eval

## Purpose

Check whether Nova can prioritize competing product requests with trade-offs instead of accepting every feature.

## Scenario

User says:

```text
For v1, include onboarding, team invites, billing, analytics, AI reports, templates, export, admin roles, and mobile.
```

## Required Inputs

- Feature list.
- Product goal and target user if available.
- Nova prioritization, scope-control, MVP/release-scope, roadmap, and risk-assumption assets.

## Expected Behavior

- Ask for product goal, primary user, and release success metric if absent.
- Group items by user value, risk reduction, dependency, and release necessity.
- Propose a v1 cut with must-have, should-have, later, and evidence-needed groups.
- Explain trade-offs and assumptions.
- Avoid promising delivery effort without Atlas feasibility input.

## Pass Criteria

- Nova makes prioritization criteria explicit.
- Nova reduces scope to a coherent release hypothesis.
- Nova labels feasibility and market evidence as assumptions when not verified.
- Nova recommends Atlas / Quinn collaboration when implementation or acceptance risk matters.

## Fail Criteria

- Nova says all features should be included.
- Nova gives dates or effort estimates without technical assessment.
- Nova hides trade-offs or user confirmation points.

## Evidence Required

The output must include priority groups, rationale, trade-offs, assumptions, and confirmation points.

## No-code Boundary

This eval does not run planning tools or create a project-management system.
