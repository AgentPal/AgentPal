# Create AI Team Request Runbook

## Trigger

The user asks to create an AI team, workgroup, set of Pals, or collaboration plan.

## Inputs

- User's team goal.
- Desired roles and boundaries.
- Existing contacts / registry.
- Project binding if present.
- Runtime capability limits.

## Steps

1. Explain that AgentPal v0.1 is Pal layer and Simple Pal Mode only.
2. Identify required team roles and deliverables.
3. Check whether existing Pals already fit.
4. Use PalSmith governance for new or modified Pal assets.
5. Prepare a staged task package for asset changes if needed.
6. Report the team plan without claiming active multi-agent execution.

## Decision points

- Is the user asking for Pal assets or runtime agents?
- Are new Pals necessary?
- Is project binding required?
- Is any execution capability unavailable in current runtime?

## Outputs

Team role plan, Pal asset task package, owner judgement, and boundary report.

## Quality checks

- No active parallel agent execution is claimed.
- New Pal work goes through PalSmith.
- Existing Pal boundaries are respected.
- Runtime limitations are explicit.

## Required user confirmation

Required before creating durable Pal assets, updating contacts / registry, or binding an external project.

## Evidence to return

Return contacts / registry consulted, proposed Pal assets, files changed, and checks not run.
