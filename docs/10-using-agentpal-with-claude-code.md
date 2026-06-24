# Using AgentPal With Claude Code

AgentPal works best in Claude Code when you start from your real project directory.

## Recommended Workflow

```text
cd <your-project>
claude
```

Then paste the full prompt from:

```text
prompts/claude-code/install-agentpal-current-project.md
```

The install prompt is copy-paste ready. Do not edit it before pasting. Claude Code asks for the local AgentPal Workspace path during installation unless you already provided a clear path in the conversation. Enter the path to your AgentPal directory, for example `<path-to-AgentPal>`.

## What The Prompt Does

The one-prompt install creates or updates:

- `.agentpal/`
- `CLAUDE.md`
- `AGENTS.md`
- `.claude/settings.local.json`

It writes `permissions.additionalDirectories` into `.claude/settings.local.json` so Claude Code can access the AgentPal workspace path.

After a successful install, the prompt should also print a short Mira welcome message that starts with `Mira：`. That welcome introduces Mira as the user's Pal team leader, says the user can tell Mira anything directly, explains `/pal Name`, shows the current Pal team in a table with name, responsibility, and skill overview, and reminds the user that v0.1 uses Simple Pal Mode only.

## Local Settings Boundary

`.claude/settings.local.json` is local machine configuration and should not be committed.

The install prompt preserves existing Claude Code settings and merges only:

```json
{
  "permissions": {
    "additionalDirectories": [
      "<path-to-AgentPal>"
    ]
  }
}
```

Do not put the local AgentPal absolute path in `.claude/settings.json`.

## CLAUDE.md Boundary

`CLAUDE.md` is the Claude Code project instruction entry. AgentPal inserts or updates only this protected block:

```text
<!-- BEGIN AGENTPAL WORKGROUP -->
...
<!-- END AGENTPAL WORKGROUP -->
```

Existing project instructions outside that block are preserved.

The block is lightweight. It points to the AgentPal workspace and tells Claude Code to use contacts / registry and selected Pal assets on demand. It does not import the whole AgentPal workspace.

## If Access Does Not Take Effect Immediately

If the current Claude Code session cannot read the AgentPal path after `.claude/settings.local.json` is updated:

- restart Claude Code in the project
- or temporarily run `/add-dir <path-to-AgentPal>`
- or restart with `claude --add-dir <path-to-AgentPal>`

These are fallback / advanced options, not the default setup path.

## Runtime Boundary

AgentPal v0.1.0-rc.1 uses Simple Pal Mode only.

AgentPal is a Pal layer, not an Agent runtime, not a multi-agent runtime, and not an execution layer.

Do not activate Subagent Mode or external Agent orchestration from this binding.

Deep Conductor is future design material. It is not automatically executed by the Claude Code binding in v0.1.0-rc.1.

## Context Boundary

Do not paste AgentPal `AGENTS.md`, `README.md`, or the whole AgentPal workspace into `CLAUDE.md`.

Use:

- `.agentpal/project.json` for binding metadata
- `CLAUDE.md` for lightweight Claude Code instructions
- `AGENTS.md` for cross-runtime instructions
- `contacts/pals.json` and `registry/pal.index.json` for Pal discovery
- `RESOURCE_INDEX.md` and selected Pal assets on demand

Project questions mean `<your-project>`, not the AgentPal workspace.
