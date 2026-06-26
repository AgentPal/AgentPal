# Default Pal Collaboration Boundaries

## Concept explanation

Atlas collaborates with default Pals through case-specific AI judgement and Context Packets. This file describes boundaries, not static routes.

## Judgement standards

For each Pal, decide consult, delegate, handoff, or no use from the current deliverable, risk, evidence needs, and contacts / registry.

## Collaboration map

| Pal | Atlas should consult when | Atlas should delegate / handoff when | Atlas should not use this Pal when | Context to share | Context not to share | Expected output |
| --- | --- | --- | --- | --- | --- | --- |
| Mira | Task needs leader framing, progress summary, or cross-Pal synthesis. | Composite task needs Mira to resume conductor role. | Single implementation task is already bounded and Atlas owns it. | Goal, stage status, owner needs, evidence summary. | Full repo dumps, secrets, unrelated memory. | Owner judgement, context packet, progress summary. |
| PalSmith | Work touches Pal Pack assets, Pal identity, skills, knowledge, workflows, evals, contacts, registry, import/export, or publish governance. | Pal asset governance is the main deliverable. | Ordinary app code work has no Pal asset impact. | Target Pal path, allowed files, source material, risk boundary. | Private memory or broad project files without approval. | Gap report, task package, quality review. |
| Vega | Current technical facts, API/library behavior, market or source-backed analysis are needed. | Research is a major stage. | The task can be solved from local repo evidence. | Research question, source scope, freshness need. | Secrets, private code beyond necessary snippets. | Source-backed research brief. |
| Rhea | Environment, runtime, permissions, system state, startup items, installs, or command failure context matters. | Environment repair is the main deliverable. | Pure code planning needs no system state. | Commands, error text, OS/runtime constraints. | Credentials and unrelated system data. | Environment risk review or repair plan. |
| Quinn | Acceptance criteria, test coverage, release gate, regression, or risk review needs independent quality judgement. | Quality gate or release readiness is the main deliverable. | Atlas only needs a simple engineering task package. | Task goal, changed files, test evidence, risks. | Private material not needed for quality judgement. | Acceptance review, test/risk findings. |
| Morgan | Development work involves documents, spreadsheets, PDFs, file naming, or office artifacts. | Document/file workflow is the main deliverable. | Pure code or repo task has no document artifact. | File paths, required artifact, formatting needs. | Unrelated private docs. | Document/file workflow guidance. |
| Harper | User-facing copy, release notes wording, docs tone, or communication polish matters. | Writing or editing is the main deliverable. | The change is code-only and wording is not user-facing. | Audience, tone, draft, constraints. | Private notes not needed for text. | Edited copy or communication review. |
| Nova | Product scope, PRD, user scenario, prioritization, or acceptance behavior is unclear. | Product definition is the main deliverable. | Requirements are already bounded and technical. | Problem, users, constraints, decision needed. | Technical secrets not needed for product scope. | Product scope, acceptance criteria, PRD slice. |

## Examples

- Good: Atlas asks Quinn to review release readiness evidence before a release claim.
- Good: Atlas asks PalSmith to inspect Atlas itself before editing Atlas assets.
- Good: Atlas keeps implementation package ownership after Vega provides source research.

## Counterexamples

- Bad: Atlas always sends code work to Quinn because tests are mentioned.
- Bad: Atlas uses PalSmith for ordinary app bugs.
- Bad: Atlas shares the whole project with every collaborator.

## Scope

Applies to AgentPal default Pal collaboration in v0.1 Simple Pal Mode.

## How it becomes skill / workflow / eval

Use with `multi-agent-development-coordination-skill.md`, `collaboration-with-default-pals.md`, and `atlas-developer-capability-eval.md`.

## Common mistakes

- Fixed collaborator routes.
- Excess context sharing.
- Missing same-response owner handoff when required.
- Treating runtime tools as Pals.

## Source references or local notes

Local: contacts / registry, Mira default boundary, PalSmith handoff guidance, AgentPal route rules.
