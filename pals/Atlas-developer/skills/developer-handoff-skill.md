# Developer Handoff Skill

## Purpose

Help Atlas hand development work to a runtime or another Pal with enough context, boundaries, and evidence expectations.

## When to use

Use when Atlas prepares work for Codex, Claude Code, OpenHands, CodeWhale, another runtime, or a specialist Pal.

## Inputs

- Goal and current status.
- Source context and files already read.
- Allowed files and forbidden files.
- Required implementation steps.
- Verification and report format.
- Collaboration owner or reviewer.

## Required context

Use task package, current evidence, contacts / registry for Pal collaboration, and current runtime capability notes if known.

## Process

1. Name the receiver and whether it is a Pal or runtime.
2. State objective, scope, and non-goals.
3. Provide minimal context and source references.
4. List allowed/forbidden files and actions.
5. Define verification evidence and final report format.
6. Add stop conditions and approval gates.
7. Keep specialist ownership separate from runtime execution.

## Output

A developer handoff packet or Context Packet.

## Quality bar

The receiver should know what to do, what not to touch, and how to prove the work.

## User confirmation points

Ask before sharing sensitive context, using private logs, delegating beyond the requested scope, or changing durable assets.

## No-code boundary

This skill writes handoff instructions only.

## Common mistakes

- Passing full chat history instead of a bounded packet.
- Leaving verification vague.
- Calling the runtime the owner Pal.
- Omitting stop conditions.

## Example

Atlas sends Codex a package with goal, target files, forbidden release files, expected tests, final report headings, and a stop condition for dependency changes.
