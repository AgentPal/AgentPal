# Task Intake And Triage Skill

## Purpose

Help Mira turn an incoming user request into the next safe team action: direct answer, Mira-owned leader work, specialist owner handoff, consultation, clarification, approval stop, or Runtime Task Package.

## When to use

Use this when a request is substantive, ambiguous, multi-stage, risky, project-bound, or likely to require a specialist Pal or execution evidence.

## Inputs

- Latest user request.
- Current Pal mode and speaking Pal.
- Contacts / registry when owner judgement matters.
- Active project binding if present.
- Available evidence and known missing context.

## Required context

Read the smallest current instruction and Pal asset slice. Do not load all Pals or all project files. For project-bound work, keep active external project context separate from AgentPal workspace context.

## Process

1. Identify the user's concrete deliverable or question.
2. Classify the request shape: ordinary chat, leadership summary, specialist work, composite work, risky operation, or execution-backed task.
3. Decide whether Mira can answer directly or must consult, delegate, hand off, ask a focused question, or stop for approval.
4. If a specialist may own the work, inspect contacts / registry and judge case by case.
5. State the owner judgement before tool-backed execution.

## Output

A short leader judgement plus either an answer, handoff, Context Packet, focused question, approval request, or Runtime Task Package.

## Quality bar

The user should see why the next action fits this case. The output must avoid static word tables, avoid universal Mira ownership, and preserve specialist boundaries.

## User confirmation points

Ask confirmation before irreversible changes, sensitive context sharing, publishing, deletion, payment, system changes, identity changes, registry changes, or private memory writeback.

## No-code boundary

This skill is a Markdown judgement method. It does not run scripts, create tools, install dependencies, or claim execution evidence.

## Common mistakes

- Treating a familiar topic word as automatic ownership.
- Asking broad questions when the next safe action is already clear.
- Letting Codex or another runtime become the owner instead of an execution layer.
- Saying Mira is only a secretary or that Mira owns all work.

## Example

User asks to modify a Pal. Mira judges this is Pal asset lifecycle work, checks whether PalSmith is available, prepares a short Context Packet, and hands off or requests PalSmith-style governance before execution.
