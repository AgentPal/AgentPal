# Memory Protocol

Mira distinguishes static release files, runtime state, user memory, project memory, and knowledge candidates.

## Destinations

- user preferences: `memory/user/`
- AgentPal system memory: `memory/system/`
- runtime usage experience: `memory/runtime/`
- Pal collaboration notes: `memory/collaboration/`
- external project facts: external `.agentpal/`
- Mira local patterns: `pals/Mira-main/memory/`
- specialist domain learning before Skill creation: owner Pal `learning/`
- formal owner Pal Skill: owner Pal `skills/<skill-id>/SKILL.md`
- owner Pal Skill memory before either formal trigger is met: owner Pal `memory/skill-memory/`
- unconfirmed facts: memory candidate template

## Rules

- Do not save sensitive information automatically.
- Ask before saving private or long-term personal data.
- Do not store passwords, tokens, API keys, payment data, private customer data, or unrelated personal details.
- Record source, confidence, and review date for durable memory.
- Prefer candidates over permanent writes when uncertain.

## Specialist learning boundary

Mira should not own specialist learning.

Specialist learning belongs to the specialist Pal.

Resolve the owner Pal from current contacts / registry and use that Pal's own storage:

- specialist domain learning before Skill creation -> `pals/<Owner-Pal-Directory>/learning/`
- owner Pal Skill memory before either formal trigger is met -> `pals/<Owner-Pal-Directory>/memory/skill-memory/`
- formal owner Pal Skill -> `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`

Mira may store only routing summaries, collaboration summaries, and user-approved preferences. Mira must not absorb all specialist fallback experiences into her own memory.

When the user explicitly asks to save a Skill, or similar operations exceed 3 times, the owner Pal must create the formal Skill under its own `skills/` directory.

## Pal-owned Skill storage boundary

If the user explicitly asks to make or save a method as a Skill, or similar operations exceed 3 times, the default target is the owner Pal's own `skills/` directory:

- formal Skill -> `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`
- human notes -> `pals/<Owner-Pal-Directory>/skills/<skill-id>/README.md`
- index update -> `pals/<Owner-Pal-Directory>/skills/index.md`
- exception-only not-yet-reviewed learning -> `pals/<Owner-Pal-Directory>/learning/`
- repeated runtime notes before either formal trigger is met -> `pals/<Owner-Pal-Directory>/memory/skill-memory/`

Do not use Codex global Skills, CodeWhale global Skills, plugin directories, external tool folders, or external project source directories as the default destination for AgentPal Pal-owned learning. Those are only valid when the user explicitly asks for that runtime/global Skill.

