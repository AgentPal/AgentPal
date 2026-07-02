# Create AI Team From Goal Task Package

task_name: Create AI Team From Goal
owner_pal: PalSmith
executing_runtime: current Agent Runtime
status: copyable template

## User Fill Area

```text
Team goal:
Target users:
Business goal:
Main task types:
Recurring work situations:
Existing Team Pack to use or extend:
Preferred team size or maximum:
Need Mira as main entry: yes / no / unsure
Existing Pals to reuse:
Pals or domains to avoid:
Need Faye for business workflow discovery: yes / no / unsure
Existing materials:
Expected user-facing entry Pal:
Sensitive or private materials:
Target write path:
Public, team-local, or private use:
May the runtime write files after showing the path list: yes / no
```

## Goal

Create a small, bounded AI team design and optional draft Pal assets from a plain-language user goal. Team members are candidate capability holders. Mira or another explicitly selected leader remains the Conductor according to the current contacts, registry, and user-confirmed team design.

PalSmith team creation is a governance and design workflow. It must preserve
Team Pack selection, no fake verifier, and no simulated-as-real boundaries.

## Required Inputs

- user goal and target audience;
- business goal and main task types;
- recurring scenarios and success criteria;
- existing Team Pack name or path if the user wants to use or extend one;
- preferred team size;
- whether Mira should remain the main entry for ordinary use;
- candidate existing Pals to reuse or avoid;
- whether Faye is needed for business process discovery or workflow redesign;
- existing user materials;
- approved source materials;
- target write path;
- privacy and publication boundary;
- explicit confirmation before writes.

## Allowed Reads

- PalSmith AI team design and team creation protocols;
- v0.6 Team Pack standard and templates;
- v0.6 Team Asset Preflight, Pal Asset Preflight, and Team / Pal priority protocols;
- Workflow Execution Contract and Closure Gate protocols;
- Pal naming and same-name import conflict protocol;
- current contacts and registry for existing Pal candidates;
- approved reference Pal Packs;
- approved user materials only.

## Allowed Writes

- approved team design directory;
- approved new member Pal directories when explicitly confirmed;
- team-level README, context rules, examples, evals, and health report;
- creation report inside the approved target directory.

## Forbidden Writes

- `contacts/`;
- `registry/`;
- unrelated Pal directories;
- runtime source code, scripts, package manifests, scanners, validators, installers, or UI files;
- private memory, credentials, or unapproved material.

## PalSmith Steps

1. Restate the team goal, target users, privacy boundary, and allowed write scope.
2. Ask focused clarification questions only for missing role, material, or boundary information.
3. Check whether an existing Team Pack can be used or extended.
4. Identify capability domains needed for the goal.
5. Check current contacts and registry for reusable Pal candidates.
6. Build the roster open-role-first: `roster.members` may reference only
   existing Pal ids from current contacts / official Pals or user-confirmed
   Pals.
7. Put missing seats, responsibilities, capabilities, and workflow jobs into
   `open_roles`.
8. Default `optional_new_pal_proposals` to `[]`. Add at most one proposal only
   when the user explicitly asks for new Pals or a durable missing role cannot
   remain an open role. Proposals are not installed, not roster members, and not
   participants.
9. Propose a small team with existing members, open roles, each role's job,
   non-job, evidence needs, and collaboration boundary.
10. Identify the Main Pal / leader / Conductor candidate and explain why it fits this case.
11. Define whether Faye is needed for process discovery or should exit before routine execution.
12. Define context-sharing rules, escalation rules, and handoff examples without permanent dispatch rules.
13. Define typical team tasks and user-facing team usage instructions.
14. Draft Team Asset Preflight, Workflow Execution Contract, member Pal Asset
    Preflight, and Closure Gate requirements.
15. Draft team asset structure and member Pal asset structure, including health-check expectations.
16. Record verifier policy: no fake verifier output; named verifiers must
    review, be skipped with reason, be blocked, or be replanned.
17. Review runtime evidence after execution and produce team health status,
    repair package when needed, and first usage examples without presenting
    simulated or fixture-only work as real execution.

## Prohibitions

- Do not create fixed collaborator rules or permanent domain routes.
- Do not claim Deep Conductor or multi-agent execution is active in the current release.
- Do not make team members automatic route targets.
- Do not register Pals in contacts or registry inside this package.
- Do not create role-title-only Pal display names.
- Do not assign Faye to routine execution after team workflow handoff unless the current task is workflow redesign.
- Do not create runtime code, scanners, validators, importers, exporters, installers, or UI.
- Do not expose private user material in public examples.

## Expected Evidence

- approved target path;
- existing Team Pack check result;
- existing member references, open roles, and candidate capability domains;
- optional new Pal proposal result, or `[]` when no user-confirmed need exists;
- files created, changed, skipped, and not found;
- `pal.json` parse result for every created member Pal;
- current contacts / registry read evidence when existing Pal reuse is considered;
- Team Asset Preflight, Workflow Execution Contract, member Pal Asset Preflight,
  and Closure Gate placeholders;
- context-sharing and privacy boundary report;
- not-run checks;
- team health-check result;
- repair package when health status is not clean.

## Acceptance Criteria

- The team has a clear purpose, success criteria, and Main Pal / leader / Conductor boundary.
- Every roster member is an existing or user-confirmed Pal with a job, non-job,
  source evidence needs, and first usage example.
- Missing capabilities stay in `open_roles` unless the user explicitly confirms
  new Pal creation.
- Existing Pals are reused only when current evidence supports the choice.
- Optional new Pal proposals, if any, are separate from roster members and use
  human display names with separate role titles.
- Faye is limited to process discovery / redesign when relevant and has an exit condition.
- No member is presented as a permanent route target.
- Context-sharing rules protect private and internal-only material.
- The team includes evals for collaboration, overlap, missing owner, and unsafe private leakage.
- The result is labeled `idea`, `draft`, `testing`, `stable`, `publish-ready`, or `not ready` with evidence.
