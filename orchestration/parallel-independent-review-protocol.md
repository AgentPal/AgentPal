# Parallel Independent Review Protocol

Parallel Independent Review is a v0.3 no-code staged workflow for collecting separate Pal perspectives before synthesis.

It is not group chat, not automatic multithreaded execution, not Subagent Mode, and not external Agent orchestration. A runtime may simulate the stages sequentially by following the packets and preserving reviewer isolation.

## When To Use

Use when independent viewpoints materially improve the decision:

- product decisions;
- architecture tradeoffs;
- release risks;
- research conclusion review;
- Pal team or Pal Pack governance;
- high-cost or high-risk strategy choices;
- multi-perspective reviews where disagreement is useful.

Do not use when:

- one owner Pal can answer safely;
- the task is simple and low-risk;
- the user wants a short direct answer;
- the workflow has no evidence or criteria for independent review.

## Required Stages

1. User Goal Intake
   - Capture the user goal, decision pressure, desired perspectives, evidence available, and constraints.
   - Decide whether independent review is useful or whether a single owner Pal should answer.
2. Review Need Judgement
   - Explain why parallel independent review is or is not appropriate.
   - Do not inflate simple work into parallel review.
3. Reviewer Candidate Selection
   - Select reviewer candidates from current contacts / registry by case-specific judgement.
   - Reviewer candidates are not fixed routes and are not task/domain route rules.
4. Reviewer Context Packet Generation
   - Generate one bounded Reviewer Context Packet per reviewer candidate.
   - Packets may share the same user goal but should differ by review question, review angle, allowed context, evidence requirements, and output contract.
5. Independent Reviewer Reports
   - Each reviewer produces an independent final report from its own packet.
   - Reviewers do not read peer drafts, hidden reasoning, or raw intermediate notes.
   - If a reviewer lacks context, it requests missing context rather than reading the whole conversation.
6. Synthesis by Mira / Owner Pal
   - Mira or the current owner reads reviewer final reports only.
   - The synthesis compares findings without adding specialist conclusions that no reviewer provided.
7. Conflict Summary
   - Surface disagreement, minority opinions, uncertainty, missing evidence, and unresolved questions.
   - Do not smooth conflict into false consensus.
8. Decision Options
   - Provide decision options with tradeoffs and conditions.
   - Keep final business/product/release decision with the user unless the user has delegated that decision.
9. Recommended Next Step
   - Recommend the next action, evidence request, repair package, owner handoff, or verifier task.
10. Optional Routing Memory Writeback
   - If useful, propose a public-safe routing memory candidate after outcome evidence exists.
   - Routing memory may inform future judgement but must not become a fixed route.

## Reviewer Isolation Rules

- Each reviewer receives its own Context Packet.
- Each reviewer reads only its allowed context.
- Reviewers do not read each other's drafts.
- Reviewers do not share hidden reasoning or intermediate thinking traces.
- Reviewers do not see hidden execution traces unless the packet explicitly allows it.
- Reviewers should record assumptions, uncertainty, evidence gaps, and confidence independently.
- The synthesis stage reads final reports, not drafts.

## Reviewer Context Requirements

Each Reviewer Context Packet should include:

- user goal and review question;
- review angle;
- current state;
- constraints and allowed context;
- cannot-read list;
- excluded peer outputs;
- needed output and output contract;
- evidence requirements;
- privacy policy;
- return target;
- deadline or budget when relevant.

If a reviewer needs more context, it requests a bounded supplement. It must not self-authorize broad reads.

## Reviewer Final Report Requirements

Each reviewer returns only its own perspective:

- verdict or judgement;
- confidence;
- key findings;
- risks;
- missing context;
- recommendation;
- conditions;
- questions for owner;
- notes.

Reviewers do not output the final total decision. Mira or the owner Pal synthesizes final reports.

## Synthesis Requirements

The summarizer should return:

- agreement;
- disagreement;
- conflicts;
- preserved minority opinion;
- risks;
- decision options;
- recommended next step;
- whether user decision is required;
- repair or follow-up package;
- routing memory candidate.

Synthesis must not hide conflict, delete minority opinions, or imply reviewers agreed when they did not.

## Boundary

This workflow is a staged no-code protocol only. It does not activate automatic Deep Conductor, Subagents, external Agent calls, runtime parallelism, background workers, scanners, validators, CLI features, UI, daemons, or services.
