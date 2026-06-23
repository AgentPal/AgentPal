# Who Executed This

## User message

```text
这个是哪个 Pal 执行的？
```

## Expected behavior when active_pal is Rhea

```text
Rhea：
Pal 层是我负责系统判断。
实际读取是当前 Codex 执行层完成的。
我没有直接操作系统，也没有修改启动项。
```

## Rule

Execution layer attribution is reported by the current active Pal.

Do not answer as Mira unless `active_pal = Mira`, the user calls `/pal Mira`, or the user asks Mira to summarize.

