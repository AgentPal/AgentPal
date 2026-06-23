# Pal-Owned Skill Creation Self-Test

## Purpose

Verify that explicit Skill-saving requests and repeated similar operations create formal Skills under the owner Pal's own `skills/` directory.

## Test input

```text
This is the fourth similar startup-item-audit task for Rhea.
```

Additional explicit trigger input:

```text
/pal Rhea 以后这种启动项检查保存成 skill，下一次直接调用。
```

## Expected behavior

- owner Pal = Rhea.
- task family = startup-item-audit.
- trigger reason is either `explicit_user_request` or `similar_operation_count_gt_3`.
- formal Skill path is under `pals/Rhea-system/skills/<skill-id>/SKILL.md`.
- `pals/Rhea-system/skills/index.md` is updated.
- Rhea reports asset name, task family, trigger reason, safety boundary, and storage target.
- Codex global Skills, CodeWhale global Skills, plugin folders, tool folders, and external project source directories are not used unless the user explicitly requests a runtime/global Skill.

## Fail signs

- Skill goes under Mira.
- Skill goes under `~/.codex/skills/`, `.codex/skills/`, `~/.codewhale/skills/`, `.codewhale/skills/`, or an external tool folder by default.
- Explicit user request is treated only as a candidate.
- Similar operation count greater than 3 is treated only as a candidate.
- No owner Pal is named.
- No storage target is reported.

