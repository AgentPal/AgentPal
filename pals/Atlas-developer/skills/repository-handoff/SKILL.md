---
name: repository-handoff
description: Use this skill when you need to 为执行层准备仓库级开发交接包，让 Codex、Claude Code、OpenHands 或外部 Runtime 快速理解项目上下文和边界。
---

# repository-handoff

## Purpose

为执行层准备仓库级开发交接包，让 Codex、Claude Code、OpenHands 或外部 Runtime 快速理解项目上下文和边界。

## When to use

- 新执行线程需要接手仓库。
- 用户要把任务交给外部 Runtime。
- 当前项目有多份必读文档。
- 需要明确不可修改文件和测试命令。

## Inputs

- 项目路径。
- 当前目标。
- 必读文档。
- 相关文件。
- 禁止修改文件。
- 测试、构建、格式化命令。
- 已知问题、风险和期望产物。

## Process

1. 用最短说明描述项目和当前目标。
2. 列出必须先读的文件，而不是让执行层读全仓库。
3. 写清可修改范围和禁止事项。
4. 写清验证命令、手工检查和完成报告格式。
5. 标注高风险动作必须等待审批。
6. 要求执行层返回 evidence。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户只是咨询概念。
- 任务没有仓库或文件目标。
- 用户要求把未授权第三方内容打包发布。

Risk boundary:
仓库交接不能包含密钥、token、私人记忆、真实用户日志或无关内部资料。执行命令只是建议，由 Runtime 在权限内执行。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 执行层能根据交接包开始工作。
- 没有泄露私人记忆或无关上下文。
- 不要求执行层做越权动作。

## Related files

- Runtime entry: skills/repository-handoff/SKILL.md
- Human notes: skills/repository-handoff/README.md
- Parent index: skills/index.md

- `context-engineering` 负责压缩交接上下文。
- `source-driven-development` 指定需要查证的来源。
- `security-and-hardening` 检查敏感信息。

