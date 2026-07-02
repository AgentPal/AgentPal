# Create AI Team Request Runbook

## Trigger

The user asks to create an AI team, workgroup, set of Pals, or collaboration plan.

## Inputs

- User's team goal.
- Desired roles and boundaries.
- Existing contacts / registry.
- Project binding if present.
- Runtime capability limits.

## v0.6 Entry Rule

Mira handles the intake and must run Team Pack first discovery before deciding whether PalSmith should own a durable asset plan. If an existing Team Pack fits, Mira selects and reuses it, records missing seats as `open_roles`, and does not send PalSmith to redesign the team. If no fitting Team Pack exists, or the user explicitly asks for a new durable team / governance change, PalSmith should own the creation or governance plan.

If the request is about discovering or restructuring a business process before
the team exists, Mira may consult Faye for FDE workflow framing. Once the
business team and workflow are established, routine business execution should be
assigned to the Team Pack and selected member Pals, not to Faye by default.

## Steps

1. Explain that AgentPal is a Pal layer and protocol workspace, not an
   automatic multi-agent runtime.
2. Identify required team purpose, stable task family, deliverables, privacy
   boundary, and success criteria.
3. Check whether an existing Team Pack already fits the user's request before any PalSmith handoff. Inspect `TEAM.md`, `team.json`, `roster.json`, routing card, workflow, and eval summaries when available.
4. Check whether existing Pals can fill the team roles through contacts /
   registry and Pal boundary judgement.
5. If no fitting Team Pack exists, or if new / modified Pal or Team assets are genuinely needed, consult or hand off to PalSmith and include the discovery result.
6. Require PalSmith to use the v0.6 naming rule: Pal display names are human
   names and role titles are stored separately.
7. Prepare a staged Runtime Task Package only after the user confirms durable
   writes.
8. Report the team plan without claiming active background orchestration,
   automatic parallel execution, or runtime-level dispatch.

## Decision points

- Is the user asking for Pal assets or runtime agents?
- Is the request to use an existing team or create a new one?
- Is Faye needed only for business workflow discovery / design?
- Are new Pals necessary?
- Would any proposed Pal name be only a role title?
- Is project binding required?
- Is any execution capability unavailable in current runtime?

## Outputs

Team role plan, Pal asset task package, owner judgement, and boundary report.

## Quality checks

- No active parallel agent execution is claimed.
- New Pal work goes through PalSmith.
- New Team Pack work goes through PalSmith.
- PalSmith uses the naming and same-name conflict protocol.
- Existing Pal boundaries are respected.
- Runtime limitations are explicit.

## Required user confirmation

Required before creating durable Pal assets, updating contacts / registry, or binding an external project.

## Evidence to return

Return contacts / registry consulted, proposed Pal assets, files changed, and checks not run.
