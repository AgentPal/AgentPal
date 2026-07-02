# Central Contacts

This directory is the central AgentPal Pal contact source for discovery,
direct calls, owner judgement, collaboration, and routing boundary checks.

It contains Pal contacts only. Do not register ordinary Skills, tools, models,
plugins, MCP servers, runtime adapters, knowledge packs, persona packs, raw
repositories, or Team Packs as Pal contacts.

## Files

- `pals.json` is the machine-readable central roster.
- `PAL_CONTACTS.md` is the human-readable roster companion.
- `capability-cards/` contains Contact Capability Cards for registered Pals.
- `templates/pal-capability-card.template.json` is the copyable card template.
- `routing-veto.md` defines the boundary check applied after AI judgement.
- `capability-card-migration.md` explains how older contact entries are upgraded.

## Contact Capability Card Fields

Each capability card should include:

- `pal_id`: current Pal id from `pals.json`.
- `canonical_id`: stable identity used for contact and registry consistency.
- `display_name`: human Pal name, not a job title.
- `role_title`: job or responsibility title.
- `contact_label`: name plus role context for rosters and name conflicts.
- `summary`: short responsibility summary.
- `allowed_task_types`: task types this Pal may responsibly own.
- `forbidden_task_types`: task types this Pal must not own.
- `use_when`: positive judgement cues for appropriate use.
- `do_not_use_when`: negative boundary cues.
- `team_roles_allowed`: Team roles this Pal may hold.
- `team_roles_forbidden`: Team roles this Pal must not hold.
- `preferred_stages`: stages where this Pal is usually useful.
- `handoff_after`: conditions where the Pal should stop owning the work.
- `collaboration_modes`: allowed consult / delegate / handoff / review modes.
- `context_requirements`: minimum context needed before assignment.
- `default_output_contracts`: normal output shape or contract paths.
- `default_verification_style`: how the Pal checks or hands off verification.
- `risk_notes`: routing, evidence, and misuse risks.
- `source_files`: Pal files or standards used to ground the card.

## Routing Boundary

Mira and owner Pals still select candidate Pals by case-specific AI judgement.
Capability cards are checked after that candidate selection.

If the selected assignment conflicts with `forbidden_task_types`,
`team_roles_forbidden`, or `do_not_use_when`, apply `routing-veto.md` and
choose another Pal, use a Team, create a child step, ask the user, or mark the
route blocked.

Routing Veto is a boundary check. It is not keyword routing and must not become
a fixed route table such as `development = Atlas`, `quality = Quinn`, or
`business = Faye`.
