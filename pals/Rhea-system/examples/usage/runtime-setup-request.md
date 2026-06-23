# Usage Example: Runtime Setup Request

## User Request

```text
我想配置 Claude Code，让它能在这个项目里作为外部开发 Agent 使用。
```

## Rhea 判断

这是 Runtime / Agent 安装配置任务，不是 Rhea 直接安装任务。需要先确认系统、官方来源、当前安装状态、账号 / provider、PATH、项目权限和 evidence 要求。

## 执行策略

- 先做只读检测：是否已安装、版本、路径、能否启动。
- 查证官方来源和当前安装方式。
- 如果需要安装、登录或修改 PATH，生成审批请求。
- 执行层完成后返回版本、路径、启动状态和失败日志摘要。

## 任务包

```text
目标：检查并准备 Claude Code 作为外部开发 Agent。
允许：只读检测安装状态、版本、路径和启动状态。
禁止：自动安装、保存凭据、修改 PATH、连接未知 MCP、扩大项目权限。
建议 Runtime：Codex 或 Claude Code 自身可用时由用户确认。
模型 / 推理强度：中等；如涉及权限策略或 SDK 集成，提高推理强度。
Evidence：版本、路径、启动状态、provider 状态摘要、未完成项。
```

## 验收标准

Rhea 只在 evidence 覆盖安装状态、路径、版本和启动状态后，才能判断 Runtime 准备是否可信。

