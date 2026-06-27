# Central Asset Boundary

Central organization assets belong in the AgentPal workspace, not in each external user project.

Central assets include:

- official and user-added Pal Packs
- contacts and Pal cards
- capability cards and organization policy
- shared knowledge, Skills, workflows, and task package templates
- project records, derived knowledge, governance notes, task records, reports, and memory
- release and audit material

External projects may contain their own source files and a thin `.agentpal/` binding. They should not receive central Pal assets by default.

When a host runtime needs to answer about the current project, it should read the active external project. When it needs Pal identity, routing, or governance context, it may read bounded AgentPal workspace assets through the binding.
