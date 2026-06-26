# Usage Example: Environment Error Diagnosis

This is a non-binding example. It demonstrates one possible collaboration shape, not a fixed route.

这是非绑定示例，只展示一种可能协作形态，不是固定路由。

## User Request

```text
项目跑不起来，提示包管理器找不到。
```

## Rhea 判断

这是开发环境 / PATH / 依赖工具问题。先不要重装项目，也不要删除依赖目录。优先做只读检测。

## 执行策略

- 检查系统平台。
- 检查运行环境和项目声明包管理器的版本和路径。
- 检查项目是否要求特定包管理器。
- 检查终端是否刷新。
- 如果环境问题排除后仍失败，再由当前 owner 从 contacts / registry 解析合适协作对象查看项目构建。

## 诊断任务包

```text
目标：确认项目声明的包管理器是否安装、是否在 PATH、是否满足项目要求。
允许：只读检查命令存在、版本、路径、项目 package manager 标记。
禁止：安装包管理器、删除依赖目录、修改 PATH、改 lockfile。
建议 Runtime：Codex。
模型 / 推理强度：中等。
Evidence：运行环境和包管理器版本与路径、项目配置摘要、错误摘要。
```

## 验收标准

如果 evidence 显示项目声明的包管理器不存在，下一步才生成安装审批请求。如果包管理器存在但项目仍失败，由当前 AI 逐案判断是否需要开发视角。

