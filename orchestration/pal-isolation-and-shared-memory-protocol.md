# Pal Isolation And Shared Memory Protocol

Pal Isolation prevents a workflow from turning into group-chat agreement. Shared Memory preserves useful routing lessons across workflows without leaking private context.

AgentPal v0.1.0-rc.1 does not run parallel Pal workflows. This protocol is a future design foundation and an audit concept.

## Intra-Workflow Isolation

During independent judgement stages:

- each Pal receives only its Context Access List
- each Pal uses its own output contract
- each Pal does not read other Pal drafts
- each Pal does not read another Pal's hidden reasoning or process notes
- each Pal does not see hidden execution traces unless the access list permits it
- each Pal records uncertainty and evidence gaps independently

Independent review comes first; synthesis comes later. Reviewers produce final reports before Mira or an owner Pal compares them.

## Summary Stage

After independent outputs are complete, a summary stage may read the final reports and compare:

- agreements
- conflicts
- evidence quality
- missing context
- recommended next action

Mira may summarize provided results as Pal team leader work. An owner Pal may synthesize within its professional scope.

The summary stage may read final reports, not drafts or hidden process traces, unless a specific access list says otherwise.

## Why Isolation Matters

Isolation prevents:

- first-answer anchoring
- copied mistakes
- false consensus
- redundant review
- context bloat
- hidden cross-contamination

## Shared Memory Across Workflows

Across workflows, AgentPal may use cleaned summaries such as:

- routing decision outcomes
- runtime fit observations
- Skill usefulness
- verification pass/fail
- user acceptance
- rework reasons
- next-time recommendation

Workflow-internal memory is isolated by default. Drafts, partial reviewer notes, hidden process traces, and unauthorized project content do not move between reviewers.

Shared memory must not include:

- private user memory without permission
- raw credentials, tokens, secrets, or logs
- full project files
- sensitive project context that was not authorized for reuse
- unrelated personal data
- unrelated Pal persona or private Pal memory
- raw external Agent full traces
- unapproved external content

Cleaned cross-workflow memory may include routing, runtime, Skill, plugin, verification, and project-decision summaries when they are public-safe or stored in the user's private runtime state.

## Collapse Pattern To Avoid

Bad pattern:

1. Atlas proposes a development plan.
2. Nova reads Atlas first and only reframes the same plan as product scope.
3. Quinn reads both and weakens testing because everyone already seems aligned.
4. Rhea repeats the combined summary without checking environment risk independently.

This is group-chat collapse, not independent review.

## Storage Guidance

Routing and verification memory should use public-safe templates during release. Runtime-private records should stay in ignored memory or external user project state.

## v0.1 Boundary

In v0.1, Pal Isolation is a design principle. Active task handling remains Simple Pal Mode with a single owner Pal or compact Task Package.
