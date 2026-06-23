---
name: result-summarizer
description: Summarize specialist Pal, runtime, or non-Pal tool results with evidence status.
---

# Result Summarizer

## When to use

Use after a Pal, runtime, Skill, plugin, MCP server, tool, or non-Pal runtime returns output.

Use Mira's result summarizer only when Mira is the active Pal, the user asks Mira to summarize, or the active Pal hands the task back to Mira.

## Inputs needed

- returned result
- evidence
- files or actions claimed
- verification status
- risks

## Steps

1. Check who is the active Pal.
2. If a specialist Pal is active, let that Pal report directly unless Mira was asked to summarize.
3. For real modifications or "who executed this" questions, separate Pal layer and Execution layer.
4. For read-only checks, keep the report brief.
5. Report evidence.
6. Name remaining risk.
7. Give next step.

## Output format

Short user-facing summary starting with the active Pal prefix.

For real modification or execution attribution questions, include:

- Pal layer
- Execution layer
- evidence
- result
- note that the Pal did not personally execute the operation

## Safety notes

Do not convert unverified reports into completed claims.

