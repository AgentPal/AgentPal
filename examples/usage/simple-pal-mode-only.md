# Simple Pal Mode Only

AgentPal v0.1 uses Simple Pal Mode only.

Example:

```text
User:
用 PHP 开发一个团队任务管理系统，帮我提供建议。

Mira：
我判断这次更适合由 Atlas 接手，因为当前请求需要开发方案和架构取舍判断。我交给 Atlas。

Atlas：
我接手。
...
```

The important behavior is:

- Mira routes and stops.
- The owner Pal answers immediately.
- The owner Pal uses its own Pal assets and Output Contract.
- No separate runtime process is claimed.

