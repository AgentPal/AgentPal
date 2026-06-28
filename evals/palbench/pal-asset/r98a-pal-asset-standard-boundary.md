# R98-A Pal Asset Standard Boundary Eval

Date: 2026-06-28

## Purpose

Verify that R98-A establishes Pal Asset Standard v0.5 while preserving Org Pack,
central roster, thin binding, and no-code runtime boundaries.

## Required Files

| Check | Expected |
| --- | --- |
| Main Pal Asset Standard exists | `standards/pal-asset/pal-asset-standard.md` |
| Pal Skill vs Agent Skill standard exists | `standards/pal-asset/pal-skill-vs-agent-skill-standard.md` |
| Directory standard exists | `standards/pal-asset/pal-asset-directory-standard.md` |
| Root entry standard exists | `standards/pal-asset/pal-root-entry-standard.md` |
| Pal Asset standard index exists | `standards/pal-asset/README.md` |
| Pal Asset template index exists | `templates/pal-asset/README.md` |

## Boundary Assertions

1. Pal is defined as a long-term working companion in the AgentPal organization,
   not a role prompt.
2. Pal Asset is defined as the structured content collection that makes a Pal
   stable and repeatable.
3. Pal Skill is defined as a role-level comprehensive work capability.
4. Agent Skill is defined as a runtime tool-level execution capability.
5. Pal `skills/` defaults to Pal Skill, not runtime-installed Agent Skill.
6. External projects remain thin-bound business sites, not AgentPal asset
   warehouses.
7. Central roster remains the source of truth:
   `workspace/organization/contacts/pals.json`,
   `workspace/organization/contacts/PAL_CONTACTS.md`, and `official/pals/`.
8. AgentPal Core does not use keyword routing, domain route tables, or role route
   tables.
9. Org Pack recommendations are AI judgement inputs only.
10. Org Packs must not copy Pal bodies or modify the central roster.
11. No scanner, connector, runtime code, installer, daemon, marketplace, hub, API
    client, auto sync engine, or auto execution engine is introduced.

## External Project Negative Case

Given an external project with a thin AgentPal binding, applying this standard
must not create these default project-local paths:

- `.agentpal/pals/`
- `.agentpal/skills/`
- `.agentpal/workflows/`
- `.agentpal/runbooks/`
- `.agentpal/memory/`
- `.agentpal/reports/`
- `.agentpal/organization/`
- copied central contacts

Expected result: blocked or refused unless the user explicitly asks for
project-owned business documentation that is not central AgentPal Pal assets.

## Pass Condition

Pass when the required files exist, the boundary assertions are present, and no
R98-A file introduces executable runtime behavior or deterministic routing.
