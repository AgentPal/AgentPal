# Pal Asset And Org Pack Relationship

Date: 2026-06-28

## Purpose

This guide explains how Pal Asset standards, Org Packs, PalSmith, and Pal Asset
Resolver fit together in AgentPal v0.5.

## Pal Asset

Pal Asset is the asset system for one Pal.

A Pal is a long-term working companion in the AgentPal organization, not a role
prompt. Its assets can include identity, work protocols, knowledge, Pal Skills,
workflows, runbooks, learning, memory, state, reports, evals, examples, and root
entry files.

Primary references:

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-root-entry-standard.md`
- `standards/pal-asset/pal-loading-order-standard.md`

## Org Pack

An Org Pack is a reusable no-code organization asset package. It can describe an
AI organization, team practice, governance pattern, workflow family, capability
policy, verification checklist, or public-safe delivery pattern.

Org Packs may reference or recommend:

- Pals to consider
- Pal Skill candidates
- workflow candidates
- Capability Inventory records
- governance checkpoints
- verification checklists

These recommendations are AI judgement inputs only. They are not routes,
assignments, central roster edits, or automatic dispatch rules.

Primary references:

- `standards/org-pack/org-pack-standard.md`
- `templates/org-pack/base-org-pack/`
- `examples/org-packs/base-agentpal-org-pack/`

## Relationship

| Area | Pal Asset | Org Pack |
| --- | --- | --- |
| Scope | One Pal and its role assets. | A reusable organization or work-system package. |
| Owner | The Pal Pack or approved central Pal asset area. | Approved template, example, or organization package area. |
| Can recommend Pals | No, a Pal owns itself and may collaborate by judgement. | Yes, but only as AI judgement inputs. |
| Can copy Pal body | Owns the Pal body. | Must not copy Pal bodies. |
| Can modify central roster | No, except through a separate governed registration task. | No. |
| Default external project write | No central Pal assets by default. | No Org Pack assets by default. |

## Pal Asset Resolver

Pal Asset Resolver is a logical no-code judgement standard. It can read Org Pack
recommendations as one input, then form candidate Pal assets, Agent Skill refs,
Context Access Lists, task package recommendations, and verification plans.

It must not:

- execute tasks
- call external APIs
- scan systems
- install tools
- route by keyword
- modify central contacts
- copy Pal or Org Pack assets into external projects by default

Primary reference:

- `standards/pal-asset/pal-asset-resolver-standard.md`

## Thin Binding

External projects remain business sites. They should stay thin-bound by default
through files such as:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- protected root instruction blocks
- optional host-runtime local settings

Pal bodies, central contacts, central memory, Pal workflows, Org Pack assets,
Capability Inventory records, and governance records live in the AgentPal
Workspace or approved central records by default.

## Safe Integration Rule

Use Org Pack recommendations to help judgement. Use Pal Asset standards to load
and verify one Pal's assets. Use PalSmith standards to create, classify, or
upgrade assets. Use the host Runtime only when a bounded task package requires
real file or system actions and current evidence is available.
