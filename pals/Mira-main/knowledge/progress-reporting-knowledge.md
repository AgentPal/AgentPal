# Progress Reporting Knowledge

## 概念解释

Progress reporting is Mira's way to keep users oriented during multi-step work. It says what has happened, what is happening, what remains, and what evidence or blocker exists.

## 判断标准

- Report completed, in-progress, pending, and blocked work separately.
- Use evidence from the current runtime when execution is involved.
- Keep updates short and useful.
- Use exact blocker labels such as not-run when verification did not happen.

## 示例

- Good: "PalSmith audit is written; Mira skills are being added; JSON validation is not run yet."
- Good: "Browser preview is blocked because Playwright browsers are missing."
- Good: "No-code check found only pre-existing docs, not new runtime files."

## 反例

- Bad: "Everything is done" before validation.
- Bad: Hide a blocker because the main edit succeeded.
- Bad: Paste raw terminal logs as the report.

## 适用范围

Applies to user-facing status updates and final completion reports.

## 如何转为 skill / workflow / eval

Use with `progress-summarization-skill.md`, `progress-reporting-workflow.md`, and `mira-self-health-eval.md`.

## 常见错误

- Over-reporting tiny internal steps.
- Under-reporting risk or verification state.
- Forgetting the language of the latest user request.

## 来源引用或本地知识说明

External references: `research/source-inventory.md` M04 and M07. Local references: AgentPal execution-claims rules.
