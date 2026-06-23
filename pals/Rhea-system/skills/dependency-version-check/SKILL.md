---
name: dependency-version-check
description: Use this skill when you need to 检查开发任务所需依赖、版本、PATH 和项目配置是否匹配。
---

# dependency-version-check

## Purpose

检查开发任务所需依赖、版本、PATH 和项目配置是否匹配。

## When to use

- 项目启动失败。
- 依赖安装失败。
- 工具版本太旧或版本冲突。
- 多个 Node / Python / Git / .NET / Flutter 版本混用。

## Inputs

- 目标工具和预期版本。
- 当前版本或错误输出摘要。
- 项目文件特征，如 lockfile、配置文件、README 摘要。

## Process

1. 比较项目要求和当前状态。
2. 检查命令路径和版本来源。
3. 标记冲突或过期风险。
4. 生成只读检测和修复候选。
5. 由当前 owner 逐案请从当前 contacts / registry 解析出的合适协作对象补充代码层判断。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 需要直接升级或卸载工具。
- 用户未提供项目要求或错误摘要。

Risk boundary:
不自动升级、不删除 lockfile、不清理依赖目录。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 区分环境问题和项目代码问题。
- 不把待核查版本写成已确认事实。
- 给出下一步 evidence。

## Related files

- Runtime entry: skills/dependency-version-check/SKILL.md
- Human notes: skills/dependency-version-check/README.md
- Parent index: skills/index.md

连接 `environment-diagnosis-plan` 和 implementation collaborator handoff。

