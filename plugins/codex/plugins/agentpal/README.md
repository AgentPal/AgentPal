# AgentPal for Codex

AgentPal for Codex is the public Codex plugin entry for AgentPal.

It is a global Codex plugin. Install it once as `agentpal@agentpal`, then use it
from any Codex project to add, check, repair, or remove the project-level
AgentPal binding.

Install from the AgentPal GitHub install document:

```text
https://github.com/AgentPal/AgentPal/blob/master/plugins/codex/codex-install.md
```

Users can ask Codex to execute that document. It prepares the local AgentPal
workspace and writes the install config that this plugin later reads when
adding AgentPal to a project.

Then open any Codex project and ask Codex to add AgentPal to the project. No
project path or AgentPal path should be needed.

To remove AgentPal from that project later, ask Codex to remove AgentPal from
the project. This removes only the project binding and keeps the global plugin
installed for other projects.

This plugin writes only the project-level thin binding:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- `AGENTS.md` Codex protected block

It does not copy full AgentPal workspace assets into the project.
It ships no runtime helper code; Codex performs the requested file edits as the
execution layer after reading the Skill instructions.

The plugin should read the install config from:

```text
%USERPROFILE%\.agentpal\config.json
```

The default full AgentPal workspace path is:

```text
%USERPROFILE%\.agentpal\workspace
```

Remove the installed Codex plugin with:

```powershell
codex plugin remove agentpal@agentpal
```

Remove the configured AgentPal marketplace source with:

```powershell
codex plugin marketplace remove agentpal
```

Project-level removal is separate: in the connected project, ask Codex to
disable AgentPal in this project.

To remove the downloaded AgentPal workspace and install config, delete the
chosen AgentPal install directory, for example:

```powershell
Remove-Item -Recurse -Force (Join-Path $env:USERPROFILE ".agentpal")
```

## Skills

- `agentpal`: explain the installed plugin and route to binding operations
- `agentpal-enable`: add AgentPal to the current Codex project
- `agentpal-status`: inspect the current project's binding
- `agentpal-repair`: repair a partial binding
- `agentpal-disable`: remove the Codex binding from the current project
