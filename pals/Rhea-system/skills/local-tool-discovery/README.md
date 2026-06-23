# local-tool-discovery

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：本地工具发现

## 用途

识别当前机器或 Runtime 可用的包管理器、开发工具、Agent、Skill、插件、MCP、hooks 和 commands。

## 适用场景

- 需要判断该用哪个执行层。
- 安装前要看是否已有工具。
- 需要建立能力卡片或路由建议。

## 不适合场景

- 要求 Rhea 直接扫描私密目录。
- 要求保存完整系统清单或私人软件列表。

## 输入信息

- 当前 Runtime。
- 目标系统范围。
- 允许检查的工具类型。
- 用户隐私边界。

## 处理流程

1. 生成只读发现任务。
2. 区分工具、Runtime、Skill、插件、MCP 和 Pal。
3. 建立能力摘要。
4. 写入 runtime/capabilities 相关记忆候选。
5. 不把外部 Runtime 加入 contacts。

## 输出格式

```text
## 发现目标
## 只读检查范围
## 能力卡片
## 路由建议
## 隐私边界
```

## 验收标准

- 发现任务不越权。
- 能区分 Pal 通讯录和外部工具。
- 只记录必要摘要。

## 风险边界

不保存完整用户软件清单，不读取敏感路径。

## 与其他 Skill / Runbook 的关系

连接 runtime、models、plugins、capabilities、orchestration 和 memory/runtime。

