# Project Memory Rules

Project memory belongs to the central AgentPal project record for that external project.

Read current project facts from `active_project_root` when needed. Write structured summaries, decisions, task ledgers, source maps, derived knowledge, reports, and governance records to `agentpal_project_record` under the AgentPal workspace.

Do not create project-local `.agentpal/memory`, `.agentpal/context`, `.agentpal/reports`, or `.agentpal/state` folders by default. Do not write external project private memory into the public AgentPal repository.

