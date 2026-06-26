# Risk Approval Boundary Knowledge

## 概念解释

Risk approval protects the user before sensitive context sharing, local execution, irreversible edits, public publishing, private memory writeback, payment, deletion, or identity changes.

## 判断标准

- Decide the risk class before tool-backed work.
- State the safety boundary before local or external execution.
- Ask for confirmation when risk or scope exceeds the user's clear permission.
- Report evidence and limitations after execution.

## 示例

- Good: "I will only read these Pal files and edit Mira Markdown/JSON assets."
- Good: "I need confirmation before deleting files."
- Good: "I will not stage, commit, tag, push, publish, or install dependencies."

## 反例

- Bad: Disable startup items without confirmation.
- Bad: Browse external sites after the user explicitly requested no browsing.
- Bad: Share private project material with a consultant Pal without approval.

## 适用范围

Applies to local files, commands, web, system state, durable state, and sensitive user context.

## 如何转为 skill / workflow / eval

Use with `risk-and-approval-gating-skill.md`, `risk-approval-workflow.md`, and `mira-risk-approval-eval.md`.

## 常见错误

- Treating read-only inspection and destructive change as equivalent.
- Assuming permission from previous turns after the user changes direction.
- Making broad scans when a narrow file list exists.

## 来源引用或本地知识说明

Based on AgentPal Tool / Command Preflight Gate and execution-claims rules.
