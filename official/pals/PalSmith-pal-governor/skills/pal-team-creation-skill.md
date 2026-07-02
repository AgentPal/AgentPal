# Pal Team Creation Skill

## Purpose

Turn a user goal into a small, understandable Pal team with clear ownership, verification, shared knowledge, and creation boundaries.

## When To Use

Use when the user wants an AI team, a group of Pals for a domain, a blueprint turned into a team, or a multi-Pal workgroup design.

## Inputs

- team goal and business or creative scenario
- desired team size or complexity
- approved blueprint or reference team
- user materials and privacy constraints
- whether any member should become a global contact

## Required Context

Read `pal-team-design-knowledge.md`, `ai-team-builder-protocol.md`, `pal-team-creation-protocol.md`, team creation template, and relevant blueprint if one is named.

## Process

1. Clarify the team outcome and first useful workflow.
2. Propose Team + Roles by default, not new Pals.
3. Fill `roster.members` only with existing registered Pal ids or
   user-confirmed Pals.
4. Put missing capabilities and seats into `open_roles`.
5. Assign owner, verifier, and consultants from existing Pals when evidence
   supports the fit.
6. Define responsibilities and non-responsibilities for each existing member
   and open role.
7. Keep `optional_new_pal_proposals` as `[]` unless the user explicitly asks
   for a new Pal or one durable missing role cannot remain an open role.
8. If a proposal is needed, propose at most one, keep it outside
   `roster.members`, and mark it not installed / not participating until user
   confirmation.
9. Report naming checks as current-output evidence:
   `generated_display_name_violations: []`. Do not list hypothetical invalid
   display names unless the current answer actually generated them.
   When `optional_new_pal_proposals` is `[]`, do not list candidate human names,
   future Pal ideas, or example proposal tables anywhere else.
   When explaining naming rules without creating a Pal, use placeholders such
   as `<HumanName>` and `<Role Title>`, not concrete human-name examples.
10. Define shared knowledge, shared workflows, Context Packet rules, eval plan, and quality gate.
11. Identify research and user-material gaps for the team domain.
12. Ask whether to create files or keep the output as a design.
13. Prepare a Team Creation Runtime Task Package only after confirmation.

## Output

- team design
- existing member references
- open roles
- optional new Pal proposals, default `[]`
- governance plan
- shared knowledge/workflow/eval plan
- Context Packet rules
- Team Creation Runtime Task Package

## Quality Bar

The team should be small enough to understand, have one owner and one verifier, and avoid all-global-contact or all-memory-access shortcuts.

## User Confirmation Points

- accepted team size
- selected member Pals
- team-local/global contact choices
- read scope for user materials
- write paths for team assets

## No-Code Boundary

PalSmith plans and reviews. Runtime creates team files only after confirmation.

## Common Mistakes

- creating too many Pals from one sentence
- putting unconfirmed new Pal ideas into `roster.members`
- treating a role, job, responsibility, or capability as a Pal identity
- making every Pal globally contactable
- lacking a verifier
- skipping shared workflow and Context Packet rules
- treating a blueprint as already installed

## Example

For a cross-border commerce team, PalSmith first references any existing Pals
that fit, places missing commerce roles in `open_roles`, and keeps
`optional_new_pal_proposals` empty unless the user explicitly confirms a new
Pal creation need.
