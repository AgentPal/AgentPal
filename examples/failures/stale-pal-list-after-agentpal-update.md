# Failure Example: Stale Pal List After AgentPal Update

## Wrong Scenario

An external project keeps showing an old Pal list after the AgentPal Workspace contacts or registry changed.

## Consequence

Direct Pal calls may fail, new Pals may be invisible, and old names may appear even though the AgentPal Workspace has moved on.

## Correct Check

- Confirm the project binding points to the intended AgentPal Workspace.
- Read `contacts/pals.json` and `registry/pal.index.json` from that workspace.
- Inspect root instruction blocks and `.agentpal/` for copied roster text.

## Correct Fix

Replace copied roster text with a thin pointer to contacts and registry. Restart or reload the host runtime if it keeps old instructions in memory.

## Wrong Fixes

- Edit a project-local roster as if it were authoritative.
- Copy the full current Pal list into every external project.
- Modify Pal Pack files inside the external project.
