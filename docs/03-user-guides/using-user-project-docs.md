# Using User Project Docs

User projects may contain their own docs, design notes, requirements, assets, data, and source files.

AgentPal may read those materials when a task requires project context. The external project remains the source of current facts.

AgentPal should write structured outputs to the central project record:

- source map: `workspace/projects/<project-id>/source-map/`
- derived knowledge: `workspace/projects/<project-id>/derived-knowledge/`
- project memory: `workspace/projects/<project-id>/memory/`
- task packages and reports: `workspace/projects/<project-id>/tasks/` and `workspace/projects/<project-id>/reports/`

If the user explicitly asks for a business-facing document inside the external project, create it in the requested project path. That is user project content, not AgentPal internal memory.

