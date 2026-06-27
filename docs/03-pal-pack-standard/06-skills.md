# Skills

## Status

Current for AgentPal `v0.1.0-rc.1`.

`skills/` stores formal Pal-owned Skills. A Skill is a focused capability; a Pal is the broader working companion that owns identity, judgment, context, memory boundaries, and output contracts.

## Minimum

```text
skills/index.md
```

The index can be short. It may say no formal Skills exist yet.

## Standard Skill Structure

```text
skills/<skill-id>/
├─ SKILL.md
└─ README.md
```

`SKILL.md` is the runtime entry. `README.md` is human notes.

## Pal-Owned Storage Rule

When the user explicitly asks to save a Skill, or similar operations repeat three or more times, the formal Skill belongs under the owner Pal's own `skills/` directory:

```text
official/pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md
```

Do not default to global runtime Skill folders.

## Not Contacts

Skills are not Pals. Do not add ordinary Skills to `workspace/organization/contacts/`.
