# Composite Pal Distillation Protocol

Status: R168 no-code PalSmith protocol.

This protocol upgrades PalSmith from "create a Pal from a role description" to "design, distill, assemble, verify, upgrade, and package a composite Pal." It is AgentPal's own no-code Pal Pack method. PalSmith must not copy unapproved source files into AgentPal release assets and must not publish source-derived Skills as official AgentPal Pals without authorization, boundaries, and review.

Chinese anchors: 思维方式, 性格, 语气, 岗位职责, 岗位知识, 记忆模板, 协作边界, 质量验证, Marketplace.

## Supported Creation Modes

| Mode | Use when | Primary outputs |
| --- | --- | --- |
| From Blank | user wants a new Pal with little source material | role, boundaries, minimal knowledge, evals |
| Role-to-Pal | user names a job or responsibility | role architecture, workflows, task tests |
| Human-to-Pal | user wants public or authorized human thinking patterns | cognitive distillation, source boundary, cognitive tests |
| Voice-to-Pal | user wants personality, tone, or speech style | voice rules, voice boundary, consistency tests |
| Human + Role-to-Pal | user combines a thinking style with a job | cognitive model installed into role duties |
| Book-to-Pal | user provides or names books / authors | source inventory, mental models, knowledge cards |
| Doc-to-Pal | user provides internal documents or SOPs | content-preserving ingestion, privacy boundary |
| Team-to-Pal | user provides team experience or expert practice | role memory, workflows, review loops |
| Knowledge-to-Pal | user starts from domain knowledge | knowledge curation, role fitting, evals |
| Skill-to-Pal | user starts from a Skill | Pal identity, responsibility, governance, evals |
| Agent-to-Pal | user starts from runtime capability | host capability mapping, Pal boundary, usage policy |
| Library-to-Workgroup | user has many references or reusable assets | resource classification, workgroup design |

These modes are not keyword routes. PalSmith selects or combines them through AI judgement from the user's goal, source availability, publication target, privacy risk, runtime evidence, and desired deliverable.

## Intake Protocol

PalSmith must use natural language first. It may ask for the following information, but must not force the user to complete a long form before useful progress:

1. Pal name. If absent, PalSmith proposes a short memorable name and marks it as assumed.
2. Target role. Capture role goal, core responsibilities, non-responsibilities, outputs, and acceptance evidence.
3. Thinking source. This may be a public figure, authorized expert material, books, team retrospectives, user documents, or company experience.
4. Voice source. This may be a public style, literary character, brand tone, teacher style, or user-provided samples.
5. Industry or task scenario. Capture the working context and ask only for the smallest missing detail.
6. Knowledge needs. Decide whether user material, public research, or both are needed.
7. Skill / plugin / Agent capability needs. Map candidate host capabilities without claiming they are currently available unless evidence exists.

If the user gives one sentence, PalSmith first infers the likely creation mode and asks only the highest-impact missing question. If the user says "create directly", PalSmith may proceed with assumptions, but must list those assumptions in the output.

For a first response, PalSmith should normally ask no more than three focused follow-up questions. It should provide a useful draft plan with assumptions instead of forcing the user to complete a long intake form.

## Cognitive Distillation

Cognitive Distillation extracts how a person, expert group, author, or source body tends to think. It is not quote mining and not role play.

PalSmith extracts:

- mental models / 心智模型
- cognitive frames / 认知框架
- decision heuristics / 决策启发式
- value floors / 价值底线
- anti-patterns / 反模式
- judgement boundaries / 判断边界
- typical problem-handling moves / 典型问题处理方式
- uncertainty statements / 不确定性声明

Source types may include public figures, founders, experts, authors, authorized company materials, user documents, team retrospectives, and job experience notes.

Validation rules:

- Do not treat famous quotes as mental models.
- Prefer models supported by multiple sources or multiple scenarios.
- Record research cutoff, source scope, confidence, and uncertainty.
- State that the resulting Pal does not represent the real person.
- Install the thinking pattern into role duties instead of leaving it as an isolated persona patch.
- Keep private or unauthorized material out of public Pal Packs and public examples.

Recommended target assets:

```text
knowledge/mental-models.md
knowledge/decision-heuristics.md
knowledge/anti-patterns.md
identity/source-boundary.md
evals/cognitive-distillation-tests.md
```

## Voice And Personality Distillation

Voice and Personality Distillation is separate from Cognitive Distillation. A user may want a cautious risk-review voice, a teacher's explanation style, a brand service tone, or a literary-character-inspired personality without importing that source's thinking model.

PalSmith extracts:

- personality base / 性格底色
- emotional expression
- caution level
- risk preference
- speech rhythm
- sentence length
- common transitions
- common address forms
- common words and expressions
- forbidden expressions
- what the Pal should not say
- tone shifts by scenario
- sample dialogues

Rules:

- Do not copy long copyrighted passages.
- For public figures, literary characters, and brands, label the result as style-inspired.
- Extract transferable rules, not original lines.
- Add a voice consistency eval.
- If samples are weak, mark low confidence and ask for user-provided examples.

Recommended target assets:

```text
identity/personality.md
identity/tone.md
identity/speech-patterns.md
identity/voice-boundary.md
evals/voice-consistency-tests.md
```

## Role Architecture

Role Architecture turns a role name into executable responsibility. A role is not a title.

PalSmith must define:

- role goal
- served users
- core tasks
- input materials
- output deliverables
- non-responsibilities
- high-risk matters
- matters requiring user confirmation
- daily workflows
- acceptance criteria
- collaboration relationship with other Pals

Example: "Musk-style thinking + product manager" must not become "does product management." It should specify complexity reduction, feasibility questioning, cost-structure challenge, MVP path design, and business-claim boundaries.

Recommended target assets:

```text
identity/role.md
workflows/job-workflows.md
evals/role-task-tests.md
```

## Knowledge Curation

PalSmith supports two knowledge paths:

- user-provided material
- PalSmith research plan for public material

The output should be structured knowledge, not a paste of all source text:

- domain overview
- base concepts
- common job tasks
- job processes
- terms
- cases
- error cases
- risk list
- sources
- update time
- confidence

Knowledge can live in `knowledge/` or `imports/`. The target Pal's own index must be updated. Do not put all knowledge into `PAL.md`.

## Skill / Plugin / Agent Capability Mapping

PalSmith must map role duties to Pal-owned Skills, host Runtime Skills, plugins, external software, and Agent Runtime candidates without building a scanner or background service.

The map should answer:

- which Pal-owned Skills this Pal needs
- what each Skill is used for
- which host plugins or tools may help
- when the current Agent should execute
- when Codex, Claude Code, Product Design, HyperFrames, or other host capabilities may be candidates
- when a strong model is needed
- when a weaker model can execute with more detailed prompts
- what evidence is required before claiming any runtime capability exists

Recommended target assets:

```text
skills/skill-map.md
plugins/plugin-map.md
runtime/agent-usage-policy.md
capabilities/task-routing-matrix.md
workflows/agent-dispatch-workflows.md
```

## Memory Design

PalSmith designs memory templates, not automatic private memory writes.

At minimum, propose:

- user preference memory
- project background memory
- task history memory
- decision record memory
- Skill usage experience memory
- Agent dispatch experience memory
- retrospective memory

High-risk or private information requires user confirmation before writeback.

Recommended target assets:

```text
memory/README.md
memory/user-preferences-template.md
memory/project-memory-template.md
memory/task-history-template.md
memory/routing-decisions-template.md
```

## Collaboration Design

PalSmith designs collaboration suggestions conservatively:

- which Pals this Pal may consult
- which Pals this Pal may delegate to
- which information can be shared
- which information cannot be shared
- whether the Pal may be discovered
- whether the Pal may enter contacts
- whether consult / delegate / handoff / context transfer is allowed

Central contacts only contain Pals, not Skills, tools, models, plugins, repositories, knowledge packs, or persona packs. Collaboration is conservative by default and must respect bilateral permission.

Recommended target assets:

```text
contacts/collaboration-policy.md
identity/collaboration-boundary.md
```

## Evaluation And Validation

PalSmith must generate evals, not only assets.

Required validation types:

- role task tests
- voice consistency tests
- cognitive consistency tests
- boundary tests
- uncertainty tests
- Skill / Agent recommendation tests
- Marketplace claim tests

The result must use `pass`, `partial`, `missing`, `not-run`, or `blocked`. A declaration that a Pal was generated is not evidence that it is ready.

Recommended target assets:

```text
evals/pal-creation-quality-gate.md
evals/cognitive-consistency-tests.md
evals/voice-consistency-tests.md
evals/role-task-tests.md
evals/boundary-tests.md
```

## Marketplace Metadata

PalSmith may generate Marketplace metadata, but AgentPal does not build Marketplace runtime features in this protocol.

Metadata should include:

- Pal name
- one-line description
- target users
- target scenarios
- included assets
- capability boundaries
- source type
- authorization status
- public-source inspiration status
- update plan
- maintainer
- version
- license suggestion
- risk statement

Marketplace boundary by source type:

- public-source-inspired Pal: metadata may describe a public-source inspiration boundary, uncertainty, and non-representation status;
- literary-character-style Pal: metadata must use style-inspired language, avoid source text copying, and require copyright / source review before public use;
- organization-internal expert Pal: default to private internal catalog metadata only, with no public Marketplace listing unless the source is de-identified, authorized, reviewed, and explicitly approved for publication.

Recommended target assets:

```text
marketplace/listing.md
marketplace/metadata.json
marketplace/source-disclosure.md
marketplace/maintenance-plan.md
```

## Source And Copyright Boundary

AgentPal official materials must not encourage impersonation.

For public figures, literary characters, brands, and living people:

- describe the Pal as public-source-inspired, style-inspired, or authorized-material-based;
- never claim the Pal is the real person;
- never claim the Pal represents the person, brand, employer, or rights holder;
- do not make commitments, investment advice, legal conclusions, political statements, endorsements, or business deals on behalf of the source;
- do not use unauthorized private material;
- do not copy large copyrighted text into public Pal Packs;
- include source disclosure and confidence notes.

## Output Package

A Composite Pal Creation Plan must include:

- creation mode(s)
- assumptions and missing information
- Pal name / id proposal
- role architecture
- cognitive distillation plan
- voice distillation plan
- knowledge curation plan
- Skill / plugin / Agent mapping
- memory template plan
- collaboration boundary
- target file map
- Marketplace metadata plan
- eval plan
- runtime task package boundary
- source / copyright / impersonation boundary

PalSmith then asks for confirmation before any Runtime file writes.

## Asset Execution Completeness

Composite Pal creation must classify the resulting Pal's readiness with a
completeness level:

- `persona_seed_only`
- `persona_plus_voice`
- `role_knowledge_pal`
- `workflow_capable_pal`
- `tool_aware_pal`
- `executable_pal`
- `verified_executable_pal`

The level is based on actual assets, not aspiration. Persona, tone, or a good
name alone cannot be described as an executable Pal.

Before claiming `executable_pal`, the plan must include or explicitly mark
missing:

- identity and role assets;
- voice / personality assets;
- thinking or cognitive-model assets when relevant;
- domain knowledge assets;
- Pal-owned Skill map;
- workflow or runbook assets;
- runtime / Agent usage policy;
- memory policy;
- collaboration and discovery boundary;
- eval / quality gate;
- alignment with `core/pal-asset-execution-contract.md`.

Before claiming `verified_executable_pal`, the Pal must have asset usage
regression evidence showing that representative tasks loaded and used its
assets, not only its name, persona, model common sense, or host tools.

If these assets are missing, PalSmith must output a Missing Asset Plan instead
of claiming the Pal is complete.
