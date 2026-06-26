# Formal Skill Assets

Status: R13 release-readiness standard.

This standard defines how `pal.json` formal skill declarations map to real Pal-owned Skill assets in AgentPal v0.1.0-rc.1.

## What A Formal Skill Is

A formal skill is a Pal-owned capability listed in `pal.json` under `formal_skills`. It is part of that Pal's release-facing capability surface and must be backed by a real no-code asset under the Pal's own `skills/` directory.

Formal skills are not runtime tools. They are Markdown work manuals that guide judgement, context loading, task packaging, review, and output quality.

## Valid Representations

AgentPal accepts two release-valid representations.

### Flat Skill Card

A Flat Skill Card is a single Markdown file:

```text
skills/<formal-skill-id>.md
```

This form is valid for built-in Pal skills that do not need a separately packaged directory. A flat card is valid only when it is substantive and mapped from the formal skill ID.

### Directory Skill Package

A Directory Skill Package is one directory with an entry file:

```text
skills/<formal-skill-id>/SKILL.md
skills/<formal-skill-id>/README.md
```

Use this form when the skill has supporting examples, templates, evals, or multiple internal files.

## Required Mapping

Each official Pal should provide a skill asset map:

```text
skills/skill-asset-map.md
```

The map should include:

| formal_skill | asset_path | representation | status | notes |
| --- | --- | --- | --- | --- |

Valid `representation` values:

- `flat-card`
- `directory-package`
- `index-only-invalid`
- `missing`

Valid `status` values:

- `mapped`
- `partial`
- `missing`
- `deprecated`

## Release Validity Rules

- `formal_skill_count` must equal the length of `formal_skills`.
- Every `formal_skills` entry must map to at least one real asset.
- A Flat Skill Card is valid when `skills/<formal-skill-id>.md` exists and contains substantive method content.
- A Directory Skill Package is valid when `skills/<formal-skill-id>/SKILL.md` or `skills/<formal-skill-id>/README.md` exists and contains substantive method content.
- `skills/index.md` or `skills/README.md` may summarize or navigate skills, but an index alone does not satisfy a formal skill.
- Do not create empty directories or empty README files to satisfy a count.
- Do not duplicate existing skills only to satisfy a checker. If a skill already exists under a different valid representation, map it.
- If a declared formal skill is no longer real, remove or deprecate the declaration deliberately and explain the change in the map or release report.

## Content Depth Bar

A release-valid formal skill asset should normally cover:

- Purpose
- When to use
- Inputs
- Required context
- Process
- Output
- Quality bar
- User confirmation points
- No-code boundary
- Common mistakes
- Example

Older directory packages may use equivalent headings, but they must still provide enough method detail for the Pal to use the skill without inventing the process.

## Check Procedure

For each official Pal:

1. Parse `pal.json`.
2. Confirm `formal_skill_count == formal_skills.length`.
3. For each formal skill ID, check for:
   - `skills/<id>.md`
   - `skills/<id>/SKILL.md`
   - `skills/<id>/README.md`
4. Confirm `skills/skill-asset-map.md` records the mapping.
5. Sample content depth for new or changed skill assets.
6. Report missing, partial, deprecated, and index-only-invalid entries honestly.

