# AgentPal Codex Install

This document is the no-code installation runbook for installing AgentPal into
Codex as a global Codex plugin from the public AgentPal GitHub repository.

Users do not need to copy the implementation steps below one by one. In Codex,
they can say:

```text
Please execute the AgentPal Codex install document:
https://github.com/AgentPal/AgentPal/blob/master/plugins/codex/codex-install.md
```

After this install completes, users can open any Codex project and say:

```text
Add AgentPal to this project
```

Codex should then use the installed `agentpal@agentpal` plugin to create the
project-level thin binding.

Users can also remove AgentPal from any connected project by saying:

```text
Remove AgentPal from this project
```

This removes only the project-level binding. It does not uninstall the global
Codex plugin.

## Global Plugin Model

AgentPal for Codex has two layers:

- Global host plugin: installed once into Codex as `agentpal@agentpal`.
- Project thin binding: added or removed separately in whichever project is
  currently open.

The global plugin must be available from any Codex project after installation.
Users should not need to pass the AgentPal workspace path when adding or
removing AgentPal from a project.

## Execution Contract For Codex

When asked to execute this document, Codex should perform the install steps
below as the execution layer.

Rules:

- Install only from the public AgentPal repository.
- Do not copy private files, tests, local materials, reports, evals, workspace
  state, tokens, or developer-only notes into the user's project.
- Do not write anything into a user project during this host-level install.
- Install the Codex plugin globally for the current Codex user, not inside a
  project repository.
- Ask the user to choose the AgentPal workspace directory with a simple
  numbered choice:
  `1` means use the default path, and `2` means enter a custom path.
- If the user chooses `1` or presses Enter, use the default path.
- If the user chooses `2`, ask for the custom AgentPal workspace path.
- Always write the install pointer to `%USERPROFILE%\.agentpal\config.json`.
  This lets the plugin remember the workspace location across Codex restarts.

## Default Layout

Default install config:

```text
%USERPROFILE%\.agentpal\config.json
```

Default full public AgentPal workspace:

```text
%USERPROFILE%\.agentpal\workspace
```

The workspace path may be customized, but the config file path stays fixed.

## Install Steps

1. Confirm `git` and `codex` are available.
2. Ask the user to choose the AgentPal workspace path:
   `1` for `%USERPROFILE%\.agentpal\workspace`, or `2` for a custom path.
3. Clone or update the public AgentPal repository at that workspace path.
4. Write `%USERPROFILE%\.agentpal\config.json` with the selected workspace path.
5. Register the Codex marketplace package from GitHub.
6. Install the Codex plugin.
7. Verify that `agentpal@agentpal` is available.
8. Print the post-install usage message from this document.

## PowerShell Reference

Codex may run this reference implementation on Windows PowerShell.

```powershell
$agentpalConfigRoot = Join-Path $env:USERPROFILE ".agentpal"
$defaultAgentPalWorkspace = Join-Path $agentpalConfigRoot "workspace"
$agentpalRepo = "https://github.com/AgentPal/AgentPal.git"

Write-Host ""
Write-Host "Choose AgentPal workspace install directory:"
Write-Host "1. Use default: $defaultAgentPalWorkspace"
Write-Host "2. Enter custom path"
$agentpalInstallChoice = Read-Host "Select 1 or 2 [1]"

if ([string]::IsNullOrWhiteSpace($agentpalInstallChoice) -or $agentpalInstallChoice -eq "1") {
  $agentpalWorkspace = $defaultAgentPalWorkspace
} elseif ($agentpalInstallChoice -eq "2") {
  $agentpalWorkspace = Read-Host "Enter AgentPal workspace path"
  if ([string]::IsNullOrWhiteSpace($agentpalWorkspace)) {
    throw "Custom AgentPal workspace path cannot be empty."
  }
  $agentpalWorkspace = [Environment]::ExpandEnvironmentVariables($agentpalWorkspace)
} else {
  throw "Invalid selection. Please rerun the install and choose 1 or 2."
}

New-Item -ItemType Directory -Force $agentpalConfigRoot | Out-Null

if (Test-Path (Join-Path $agentpalWorkspace ".git")) {
  git -C $agentpalWorkspace pull --ff-only
} elseif (Test-Path $agentpalWorkspace) {
  throw "AgentPal workspace path already exists and is not a Git checkout: $agentpalWorkspace"
} else {
  git clone $agentpalRepo $agentpalWorkspace
}

[ordered]@{
  schema_version = "agentpal.install_config.v1"
  workspace_root = $agentpalWorkspace
  installed_by = "codex"
  source = $agentpalRepo
  installed_at = (Get-Date).ToUniversalTime().ToString("o")
} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $agentpalConfigRoot "config.json")

codex plugin marketplace add AgentPal/AgentPal --ref main --sparse plugins/codex
codex plugin add agentpal@agentpal
codex plugin list --available --json

Write-Host ""
Write-Host "AgentPal for Codex is installed."
Write-Host ""
Write-Host "After installation, open any Codex project and say:"
Write-Host ""
Write-Host "Add AgentPal to this project"
Write-Host ""
Write-Host "To remove AgentPal from the current project while keeping the global Codex plugin installed, say:"
Write-Host ""
Write-Host "Remove AgentPal from this project"
Write-Host ""
Write-Host "The project binding is thin. It writes only .agentpal/project.json, .agentpal/AGENTPAL.md, and the AgentPal protected block in AGENTS.md."
```

## Post-Install Message

After installation, print this message for the user:

```text
After installation, open any Codex project and say:

Add AgentPal to this project

To remove AgentPal from the current project while keeping the global Codex plugin installed, say:

Remove AgentPal from this project

The project binding is thin. It writes only .agentpal/project.json, .agentpal/AGENTPAL.md, and the AgentPal protected block in AGENTS.md.
```

## Upgrade

```powershell
git -C (Join-Path $env:USERPROFILE ".agentpal\workspace") pull --ff-only
codex plugin marketplace upgrade
codex plugin add agentpal@agentpal
```

## Host-Level Uninstall

Remove the Codex plugin:

```powershell
codex plugin remove agentpal@agentpal
```

Remove the marketplace source:

```powershell
codex plugin marketplace remove agentpal
```

Optional full local cleanup:

```powershell
Remove-Item -Recurse -Force (Join-Path $env:USERPROFILE ".agentpal")
```

Project-level removal is separate. In any connected project, ask Codex:

```text
Remove AgentPal from this project
```

The plugin must remove only the project-level thin binding.

## Expected Result

After host-level install, the global Codex plugin `agentpal@agentpal` is
installed for the current Codex user and can be used from any Codex project.

After project-level enable, the current project may contain only:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the AgentPal protected block in `AGENTS.md`

The plugin must not copy the full AgentPal workspace into the project.
