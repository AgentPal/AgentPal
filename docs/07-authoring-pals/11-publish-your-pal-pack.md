# Publish Your Pal Pack

## Status

Current for AgentPal `v0.1.0-rc.1`.

Publishing means making a Pal Pack safe and discoverable. It does not mean a Pal marketplace is live.

## Before Registration

Complete the [Pal Pack checklist](../03-pal-pack-standard/12-pal-pack-checklist.md).

At minimum, verify:

- required files exist
- `pal.json` uses `type: pal-pack`
- `core/output-contract.md` exists
- placeholder indexes and README files exist
- memory, state, and reports are public-safe
- examples and evals use synthetic data

## Add To Central Roster

Only after the directory is a valid Pal Pack, update:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `workspace/organization/contacts/aliases.json`, when aliases change

These central roster files are the source of truth for Pal discovery.

For normal users, the recommended path is to run [`../../prompts/add-pal-to-agentpal.md`](../../prompts/add-pal-to-agentpal.md) from the AgentPal Workspace after copying the completed Pal Pack into `official/pals/<Name-role>/`.

### Where To Run The Registration Prompt

Run the registration prompt in the AgentPal Workspace, not in the external project where you normally use AgentPal.

Codex:

1. Open the AgentPal directory as its own Codex project.
2. Copy the finished Pal Pack into `official/pals/<Name-role>/`.
3. Open [`../../prompts/add-pal-to-agentpal.md`](../../prompts/add-pal-to-agentpal.md).
4. Copy the prompt block.
5. Paste it into the AgentPal project conversation.
6. After registration succeeds, smoke-test with `/pal Name`.

Claude Code:

1. Open a terminal in the AgentPal Workspace:

   ```text
   cd <path-to-AgentPal>
   claude
   ```

2. Copy the finished Pal Pack into `official/pals/<Name-role>/`.
3. Paste the full [`../../prompts/add-pal-to-agentpal.md`](../../prompts/add-pal-to-agentpal.md) prompt into that Claude Code session.
4. Reinitialize any external project session if it still has the old Pal list.

Generic CLI Agent:

1. Open the CLI agent from the AgentPal Workspace:

   ```text
   cd <path-to-AgentPal>
   <your-cli-agent>
   ```

2. Copy the finished Pal Pack into `official/pals/<Name-role>/`.
3. Paste the full registration prompt into that session.
4. The agent should scan only `official/pals/`, validate the Pal Pack, and update `workspace/organization/contacts/`.

## Do Not Register

- ordinary Skills
- plugins
- models
- MCP servers
- runtimes
- raw repositories
- knowledge packs
- persona packs

## Final Smoke Check

Ask the runtime to call the Pal with `/pal Name` and verify the response uses the Pal identity, output contract, and an asset or fallback method.
