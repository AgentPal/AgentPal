# Delivery Pack Governance Loop

Date: 2026-06-29
Status: local v0.5 no-code protocol

## Purpose

This protocol defines the governance loop for Faye Delivery Pack work.

The loop turns a user request into auditable no-code records without connector
calls, automatic execution, keyword routing, or external project thick binding.

## Required Loop

```text
User request
-> Faye task judgement
-> missing information
-> assumptions
-> Delivery Pack update
-> Pal Team Blueprint
-> Context Access List
-> Task Package
-> Human review
-> Verification Result
-> Governance Record
-> Routing Memory candidate
-> reusable/private asset review
```

## Loop Records

| Stage | Record | Required Content |
| --- | --- | --- |
| User request | request summary | user goal, constraints, requested deliverables |
| Faye task judgement | task judgement packet | task type candidates, risk, topology, candidate Pals |
| Missing information | missing list | questions, unavailable evidence, blocked facts |
| Assumptions | assumptions list | public-safe assumptions and confidence |
| Delivery Pack update | delivery update note | reusable asset changes and private-record pointers |
| Pal Team Blueprint | blueprint | candidate Pals as AI judgement inputs only |
| Context Access List | CAL | can-read, cannot-read, output contract, verification need |
| Task Package | task package | stages, inputs, outputs, evidence requirements |
| Human review | review note | reviewer role, required review, unapproved claims |
| Verification Result | result record | pass/fail/missing/not-run/blocked/requires-human-review |
| Governance Record | decision record | decision, evidence, risks, private storage target |
| Routing Memory candidate | memory candidate | topology used, result, rework, recommendation |
| reusable/private review | classification | publishability and customer-private status |

## Governance Rules

- Do not write customer-private evidence into reusable examples.
- Do not copy Delivery Pack assets into external project `.agentpal/` paths by default.
- Do not modify central contacts or official Pal assets.
- Do not convert candidate Pals into routes.
- Do not convert `not-run`, `missing`, or `requires-human-review` into `pass`.
- Do not call connectors, scanners, validators, installers, daemons, databases,
  marketplace programs, or external business systems.

## Delivery Pack Update Boundary

A Delivery Pack update may add or revise public-safe:

- reusable workflow notes;
- Task Package templates;
- Context Access Lists;
- verification checklists;
- governance record shells;
- Pal Team Blueprint candidates.

Customer-specific source files, private evidence, real credentials, customer
records, and real review decisions must stay in approved private records.

## Human Review Boundary

Human review is required when the task includes:

- customer-private evidence;
- regulated professional claims;
- public publication;
- external system operation;
- credential or access decisions;
- final business approval.

## Completion Bar

The loop is complete only when every stage either has a record or is explicitly
marked `missing`, `not-run`, `blocked`, or `requires-human-review`.
