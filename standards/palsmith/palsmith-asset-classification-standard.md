# PalSmith Asset Classification Standard

Date: 2026-06-28

## Purpose

This standard defines how PalSmith v0.5 classifies user-provided content into AgentPal assets.

The goal is source-preserving asset placement. PalSmith must not compress all user material into a short summary, misplace Runtime / Agent Skills as Pal Skills, or copy central Pal assets into external projects.

## Classification Flow

1. Confirm the user approved the material for reading.
2. Assign a source id and sensitivity mark.
3. Preserve source anchors such as filename, section, heading, timestamp, or page.
4. Split the material into meaningful sections.
5. Classify each section into one primary asset type and optional secondary types.
6. Choose a central workspace target path by default.
7. Mark whether user confirmation is required.
8. Keep uncertain sections as `learning candidate`, `memory candidate`, or `review/unclassified`; do not drop them.
9. Produce a classification result record.

## Asset Types

| Asset type | Use when content is | Default target | Confirmation needed |
| --- | --- | --- | --- |
| identity | persona, voice, style, relationship boundary, role promise, non-responsibility | `identity/`, `PAL.md`, `core/output-contract.md` | yes for persona or voice changes |
| core protocol | cross-task rule that governs how the Pal works | `core/` | yes |
| knowledge | stable facts, rules, domain context, policy, glossary, cases | `knowledge/` | depends on sensitivity |
| research | source inventory, evidence matrix, web-research notes, coverage matrix | `research/` | yes if external research or citation risk exists |
| pal-skill | no-code recurring Pal capability or method | `skills/` | yes |
| agent-skill-ref | host Runtime Skill, plugin, MCP, browser, document, repo, or API capability reference | task package `runtime_skill_candidates` | yes; never write into Pal `skills/` |
| workflow | multi-step task sequence with stages or roles | `workflows/` | yes |
| runbook | stable repeated operation manual with concrete steps | `runbooks/` | yes |
| learning candidate | possible future improvement learned from work | `learning/` or owner Pal learning notes | yes before durable write |
| memory candidate | user/project/team fact that may help future continuity | approved memory area or central project record | strong yes if private |
| report | result, inspection, health, readiness, release, or evidence record | `reports/` or approved central report path | depends on privacy |
| eval | acceptance case, regression case, failure mode, Definition of Done | `evals/` | yes for new eval suites |
| example | public-safe input/output pair, scenario, anti-example, demo call | `examples/` | yes if derived from user material |
| org-pack candidate | reusable organization pattern, workflow, governance, capability profile, verification checklist | `templates/org-pack/`, `examples/org-packs/`, or approved org-pack area | yes |
| project business doc | active-project requirement, private customer fact, project plan, business-system note | active project docs or central project record | yes; not public by default |

## Judgement Table

| Question | Classification |
| --- | --- |
| Is it a fact, rule, policy, or domain concept? | `knowledge` |
| Is it a recurring Pal capability? | `pal-skill` |
| Is it a host Runtime or tool capability? | `agent-skill-ref` |
| Is it a sequence with stages or handoffs? | `workflow` |
| Is it a stable operation manual? | `runbook` |
| Is it a reusable output shell? | template, or `example` if filled |
| Is it a test, acceptance case, risky edge case, or failure mode? | `eval` |
| Does it define persona, tone, boundaries, or relationship style? | `identity` |
| Does it record current task outcome or evidence? | `report` |
| Does it describe an organization-level reusable pattern? | `org-pack candidate` |
| Does it describe a specific customer's project or business system? | `project business doc` |
| Is it private continuity information? | `memory candidate` |
| Is it a possible improvement but not yet approved? | `learning candidate` |

## Sensitivity Marks

Use one of:

- `public-safe`
- `team-local`
- `private`
- `internal-only`
- `excluded`
- `unknown`

`unknown` is not a public-safe state. Keep it out of public templates and examples until resolved.

## Targeting Rules

Default to central AgentPal workspace targets for Pal and organization assets.

External project writes are allowed only when the user explicitly requests a project-local business document or approved project file. Even then, do not write central Pal assets, organization memory, Pal Packs, contacts, registry, reusable Org Packs, or governance records into external project `.agentpal/` by default.

## Pal Skill vs Agent Skill

Classify as `pal-skill` only when the content is a no-code method the Pal uses as professional judgement.

Classify as `agent-skill-ref` when the content is an installed or potential Runtime capability, including:

- Codex Skill;
- Claude Code Skill;
- plugin;
- MCP tool;
- browser/document/repository capability;
- external API helper;
- command-line tool.

`agent-skill-ref` belongs in task package fields such as `runtime_skill_candidates`; it must not be copied into a Pal `skills/` directory.

## Classification Result Requirements

Each classification result must include:

- `content_summary`
- `recommended_asset_type`
- `target_path`
- `reason`
- `confidence`
- `requires_user_confirmation`
- `central_workspace_target`
- `external_project_write_allowed`
- `forbidden_targets`
- `notes`

`external_project_write_allowed` defaults to `false`.

## Prohibited Classification Outcomes

Do not:

- treat every user note as knowledge;
- turn every process into a Skill;
- hide workflows inside knowledge without steps;
- store private user facts in public examples;
- store credentials, tokens, secrets, cookies, API keys, or passwords;
- create keyword routes, `keyword_map`, `domain_map`, or `role_map`;
- classify Runtime tools as Pals;
- classify Agent Skills as Pal-owned Skills;
- copy central contacts or official Pals into external projects;
- auto-call Runtime, Skill, plugin, MCP, connector, or business system capabilities while classifying.

## Fallback

If a section cannot be safely classified, use:

```text
recommended_asset_type: learning candidate
target_path: review/unclassified
requires_user_confirmation: true
external_project_write_allowed: false
```

Preserve the source anchor and explain what decision is missing.
