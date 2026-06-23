# Pal-Owned Skill Storage Protocol

This protocol decides where AgentPal-created Skills, Runbooks, Workflows, and Knowledge Cards are stored.

## Core Rule

AgentPal Pal learning belongs to the owner Pal, not to the runtime.

When the user asks a Pal to "make this a Skill", "save this as a Skill", "以后直接用", "下次直接调用", or otherwise turn a repeated method into a reusable Pal capability, the storage target is the owner Pal's own `skills/` directory unless the user explicitly asks for a Codex global Skill, CodeWhale Skill, plugin, MCP server, or external runtime asset.

When similar operations are requested more than 3 times, the owner Pal must automatically create a formal Pal-owned Skill under its own `skills/` directory.

## Default Destinations

- Formal Pal Skill: `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`
- Pal Skill human notes: `pals/<Owner-Pal-Directory>/skills/<skill-id>/README.md`
- Pal skills index update: `pals/<Owner-Pal-Directory>/skills/index.md`
- Explicit user request to save a Skill: `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`
- Similar operation count > 3: `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`
- Exception fallback only when not enough information exists to safely write a formal Skill: `pals/<Owner-Pal-Directory>/learning/`
- Runtime-local notes only before either trigger is met: `pals/<Owner-Pal-Directory>/memory/skill-memory/`
- Runbook: `pals/<Owner-Pal-Directory>/runbooks/`
- Workflow: `pals/<Owner-Pal-Directory>/workflows/`
- Knowledge Card: `pals/<Owner-Pal-Directory>/knowledge/`

## Forbidden Default Destinations

Do not store AgentPal Pal-owned Skills in these locations by default:

- `~/.codex/skills/`
- `%USERPROFILE%\\.codex\\skills\\`
- `~/.codewhale/skills/`
- `.codewhale/skills/`
- global runtime plugin folders
- external tool-owned Skill folders
- external project source directories

Those destinations are only valid when the user explicitly asks to create a runtime/global Skill for that runtime, and the answer must state that it is not an AgentPal Pal-owned Skill.

## Owner Selection

The owner Pal is selected by AI judgement from the current registered Pal pool. The Skill must be stored under that owner Pal, even if the current execution layer uses Codex, CodeWhale, Claude Code, OpenHands, or another runtime to write files.

Examples:

- CodeWhale control method learned by Atlas -> `pals/Atlas-developer/skills/codewhale-control/SKILL.md`
- Windows startup audit learned by Rhea -> `pals/Rhea-system/skills/windows-startup-audit/SKILL.md`
- meeting follow-up method learned by Mira -> `pals/Mira-main/skills/action-item-tracker/SKILL.md`

These are examples only. They do not create semantic routing rules.

## Required Skill Shape

A formal Pal Skill must have:

- `SKILL.md` as the runtime entry.
- concise frontmatter with `name` and `description`.
- when-to-use conditions.
- required inputs.
- steps.
- output format.
- safety notes.
- related Skill / Runbook / Knowledge links when relevant.

If the user explicitly asked to save a Skill, or similar operation count is greater than 3, create the formal Skill in the owner Pal's `skills/` directory. Only use `learning/` as an exception when required inputs are missing, the content is unsafe/private, or the user has not approved a high-risk write.

## Reporting

When a Pal creates a Skill, it must report:

- owner Pal
- trigger: `explicit_user_request` or `similar_operation_count_gt_3`
- storage mode: `formal_skill`, `runbook`, `workflow`, or `knowledge_card`
- target path
- whether `skills/index.md` was updated
- whether the user asked for AgentPal Pal-owned Skill or a runtime/global Skill

Do not say "stored as Skill" unless the file is under the owner Pal's Pal Pack or the user explicitly requested a different runtime/global destination.


