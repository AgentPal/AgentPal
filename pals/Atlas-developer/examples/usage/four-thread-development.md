# Four Thread Development Example

```text
# 线程 1：任务接入与边界
负责梳理开发任务接入、缺口判断和高风险动作识别。
只修改 skills/developer-task-intake/ 和相关知识文件。
完成后返回 affected paths、检查清单和测试建议。
```

```text
# 线程 2：执行层交接
负责完善 Codex / Claude Code 任务提示词和仓库交接格式。
只修改 skills/requirement-to-agent-task/、skills/repository-handoff/ 和 examples/usage/。
不要修改通讯录或 runtime 文件。
```

```text
# 线程 3：evidence 复验
负责完善 evidence 检查项、验收结论和返工条件。
只修改 skills/execution-evidence-review/、core/verification-protocol.md 和 knowledge/runtime/。
```

```text
# 线程 4：最终整合复验
读取前三个线程报告，检查文件范围冲突、术语一致性和验收标准。
不做大范围重写，只修正明显不一致。
```

