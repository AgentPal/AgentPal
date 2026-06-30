# Existing Pal Composite Upgrade Protocol

Status: R196 no-code PalSmith protocol.

This protocol governs requests that target an existing Pal and ask to change the
Pal in a way that may affect identity, voice, personality, thinking model, role
duties, domain knowledge, workflows, Skill or Agent usage, memory behavior,
collaboration, discovery, Marketplace metadata, or publication boundary.

The protocol is based on AI judgement, not keyword routing. The dimensions above
are review dimensions, not deterministic triggers. PalSmith must inspect the
target Pal, the user's intent, the likely write surface, and the risk before
classifying the request.

## Definition

Existing Pal Composite Distillation Upgrade means upgrading an already existing
Pal by distilling new sources, roles, voices, thinking patterns, knowledge,
workflows, capability mappings, memory rules, or collaboration policies into the
Pal's asset package.

It differs from new Pal creation because the target Pal already has identity,
scope, files, boundaries, evals, and collaboration relationships. The upgrade
must preserve existing Pal integrity while adding or revising selected assets.

It differs from Simple Existing Pal Edit because the change is not merely a
typo, path correction, Markdown cleanup, JSON syntax fix, or obviously stale
single sentence. It can change how the Pal thinks, speaks, acts, collaborates,
remembers, or is published.

## AI Judgement Flow

PalSmith must not classify by matching words such as `voice`, `thinking`,
`Skill`, `contacts`, or their Chinese equivalents. Those words may signal
possible dimensions, but the route is decided by semantic judgement.

Required flow:

1. Identify the target Pal and whether it is official, user custom, draft, or
   unknown.
2. Read the smallest necessary target Pal inventory: root files, `pal.json`,
   identity files, relevant knowledge, workflows, skills, runtime policy,
   memory, collaboration, and eval indexes when present.
3. Judge the user's real intent and likely impact.
4. Decide whether the request is Simple Existing Pal Edit, Existing Pal
   Composite Distillation Upgrade, role/duty upgrade, knowledge/capability
   upgrade, workflow upgrade, memory/learning upgrade, authorization flow, or
   blocked/unclear.
5. Explain the judgement reason and uncertainty.
6. For high-impact changes, output an upgrade plan before any file write.
7. Ask the smallest required confirmation question before controlled writes.

## Direct Write Prohibition

PalSmith must not directly edit `PAL.md`, identity files, voice files,
knowledge, workflows, skills, runtime policy, memory, contacts, registry, or
Marketplace metadata when the request may alter Pal-defining behavior.

Direct minimal edits are allowed only when AI judgement proves the change is a
Simple Existing Pal Edit and the write surface is narrow, such as a typo,
broken link, Markdown heading, stale one-line note, or JSON syntax repair.

## Required Upgrade Plan

Before controlled writes, PalSmith must produce an upgrade plan containing:

- upgrade mode judgement;
- target Pal and current Pal inventory;
- user request and assumptions;
- source type and source boundary;
- cognitive distillation plan;
- voice and personality distillation plan;
- role-duty installation plan;
- domain knowledge installation plan;
- Skill, plugin, and Agent capability map;
- workflow impact plan;
- memory impact plan;
- collaboration, discovery, contacts, and Marketplace boundary impact plan;
- target file map;
- write order;
- eval plan;
- allowed write paths;
- blocked write paths;
- required confirmation question.

## Impact Ranges

Use AI judgement to decide which ranges apply. Do not require every upgrade to
touch every range.

| Range | Typical target assets | Required care |
| --- | --- | --- |
| identity | `PAL.md`, `identity/role.md`, `identity/persona.md` | preserve existing Pal identity and non-responsibilities |
| voice | `identity/voice.md`, `identity/tone.md`, `identity/speech-patterns.md` | extract transferable rules, not copied source lines |
| thinking | `knowledge/mental-models.md`, `knowledge/decision-heuristics.md` | use source boundary and uncertainty notes |
| role | `identity/role.md`, `README.md`, workflows | update duties and acceptance criteria |
| knowledge | `knowledge/`, `research/`, source notes | preserve source scope and confidence |
| skills | `skills/skill-map.md`, Pal-owned Skills | separate Pal-owned methods from host Skills |
| runtime | `runtime/agent-usage-policy.md` or task package notes | do not claim host capability without evidence |
| workflows | `workflows/` | add workflow evals when behavior changes |
| memory | `memory/`, learning notes | keep private memory out of public assets |
| contacts | `contacts/`, central contacts proposals | do not mutate central contacts without separate approval |
| discovery | user custom discovery policy | discovery does not imply delegation or contacts registration |
| marketplace | `marketplace/` metadata drafts | metadata planning is not Marketplace backend implementation |
| evals | `evals/` | include role, voice, thinking, boundary, and runtime claim tests as needed |

## Source Boundary

For public figures, literary characters, brands, books, and living people,
PalSmith must describe the result as public-source-inspired, style-inspired, or
authorized-material-based. It must not claim the Pal is the real person, speaks
for a rights holder, copies original lines, or uses private material without
authorization.

For private company material or user documents, default to private or team-local
assets. Public examples, official Pal updates, and Marketplace metadata require
separate authorization and review.

## Confirmation And Writeback

The upgrade plan must ask for confirmation before any Runtime write. The
confirmation must name the target Pal, allowed write paths, blocked write paths,
and whether central contacts, discovery, Marketplace, or official status are out
of scope.

After any approved write, PalSmith must require:

- file list evidence;
- JSON parse evidence when JSON changed;
- target file map coverage;
- eval evidence with `pass`, `partial`, `missing`, `not-run`, or `blocked`;
- no-code boundary scan;
- source and impersonation boundary scan;
- report summarizing done, not-run, risk, and next step.

## Relationship To Other Protocols

Read this protocol together with
`core/composite-pal-distillation-protocol.md` for source, thinking, voice,
knowledge, capability, memory, collaboration, eval, and Marketplace planning.

For user custom Pal discovery, limited delegation, contacts registration, or
revocation, also use
`core/user-custom-pal-discovery-authorization-protocol.md`.

For draft-to-user-custom installation, use
`core/custom-pal-installation-protocol.md`.
