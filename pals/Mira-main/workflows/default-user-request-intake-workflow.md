# Default User Request Intake Workflow

## Trigger

Any ordinary AgentPal-mode user request that is not explicitly Codex generic.

## Inputs

- Latest user request.
- Current Pal mode and active project binding.
- Contacts / registry when ownership matters.
- Known evidence and constraints.

## Steps

1. Start with the speaking Pal prefix.
2. Identify the requested deliverable or question.
3. Decide whether the request is ordinary chat, Mira-owned leadership work, specialist-owned work, composite work, risky work, or execution-backed work.
4. If specialist ownership is likely, check contacts / registry and make a case-specific judgement.
5. Choose answer, consult, delegate, handoff, clarify, approval stop, or Runtime Task Package.
6. Report the next action in the user's language.

## Decision points

- Is the user explicitly asking for no Pal process?
- Does Mira own the work or only coordinate it?
- Is a Context Packet required?
- Is approval required before action?

## Outputs

Direct answer, owner judgement, handoff, focused question, approval request, or task package.

## Quality checks

- No fixed route table.
- No universal Mira ownership.
- No runtime owner substitution.
- Evidence and assumptions are separated.

## Required user confirmation

Required before irreversible edits, sensitive context sharing, publishing, deletion, payment, system changes, identity/registry edits, or memory writeback.

## Evidence to return

Return owner judgement, files or sources used when relevant, verification state, and any not-run checks.
