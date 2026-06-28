# Pal Asset Standard

Date: 2026-06-28
Standard id: `agentpal-pal-asset-standard.v0.5`

## Purpose

The Pal Asset Standard defines how a Pal becomes a stable long-term working
partner in an AgentPal organization.

A Pal is not a role prompt. A Pal is a long-term position and working companion
with identity, responsibilities, knowledge, role-level skills, workflows,
runbooks, memory, state, reports, examples, verification rules, collaboration
boundaries, and runtime-facing task packaging habits.

## Scope

This standard applies to Pal Packs and Pal-owned assets in the AgentPal
Workspace. It is compatible with the existing official Pal directory shape and
clarifies semantics, indexes, and future upgrade rules without overturning the
current Pal architecture.

This standard does not upgrade any specific Pal by itself and does not modify
the central roster.

## Definitions

### Pal

A Pal is a long-term working companion in the AgentPal organization. It has a
position, ownership boundary, collaboration style, professional assets, and
evidence-aware working method.

### Pal Asset

A Pal Asset is a structured content item that makes a Pal stable, repeatable,
auditable, and useful across projects. Pal Assets include root entry files and
the asset directories listed in this standard.

### Pal Skill

A Pal Skill is a role-level comprehensive work capability. It describes how a
Pal organizes a class of work through goals, context selection, knowledge
references, workflow references, runtime Agent Skill references, collaboration,
approval, output contracts, verification, and memory writeback.

### Agent Skill

An Agent Skill is a runtime tool-level execution capability. It helps a host
runtime perform concrete actions such as reading a file type, running a browser
test, generating a document, calling a CLI, or operating an external tool.

Pal `skills/` defaults to Pal Skills. Runtime-installed Agent Skills may be
referenced from Pal Skills, but they are not copied into Pal `skills/` as if
they were Pal-owned role capabilities.

## Four-Layer Model

| Layer | Purpose | Typical assets |
| --- | --- | --- |
| Identity and boundary | Defines who the Pal is, what it owns, how it collaborates, and what it must refuse or escalate. | `README.md`, `PAL.md`, `pal.json`, `identity/` |
| Work protocol | Defines how the Pal receives work, slices context, prepares task packages, verifies output, reports, and learns. | `AGENTS.md`, `SKILL.md`, `core/` |
| Professional capability | Stores stable knowledge, role-level skills, workflows, runbooks, research, and examples. | `knowledge/`, `research/`, `skills/`, `workflows/`, `runbooks/`, `examples/` |
| Runtime sedimentation | Stores state, memory candidates or memories, reports, evals, and learning records after real work. | `state/`, `learning/`, `memory/`, `reports/`, `evals/` |

## Standard Asset Directories

A standard Pal Pack may use these directories:

- `identity/`
- `core/`
- `knowledge/`
- `research/`
- `skills/`
- `workflows/`
- `runbooks/`
- `learning/`
- `memory/`
- `state/`
- `reports/`
- `evals/`
- `examples/`

Directory absence is not automatically invalid for older Pals. New or upgraded
Pals should add clear indexes or README files as assets mature.

## Root Entry Files

A standard Pal Pack should expose these root entries:

- `README.md`: human-facing overview.
- `PAL.md`: identity, ownership, collaboration, and boundary statement.
- `pal.json`: machine-readable manifest.
- `AGENTS.md`: runtime-facing instructions for working as this Pal Pack.
- `SKILL.md`: Pal Pack compatible entry, not a single runtime Agent Skill.
- `asset-manifest.json`: optional asset index for upgraded or generated Pals.

## Relationship To Org Pack

An Org Pack and a Pal Pack are related but not interchangeable.

| Org Pack | Pal Pack |
| --- | --- |
| Describes a reusable organization, team, workflow system, governance pattern, or business practice. | Describes one long-term Pal and its assets. |
| May recommend Pals, skills, workflows, and verification checklists. | Owns one Pal identity, professional assets, and output contracts. |
| Recommendations are AI judgement inputs only. | Pal participation still depends on central roster discovery and AI owner judgement. |
| Must not copy Pal bodies or modify the central roster. | May become discoverable only through a separate governed registration process. |

Org Packs may recommend Pal perspectives, Pal Skill candidates, or workflow
candidates. They must not copy a Pal body, fork the central contacts into an
external project, or create keyword routes.

## Central Roster

The source of truth for discoverable Pals is the central roster:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `official/pals/`

All projects should read Pal availability through the central roster. A Pal is
a unified organization asset, not a per-project local copy.

## Thin Binding

An external project is a business site, not an AgentPal asset warehouse.

External project binding may use minimal files such as:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- protected root instruction blocks
- optional host-runtime local settings

External projects must not receive copied Pal bodies, central contacts, central
memory, central workflows, central runbooks, central reports, or central
governance assets by default.

## Routing Boundary

AgentPal Core must not use keyword routing, task-domain route tables, or fixed
semantic dispatch rules. Pal selection is case-by-case AI judgement using the
current request, expected deliverable, risk, current roster, available assets,
runtime evidence, and user instruction.

Org Pack recommendations, Pal capability notes, examples, and previous routing
records are judgement inputs only. They are not routes.

## Forbidden Behaviors

Pal Asset Standards and Pal Packs must not:

- Treat a Pal as only a role prompt.
- Treat a Pal Skill as a runtime Agent Skill.
- Treat a runtime Agent Skill as a Pal Skill.
- Copy central Pal assets into external projects by default.
- Copy, replace, or modify the central roster through an Org Pack.
- Route by keyword, domain map, role map, or deterministic task-to-Pal table.
- Claim runtime execution without current host-runtime evidence.
- Add a CLI, Web App, Desktop App, scanner, validator, daemon, database,
  connector, API client, marketplace, hub, installer, auto sync engine, or auto
  execution engine as part of this standard.
