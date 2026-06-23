# Multi-Pal Dispatch Self-Test

## Purpose

Verify that multi-Pal collaboration has ordered roles and case-by-case selection.

## Test Input

```text
Research this product idea, define MVP scope, turn it into dev tasks, then check acceptance risk.
```

## Expected Behavior

Use AI routing judgement to choose:

- owner Pal
- consultant Pal(s)
- reviewer Pal(s)
- whether sequential, parallel, or simple-owner consult mode is useful
- whether execution layer is required
- final summarizer

No hard-coded semantic routing. Pal capability reference is not a route map.

Required fields:

- owner Pal for the current case
- consultant Pal(s), if any
- reviewer Pal(s), if any
- execution layer, if any
- final summarizer
- Specialist assets used
- fallback allowed / Knowledge gap if assets are missing
- evidence review requirements

## Fail Signs

- Multiple Pals answer without owner/consultant/reviewer roles.
- Mira owns all specialist learning.
- No Context Packet is used.
- No evidence review is required when execution is involved.
- A fixed stage chain is required solely by task wording.

