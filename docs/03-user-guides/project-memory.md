# Project Memory

Use project memory when AgentPal needs durable context for an external user project.

Default location:

`workspace/projects/<project-id>/memory/`

Use it for:

- current project goal and status
- task ledger
- decisions
- routing-memory evidence
- runtime availability notes
- governance observations

Do not store this memory in the external project's `.agentpal/` directory. The external project should remain a thin-bound user project.

Do not store secrets, tokens, private credentials, or unnecessary personal data.

