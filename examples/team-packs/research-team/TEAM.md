# Research Team

## Team Identity

- team_id: `research-team`
- type: `team-pack`
- version: `0.6.0`
- status: `draft`

## Team Mission

Help users turn open research questions into source-grounded findings,
evidence-aware summaries, and decision-ready reports.

## Suitable Tasks

- market or competitor research
- source-grounded topic briefs
- evidence inventory and synthesis
- research report planning

## Unsuitable Tasks

- direct code implementation
- legal, medical, or financial advice as a final authority
- private investigation or credentialed background checks
- tasks where the user only needs a small wording edit

## Member Overview

This Team Pack references Pals from the central roster. It does not copy Pal
assets into this example.

| Role | Pal reference | Notes |
| --- | --- | --- |
| coordinator | `mira-main` | Clarifies the user question and team fit |
| lead-researcher | `vega-research` | Owns source discovery and synthesis |
| strategy-reviewer | `nova-product` | Reviews decision framing when product or strategy is involved |
| evidence-verifier | `quinn-quality` | Reviews source quality and unsupported claims |

## Team Roles

- `research-coordinator`: turns the user goal into research questions.
- `lead-researcher`: gathers and synthesizes evidence.
- `strategy-reviewer`: checks whether findings answer the decision need.
- `evidence-verifier`: reviews source quality, gaps, and claim boundaries.

## Default Workflow

1. Clarify the research question.
2. Define source scope and exclusion rules.
3. Gather or request sources.
4. Synthesize findings with evidence boundaries.
5. Review claims against team evals.
6. Report findings, uncertainty, and next research gaps.

## Team Acceptance

The team uses `evals/research-definition-of-done.md`.

## Collaboration Boundary

- The team does not invent sources.
- The team reports uncertainty and source gaps.
- Routing notes are judgement inputs, not hard-coded routes.
- Runtime web access or file access requires current host evidence.

## User Invocation

```text
Mira, use the research team to investigate this market.
Mira, ask the research team for a source-grounded brief.
```
