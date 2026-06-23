---
name: environment-diagnosis-plan
description: Use this skill when you need to 把环境异常整理成只读诊断任务，帮助执行层检查命令是否存在、版本是否正确、PATH 是否可用、依赖是否缺失。
---

# environment-diagnosis-plan

## Purpose

把环境异常整理成只读诊断任务，帮助执行层检查命令是否存在、版本是否正确、PATH 是否可用、依赖是否缺失。

## When to use

- 命令找不到。
- 项目依赖安装失败。
- 终端里版本不对。
- 多版本冲突或 PATH 顺序异常。

## Inputs

- 操作系统。
- 目标命令或工具。
- 错误信息摘要。
- 项目目录和相关配置文件，如果可共享。

## Process

1. 确定诊断目标。
2. 列出只读检查项。
3. 标注禁止动作。
4. 指定 evidence 格式。
5. 选择执行层和模型强度。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 需要直接修复 PATH、删除目录或安装依赖。
- 没有说明系统平台和目标工具。

Risk boundary:
不修改系统设置，不清理缓存，不安装依赖，不删除目录。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 所有检查项都是只读或明确标注需要审批。
- 能返回版本、路径、配置摘要和错误摘要。
- 不包含自动修复承诺。

## Related files

- Runtime entry: skills/environment-diagnosis-plan/SKILL.md
- Human notes: skills/environment-diagnosis-plan/README.md
- Parent index: skills/index.md

参考 `runbooks/environment/diagnose-dev-environment.md`，结果交给 `system-evidence-review`。

