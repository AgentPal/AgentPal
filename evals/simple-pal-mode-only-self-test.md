# Simple Pal Mode Only Self-Test

Verify that AgentPal v0.1 task handling uses Simple Pal Mode only.

## Inputs

```text
用 PHP 开发一个团队任务管理系统，帮我提供建议。
```

```text
这个项目下一版值不值得继续做？如果值得，怎么开发、怎么验收？
```

## Expected

- Mira judges whether an owner Pal exists.
- Mira gives at most 2 short handoff sentences.
- The owner Pal answers immediately in the same response.
- The owner Pal uses its own assets, Output Contract, and fallback if needed.
- No runtime-mode metadata is printed.
- No parallel child-agent workflow is probed, called, or narrated.

## Failure

- Mira writes the professional body herself.
- The answer claims an unavailable runtime workflow.
- The answer delays owner Pal output to a later result.
- The answer treats Pal as an independent runtime process.

