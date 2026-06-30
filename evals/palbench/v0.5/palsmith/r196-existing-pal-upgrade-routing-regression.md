# R196 Existing Pal Upgrade Routing Regression

## Current Bug

PalSmith already supports composite Pal creation, but a request to change an
existing Pal's behavior can be mistaken for a narrow file edit. For example, a
request to give Luma a character-inspired voice and public product-design
thinking could lead directly to editing `persona.md` or `PAL.md`.

That is wrong because the request semantically affects Pal-defining assets:
identity, voice, personality, thinking model, role installation, knowledge,
workflow, Skill / Agent usage, evals, and source boundary.

## Fixed Rule

PalSmith must use AI judgement, not keyword routing. The presence of words such
as voice, thinking, Skill, contacts, or Marketplace is not a deterministic
trigger. The current Brain / Pal must inspect the target Pal, user intent,
write impact, source boundary, and risk before selecting a route.

If the request targets an existing Pal and materially affects Pal-defining
behavior, classify it as:

```text
Existing Pal Composite Distillation Upgrade
```

PalSmith must produce an upgrade plan before any write.

## Classification Matrix

| Semantic mode | Use when AI judgement finds | Required first output |
| --- | --- | --- |
| Simple Existing Pal Edit | typo, path, heading, JSON syntax, or stale one-line text with no behavior impact | narrow scope and minimal edit plan |
| Existing Pal Composite Distillation Upgrade | existing Pal behavior, voice, thinking, role, knowledge, workflow, Skill / Agent, memory, collaboration, or publication boundary may change | upgrade plan and confirmation |
| Role / Duty Upgrade | responsibilities, non-responsibilities, outputs, or acceptance criteria change | role impact plan |
| Knowledge / Capability Upgrade | knowledge, Pal-owned Skill, host Skill, plugin, MCP, software, Agent, or runtime policy changes | capability map and evidence boundary |
| Workflow Upgrade | review, creation, delivery, QA, reporting, or runbook behavior changes | workflow impact and workflow eval |
| Memory / Learning Upgrade | memory, retrospective, learning, or private writeback behavior changes | privacy and memory boundary |
| Collaboration / Discovery / Marketplace Upgrade | discovery, delegation, contacts, official status, Marketplace, or publication changes | authorization/governance plan |

The matrix is not a keyword route table. It is a review checklist after semantic
judgement.

## Pass Conditions

- PalSmith states an AI judgement reason.
- PalSmith distinguishes simple edits from high-impact upgrades.
- High-impact existing Pal upgrades produce a plan before writes.
- Target file map and eval plan are included.
- Central contacts, discovery, official status, and Marketplace publication are
  not changed without separate authorization.
- No runtime, backend, scanner, connector, daemon, or Marketplace service is
  introduced.

## Fail Conditions

- Directly edits `PAL.md`, `persona.md`, voice, knowledge, workflow, or runtime
  policy before an upgrade plan.
- Uses deterministic keyword routing.
- Claims source-person replication or character impersonation.
- Copies protected source text.
- Writes contacts, registry, discovery, Marketplace, or official status without
  separate confirmation.
