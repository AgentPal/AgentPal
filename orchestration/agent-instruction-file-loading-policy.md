# Agent Instruction File Loading Policy

This policy controls how AgentPal loads `AGENTS.md`, `PAL.md`, `SKILL.md`, `README.md`, and similar instruction files.

## Level 0: Root Minimum

During normal initialization or workspace context setup, use the short path and load:

- root `AGENTS.md`
- `prompts/codex/initialize-agentpal-workspace.md`
- `agentpal.json`
- `workspace/organization/contacts/pals.json` or summary
- `workspace/organization/contacts/PAL_CONTACTS.md` or summary
- `official/pals/Mira-main/PAL.md`
- `official/pals/Mira-main/AGENTS.md`
- `official/pals/Mira-main/SKILL.md`
- `orchestration/runtime-response-gate.md`

If the session is bound to an external project, also read only the existing project binding files needed to establish context:

- external project `AGENTS.md`
- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`

Do not load every Pal's instruction files during initialization. Do not load templates, multiple orchestration protocols, all Mira identity files, registry Markdown, or resource maps during default initialization.

## Deep Initialization

Wide initialization is diagnostic only. Use it for release checks, failed initialization, registry/contact repair, explicit user requests, or asset diagnostics.

Deep initialization may load selected additional files such as:

- `RESOURCE_INDEX.md`
- `workspace/resources/registry/pal.index.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `workspace/organization/contacts/aliases.json`
- selected Mira core protocol files
- selected orchestration protocols
- selected templates

Deep initialization must still avoid all-Pal, all-project, all-memory, examples/evals, future design, reports, and imports unless that exact scope is requested and justified.

## Index Exposure Versus Content Read

Directory listings, registry entries, resource indexes, and file names count as index exposure. They do not mean the file content was opened.

When a user asks what was loaded, report both:

- `index_known_count`
- `index_known_source`
- `index_known_paths` or a short summary
- `content_read_count`
- `content_read_paths`
- `index_only_not_content_read`
- `not_content_read_note`

Example note:

```text
Some file paths were discovered through directory index or registry lookup. They were not opened or read as content.
```

## Level 1: Selected Pal Minimum

After an owner Pal is selected, load only that Pal's:

- `PAL.md`
- `AGENTS.md`
- `SKILL.md`
- `pal.json`
- `core/output-contract.md`

## Level 2: Selected Pal Relevant Assets

Then read relevant owner Pal assets by index:

- selected skill
- selected knowledge card
- selected runbook
- selected workflow
- selected learning candidate if needed

## Level 3: Project Relevant Slice

Read only project files needed for the task:

- file list or relevant directory list
- README or config summary when needed
- relevant docs/source/tests

Do not read all source files or all docs by default.

## Level 4: Optional / Ask First

Default exclusions:

- full memory
- reports
- imports
- examples
- evals
- future design docs
- archived materials
- private project data
- large files

Ask or justify before loading them.

## AGENTS.md Optimization

- Root `AGENTS.md`: load at initialization or context switch.
- Selected Pal `AGENTS.md`: load only when that Pal is selected.
- External project `AGENTS.md`: load when entering that external project context.
- Do not read all Pal `AGENTS.md` files.
- Do not merge all `AGENTS.md` files into one context.
- If an instruction file is long, prefer headings and relevant sections.

## README Optimization

Do not treat README as default task context.

Read README when:

- the user asks what a project or Pal is
- initializing or release checking
- no better index exists
- project positioning is required

Otherwise prefer indexes, selected skills, selected knowledge cards, selected runbooks, and current task files.

## Examples And Evals

Do not load examples or evals for normal professional tasks.

Load them only when:

- the user asks for examples
- running self-tests or release checks
- output contract is unclear
- investigating a regression or failure sample
