# Skills Index

## Purpose

This directory lists Harper's Pal Skills for Writing / Content Craft Lead work.

Harper's skills are no-code Markdown assets. They help Harper organize recurring writing work through audience framing, style and voice control, structure, drafting, rewriting, editing, content preservation, claim safety, and content quality self-review.

## Pal Skill definition

A Pal Skill is a role-level work capability owned by Harper. It describes how Harper handles a recurring writing class, what context is needed, how user meaning is preserved, what claims need evidence, what publication decisions remain with the user, and what output or handoff is expected.

Harper Pal Skills are not one-off prompts, prompt libraries, publishing bots, marketing automation systems, SEO crawlers, validators, or Runtime tools.

## Agent Skill boundary

Agent Skills, Runtime Skills, plugins, MCP tools, document tools, browser tools, API tools, and CLI commands belong to the host Runtime layer. They may be referenced as execution candidates in a Runtime Task Package, but they are not stored in Harper's `skills/` directory.

Harper may request Runtime evidence when writing work needs document conversion, source retrieval, fact checking, publication preview, or repository edits. Harper does not execute those actions herself.

## What belongs here

- Writing and content craft Pal Skills.
- Writing intake, audience and goal, voice and style, long-form structure, short-form social content, copywriting, narrative, editing, plain language, brand voice, content preservation, claim safety, and self-review methods.
- Links to related writing knowledge, workflows, runbooks, examples, and evals.
- Notes that help choose the smallest relevant Harper skill after Harper is selected as owner or consultant.

## What does not belong here

- Agent Skills, Runtime Skills, plugins, MCP tools, publishing systems, social scheduling tools, SEO scanners, browser automation, or raw CLI command docs.
- Single prompts, one-off drafts, long reports, private user memory, source dumps, or customer-private writing samples.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic task-to-Pal dispatch rules.
- Credentials, tokens, secrets, private customer data, private reports, or private project memory.

A single prompt is not a complete Pal Skill. A Harper Pal Skill must describe a repeatable writing method with context, preservation, claim boundary, output, verification, and writeback boundaries.

## Current assets

Legacy foundational skill directories remain valid:

- `announcement-writer/`
- `audience-and-tone-analysis/`
- `communication-risk-review/`
- `draft-writer/`
- `email-and-message-writer/`
- `humanizing-rewrite/`
- `outline-writer/`
- `rewrite-and-edit/`
- `source-grounded-writing/`
- `style-guide-applier/`
- `translation-localization-brief/`
- `writing-task-intake/`

Lead-level flat skill cards:

- `audience-and-goal-framing-skill.md`
- `brand-voice-consistency-skill.md`
- `content-preservation-in-writing-skill.md`
- `content-quality-self-review-skill.md`
- `copywriting-and-persuasion-skill.md`
- `editing-and-rewriting-skill.md`
- `fact-boundary-and-claim-safety-skill.md`
- `long-form-structure-skill.md`
- `narrative-storytelling-skill.md`
- `plain-language-clarity-skill.md`
- `short-form-social-content-skill.md`
- `style-and-voice-control-skill.md`
- `writing-intake-skill.md`

Supporting index:

- `README.md`
- `skill-asset-map.md`

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| publication-readiness wording review method | Could clarify final user approval and risk boundaries before publishing. | needs-review |
| multi-source rewrite preservation method | Could strengthen how Harper preserves meaning across several source notes. | needs-review |

Candidate skills are not approved capability until reviewed, written as Pal-owned methods, and linked to evidence, preservation, output, and user-confirmation boundaries.

## Agent Skill references

No Agent Skill is stored here.

Possible Runtime capability references for future Task Packages may include document conversion, browser preview, source retrieval, spelling/grammar tooling, repository edits, or publishing-system checks. These must stay as Runtime candidates and require current Runtime availability and evidence.

## Related workflows / runbooks

Use Harper workflows for multi-stage writing systems and Harper runbooks for concrete repeated checks such as claim-safety review, publication caution, or source-preservation handling.

Do not treat a single prompt, one-off rewrite, or marketing draft as a Pal Skill.

## Verification boundary

Harper skill use does not prove factual accuracy, publication safety, legal approval, product evidence, or source quality by itself.

Mark as `not-run` when fact checking, source review, product review, quality gate, privacy review, or publication approval did not run. Keep publication decisions with the user.

## Memory writeback boundary

Only extracted long-term writing preferences, approved voice guidelines, stable style lessons, or routing lessons may become memory candidates after review.

Full drafts, private writing samples, private reports, and customer-specific materials must not be copied into memory by default.

## External project boundary

Harper skills belong in the AgentPal central Pal Pack. Do not copy Harper skills into external project `.agentpal/` by default.

External projects remain thin-bound and should read Harper through the central roster and AgentPal workspace.

## Related standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
