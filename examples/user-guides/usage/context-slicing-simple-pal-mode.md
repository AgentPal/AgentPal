# Context Slicing In Simple Pal Mode

这是非绑定示例，不能升级成固定路由规则。

## User

```text
用 PHP 开发一个团队任务管理系统，帮我提供建议。
```

## Correct Shape

Mira only reads the user goal, current guardrails, contacts / registry summary, and active project summary if any.

Mira chooses an owner Pal by AI judgement and sends a minimal Context Packet.

The owner Pal reads only:

- own `PAL.md`
- own `AGENTS.md`
- own `SKILL.md`
- own `pal.json`
- own `core/output-contract.md`
- one to three relevant assets

The owner Pal does not read all Pals, all project files, all memory, examples, evals, or future design docs.

## Why

Simple Pal Mode should still be token-aware. The Pal layer becomes valuable when it selects the right small asset slice instead of flooding the context.
