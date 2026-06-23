<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# AI Routing Judgement No-Hardcode Self-Test

## Purpose

Verify that AgentPal uses AI routing judgement instead of fixed semantic routes.

## Required Pass Criteria

- No hard-coded semantic routing appears in runtime rules.
- AI routing judgement is case-by-case.
- Pal capability reference is not a route map.
- Explicit commands are deterministic.
- Safety and availability guardrails are deterministic.
- Subagent Mode is an option, not keyword-triggered.
- Examples are marked as non-binding examples.

## Test Cases

### 1. Explicit Pal Command

User:

```text
/pal Atlas 帮我看看这个任务。
```

Expected:

- Direct Pal command is honored if Atlas exists.
- This is deterministic command handling, not semantic routing.

### 2. Semantic Request

User:

```text
这个项目下一步怎么推进，给我专业建议。
```

Expected:

- Mira does not use a keyword map.
- Mira explains a case-specific owner judgement.
- Owner Pal answers immediately.

### 3. Multi-Perspective Request

User:

```text
我想听几个角度分别怎么看。
```

Expected:

- Mira decides case-by-case whether multi-Pal or Subagent Mode is useful.
- No fixed Pal set is required by the phrase alone.

### 4. Example Safety

Search examples and evals:

- Files may contain non-binding examples.
- No example may state that a semantic phrase must always route to a fixed Pal.

## Failure Examples

These are forbidden in runtime rules:

- task-domain to Pal maps
- keyword-triggered specialist dispatch
- natural-language trigger gates
- fixed Pal set required by broad semantic task shape
- capability references presented as route tables

