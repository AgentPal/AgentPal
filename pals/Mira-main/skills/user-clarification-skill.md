# User Clarification Skill

## Purpose

Help Mira ask the fewest useful questions needed to proceed safely.

## When to use

Use when missing information materially changes ownership, scope, risk, deliverable, or acceptance criteria.

## Inputs

- Current request.
- Missing facts.
- Safe default assumptions.
- Risk level.
- Available evidence.

## Required context

Use the latest user request first. Check existing project binding or task package before asking the user for information already available.

## Process

1. Decide whether a reasonable assumption is safe.
2. If yes, state the assumption briefly and proceed.
3. If not, ask one to three focused questions.
4. Offer a default path only when continuing without an answer is safe.
5. Avoid broad discovery questions.

## Output

A focused clarification question or a brief assumption statement.

## Quality bar

The question should unblock the next action. It should not transfer Mira's judgement work back to the user.

## User confirmation points

Require explicit confirmation when missing information affects irreversible action, sensitive data, public release, or identity/registry changes.

## No-code boundary

This skill is conversational. It does not run checks or write files.

## Common mistakes

- Asking the user to choose a Pal when Mira can judge from contacts / registry.
- Asking many questions to avoid making a safe decision.
- Proceeding silently when approval is required.
- Reusing an old answer after the user changed direction.

## Example

If the user asks to add AgentPal to "the project" but no project binding exists and no project list is available, Mira asks for the external project path instead of scanning random directories.
