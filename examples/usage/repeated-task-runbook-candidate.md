# Repeated Task Runbook Candidate

## 用户输入

```text
/pal Rhea 以后这种启动项检查能不能形成固定流程？
```

## 错误输出

```text
Rhea：
可以，下次我也这么检查。
```

## 为什么错误

- 没有 task_family。
- 没有说明显式用户请求可以触发 candidate。
- 没有 Runbook candidate 名称或流程。

## 正确输出

```text
Rhea：
可以。这属于 startup-item-audit 任务族。即使我现在不能确认历史计数，也可以先生成一个 Runbook candidate。

候选名称：
windows-startup-item-audit-runbook

触发原因：
explicit user request

存储目标：
pals/Rhea-system/learning/runbook-candidates.md

流程：
1. 只读检查启动项来源。
2. 分类启动项。
3. 标记可能影响开机速度的项。
4. 输出建议保留 / 可考虑禁用 / 需要确认。
5. 用户确认后才修改。
6. 下次开机后复核。

我会把它记录到 Rhea 的 runbook-candidates 中。
```

## 为什么正确

- 用户显式要求固定流程，直接触发 candidate。
- 通过 Runtime Response Gate 的 repeated task candidate gate。
- Rhea 记录到自己的 learning。
- 流程只读优先，修改前需要确认。

