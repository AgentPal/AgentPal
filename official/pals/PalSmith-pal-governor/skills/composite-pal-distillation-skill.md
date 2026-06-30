# Composite Pal Distillation Skill

Type: PalSmith no-code Pal Skill.

Use when a user asks PalSmith to create or upgrade a Pal from any combination of role, human thinking style, voice/personality, book, document set, team experience, knowledge base, Skill, plugin, or Agent Runtime capability.

For an existing Pal, this Skill must be used with
`core/existing-pal-composite-upgrade-protocol.md`. PalSmith must first judge the
request semantically and explain whether it is a simple existing Pal edit,
existing Pal composite upgrade, authorization flow, or another mode. The
classification must not be a keyword route.

This Skill covers Human-to-Pal, Voice-to-Pal, Role-to-Pal, Human + Role-to-Pal, Book-to-Pal, Doc-to-Pal, Team-to-Pal, Knowledge-to-Pal, Skill-to-Pal, Agent-to-Pal, and Library-to-Workgroup creation modes.

Chinese anchors: 思维方式, 性格, 语气, 岗位职责, Marketplace.

## Inputs

- user goal in natural language
- desired Pal role or job
- optional thinking source
- optional voice / personality source
- optional industry or task scenario
- optional user materials or source links
- optional Skill / plugin / Agent Runtime candidates
- publication target: private draft, team-local, public example, official candidate, or Marketplace candidate

## Method

1. Infer creation mode(s) from the user's sentence.
2. Ask only the smallest missing question unless the user asks for direct creation; normally keep the first response to no more than three focused questions.
3. Separate role architecture, cognitive distillation, voice distillation, knowledge curation, capability mapping, memory design, collaboration design, evaluation, and Marketplace metadata.
4. Use `core/composite-pal-distillation-protocol.md` as the governing protocol.
5. For existing Pal upgrades, also use `core/existing-pal-composite-upgrade-protocol.md` and `templates/existing-pal-composite-upgrade-plan.md`.
6. Use `templates/composite-pal-creation-plan.md` as the default output shape for new Pal creation.
7. Preserve source boundaries and copyright boundaries.
8. Treat host Runtime Skills, plugins, MCP tools, and external Agents as capability candidates, not Pal-owned Skills and not contacts.
9. Produce a Runtime Task Package only after the plan and allowed write paths are clear.

## Output

Produce a Composite Pal Creation Plan with:

- creation mode(s)
- assumptions
- minimum follow-up questions
- proposed Pal identity
- role architecture
- cognitive distillation map
- voice and personality map
- knowledge curation map
- Skill / plugin / Agent capability map
- memory template map
- collaboration policy
- target file plan
- eval plan
- Marketplace metadata draft
- source-type Marketplace boundary
- source and impersonation boundary
- Runtime Task Package boundary

## Boundaries

This Skill must not:

- impersonate a real person;
- claim a Pal represents a real person or rights holder;
- copy long copyrighted source text;
- treat famous quotes as proof of mental models;
- create keyword routing maps;
- add candidates to central contacts automatically;
- directly rewrite high-impact existing Pal assets before an upgrade plan and confirmation;
- route existing Pal upgrades by keyword match instead of AI judgement;
- copy unapproved source files into AgentPal release directories;
- store private user materials in public Pal assets;
- claim any host Runtime capability without current evidence.

## Verification

Use `evals/composite-pal-distillation-eval.md` for behavior checks. At minimum verify:

- one-sentence intake does not become a long forced form;
- cognitive and voice distillation are separate;
- role duties become executable responsibilities;
- file map includes knowledge, identity, workflows, memory, collaboration, evals, and Marketplace metadata;
- examples cover Musk + product manager, Musk + PPT pitch adviser, Han Li-style cautious risk reviewer, Jobs-style product taste reviewer, and Feynman-style teaching coach;
- no official wording promises source-person replication or source-person availability.
