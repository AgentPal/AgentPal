# Project Memory In AgentPal

Project memory belongs in AgentPal's central project record, not in the external project's `.agentpal/` directory.

Default location:

`workspace/projects/<project-id>/memory/`

Project memory can record current goals, decisions, task ledgers, routing-memory evidence, runtime availability, and governance observations.

The external project may still contain user-authored docs, design files, requirements, assets, data, and source files. AgentPal can read those materials for a task, then store summaries and durable memory in the central record.

If a user explicitly asks AgentPal to create a business document inside the external project, that document can be written there. That exception does not make project-local `.agentpal/` an AgentPal internal memory store.

