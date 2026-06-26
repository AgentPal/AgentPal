# Nova Problem Framing Eval

## Purpose

Check whether Nova prevents a requested feature from bypassing product problem discovery.

## Scenario

User says:

```text
Add a dashboard to our product so users can see everything.
```

## Required Inputs

- User request.
- Existing product context if available.
- Nova problem-framing, user-segment-persona, jobs-to-be-done, and requirements-discovery assets.

## Expected Behavior

- Ask what user problem the dashboard is meant to solve.
- Identify who experiences the problem and when.
- Ask what users do today and why the current alternative is insufficient.
- Define success criteria before accepting the dashboard as the right solution.
- Offer a problem statement template or draft only after assumptions are explicit.

## Pass Criteria

- Nova does not treat the dashboard as confirmed scope.
- Nova distinguishes user need, stakeholder desire, and possible solution.
- Nova asks for evidence or suggests Vega research if user behavior is unknown.

## Fail Criteria

- Nova starts implementation planning.
- Nova writes a dashboard PRD without problem confirmation.
- Nova expands the request into analytics, notifications, exports, and role permissions without user confirmation.

## Evidence Required

The response must include a problem statement candidate, open assumptions, and confirmation questions.

## No-code Boundary

This eval checks product reasoning only.
