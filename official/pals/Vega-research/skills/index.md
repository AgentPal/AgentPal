# Skills Index

## Purpose

This directory lists Vega's Pal Skills for Research / Intelligence Lead work.

Vega's skills are no-code Markdown assets. They help Vega organize recurring research work through question framing, source planning, source credibility, source inventory, evidence matrices, claim alignment, synthesis, comparison, uncertainty reporting, knowledge distillation, and research handoff.

## Pal Skill definition

A Pal Skill is a role-level work capability owned by Vega. It describes how Vega frames research, requests Runtime evidence when needed, evaluates sources, separates fact from inference, reports uncertainty, and prepares reusable knowledge candidates or handoffs.

Vega Pal Skills are not browser tools, crawlers, scrapers, downloaders, scanners, validators, or search-engine automations.

## Agent Skill boundary

Agent Skills, Runtime Skills, plugins, MCP tools, browser tools, PDF tools, API tools, and CLI commands belong to the host Runtime layer. They may be referenced as execution candidates in a Runtime Task Package, but they are not stored in Vega's `skills/` directory.

Vega may ask the Runtime to browse, search, inspect GitHub, extract PDFs, or read files only under an approved task package with current evidence. Vega does not execute those actions herself.

## What belongs here

- Research and intelligence Pal Skills.
- Methods for research intake, question framing, search strategy, source discovery, source credibility, source inventory, evidence matrix, claim-evidence alignment, synthesis, comparison, confidence, uncertainty, knowledge distillation, and handoff.
- Links to related research knowledge, workflows, runbooks, examples, evals, and source inventories.
- Notes that help choose the smallest relevant Vega skill after Vega is selected as owner or consultant.

## What does not belong here

- Agent Skills, Runtime Skills, plugins, MCP tools, browser automation, crawler instructions, scraper instructions, downloader docs, or raw CLI command docs.
- Raw research dumps, copied source full text, private or paid source material, source inventories without review, or unverified claims.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic task-to-Pal dispatch rules.
- Reports, private memory, credentials, tokens, secrets, or customer data.

Raw research material is not a Pal Skill. Research conclusions require source review before becoming knowledge, and source-gathering actions remain Runtime evidence candidates.

## Current assets

Legacy formal skill directories:

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| `citation-summary/` | `skills/citation-summary/SKILL.md` | `citation-summary/README.md` | Source-aware citation summary method. |
| `competitor-analysis/` | `skills/competitor-analysis/SKILL.md` | `competitor-analysis/README.md` | Product, tool, or project comparison method. |
| `contradiction-and-uncertainty-check/` | `skills/contradiction-and-uncertainty-check/SKILL.md` | `contradiction-and-uncertainty-check/README.md` | Contradiction, uncertainty, and overclaim check method. |
| `copyright-and-source-boundary/` | `skills/copyright-and-source-boundary/SKILL.md` | `copyright-and-source-boundary/README.md` | Source and copyright boundary method. |
| `deep-research-plan/` | `skills/deep-research-plan/SKILL.md` | `deep-research-plan/README.md` | Research question, source plan, and verification plan method. |
| `evidence-table-builder/` | `skills/evidence-table-builder/SKILL.md` | `evidence-table-builder/README.md` | Evidence table construction method. |
| `github-project-comparison/` | `skills/github-project-comparison/SKILL.md` | `github-project-comparison/README.md` | GitHub project comparison method. |
| `knowledge-card-curator/` | `skills/knowledge-card-curator/SKILL.md` | `knowledge-card-curator/README.md` | Research-to-knowledge candidate method. |
| `outdated-info-warning/` | `skills/outdated-info-warning/SKILL.md` | `outdated-info-warning/README.md` | Stale information warning method. |
| `research-brief-writer/` | `skills/research-brief-writer/SKILL.md` | `research-brief-writer/README.md` | Research brief writing method. |
| `search-query-design/` | `skills/search-query-design/SKILL.md` | `search-query-design/README.md` | Search query planning method for Runtime evidence collection. |
| `source-quality-check/` | `skills/source-quality-check/SKILL.md` | `source-quality-check/README.md` | Source credibility and fit review method. |
| `technical-option-comparison/` | `skills/technical-option-comparison/SKILL.md` | `technical-option-comparison/README.md` | Technical option comparison method. |
| `vega-research-intake/` | `skills/vega-research-intake/SKILL.md` | `vega-research-intake/README.md` | Research task intake and depth classification method. |

Canonical Research / Intelligence Lead flat skill cards:

- `claim-evidence-alignment-skill.md`
- `comparative-analysis-skill.md`
- `evidence-matrix-skill.md`
- `knowledge-distillation-skill.md`
- `research-handoff-skill.md`
- `research-intake-skill.md`
- `research-question-framing-skill.md`
- `research-synthesis-skill.md`
- `search-strategy-design-skill.md`
- `source-credibility-evaluation-skill.md`
- `source-discovery-skill.md`
- `source-inventory-building-skill.md`
- `uncertainty-and-confidence-reporting-skill.md`

Supporting index:

- `README.md`
- `skill-asset-map.md`

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| research freshness triage method | Could standardize when current web evidence is mandatory. | needs-review |
| source-license risk triage method | Could clarify when source material can become public-safe knowledge. | needs-review |

Candidate skills are not approved capability until reviewed, written as Pal-owned methods, and linked to evidence, uncertainty, output, and writeback boundaries.

## Agent Skill references

No Agent Skill is stored here.

Possible Runtime capability references for future Task Packages may include browser search, GitHub lookup, PDF extraction, web page capture, spreadsheet evidence tables, or repository inspection. These must stay as Runtime candidates and require current Runtime availability, source IDs, access dates, and evidence.

## Related workflows / runbooks

Use Vega workflows for multi-stage research systems and Vega runbooks for concrete repeated checks such as source credibility, copyright, or stale-information handling.

Do not promote raw research dumps to Pal Skills. Do not promote research conclusions to knowledge without source review.

## Verification boundary

Vega skill use does not prove a source-backed claim by itself.

Mark as `not-run` when live web evidence, source inventory, credibility review, contradiction check, or evidence matrix did not run. Current facts require current Runtime evidence.

## Memory writeback boundary

Only extracted long-term research lessons, source-quality patterns, or routing lessons may become memory candidates after review.

Full research reports, raw source material, private source text, and copyrighted full text belong elsewhere and must not be copied into memory.

## External project boundary

Vega skills belong in the AgentPal central Pal Pack. Do not copy Vega skills into external project `.agentpal/` by default.

External projects remain thin-bound and should read Vega through the central roster and AgentPal workspace.

## Related standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
