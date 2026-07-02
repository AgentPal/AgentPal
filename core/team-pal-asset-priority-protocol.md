# Team And Pal Asset Priority Protocol

Status: v0.6 current protocol draft. Markdown / JSON protocol only.

## Purpose

This protocol defines which instruction or asset wins when user instructions, project constraints, Team Pack assets, and Pal assets conflict.

It applies when a task may involve both Team Asset Preflight and Pal Asset Preflight.

## Priority Order

Use this order:

1. User current instruction.
2. Current project constraints.
3. Team Workflow / Team Eval.
4. Pal responsibility boundary.
5. Team Knowledge / Team Runbook.
6. Pal Knowledge / Pal Skill.
7. Team Memory.
8. Pal Memory.
9. General AgentPal protocol.

## Conflict Rules

Team tasks prioritize Team Workflow when the workflow is selected and valid.

Pal responsibility boundaries override team assignment. A Team Pack cannot force a Pal to perform work that its own boundary forbids.

Team Knowledge and Team Runbooks guide shared process, but Pal Knowledge and Pal Skills guide the member's professional judgement inside that role.

Memory is advisory unless the current user instruction or project constraint confirms it. Team Memory ranks above Pal Memory for stable team workflow history, but neither can override current user instruction, project constraints, workflow, eval, or Pal boundary.

General AgentPal protocols remain the fallback foundation. They do not erase current user instruction or concrete Team / Pal assets.

## Replan Rule

If an assigned Pal's boundary prevents execution, the Owner Pal or team conductor must replan. The member Pal may propose an alternative role, safer scope, or replacement Pal, but it must not privately bypass the team workflow.

## Improvement Suggestions

A Pal may suggest improving Team Workflow, Team Eval, Team Knowledge, or roster design, but it must mark that suggestion as a proposal. It cannot silently rewrite the process during the current task unless the user authorizes that change and the runtime provides write evidence.

## Reporting Requirement

For substantive team tasks, final reports should state:

- selected team workflow;
- member Pal Asset Preflight status;
- any priority conflicts;
- any replan decisions;
- skipped or blocked steps;
- verification status.
