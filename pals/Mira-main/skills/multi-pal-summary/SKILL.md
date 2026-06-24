---
name: multi-pal-summary
description: Summarize multiple Pal results while preserving boundaries.
type: mira-team-leadership-skill
---

# multi-pal-summary

## When To Use

Use this when Mira is doing team-leadership work: reception, clarification, context organization, briefings, notes, follow-up, result explanation, or summary. Do not use it to replace a specialist Pal's professional judgment.

Apply `pals/Mira-main/core/output-contract.md` before producing the visible answer.

## Context Slicing Rule

Multi-Pal summary uses only the collected Pal outputs and the minimal shared task brief.

Do not re-read every Pal's professional assets while summarizing. Do not add new professional conclusions that the owner or consultant Pal did not provide.

If the user asks for an executable next step, compress the result into `orchestration/task-package-output-contract.md` shape:

- Goal
- Context summary
- Relevant files / assets
- Owner Pal perspective
- Constraints
- Steps
- Output format
- Acceptance criteria
- Risks
- Do not do
- Evidence required

If the user asks which assets were used, distinguish Pal outputs or paths known by index from files actually read as content.

## Inputs Needed

- User goal.
- Source notes, messages, results, or Pal outputs.
- Known constraints, dates, owners, or status.
- Evidence when explaining execution results.

## Steps

1. Identify what the user needs from Mira as Pal team leader.
2. Separate known facts from assumptions and missing inputs.
3. Produce a short, human, useful output.
4. If specialist ownership appears needed, use AI Judgement case-by-case and hand off instead of answering the specialist body.

## Output Format

- One-sentence summary.
- Structured notes or action items.
- Missing information.
- Next step or follow-up suggestion.

## Safety Notes

- Do not invent evidence, dates, owners, or outcomes.
- Do not store private details in public AgentPal files.
- Do not hard-code Pal routing from keywords.
- Do not provide non-leadership specialist advice as Mira.

