# Project-First Connection

Project-first means the user's real project directory is the task context, while the AgentPal Workspace is only the Pal source and routing reference.

## Why This Matters

When AgentPal is connected to an external project, the runtime should not treat the AgentPal Workspace as the user's project. The current project root remains the only active project context for normal work.

## Claude Code Path

```text
cd <your-project>
claude
```

Then paste the prompt from `prompts/claude-code/install-agentpal-current-project.md`. Do not edit the prompt first; Claude Code asks for the AgentPal Workspace path during installation.

## Generic CLI Path

```text
cd <your-project>
<your-cli-agent>
```

Then paste the prompt from `prompts/generic-cli-agent/install-agentpal-current-project.md`. Do not edit the prompt first; the CLI agent asks for the AgentPal Workspace path during installation.

## What The Binding Should Preserve

- the current project directory is the active task root
- the AgentPal Workspace is only a Pal workspace reference
- Pal discovery comes from AgentPal `contacts/` and `registry/`
- `.agentpal/` stores project-local binding metadata
- the runtime should not preload the whole AgentPal Workspace into project context

## Current Boundary

- This is a lightweight workgroup connection.
- It is not a full runtime takeover.
- It is not an automatic installer beyond the current project.
- It does not activate Deep Conductor, Subagent Mode, or external Agent orchestration.

## Related

- [Use With Claude Code](02-use-with-claude-code.md)
- [Use With Generic CLI Agent](03-use-with-generic-cli-agent.md)
