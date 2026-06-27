# PalSmith Quickstart: Build An AI Team In 5 Minutes

Status: PalSmith v0.4 quickstart.

Use this page when you want the shortest path from an idea to a readable Pal or AI team plan. PalSmith stays no-code: it designs, asks confirmation questions, prepares Runtime Task Packages, and reviews evidence from the current Agent Runtime.

## What You Can Say

```text
/pal PalSmith 帮我创建一个个人工作 Pal
/pal PalSmith 帮我搭建一个跨境电商 AI 团队
/pal PalSmith 检查这个 Pal 是否可以发布
/pal PalSmith 用这些资料创建一个真正能做私域运营的 Pal
```

These are examples, not keyword rules. Any current Pal may consult, delegate, or hand off to PalSmith after AI judgement shows the request belongs to Pal asset governance.

## What PalSmith Will Do

1. Ask for Pal name, responsibility, goals, scenarios, user materials, and research preference.
2. Build a job expertise model before proposing files.
3. Suggest one Pal or a 3-5 Pal team.
4. Explain what each Pal owns and does not own.
5. Ask focused confirmation questions.
6. Generate a Runtime Task Package.
7. Ask the current Agent Runtime to create or inspect files only after confirmation.
8. Review evidence through job fitness inspection, health inspection, Eval Lab, and readiness review.
9. Recommend a state: `idea`, `draft`, `testing`, `stable`, or `publish-ready`.

## What You Do Not Need To Do

- You do not need to hand-write `pal.json`.
- You do not need to understand every AgentPal directory first.
- You do not need to install Python, Node.js, Rust, a CLI, a scanner, or a validator.
- You do not need to decide central roster changes before seeing the plan.

## Five-Minute Path

1. Start with one sentence:

   ```text
   /pal PalSmith 帮我搭建一个跨境电商 AI 团队。
   ```

2. PalSmith replies with a small team proposal:

   - team purpose
   - recommended 3-5 Pals
   - owner, verifier, and consultants
   - team-local vs global contact suggestions
   - shared knowledge and workflow suggestions
   - confirmation questions

3. You confirm, narrow, or reject the plan.

4. PalSmith prepares the matching Runtime Task Package.

5. The current Agent Runtime creates files or reports evidence.

6. PalSmith reviews the evidence and gives the next state.

## Common Paths

| Goal | Start Here | PalSmith Output |
| --- | --- | --- |
| Create one working companion | `/pal PalSmith 帮我创建一个个人工作 Pal` | Pal design, boundaries, Pal Creation Task Package |
| Build a small AI team | `/pal PalSmith 帮我搭建一个跨境电商 AI 团队` | 3-5 Pal team proposal, AI Team Builder Task Package |
| Create from materials | `/pal PalSmith 用这些访谈记录创建一个咨询顾问 Pal` | source inventory, material ingestion plan, job expertise model, Pal Creation Task Package |
| Add domain knowledge | `/pal PalSmith 给这个 Pal 补行业知识，并保留来源` | web research to knowledge plan, source-backed knowledge updates |
| Check if a Pal can publish | `/pal PalSmith 检查这个 Pal 是否可以发布` | readiness review, Eval Lab, publish quality gate |
| Import a Pal from GitHub | `/pal PalSmith 从 GitHub 导入这个 Pal，并验证能不能用` | staging-first import plan, risk report, verification level |
| Verify direct call readiness | `/pal PalSmith 这个 Pal 是否真的能被 /pal 调用` | Level 1/2/3 call verification report |

## Confirmation Boundary

PalSmith may propose reads, writes, imports, exports, registration, central roster updates, or release status changes. It does not perform those actions itself.

The current Agent Runtime may act only after the relevant Runtime Task Package and user confirmation. Reports must separate:

- PalSmith judgement
- runtime evidence
- `missing`
- `not-run`
- risk

## Material And Research Boundary

If you provide materials, PalSmith first asks what can be read and what must be preserved. It classifies material into knowledge, skill, workflow, runbook, template, eval, output contract, and governance assets instead of turning everything into one brief summary.

If web research is needed, PalSmith asks before network access. The Runtime returns source evidence; PalSmith keeps facts, inference, recommendation, and uncertainty separate.

## Read Next

- [PalSmith overview](../PalSmith.md)
- [PalSmith end-to-end workflows](13-palsmith-end-to-end-workflows.md)
- [Runtime Task Package standard](../03-pal-pack-standard/14-runtime-task-package.md)
- [Quickstart examples](../../official/pals/PalSmith-pal-governor/examples/quickstart/README.md)
- [AI team blueprints](../../official/pals/PalSmith-pal-governor/examples/ai-team-blueprints/README.md)
- [PalSmith demo script](16-palsmith-demo-script.md)
- [PalSmith skills index](../../official/pals/PalSmith-pal-governor/skills/README.md)
- [PalSmith knowledge index](../../official/pals/PalSmith-pal-governor/knowledge/README.md)
