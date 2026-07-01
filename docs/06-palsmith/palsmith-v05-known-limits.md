# PalSmith v0.5 Known Limits

This page lists known limits for PalSmith v0.5 release preparation. These limits are part of the public boundary, not hidden implementation gaps.

## Host Runtime Required

PalSmith is a Pal-layer planner and governor. It does not execute file writes, copies, validation commands, Git operations, or external publication by itself.

How to understand it: PalSmith can prepare a Task Package. The current host runtime must perform approved execution and provide evidence.

## No Automatic Discovery By Default

User custom Pals stay private by default. Discovery is disabled until the user explicitly authorizes a scoped discovery policy.

How to understand it: a user custom Pal can exist in `workspace/resources/user-pals/` without becoming discoverable through `/pal Name`, central contacts, delegation, or Marketplace surfaces.

## Invocation May Need Explicit Path Context

Current host behavior can vary. A user custom Pal may require an explicit path or context packet until the host has current evidence that discovery and invocation are available.

How to understand it: do not promise uniform `/pal user custom Pal` resolution unless the current runtime has proven it.

## Discovery Is Not Delegation

Discovery only means the Pal can be found in the scoped workspace context. It does not automatically permit task delegation, contacts registration, official promotion, or public publication.

How to understand it: each permission remains separate and revocable.

## Contacts Registration Is Separate Governance

Central contacts remain the official bundled Pal roster source. User custom Pals must not be written into `workspace/organization/contacts/` without a separate governance task.

How to understand it: PalSmith can draft a contacts-registration proposal, but should not silently mutate the roster.

## Marketplace Draft Is Not A Public Listing

Marketplace metadata can be drafted as planning material. It is not a live Marketplace listing and does not imply a Marketplace backend exists.

How to understand it: Marketplace work is documentation and review until a separately authorized product surface exists.

## No Runtime Backend Is Added

PalSmith v0.5 does not add AgentPal's own runtime backend, CLI, installer, scanner, daemon, connector, validator program, or app runtime.

How to understand it: the workspace remains Markdown, JSON, examples, prompts, templates, and evidence. Execution belongs to the current host runtime.

## Public Person And Source Boundary

PalSmith may design source-inspired Pals only when privacy, copyright, likeness, and publication boundaries are respected. It must not present a Pal as a real public person, rights holder, source character, brand, or proprietary expert.

How to understand it: use bounded role, method, style, and evaluation design. Do not impersonate.

## Evidence Boundary

Read-only host tests, dry-run plans, and simulated records must stay labeled as such. They must not be upgraded into live-write, remote-publish, or public-release evidence.

How to understand it: use `not-run`, `read-only`, `dry-run`, `partial`, or `blocked` when that is what happened.

## Pal Asset Execution Adoption Is Incremental

R198-R201 add the Pal Asset Execution Contract, adoption guide, templates, and
regression evidence. This is readiness work for how Pals should prove asset use.
It is not evidence that every official Pal has been individually rewritten or
fully retested under the new contract.

How to understand it: future Pal creation and upgrade work should adopt the
contract step by step. Existing Pals should not be described as fully migrated
unless their own asset inventory, Task Asset Packet, Asset Use Summary, and
regression evidence exist.

## Certification Is Scoped

R205 and R207 provide representative task-family host regression evidence across
the 10 official bundled Pals. That evidence does not certify every task family.

How to understand it: a future certification must name the Pal, task family,
evidence paths, host threads, known limits, valid scope, invalid scope, and QA
review result. R208 defines the plan and template, not a completed
certification.

R209 adds scoped certification records for selected high-priority Pal
task-family scopes. These records are limited to the named Pal plus task family
and do not change Pal discovery, contacts, publication, runtime, or backend
behavior.

## Controlled Write Fixture Is Not A Real Pal Upgrade

R200 used `FirstPrinciplesProductReviewerControlledWrite` as a controlled-write
test fixture under `evals/`. The real user custom Pal under
`workspace/resources/user-pals/FirstPrinciplesProductReviewer/` was not changed.

How to understand it: the fixture proves the write protocol and boundary. It
does not promote the fixture, publish it, or modify the real user custom Pal.

## Tool Output Is Not Pal Capability By Itself

Host tools can help execute a request, but the Pal still needs identity,
knowledge, workflow, runtime policy, memory rules, and eval assets to make the
request Pal-grounded.

How to understand it: if a tool acts first and the Pal name is attached later,
the result should be treated as missing asset evidence or a failed asset usage
regression.

## Remote Publication Not Included

R193 does not perform `push`, `pull`, `fetch`, tag creation, tag push, GitHub Release creation, or release asset upload.

How to understand it: remote publication requires a later task with explicit user authorization.
