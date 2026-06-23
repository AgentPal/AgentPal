# dependency-version-check

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：依赖与版本检查

## 用途

检查开发任务所需依赖、版本、PATH 和项目配置是否匹配。

## 适用场景

- 项目启动失败。
- 依赖安装失败。
- 工具版本太旧或版本冲突。
- 多个 Node / Python / Git / .NET / Flutter 版本混用。

## 不适合场景

- 需要直接升级或卸载工具。
- 用户未提供项目要求或错误摘要。

## 输入信息

- 目标工具和预期版本。
- 当前版本或错误输出摘要。
- 项目文件特征，如 lockfile、配置文件、README 摘要。

## 处理流程

1. 比较项目要求和当前状态。
2. 检查命令路径和版本来源。
3. 标记冲突或过期风险。
4. 生成只读检测和修复候选。
5. 由当前 owner 逐案请从当前 contacts / registry 解析出的合适协作对象补充代码层判断。

## 输出格式

```text
## 依赖对象
## 预期版本
## 当前状态
## 可能冲突
## 建议检查
## 后续交接
```

## 验收标准

- 区分环境问题和项目代码问题。
- 不把待核查版本写成已确认事实。
- 给出下一步 evidence。

## 风险边界

不自动升级、不删除 lockfile、不清理依赖目录。

## 与其他 Skill / Runbook 的关系

连接 `environment-diagnosis-plan` 和 implementation collaborator handoff。

