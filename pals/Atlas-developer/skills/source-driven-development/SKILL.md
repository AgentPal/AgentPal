---
name: source-driven-development
description: Use this skill when you need to 要求涉及第三方库、框架、API、Runtime 能力或项目内部约定时，先查可靠来源，避免凭记忆开发。
---

# source-driven-development

## Purpose

要求涉及第三方库、框架、API、Runtime 能力或项目内部约定时，先查可靠来源，避免凭记忆开发。

## When to use

- 任务涉及新库、框架、API、CLI、SDK、MCP 或插件。
- Runtime 或模型能力可能变化。
- 执行层需要修改不熟悉的项目模块。
- 用户要求使用某个具体版本或平台能力。

## Inputs

- 技术名称、版本和目标平台。
- 项目本地文档、源码或配置路径。
- 需要验证的问题。
- 可用官方文档、源码、README 或 changelog 来源。

## Process

1. 判断是否必须查来源。
2. 优先使用项目本地文档、源码和配置。
3. 涉及外部库时要求查官方文档、官方仓库或 release notes。
4. 标明来源、版本和不确定点。
5. 将来源要求写进执行层任务。
6. 如果无法确认，要求执行层停止并报告。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 完全不涉及外部依赖或版本的简单文档任务。
- 用户只需要高层解释，不进入开发。
- 无法联网且本地也没有相关文档时，不能假装已查证。

Risk boundary:
不要要求执行层复制未授权第三方文档或源码。不要把社区帖子当成唯一来源。涉及高风险 API、认证、权限或支付时必须要求官方来源。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 任务中列出应查证来源。
- 不用模型记忆替代版本事实。
- 执行层报告引用了本地或官方来源。
- 无法确认时不继续编造实现。

## Related files

- Runtime entry: skills/source-driven-development/SKILL.md
- Human notes: skills/source-driven-development/README.md
- Parent index: skills/index.md

- `requirement-to-agent-task` 在任务中写入来源要求。
- `context-engineering` 把本地来源放入 Context Pack。
- `architecture-review` 用来源确认 Runtime / Adapter 边界。

