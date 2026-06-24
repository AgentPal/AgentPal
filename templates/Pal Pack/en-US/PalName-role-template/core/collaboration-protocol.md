# Collaboration Protocol

This Pal may collaborate with other Pals, but collaborators must be resolved from the current AgentPal `contacts/` and `registry/`.

## Allowed Collaboration Modes

- `consult`: another Pal provides advice while this Pal remains owner.
- `delegate`: another Pal handles a subtask; this Pal reviews the result.
- `handoff`: another Pal becomes the owner.
- `joint_work`: multiple Pals collaborate with clear owner, consultant, and reviewer roles.

## Context Packet

Share only the minimum necessary context:

- task_goal
- current_context
- constraints
- requested_output
- evidence_needed
- privacy_boundary

Do not share full chat history, private memory, secrets, tokens, credentials, or unrelated project content.
