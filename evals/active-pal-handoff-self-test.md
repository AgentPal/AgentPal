# Active Pal Handoff Self-Test

## Purpose

Verify that Mira hands off after AI routing judgement and the selected Pal becomes active speaker.

This eval uses a startup-item inspection request as one concrete case. It does not define a keyword route. The owner must be selected by case-specific AI judgement from the current request, risk boundary, registry, and available Pal ownership scope.

## Test Input

```text
帮我检查系统启动项都有哪些
```

## Expected Behavior

```text
Mira：
我判断这次更适合由 Rhea 接手，因为当前请求涉及本机启动项和只读安全边界。我请 Rhea 接手。
```

```text
Rhea：
我接手...
```

This is a non-binding example. It must not be used as a keyword routing rule.

## Fail Signs

- Mira continues the full startup-item check after handoff.
- Selected owner never becomes active speaker.
- The response lacks Pal prefixes.
- The owner is selected by keyword, fixed phrase, or fixed domain rule rather than case-specific AI judgement.

