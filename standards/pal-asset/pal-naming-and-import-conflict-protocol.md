# Pal Naming And Import Conflict Protocol

Status: v0.6 current protocol draft. Markdown / JSON protocol only; no automatic importer or registry writer is implemented.

## Purpose

AgentPal Pals are working companions with names and roles. A Pal must not be only a job title, function label, plugin, model, Skill, MCP tool, or runtime.

This protocol gives PalSmith and roster maintainers a shared rule for naming new Pals and handling same-name imports.

## Naming Rule

A valid Pal identity must include:

- a stable machine identity;
- a human-style display name;
- a role title;
- a contact label for rosters;
- aliases;
- optional user custom name;
- original imported name when applicable;
- import source when applicable.

Recommended fields:

```json
{
  "canonical_id": "pal_faye_fde_01",
  "display_name": "Faye",
  "role_title": "FDE business workflow architect",
  "contact_label": "Faye · FDE",
  "aliases": ["Faye"],
  "user_custom_name": null,
  "original_name": null,
  "imported_from": null
}
```

`canonical_id` is stable. `display_name` is the Pal's human name. `role_title` describes the job. `contact_label` is what contacts and rosters can show when names collide or role context matters.

## Forbidden Display Names

These are role titles, not Pal display names:

- `方案定制 Pal`
- `外部调研 Pal`
- `视频剪辑 Pal`
- `产品经理 Pal`
- `测试 Pal`

They may become `role_title` values, such as `方案定制顾问`, `外部调研分析师`, `视频剪辑师`, `产品经理`, or `质量测试顾问`.

## User Custom Names

Users may rename a Pal.

Rules:

- `user_custom_name` wins for user-facing display when set;
- `canonical_id` never changes because of a rename;
- previous names move into `aliases`;
- `contact_label` should update to show the active user-facing name plus role;
- `original_name` remains available for imported or renamed Pals.

## Same-Name Import Rules

When importing an external Pal:

1. If `display_name` does not conflict, add it with its role title and stable canonical id.
2. If `display_name` conflicts but `role_title` differs, keep the human name and distinguish in `contact_label`.
3. If both `display_name` and `role_title` conflict, add source or a numeric suffix to `contact_label`, not to `canonical_id`.
4. If a short-name invocation is ambiguous, ask the user to choose. Do not guess.
5. If the external Pal has no human name, trigger naming suggestions before import.

Example same-name records:

```json
[
  {
    "canonical_id": "pal_faye_fde_01",
    "display_name": "Faye",
    "role_title": "FDE business workflow architect",
    "contact_label": "Faye · FDE",
    "aliases": ["Faye"]
  },
  {
    "canonical_id": "pal_faye_video_02",
    "display_name": "Faye",
    "role_title": "video production strategist",
    "contact_label": "Faye · Video Production",
    "aliases": ["Faye"],
    "imported_from": "external-pal-pack"
  }
]
```

If the user says `/pal Faye` and both are discoverable, ask which `contact_label` they mean.

## PalSmith Creation Rule

When the user asks for a role-named Pal, PalSmith must interpret the phrase as role intent, not as the final Pal name.

Example:

```text
User: 创建一个方案定制 Pal
PalSmith: This means a Pal with a human name and the role title "方案定制顾问". I will suggest names and ask whether you accept one, or generate a safe default if you prefer.
```

PalSmith must not create a Pal whose `display_name` is only a role or capability label.

## Contacts And Registry Rule

Contacts and registry remain the source of truth for discovery.

Naming conflict resolution must be reflected in the contact card or registration proposal before the Pal becomes discoverable. Drafts and imports may stay staged until the user approves the final name and contact label.

## Not A Pal

Do not add these as Pals just because they have names:

- ordinary Skills;
- plugins;
- models;
- MCP servers or tools;
- runtime connectors;
- raw repositories;
- knowledge packs;
- persona-only packs;
- Team Packs.

They may be referenced by a Pal or Team, but they are not Pal contacts.
