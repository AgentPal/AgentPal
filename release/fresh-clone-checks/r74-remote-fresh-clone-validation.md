# R74 Remote Fresh Clone Validation

Date: 2026-06-27

Purpose: record the remote GitHub fresh-clone validation after the R68-R73 reviewed local commits were pushed to `origin/master`.

## Remote Sync Status

- remote: `origin`
- sanitized clone source: `https://github.com/AgentPal/AgentPal.git`
- pushed branch: `master`
- pushed HEAD: `63e0070f63cd82423b2613d60c0d7385b262cc43`
- local `HEAD == origin/master` after push: true
- tag created in R74: no
- GitHub Release created in R74: no

## Fresh Clone

- clone source: `origin`
- clone location: remote fresh clone was created in a local temporary directory; the machine path is not recorded in public evidence
- clone HEAD: `63e0070f63cd82423b2613d60c0d7385b262cc43`
- clone `origin/master`: `63e0070f63cd82423b2613d60c0d7385b262cc43`
- tracked file count: 2729

## Required Paths

- required paths checked: 30
- missing required paths: 0

Required paths included root entry files, `official/pals/`, central contacts, central project-record templates, project-binding templates, standards, PalBench evidence folders, migration archive, and release fresh-clone checks.

## JSON Parse

- JSON files checked: 49
- JSON failures: 0
- fenced JSON failures: 0
- placeholder fenced JSON skipped: 1

Important JSON files checked included:

- `agentpal.json`
- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/aliases.json`
- `workspace/projects/projects.index.json`
- `workspace/projects/_template/project.json`
- `workspace/projects/_template/binding/external-binding.json`
- `templates/project-binding/generic-codex/.agentpal/project.json`
- `templates/project-binding/claude-code/settings.local.example.json`

## Central Roster

- `source_of_truth`: true
- `routing_policy`: `ai_judgement_only`
- `keyword_routing_allowed`: false
- registered Pals: 9
- official Pal directories in fresh clone: 9

## Thin Binding

- generic binding mode: `thin`
- generic binding contains `central_pal_contacts`: true
- generic binding contains `agentpal_project_record`: true
- forbidden project-binding template directories created: 0
- root `.agentpal/` in fresh clone: false
- unexpected real `workspace/projects/<project-id>` records: 0

Search hits for `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, and `.agentpal/evals` were classified as forbidden default directories, thin-binding boundary language, compatibility notes, or regression-test expectations. No active thick-binding behavior was found.

## No Keyword Routing

- `keyword_map`, `domain_map`, and `role_map` hits were classified as forbidden, boundary, template-check, or regression-test contexts.
- Pal-name route examples were classified as explicit `/pal` tests, negative examples, or non-binding examples.
- active keyword/domain/role routing bug: 0

## Private / Runtime Leak

- internal path hits: 0
- secret-like value hits: 0
- official Pal private memory/state/report non-README files: 0
- nested `.git` directories: 0
- runtime or generated archive artifacts in the tracked fresh clone: 0

## Result

Pass.

R74 remote fresh clone validation confirms that the pushed GitHub `master` state satisfies the R68-R73 directory boundary, central roster, thin binding, no-keyword-routing, JSON, and private/runtime leak gates.

This evidence does not claim that a release tag or GitHub Release exists.
