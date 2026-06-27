# Parallel Independent Review Usage Guide

Parallel Independent Review is a v0.3 no-code workflow for asking several reviewer candidates to evaluate the same question from separate perspectives, then letting Mira or the owner Pal synthesize their final reports.

It is not multi-Pal group chat. Reviewers do not read each other's drafts, do not share intermediate reasoning traces, and do not converge before final reports exist.

## When To Use

Use it when independent viewpoints materially improve the result:

- product decisions;
- architecture tradeoffs;
- release risk review;
- research conclusion review;
- PalSmith Pal team or Pal Pack governance;
- multi-perspective review where disagreement is useful.

## When Not To Use

Do not use it when:

- the task is simple and single-stage;
- a single owner Pal can answer safely;
- the user explicitly asks for a fast answer;
- the available context is too thin for meaningful independent review.

## Difference From Group Chat

Group chat lets one reviewer see another reviewer's draft and drift toward agreement. Parallel Independent Review isolates reviewer context first, collects final reports, and only then synthesizes.

Bad group-chat pattern:

1. Nova gives a product opinion.
2. Atlas reads Nova and adjusts the implementation view to fit it.
3. Quinn reads both and only summarizes the apparent consensus.

Correct pattern:

1. Mira or owner creates separate Reviewer Context Packets.
2. Nova, Atlas, Quinn, Vega, Rhea, PalSmith, or other candidates review only their assigned packet.
3. Reviewers return independent final reports.
4. Mira or owner summarizes agreement, disagreement, conflict, risk, options, and next step.

## Reviewer Independence

Each reviewer should receive:

- a distinct review question;
- a review angle;
- allowed context;
- cannot-read list;
- excluded peer outputs;
- output contract;
- evidence requirements;
- return target.

Reviewers should not read:

- peer drafts;
- peer hidden reasoning;
- full chat history by default;
- private memory;
- unrelated Pal assets;
- secrets.

If a reviewer lacks context, it should request a bounded supplement.

## Reviewer Context Packet

Use `templates/orchestration/reviewer-context-packet.md`.

The packet should make the review angle explicit. Product, implementation, quality, research, system, writing, document, and governance are examples of review angles, not fixed routes to specific Pals.

## Reviewer Final Report

Use `templates/orchestration/reviewer-final-report.md`.

The reviewer final report should include verdict, confidence, key findings, risks, missing context, recommendation, conditions, questions for owner, and notes. It is one perspective, not the final decision.

## Synthesis Rules

Use `templates/orchestration/parallel-review-synthesis-summary.md`.

Mira or the owner Pal should summarize:

- agreement;
- disagreement;
- conflicts;
- risks;
- decision options;
- recommended next step;
- whether the user must decide;
- repair or follow-up package;
- routing memory candidate when appropriate.

Synthesis must not erase minority opinions or hide conflict. If conflict is material, show it or create a follow-up package.

## Boundary

Parallel Independent Review is a no-code staged workflow. It does not automatically run multiple agents, Subagents, external Agents, background workers, multiple runtimes, or Deep Conductor automation. A runtime may simulate reviewers sequentially only if it preserves packet isolation and does not feed one reviewer's draft to another.
