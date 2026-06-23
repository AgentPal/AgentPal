<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Permission Boundary

Subagents are read-only by default unless the user and current task explicitly authorize modifications.

## Default Boundary

By default, a subagent may:

- read the required AgentPal Pal assets
- read task-relevant files inside the allowed workspace
- inspect JSON and Markdown metadata
- produce recommendations, risks, and next steps
- request execution-layer evidence when safe and relevant

By default, a subagent must not:

- modify project files
- modify system settings
- disable, delete, install, or uninstall software
- change startup items
- change services, scheduled tasks, registry keys, shell profiles, or permissions
- write private memory
- send external network requests
- use any external tool engine without explicit approval
- access unrelated projects or whole-disk locations

## Rhea System Tasks

Rhea subagents are read-only by default. For system or startup tasks, the prompt must say:

- read-only checks first
- no disabling startup items
- no service modification
- no registry modification
- no deletion
- no installation
- approval required before any risky operation

## External Tool Engines

External tool engines are not part of the default Pal set. A subagent must not run external tools unless the user explicitly asks and approves the execution boundary.

## Evidence

If a subagent asks the current Codex execution layer to inspect files or system state, it must report:

- what was inspected
- whether the action was read-only
- what evidence was returned
- what was not modified

Do not claim execution-layer evidence without actual evidence.

## Rhea Read-Only Evidence

Rhea may request read-only evidence from the current Codex execution layer for system tasks. The allowed shape is:

- read registry, startup folders, scheduled task metadata, services, process names, or event log metadata
- do not write registry
- do not disable startup items
- do not change service startup type
- do not delete shortcuts or scripts
- do not edit scheduled tasks
- do not install, uninstall, stop, or start services unless explicitly approved

Rhea must include a no-modification statement after any read-only inspection.


