# Pal Team Creation Protocol

PalSmith creates Pal team plans, not files.

Status: v0.6 entry update. This remains a Markdown / JSON protocol and Runtime
Task Package pattern. It does not implement a backend, CLI, database, UI,
scanner, installer, automatic validator, or runtime team scheduler.


## Team Pack Discovery Before Creation

PalSmith must not start by redesigning a team when the user asks in ordinary language to form, build, assemble, find, or use a team. First require a Team Pack discovery summary from Mira / the current owner or perform a bounded discovery itself.

Discovery summary must state:

- candidate Team Packs checked;
- whether a fitting `selected_team` exists;
- why an existing Team Pack can or cannot cover the user goal;
- which gaps are `open_roles` rather than new Pals;
- whether a new durable Team Pack, repair, upgrade, or governance action is actually needed.

If a fitting Team Pack exists, PalSmith may only provide governance notes or open-role gap planning. It must not redesign the team from scratch. If no fitting Team Pack exists, PalSmith may create a team plan, but proposed new Pals remain under `optional_new_pal_proposals` and never enter `roster.members` without user confirmation.
## Creation Intake

Before proposing files, PalSmith collects or states assumptions for:

- team goal and stable task family;
- target users and user-facing entry point;
- project or workspace boundary;
- privacy and publication boundary;
- expected recurring task situations;
- desired outputs and definition of done;
- preferred team size or maximum size;
- existing Team Pack, if the user named one;
- existing Pals to reuse or avoid;
- missing Pal roles that may require new Pal creation;
- team name preference;
- allowed write path and confirmation state.

PalSmith should ask no more than three focused clarification questions when
these inputs are missing and cannot be safely assumed.

## Team Name And Id

Team names should be product-readable, stable, and specific to the team's
mission. They are team names, not Pal names.

`team_id` should be stable, lowercase, ASCII-safe, and derived from the team
mission or approved team name, for example `video-production-team` or
`after-sales-workflow-team`.

If a proposed `team_id` conflicts with an existing Team Pack, PalSmith must
stage a rename or suffix proposal before any write. Do not overwrite an existing
Team Pack.

## Member Selection

PalSmith selects member candidates through current contacts / registry and AI
judgement. This is not keyword routing.

For each candidate member, record:

- Pal id and contact label;
- proposed team role;
- responsibility in this team;
- explicit non-responsibility;
- required assets or missing assets;
- whether the Pal can participate with current boundaries;
- whether a new Pal or existing Pal upgrade is needed.

Faye may be recommended for business workflow discovery, interviews, FDE
process modeling, and translating complex business operations into team
workflows. Faye should not be assigned as the routine executor for ordinary
business tasks after the team workflow is established, unless the current task
is process redesign or workflow restructuring.

## New Pal Need

Create a new Pal only when no existing Pal can cover a necessary durable role
with acceptable boundary fit and asset readiness.

New Pal creation must use
`standards/pal-asset/pal-naming-and-import-conflict-protocol.md`:

- `display_name` is a human name;
- `role_title` is the job or responsibility;
- `contact_label` disambiguates rosters and contacts;
- `canonical_id` remains stable;
- `aliases`, `user_custom_name`, `original_name`, and `imported_from` preserve
  rename and import history;
- same-name conflicts are staged for user confirmation.

If the user asks for a role-only Pal such as `方案定制 Pal`, PalSmith treats it
as role intent, proposes a human display name, and stores the role as
`role_title`. PalSmith must not create role-title-only Pal display names.

## Required Team Pack Files

A Team Pack creation plan should include at least:

- `TEAM.md`;
- `team.json`;
- `roster.json`;
- team role cards or role notes;
- team workflow placeholder;
- team eval placeholder;
- team memory placeholder;
- team routing-card placeholder;
- team knowledge / skill / runbook indexes or placeholders when useful;
- creation report.

The plan should state which directories may start with README placeholders and
which files require user confirmation before writing.

## Pal Team Creation Task Package

The task package should include:

- team id and team name
- `TEAM.md` target
- `team.json` target
- `roster.json` target
- team purpose
- member Pal list
- team roles
- each Pal's responsibility and boundary
- owner Pal and verifier Pal
- collaboration rules
- Context Packet rules
- team Workflow placeholder
- team Eval placeholder
- team Memory placeholder
- team Routing Card placeholder
- Team Asset Preflight requirement
- Workflow Execution Contract placeholder
- member Pal Asset Preflight requirement
- proposed directory structure
- registry and contacts suggestions
- user confirmation questions

Team creation must follow the v0.6 no-code preflight protocols:

- workspace `core/team-asset-preflight-protocol.md`
- workspace `core/team-pal-asset-priority-protocol.md`
- workspace `core/pal-asset-preflight-protocol.md`

This protocol does not implement the Workflow state machine. It only ensures Team Pack planning has stable asset entry points and that member Pals must run their own asset preflight before assigned work.

After confirmation, the current Agent Runtime creates files and returns evidence.
