# Add a Pal to AgentPal

Use this prompt after copying a new Pal Pack directory into `pals/`.

Copying a Pal Pack into `pals/` is not enough by itself. AgentPal resolves `/pal Name`, `@Name`, and Mira owner routing from `contacts/` and `registry/`, so the new Pal must be validated and registered there.

## Where To Run This Prompt

Run this prompt from the AgentPal Workspace, not from an external user project.

### Codex

Use this path when AgentPal is opened directly as its own Codex project.

1. In Codex, open the AgentPal project that points to your AgentPal directory.
2. Copy or create the finished Pal Pack under `pals/<Name-role>/`.
3. Open this file: `prompts/add-pal-to-agentpal.md`.
4. Copy the whole prompt block below.
5. Paste it into the AgentPal project conversation in Codex.
6. Let Codex inspect only `pals/`, validate the new Pal Pack, and update contacts / registry.
7. After it reports success, call the Pal with `/pal Name` to smoke-test registration.

### Claude Code

Use this path when you normally use AgentPal from another project, but need to register a Pal in the AgentPal Workspace.

1. Open a terminal in the AgentPal Workspace directory:

   ```text
   cd <path-to-AgentPal>
   claude
   ```

2. Copy or create the finished Pal Pack under `pals/<Name-role>/`.
3. Open this file: `prompts/add-pal-to-agentpal.md`.
4. Copy the whole prompt block below.
5. Paste it into the Claude Code session that is running inside the AgentPal Workspace.
6. Let Claude Code inspect only `pals/`, validate the new Pal Pack, and update contacts / registry.
7. Restart or reinitialize any external project session that uses AgentPal if it still shows the old Pal list.

### Generic CLI Agent

Use this path for another CLI agent that can read and edit files.

1. Open the CLI agent from the AgentPal Workspace directory:

   ```text
   cd <path-to-AgentPal>
   <your-cli-agent>
   ```

2. Copy or create the finished Pal Pack under `pals/<Name-role>/`.
3. Copy the whole prompt block below.
4. Paste it into the CLI agent session.
5. The agent should scan only `pals/`, validate the Pal Pack, and update contacts / registry.
6. Reinitialize the external project session if needed so it reloads the updated contacts / registry.

Do not run this prompt from a bound external project directory unless that runtime can also read and write the AgentPal Workspace path. If you are currently inside an external project, switch to the AgentPal Workspace first.

```text
Add newly copied Pal Pack directories to AgentPal.

Read AgentPal root rules:
- AGENTS.md
- SKILL.md
- PAL.md
- agentpal.json
- pals/README.md
- registry/README.md
- contacts/README.md

Scan only pals/. Do not scan the whole disk or external projects.

Keep the official baseline:
- Mira-main
- Atlas-developer
- Vega-research
- Rhea-system
- Quinn-quality
- Morgan-document
- Harper-writing
- Nova-product

For each new directory:
1. Check directory name follows Name-role.
2. Check PAL.md, SKILL.md, AGENTS.md, and pal.json exist.
3. Parse pal.json.
4. Check pal.json.type = pal-pack.
5. Check display_name, aliases, and direct_call.
6. Check discoverable, contactable, and collaboration permissions.
7. Add only valid Pal Packs to contacts and pal index.
8. Put invalid or uncertain candidates into contacts/discovered-candidates.md.

Update:
- registry/pal.index.md
- registry/pal.index.json
- contacts/PAL_CONTACTS.md
- contacts/pals.json
- contacts/mention-aliases.md

Do not modify the Pal's original content unless I explicitly ask you to repair that Pal Pack.
Do not add ordinary Skills, tools, models, MCP servers, plugins, non-Pal runtimes, raw repositories, knowledge packs, or persona packs to contacts.
```


