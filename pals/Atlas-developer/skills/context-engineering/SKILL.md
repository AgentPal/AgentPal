---
name: context-engineering
description: Use this skill when you need to 为 Codex、Claude Code、OpenHands 或其他外部 Runtime 准备刚好够用的 Context Pack，避免把全部文档和无关记忆塞给执行层。
---

# context-engineering

## Purpose

为 Codex、Claude Code、OpenHands 或其他外部 Runtime 准备刚好够用的 Context Pack，避免把全部文档和无关记忆塞给执行层。

## When to use

- 要把任务交给新执行线程。
- 多线程开发需要不同上下文包。
- 外部 Runtime 需要仓库、文件范围、约束和验收标准。
- 任务涉及敏感记忆，需要最小化共享。

## Inputs

- 用户目标。
- 仓库路径和相关目录。
- 必读文件候选。
- 修改范围和禁止事项。
- 相关记忆摘要。
- Runtime 能力和模型限制。

## Process

1. 判断执行层真正需要知道什么。
2. 选择少量必读文件，而不是全仓库倾倒。
3. 把用户目标、边界、验收标准和风险压缩成 Context Pack。
4. 移除私人记忆、无关历史和敏感信息。
5. 为弱模型补充更细的步骤、文件范围和停止条件。
6. 输出可复制的上下文包。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 单句咨询，不需要执行层接手。
- 用户要求共享完整私人记忆或敏感日志。
- 任务范围完全不清。

Risk boundary:
不要把 `memory/user/`、真实项目账本、密钥、日志、账号、生产数据或无关对话全文交给外部 Runtime。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 上下文足够执行任务。
- 没有倾倒无关文档。
- 没有泄露私人记忆或敏感数据。
- 弱模型收到更完整约束。

## Related files

- Runtime entry: skills/context-engineering/SKILL.md
- Human notes: skills/context-engineering/README.md
- Parent index: skills/index.md

- `repository-handoff` 提供仓库级信息，本 Skill 负责压缩和选择上下文。
- `multi-thread-agent-dispatch` 为每个线程生成不同 Context Pack。
- `security-and-hardening` 检查敏感上下文共享风险。

