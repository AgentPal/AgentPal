# Step 04: Thin-Bind A Fake Project

This step explains the shape only. It does not create a real external project.

Allowed project-local binding surface:

```text
.agentpal/project.json
.agentpal/AGENTPAL.md
AGENTS.md protected block
CLAUDE.md protected block
.claude/settings.local.json
.gitignore entry
```

Not created by default:

```text
.agentpal/pals/
.agentpal/memory/
.agentpal/reports/
.agentpal/org-pack/
.agentpal/fde-pack/
.agentpal/delivery-pack/
.agentpal/capability-inventory/
```

Expected result: the user understands that external projects point back to the
AgentPal Workspace and stay thin.
