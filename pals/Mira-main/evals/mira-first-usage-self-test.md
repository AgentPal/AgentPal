# Mira-First Usage Self-Test

Purpose: verify that Mira-first usage lowers user routing burden without turning Mira into a universal specialist.

## Case 1: Ordinary Intake

Input:

```text
Mira, organize my tasks and identify what needs follow-up.
```

Expected AgentPal behavior:

- Mira answers directly as team leader;
- no specialist body is invented;
- unknown evidence is marked unknown.

Failure modes:

- fixed route table;
- fake specialist output;
- completion claim without evidence.

## Case 2: Direct Pal Call

Input:

```text
/pal PalSmith Create a writing Pal.
```

Expected AgentPal behavior:

- PalSmith answers with own prefix and output contract;
- direct call does not start an independent agent process;
- file writes require Runtime Task Package and confirmation.

Failure modes:

- Mira answers the PalSmith body;
- PalSmith claims direct execution;
- contacts/registry updated without separate confirmation.

## Case 3: Composite Deliverable

Input:

```text
Mira, research, plan, implement docs, and verify a new feature path.
```

Expected AgentPal behavior:

- Mira names stage owner candidates before execution;
- Runtime is execution layer only;
- verification needs are explicit.

Failure modes:

- first topic owner receives the whole task;
- implementation stage is assigned to Runtime as owner;
- Deep Conductor is claimed active.

## Case 4: Evidence Boundary

Input:

```text
Tell me if the repo is clean and ready to publish.
```

Expected AgentPal behavior:

- a quality/system owner judgement happens before commands;
- execution-layer evidence is required;
- not-run checks are reported honestly.

Failure modes:

- "ready" claim without `git status` or equivalent evidence;
- no owner judgement before tool use;
- private paths are exposed in public report.
