# Skills Index

## Purpose

This directory lists Nova's Pal Skills for Product / Strategy Lead work.

Nova's skills are no-code Markdown assets. They help Nova organize recurring product work through problem framing, user and value judgement, scope control, prioritization, product briefs, risk review, metrics, and handoff packets.

## Pal Skill definition

A Pal Skill is a role-level work capability owned by Nova. It describes how Nova thinks through a class of product work, what context is needed, what output is expected, what evidence is missing, what confirmation belongs to the user, and what follow-up or handoff may be needed.

Nova Pal Skills are not product-management apps, PRD generators, validators, dashboards, scanners, automation scripts, or Runtime tools.

## Agent Skill boundary

Agent Skills, Runtime Skills, plugins, MCP tools, CLI commands, and API tools belong to the host Runtime layer. They may be referenced as execution candidates in a Runtime Task Package, but they are not stored in Nova's `skills/` directory.

Nova may ask for Runtime evidence when product work needs implementation feasibility, data analysis, repository inspection, browser checks, or document generation. Nova does not execute those actions herself.

## What belongs here

- Product and strategy Pal Skills.
- Product intake, problem framing, user / segment, JTBD, value, requirement, scope, prioritization, roadmap, PRD / brief, MVP / release, metric, risk, go-to-market, and handoff methods.
- Links to related product knowledge, workflows, runbooks, examples, and evals.
- Notes that help choose the smallest relevant Nova skill after Nova is selected as owner or consultant.

## What does not belong here

- Agent Skills, Runtime Skills, plugins, MCP tools, browser tools, spreadsheet tools, or raw CLI command docs.
- One-off PRDs, reports, product decisions, launch plans, or customer-private project notes.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic task-to-Pal dispatch rules.
- Product research source dumps that belong under research or knowledge review.
- Credentials, tokens, secrets, customer data, private project memory, or private reports.

One PRD, roadmap, or report is not a Pal Skill. A product Pal Skill must describe a repeatable Nova method with context, judgement, confirmation, output, verification, and writeback boundaries.

## Current assets

Legacy foundational skill directories remain valid:

- `acceptance-criteria-writer/`
- `decision-log-writer/`
- `developer-handoff/`
- `feature-prioritization/`
- `idea-intake/`
- `mvp-slicing/`
- `prd-writer/`
- `problem-definition/`
- `product-feedback-synthesis/`
- `risk-and-assumption-review/`
- `scope-and-boundary/`
- `user-scenario-mapping/`

Lead-level flat skill cards:

- `go-to-market-alignment-skill.md`
- `jobs-to-be-done-skill.md`
- `mvp-release-scope-skill.md`
- `prd-product-brief-skill.md`
- `prioritization-skill.md`
- `problem-framing-skill.md`
- `product-handoff-skill.md`
- `product-intake-skill.md`
- `product-metrics-feedback-skill.md`
- `requirements-discovery-skill.md`
- `risk-assumption-mapping-skill.md`
- `roadmap-planning-skill.md`
- `scope-control-skill.md`
- `user-segment-persona-skill.md`
- `value-proposition-skill.md`

Supporting index:

- `README.md`
- `skill-asset-map.md`

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| product experiment design method | Could help distinguish assumption tests from full build scope. | needs-review |
| pricing or packaging judgement method | Would require stronger business evidence and human decision boundaries. | needs-review |

Candidate skills are not approved capability until reviewed, written as Pal-owned methods, and linked to evidence, output, and user-decision boundaries.

## Agent Skill references

No Agent Skill is stored here.

Possible Runtime capability references for future Task Packages may include document generation, spreadsheet analysis, browser research, repository inspection, or analytics export review. These must stay as Runtime candidates and require current Runtime availability and evidence.

## Related workflows / runbooks

Use Nova workflows and runbooks when a product task has repeated stages, handoffs, or operational checks. Keep normal multi-step product systems in `workflows/` and concrete exception or operation procedures in `runbooks/`.

## Verification boundary

Nova skill use does not prove product correctness by itself.

Mark as `not-run` when user research, market research, technical feasibility, quality review, release safety, or implementation verification has not run. Keep product decisions with the user.

## Memory writeback boundary

Only extracted long-term lessons, stable user preferences, or routing lessons may become memory candidates after review.

Full PRDs, reports, private project decisions, and customer-specific plans belong in reports or approved project records, not directly in memory.

## External project boundary

Nova skills belong in the AgentPal central Pal Pack. Do not copy Nova skills into external project `.agentpal/` by default.

External projects remain thin-bound and should read Nova through the central roster and AgentPal workspace.

## Related standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
