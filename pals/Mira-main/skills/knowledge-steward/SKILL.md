---
name: knowledge-steward
description: Maintain public AgentPal knowledge candidates and indexes.
---

# Knowledge Steward

## When to use

Use when a public, reusable AgentPal rule or guide should be updated.

## Inputs needed

- source
- proposed fact
- target file
- review need

## Steps

1. Check release safety.
2. Summarize rather than copy long sources.
3. Mark source and confidence.
4. Write candidate if uncertain.
5. Update index if approved.

## Specialist knowledge boundary

Specialist knowledge gaps and repeated task candidates belong to the specialist Pal.

Do not turn fallback method into formal AgentPal knowledge without review.

When the user explicitly asks to save a Skill, or similar operations exceed 3 times, the owner Pal must create the formal Skill under its own `skills/` directory.

Treat saved Skills as Pal-owned learning by default. The formal destination is the owner Pal's `skills/<skill-id>/SKILL.md`, not Codex global Skills, CodeWhale global Skills, plugin folders, tool folders, or external project source directories. Use owner Pal `learning/` only as an exception when required inputs are missing, the content is unsafe/private, or the user has not approved a high-risk write.

## Output format

Knowledge update summary.

## Safety notes

Do not copy internal development documents or private data into public release files.

