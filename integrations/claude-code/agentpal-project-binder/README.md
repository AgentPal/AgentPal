# AgentPal Claude Code Project Binder

This is the first thin-binding Claude Code entry for AgentPal.

It is intentionally small:

- no background service
- no account system
- no sync system
- no database
- no GUI manager
- no MCP requirement

It only helps Claude Code create, inspect, repair, and remove the current project's thin AgentPal binding.

## Shortest User Path

1. Install or load this Claude Code plugin.
2. Open any project in Claude Code.
3. Run `/agentpal:enable`.
4. Use `/agentpal:status` to inspect the current project binding.
5. Use `/agentpal:repair` if the binding is missing or damaged.
6. Use `/agentpal:disable` when you want to remove the current project's Claude Code binding.
7. Use `/pal Name` when you want to call a specialist Pal directly after the project is bound.

After the binding is created, ordinary requests go to Mira by default.

Natural-language requests may work in interactive sessions, but slash commands are the primary tested path for this plugin.

Installing or loading the plugin is separate from enabling AgentPal in the current project. Removing the current project's binding does not uninstall the plugin itself.

## Commands

This plugin provides the following Claude Code commands:

- `/agentpal:enable`
- `/agentpal:init`
- `/agentpal:status`
- `/agentpal:repair`
- `/agentpal:disable`

## What It Touches

`enable`, `init`, and `repair` are limited to:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the runtime-qualified AgentPal block in root `CLAUDE.md`

`disable` is limited to:

- deleting `.agentpal/` only when no other runtime binding remains
- removing the AgentPal protected block from root `CLAUDE.md`

It does not:

- copy full Pal assets into the project
- modify the central AgentPal workspace
- create `AGENTS.md`
- create `.claude/settings.local.json`
- edit other project files by default
- start background services, daemons, databases, accounts, sync, MCP, or GUI flows

## Protected Block Markers

This binder writes the Claude block with:

```html
<!-- BEGIN AGENTPAL BINDING: claude-code -->
<!-- END AGENTPAL BINDING: claude-code -->
```

## AgentPal Source Resolution

`/agentpal:enable` and `/agentpal:init` resolve the AgentPal source in this order:

1. an explicit path or URL provided in the command arguments or user message
2. an already-accessible local AgentPal workspace that contains `agentpal.json`
3. one short follow-up question asking the user for the local AgentPal workspace path or GitHub source URL

## Helper

The slash-command entry is backed by a deterministic local helper:

```text
python scripts/agentpal_binding.py <enable|status|repair|disable> --project-root <current-project-root>
```

Examples:

```text
python scripts/agentpal_binding.py enable --project-root /path/to/project --agentpal-source /path/to/AgentPal
python scripts/agentpal_binding.py status --project-root /path/to/project
python scripts/agentpal_binding.py repair --project-root /path/to/project --agentpal-source /path/to/AgentPal
python scripts/agentpal_binding.py disable --project-root /path/to/project
```

This lets us verify the file protocol locally even when a real Claude Code plugin session is not running.

## `/pal Name` In This Version

This binder does not hard-code semantic routing.

`/pal Name` remains a semantic protocol, not a fixed route table:

- the model reads the current binding
- if the central AgentPal workspace is accessible, it reads the current Pal registry from that source
- then it chooses the owner Pal by AI judgement only

The binder must not hard-code rules like:

- development = Atlas
- testing = Quinn
- product = Nova

## Usage

### Install Or Load During Development

For local testing during plugin development:

```text
claude --plugin-dir /absolute/path/to/AgentPal/integrations/claude-code/agentpal-project-binder
```

In local host validation with Claude Code `2.1.150`, this load path exposed:

- `/agentpal:enable`
- `/agentpal:init`
- `/agentpal:status`
- `/agentpal:repair`
- `/agentpal:disable`

### Enable

Command:

```text
/agentpal:enable
```

Optional explicit source:

```text
/agentpal:enable /absolute/path/to/AgentPal
/agentpal:enable https://github.com/example/AgentPal
```

Natural-language requests may also trigger the same binder flow in interactive sessions, but slash commands are the primary tested path. Examples:

- `启用 AgentPal`
- `把当前项目接入 AgentPal`
- `Enable AgentPal for this project`

### Init

Command:

```text
/agentpal:init
```

`init` is an alias for the same thin-binding flow as `enable`.

### Status

Command:

```text
/agentpal:status
```

The binder should classify the current project as one of:

- `unbound`
- `complete`
- `partial`
- `damaged`
- `legacy-block`

### Repair

Command:

```text
/agentpal:repair
```

`repair` recreates missing thin-binding files, replaces a missing or legacy Claude block, and fixes malformed v1 fields when enough information is recoverable.

### Disable

Command:

```text
/agentpal:disable
```

This removes only the current project's thin binding. It must not delete the central AgentPal workspace or touch other project content.

If Codex is still enabled in the same project, `disable` removes only the Claude block and updates `.agentpal/project.json` instead of deleting `.agentpal/`.

## Disable vs Uninstall

- `/agentpal:disable` removes only the Claude Code binding from the current project.
- It does not uninstall the Claude Code plugin itself.
- If another runtime binding still depends on `.agentpal/`, the shared binding metadata may remain in place.

## Acceptance Focus

The companion acceptance checklist is in [evals/acceptance-checklist.md](./evals/acceptance-checklist.md).

## Developer Notes

This v1 uses a plugin plus skills only.

Reason:

- the required behavior is current-project file binding, not background automation
- hooks would add lifecycle complexity without being necessary for the first deliverable
- custom agents/subagents are not required to create or remove a thin binding
- the binder should stay explainable, local, and easy to audit
