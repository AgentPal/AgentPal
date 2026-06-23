# Mira Route And Stop Self-Test

## Purpose

Verify that Mira routes and stops after specialist handoff.

## Test Input

```text
帮我设计一个 html 页面
```

Additional input:

```text
如果这个项目继续开发，你会给我一些专业建议
```

## Expected Behavior

Mira uses AI routing judgement case-by-case.

One valid response shape:

```text
Mira：
我判断这次更适合由 Atlas 接手，因为当前请求需要工程边界和验收标准。我请 Atlas 接手。
```

```text
Atlas：
我接手...
```

This is a non-binding example. It must not be used as a keyword routing rule.

## Fail Signs

- Mira designs the full page herself after handoff.
- Mira provides the professional product/development advice herself after handoff.
- Mira says `我的专业建议是...` and then completes the owner Pal answer.
- Mira keeps explaining the owner's professional process after handoff.
- Owner Pal does not become active speaker.
- Owner is selected by a fixed keyword or domain table.

