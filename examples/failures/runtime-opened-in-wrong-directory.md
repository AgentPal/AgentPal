# Failure Example: Runtime Opened In Wrong Directory

## Wrong Scenario

The user intends to connect AgentPal to an external project, but the runtime is opened from a parent folder, a downloads folder, or the AgentPal Workspace itself.

## Consequence

The binding may be created in the wrong place. Later prompts may read the wrong source tree, and "this project" may no longer mean the user's real project.

## Correct Check

- Report the current directory before writing.
- Compare it with `.agentpal/project.json` `active_project_root` when present.
- Check whether the current directory contains AgentPal root files such as `agentpal.json` and `contacts/pals.json`.

## Correct Fix

Stop and ask the user to restart the runtime from the intended project directory, or provide the exact external project path if the runtime supports project selection.

## Wrong Fixes

- Copy the full AgentPal directory into the current folder.
- Bind AgentPal to the AgentPal Workspace when the user meant an external project.
- Guess the intended project by scanning unrelated folders.
