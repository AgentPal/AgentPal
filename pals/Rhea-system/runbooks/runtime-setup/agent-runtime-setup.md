# Agent Runtime Setup Runbook

用于把 Runtime / Agent 安装配置需求转成执行层 handoff。

## Required Context

- Runtime / Agent 名称。
- 用户系统平台。
- 官方来源或待查证来源。
- 目标用途。
- 是否允许安装、登录、配置 PATH 或连接外部服务。

## Steps

1. 确认目标 Runtime。
2. 优先要求查官方来源和当前安装要求。
3. 检查是否已安装、版本、路径、PATH、登录和 provider 状态。
4. 标记权限、账号、API key 和外部连接风险。
5. 生成执行层任务包。
6. 要求安装后验证和失败报告。

## Output

```text
## Runtime
## 官方来源 / 待查来源
## 安装前只读检查
## 需要确认的动作
## 执行层任务包
## 安装后验证
## 失败回收
```

## Evidence

- 版本。
- 安装路径。
- 命令可用性。
- 启动状态。
- 登录或 provider 状态摘要，不保存凭据。
- 错误日志摘要。

## Boundary

Rhea 不直接安装 Runtime，不保存 token，不替用户登录。

