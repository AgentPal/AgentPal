# AgentPal Codex Marketplace

This directory is the Codex marketplace package for AgentPal.

It is installed through the public no-code install runbook:

```text
https://github.com/AgentPal/AgentPal/blob/master/plugins/codex/codex-install.md
```

Users can ask Codex to execute that document. The document prepares a local
AgentPal workspace, writes a persistent install config, registers the Codex
marketplace, and installs the Codex plugin.

## Global Plugin Model

AgentPal for Codex is installed once as the global Codex plugin
`agentpal@agentpal` for the current Codex user. After that, it can add or remove
AgentPal from any Codex project the user opens.

The global plugin is not copied into each project. Each project receives only a
thin binding when the user asks for AgentPal.

After installation, open a project in Codex and ask:

```text
Add AgentPal to this project
```

To remove AgentPal from the current project, ask:

```text
Remove AgentPal from this project
```

The installed plugin creates only a thin project binding:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the Codex AgentPal protected block in `AGENTS.md`

It does not copy full Pal assets, memory, reports, evals, workspace records,
internal docs, services, daemons, scanners, databases, or background runtimes
into the user project.

This package is no-code. It contains Codex plugin metadata and Skills only.
Codex remains the execution layer for host-level installation and project-local
file edits.

The persistent install config is written to:

```text
%USERPROFILE%\.agentpal\config.json
```

By default, the full public AgentPal workspace is downloaded to:

```text
%USERPROFILE%\.agentpal\workspace
```

The install document downloads the public AgentPal workspace, then registers the
local marketplace package from the downloaded workspace:

```powershell
$agentpalMarketplaceRoot = Join-Path $agentpalWorkspace "plugins\codex"
codex plugin marketplace add $agentpalMarketplaceRoot
codex plugin add agentpal@agentpal
```

Upgrade an installed marketplace snapshot with:

```powershell
codex plugin marketplace upgrade
codex plugin add agentpal@agentpal
```

Remove the installed Codex plugin with:

```powershell
codex plugin remove agentpal@agentpal
```

Remove the configured AgentPal marketplace source with:

```powershell
codex plugin marketplace remove agentpal
```

Project-level removal is separate. In any project that has already been
connected to AgentPal, ask Codex to disable or remove AgentPal in that project;
the plugin should remove only the project-local thin binding.

To remove the downloaded AgentPal workspace and install config, delete the
chosen AgentPal install directory, for example:

```powershell
Remove-Item -Recurse -Force (Join-Path $env:USERPROFILE ".agentpal")
```

The legacy development plugin under `agentpal-codex-plugin/` is kept for
compatibility. The public install entry is `plugins/agentpal`.
