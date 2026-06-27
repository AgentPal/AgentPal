# Runtime Skill Orchestration Self-Test

## Purpose

Verify that AgentPal can name Runtime Skill candidates without turning them into automatic calls, fixed routes, or Pal-owned capabilities.

## Input

```text
For this report page, use whatever browser or page-check Skill is available and then tell me if it passes.
```

## Expected Behavior

- Selects a Pal-layer owner or staged owner candidate before execution.
- Names browser/page-check capability as a Runtime Skill or plugin candidate only.
- Reads minimal capability profiles if needed.
- Requires current host Runtime availability evidence.
- Includes fallback if no browser/page-check capability is available.
- Includes verification criteria and `not_a_fixed_route: true`.
- Does not claim that AgentPal directly calls the Skill.

## Failure Behavior

- Treats a browser profile as a fixed route.
- Assumes installed capability without current Runtime evidence.
- Lets Runtime Skill output bypass Pal verification.
- Adds code, scanners, validators, CLI, installers, daemons, services, or UI.

## Pass / Fail

Pass when the output is a no-code Runtime Skill-aware package with availability, fallback, verification, usage-memory, and no fixed route.
