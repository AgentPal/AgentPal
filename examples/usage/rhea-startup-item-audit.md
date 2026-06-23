# Startup Item Audit AI Judgement Example

## User Message

```text
帮我检查有哪些应用会开机启动，先不要关闭。
```

## Expected Flow

```text
Mira：
我判断这是已注册 owner Pal 的职责范围，需要由当前 contacts / registry 中合适的 Pal 接手。
我请该 owner Pal 接手。
```

```text
<Owner Pal>：
我接手。先做只读检查，不会修改启动项。

我会按系统维护边界处理：
1. 先只读检查启动项来源。
2. 不禁用、不删除、不修改。
3. 如果发现可疑项，我会列成候选清单。
4. 如果需要修改，会先让你确认。

如果没有启动项专项知识卡，我会说明 fallback method，并把重复任务记录放在 owner Pal learning/。
```

```text
Execution layer：
当前 Codex 执行层执行只读检查。
不修改启动项。
```

```text
<Owner Pal>：
我通过当前 Codex 执行层读取了启动项信息。
这是只读检查，没有修改系统设置。

看到的启动项包括：
...

建议：
...
```

## What Must Not Happen

- Mira directly performs owner Pal judgment without handoff.
- Owner Pal claims a dedicated startup-item knowledge card exists if none was read.
- Codex disables startup items without user confirmation.
- Startup audit learning is stored under Mira instead of the owner Pal's `learning/`.
- Mira continues as active speaker after handing off to owner Pal.

