# runtime-setup-handoff

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：Runtime 安装与配置交接

## 用途

为 Codex、Claude Code、OpenHands、Gemini CLI、DeepSeek-TUI 等 Runtime / Agent 的安装、检测和配置生成执行层 handoff。

## 适用场景

- 用户要准备外部 Runtime Runtime。
- Runtime 已安装但不可用。
- 需要检查登录、provider、PATH、依赖或项目目录。

## 不适合场景

- 让 Rhea 直接安装 Runtime。
- 未确认官方来源或安装方式。
- 需要输入密钥、token 或账号凭据。

## 输入信息

- Runtime 名称。
- 用户系统平台。
- 目标用途。
- 官方来源或待查证来源。
- 用户允许的执行范围。

## 处理流程

1. 确认 Runtime 和目标平台。
2. 要求优先查官方来源。
3. 检查安装前准备、权限和账号风险。
4. 生成执行层任务包。
5. 定义安装后验证和失败回收。

## 输出格式

```text
## Runtime
## 安装前确认
## 执行层任务
## 禁止事项
## 安装后验证
## 失败回收
```

## 验收标准

- 来源优先级清楚。
- 不含未知脚本自动执行。
- 验证要求包含版本、路径、启动状态和登录/可用性说明。

## 风险边界

不保存凭据，不代替用户登录，不批准管理员权限。

## 与其他 Skill / Runbook 的关系

使用 `runbooks/runtime-setup/agent-runtime-setup.md`，必要时咨询问从当前 contacts / registry 解析出的合适协作对象 查证官方资料。

