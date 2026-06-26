# Progress Summarization Skill

## Purpose

Help Mira produce clear progress reports during multi-stage, tool-backed, or blocked work.

## When to use

Use when work lasts across steps, involves file reads or edits, has verification requirements, or the user asks for status.

## Inputs

- Current task objective.
- Completed steps.
- Current step.
- Evidence from tools or files.
- Blockers, risks, and next action.

## Required context

Use the current task log and verified evidence. Do not infer completed work without a current signal.

## Process

1. State what is done.
2. State what is in progress.
3. State what remains.
4. Name blockers honestly.
5. Keep the update short and user-facing.

## Output

A concise progress update or final status section.

## Quality bar

The report must be easy to scan, evidence-backed, and honest about not-run or blocked checks.

## User confirmation points

Ask confirmation when the next step changes scope, adds risk, or requires user-owned credentials or approvals.

## No-code boundary

This skill formats communication only. It does not execute commands or validate files by itself.

## Common mistakes

- Reporting planned work as completed.
- Hiding blockers behind generic success language.
- Overloading the user with internal logs.
- Dropping the Pal prefix in AgentPal mode.

## Example

After writing Mira skills, Mira reports that skill assets are complete, knowledge assets remain, and JSON validation is still not run.
