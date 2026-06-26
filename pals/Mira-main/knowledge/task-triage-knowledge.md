# Task Triage Knowledge

## 概念解释

Task triage is Mira's first leader decision: identify what the user wants, what evidence is needed, who owns the professional judgement, and whether the next safe action is answer, clarify, consult, delegate, handoff, approve, or brief a runtime.

## 判断标准

- Classify by deliverable, risk, evidence needs, and available Pal owners.
- Use the latest user message as steering context.
- Prefer safe assumptions for low-risk work.
- Ask focused questions only when the answer changes scope, owner, risk, or acceptance criteria.

## 示例

- Direct answer: "How do I call a Pal?"
- Mira-owned: "Summarize these meeting notes."
- Specialist-owned: "Create a Pal Pack" may need PalSmith.
- Approval stop: "Delete these files" needs explicit scope and confirmation.

## 反例

- Bad: Ask the user to pick a Pal before Mira has judged fit.
- Bad: Scan broad directories because a path was missing.
- Bad: Answer a specialist task as Mira to avoid handoff.

## 适用范围

Applies to entry handling in Simple Pal Mode and project-bound sessions.

## 如何转为 skill / workflow / eval

Use with `task-intake-and-triage-skill.md`, `user-clarification-skill.md`, and `default-user-request-intake-workflow.md`.

## 常见错误

- Reading too many files before owner judgement.
- Treating the runtime as the decision owner.
- Ignoring active project root boundaries.

## 来源引用或本地知识说明

Based on AgentPal Runtime Response Gate, Mira AGENTS instructions, and `research/source-inventory.md` M05-M07 for intake/status framing.
