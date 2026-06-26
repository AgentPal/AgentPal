# Failure Example: Active Project Root Confused With AgentPal Root

## Wrong Scenario

A bound external project stores the AgentPal Workspace path as `active_project_root`, or the runtime treats both roots as project source.

## Consequence

User requests about "this project" may inspect AgentPal docs and Pal assets instead of the user's real project. Reports may mix product files with framework files.

## Correct Check

- Read `.agentpal/project.json`.
- Confirm `active_project_root` points to the external user project.
- Confirm `agentpal_workspace_root` points to the AgentPal Workspace.
- Confirm routine project inspection uses only `active_project_root`.

## Correct Fix

Correct the binding roots and rerun verification. If the current session already loaded the wrong root, restart or reload project instructions.

## Wrong Fixes

- Treat AgentPal as a second active project.
- Scan both roots for ordinary source questions.
- Copy AgentPal root files into the external project to make the paths match.
