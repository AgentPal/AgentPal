# PalName-role-template

This is the English AgentPal Pal Pack standard template. Copy this directory and replace `PalName`, `pal-id`, `role`, `domain`, and related placeholders to create a new embedded Pal Pack.

Core principle:

```text
AgentPal owns the system layer.
Each Pal Pack owns only its professional layer.
```

More specifically:

- AgentPal owns the central roster, runtime, models, plugins, orchestration, templates, and project binding.
- A Pal Pack owns identity, voice, domain knowledge, Skills, workflows, learning notes, output standards, examples, evals, and public-safe placeholders.

Do not turn a Pal Pack into an independent project, an Agent runtime, a tool bundle, a fixed routing table, or an external project binding folder.

## Who This Template Is For

Use this template when you want to:

- add a new professional Pal to AgentPal
- package domain knowledge, Skills, workflows, and output standards as a reusable Pal Pack
- create a public-safe Pal Pack starter structure
- provide Codex, Claude Code, or another Markdown/JSON-capable runtime with readable Pal working assets

Do not use this template to create:

- an Agent runtime
- a multi-agent execution system
- a desktop app, web app, daemon, service, or installer
- a place for real user memory, private project state, secrets, tokens, internal reports, or local machine paths

## Create A Pal

1. Copy this directory:

   ```text
   PalName-role-template/
   ```

2. Rename it:

   ```text
   PalName-role/
   ```

   Examples:

   ```text
   Atlas-developer
   Nova-product
   Morgan-document
   ```

3. Replace placeholders in the root files:

   - `PAL.md`
   - `AGENTS.md`
   - `SKILL.md`
   - `pal.json`
   - `README.md`

4. Update identity, boundaries, output contract, and working protocols under `identity/` and `core/`.
5. Add minimum public-safe knowledge, Skills, examples, evals, and placeholders.
6. Register the Pal Pack in AgentPal `workspace/organization/contacts/` only after it is complete, public-safe, and reviewed.

## Standard Structure

Recommended structure:

```text
PalName-role/
  README.md
  PAL.md
  AGENTS.md
  SKILL.md
  pal.json

  identity/
    persona.md
    voice.md
    boundaries.md

  core/
    output-contract.md
    collaboration-protocol.md
    memory-protocol.md
    runtime-boundary.md

  knowledge/
    index.md
    domain-principles.md

  skills/
    index.md
    example-skill/
      SKILL.md
      README.md

  workflows/
    index.md
    lifecycle/
      README.md

  runbooks/
    index.md
    basic-check.md

  learning/
    README.md
    knowledge-gaps.md
    repeated-tasks.md
    skill-candidates.md
    runbook-candidates.md
    workflow-candidates.md

  evals/
    README.md
    pal-self-test.md

  examples/
    README.md
    usage-example.md

  memory/
    README.md

  state/
    README.md

  reports/
    README.md
```

Minimum viable structure:

```text
PalName-role/
  README.md
  PAL.md
  AGENTS.md
  SKILL.md
  pal.json

  identity/
  core/
  knowledge/
  skills/
  learning/
```

## Root Files

| File | Required | What to write | What to avoid |
| --- | ---: | --- | --- |
| `PAL.md` | Yes | Identity, responsibilities, boundaries, voice, collaboration principles, and refusals. | Fixed routing tables or claims that a task type must always go to a specific Pal. |
| `AGENTS.md` | Yes | Runtime read order, work rules, risk boundaries, and output requirements for this Pal. | Repeating global AgentPal central roster or runtime logic. |
| `SKILL.md` | Yes | Pal Pack entry: when to load this Pal, what to read, and how to answer. | Reducing the Pal to a single small tool Skill. |
| `pal.json` | Yes | Machine-readable metadata: `id`, human `display_name`, separate `role_title`, `contact_label`, `directory_name`, `aliases`, `role`, `capabilities`, `collaboration`. | Role-title-only `display_name`, `domain_map`, fixed owners, or hard-coded task-to-Pal routes. |
| `README.md` | Recommended | Human guide: who this Pal is, when to use it, how to call it, and how to maintain it. | Internal logs, local paths, private data, or outdated standards. |

## `identity/`

`identity/` defines who the Pal feels like to work with.

| File | Purpose |
| --- | --- |
| `persona.md` | Role archetype, professional stance, and personality. |
| `voice.md` | Communication style, such as concise, rigorous, warm, direct, or question-led. |
| `boundaries.md` | What this Pal refuses, delegates, or asks the runtime to handle. |

Optional additions:

- `relationship.md`: how the Pal relates to the user, such as advisor, reviewer, writing partner, or development partner
- `user-addressing.md`: how the Pal addresses users across languages and contexts

## `core/`

`core/` defines how the Pal works.

| File | Purpose |
| --- | --- |
| `output-contract.md` | Required answer structure, evidence expectations, and closing style. |
| `collaboration-protocol.md` | How this Pal consults, delegates, hands off, or reviews without fixed routes. |
| `memory-protocol.md` | What can become memory or a learning candidate, and what must never be saved. |
| `runtime-boundary.md` | Clear boundary between Pal-layer judgement and runtime-layer execution. |

Optional additions:

- `task-loop.md`
- `verification-protocol.md`
- `reporting-protocol.md`
- `learning-protocol.md`
- `risk-protocol.md`

The output contract should fit the Pal's domain. Examples:

- Development Pal: engineering state, file scope, implementation stage, verification commands, next runtime task
- Product Pal: user scenario, problem definition, scope split, Must / Should / Won't, pre-development questions
- Quality Pal: scope, evidence, risks, conclusion, blockers, remaining uncertainty
- Writing Pal: audience, tone, structure, revision notes, final copy

## `knowledge/`

`knowledge/` is the Pal's reusable domain knowledge. It is not runtime state and not user memory.

Good content:

- stable domain knowledge
- public-safe checklists
- methods and principles
- glossary and patterns

Do not store:

- real user privacy
- temporary task state
- API keys, tokens, passwords, private keys
- unauthorized third-party full text
- full private chat logs

## `skills/`

`skills/` contains formal Pal-owned Skills. These are primarily cognitive work methods, not scripts.

Recommended structure:

```text
skills/
  index.md
  example-skill/
    SKILL.md
    README.md
```

Each `skills/<skill-name>/SKILL.md` should include:

- `name`
- `description`
- `when to use`
- `inputs needed`
- `steps`
- `output format`
- `safety notes`

If the user explicitly asks to save a Skill, or if a similar task repeats more than three times, promote it into this Pal's own `skills/` directory rather than a global runtime skill folder.

## `workflows/`

`workflows/` contains longer multi-step patterns that often combine several Skills.

Use it for project recovery, development planning, release checks, document cleanup, or handoff flows.

## `runbooks/`

`runbooks/` contains repeatable operating guides.

Good candidates are repeated, stable, clear, and verifiable. Avoid one-off ideas, casual chat, private user content, or untested practices.

## `learning/`

`learning/` stores candidates for this Pal's future improvements.

Use it for:

- knowledge gaps
- repeated task families
- candidate Skills
- candidate Runbooks
- candidate Workflows

Learning files are not private memory. Do not store user secrets, private project facts, raw logs, or private conversations here.

## Runtime-Only Placeholders

`memory/`, `state/`, and `reports/` are placeholders in a public template.

Public releases should contain only README files or public-safe placeholders. Real runtime memory, live state, and task reports should stay local or be ignored.

## Examples And Evals

Examples are illustrative, not routing rules. If an example mentions another Pal, label it as non-binding.

Evals should check:

- identity and voice
- output contract
- boundary behavior
- no fabricated execution
- no private data in public files
- no hard-coded Pal routing

## Directories To Avoid Inside A Pal Pack

| Directory | Recommendation | Why |
| --- | --- | --- |
| `.agentpal/` | Remove | External project binding, not Pal Pack content. |
| `.agents/` | Remove or migrate | Runtime adapter material should not be default Pal content. |
| `.claude/` | Remove or migrate | Claude Code local configuration is not portable Pal content. |
| `contacts/` | Remove | Owned by AgentPal root. |
| `registry/` | Remove | Owned by AgentPal root. |
| `runtime/` | Remove | Owned by AgentPal central capability inventory under `workspace/organization/capability-inventory/runtimes/`. |
| `models/` | Remove | Owned by AgentPal central capability inventory under `workspace/organization/capability-inventory/models/`. |
| `plugins/` | Remove | Owned by AgentPal central capability inventory under `workspace/organization/capability-inventory/plugins/`. |
| `orchestration/` | Usually remove | Global orchestration belongs to AgentPal root. Pal-specific patterns belong in `core/` or `workflows/`. |
| `imports/` | Remove or migrate | Imported resources should be staged by AgentPal root; Pal-specific knowledge can move to `knowledge/references/`. |
| `tools/` | Keep only with care | Tooling can introduce runtime dependencies. Keep only optional, public-safe assets. |

## Public-Safe Rules

Do not commit:

- real user memory
- private project state
- customer data
- API keys, tokens, passwords, secrets, credentials, private keys
- local absolute paths
- unauthorized logs
- internal development reports
- live runtime state

You may commit:

- README files
- templates
- public-safe placeholders
- synthetic examples
- stable domain knowledge
- public checklists
- output contracts and working protocols

## Collaboration And Routing Boundary

A Pal Pack can describe how it collaborates, but it must not hard-code fixed routes to other Pals.

Good:

```text
Resolve collaborators from the current AgentPal central Pal roster.
```

Bad:

```text
All development tasks must go to Atlas.
All release checks must go to Quinn.
```

Capability examples are orientation only. They are not route maps.

## Runtime Boundary

The Pal does not execute actions directly.

The Pal may organize goals, select context, create Task Packages, request evidence, review evidence, and summarize next steps.

The runtime performs file writes, commands, tool calls, system modifications, publishing, and deletion.

If real execution happened, the report must identify the runtime or tool evidence instead of claiming that the Pal personally executed the action.

## Developer Checklist

Before publishing or registering this Pal Pack:

- [ ] `PAL.md` clearly states identity, responsibility, and boundaries.
- [ ] `AGENTS.md` describes runtime behavior for this Pal.
- [ ] `SKILL.md` is a Pal Pack entry, not a single-purpose tool Skill.
- [ ] `pal.json` is valid JSON.
- [ ] `pal.json` has no fixed route table or `domain_map`.
- [ ] `core/output-contract.md` constrains the Pal's output.
- [ ] `identity/` includes at least persona, voice, and boundaries.
- [ ] `knowledge/` contains only public-safe domain knowledge.
- [ ] `skills/` contains Skills owned by this Pal's domain.
- [ ] `learning/` contains no private user or project facts.
- [ ] `memory/`, `state/`, and `reports/` contain only public-safe placeholders.
- [ ] `examples/` uses synthetic or placeholder data.
- [ ] `evals/` checks identity, boundaries, output contract, and hard-coded routing risks.
- [ ] No `.agentpal/`, `.claude/`, `contacts/`, or `registry/` directories are included.
- [ ] Deep Conductor, Subagent Mode, or multi-agent execution are not described as current active capabilities.

## One-Line Standard

```text
AgentPal owns the system layer.
Pal Pack owns the professional layer.
```
