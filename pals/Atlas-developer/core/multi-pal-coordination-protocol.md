# Multi Pal Coordination Protocol

This protocol describes Pal coordination, not multi-agent runtime orchestration.

Current AgentPal v0.1 behavior:

1. Use AI judgement case by case.
2. Resolve Pals from contacts / registry.
3. Keep owner, consultant, and reviewer roles explicit when more than one Pal is useful.
4. Use the minimum Context Packet needed for the task.
5. Do not treat tools, models, plugins, MCP servers, websites, skills, or external runtimes as Pal contacts.
6. Execution belongs to the current runtime or a user-approved external runtime, not to the Pal layer itself.
7. Any execution result needs evidence before a Pal summarizes or reviews it.

## Degraded Runtime Behavior

`@Pal` and `/pal Name` are AgentPal protocol conventions. If the current runtime does not support multi-Pal interaction natively, the active Pal prepares a concise Context Packet or same-response handoff that the runtime can follow.