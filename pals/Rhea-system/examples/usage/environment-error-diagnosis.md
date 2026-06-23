# Usage Example: Environment Error Diagnosis

This is a non-binding example. It demonstrates one possible collaboration shape, not a fixed route.

这是非绑定示例，只展示一种可能协作形态，不是固定路由。

## User Request

```text
项目跑不起来，提示 pnpm 找不到。
```

## Rhea 判断

这是开发环境 / PATH / 依赖工具问题。先不要重装项目，也不要删除依赖目录。优先做只读检测。

## 执行策略

- 检查系统平台。
- 检查 pnpm、node、npm 的版本和路径。
- 检查项目是否要求 pnpm。
- 检查终端是否刷新。
- 如果环境问题排除后仍失败，再由当前 owner 从 contacts / registry 解析合适协作对象查看项目构建。

## 诊断任务包

```text
目标：确认 pnpm 是否安装、是否在 PATH、是否满足项目要求。
允许：只读检查命令存在、版本、路径、项目 package manager 标记。
禁止：安装 pnpm、删除 node_modules、修改 PATH、改 lockfile。
建议 Runtime：Codex。
模型 / 推理强度：中等。
Evidence：pnpm/node/npm 版本和路径、项目配置摘要、错误摘要。
```

## 验收标准

如果 evidence 显示 pnpm 不存在，下一步才生成安装审批请求。如果 pnpm 存在但项目仍失败，由当前 AI 逐案判断是否需要开发视角。

