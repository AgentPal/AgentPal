# Workflow Topology Protocol

Workflow Topology describes possible shapes for organizing Pal, runtime, Skill, and verification work.

AgentPal active task handling is host-runtime executed and no-code governed. The conservative active shapes are Fast Route, Single Owner, and Task Package. A Task Package may be staged when the user goal contains multiple deliverables or work phases. Deep Conductor topologies are protocol foundations and planning artifacts unless the current host runtime provides explicit execution evidence.

See also:

- `orchestration/fast-route-protocol.md`
- `orchestration/deep-conductor-protocol.md`

## Topologies

| Topology | v0.1 Active | Summary |
| --- | --- | --- |
| Fast Route | Yes | Mira chooses an owner or answers team-leadership work quickly |
| Single Owner | Yes | One owner Pal answers in the same response |
| Task Package | Yes | Pal compresses work for an execution runtime |
| Staged Task Package | Yes | Current Main Pal / owner Pal organizes multiple stages as candidates without automated multi-agent execution |
| Owner + Verifier | Future | Owner produces, verifier reviews evidence |
| Plan -> Execute -> Verify | Future | Planner prepares, runtime executes, verifier checks |
| Parallel Independent Review | Future | reviewers work independently before summary |
| Sequential Chain | Future | staged handoff from research to product to development to QA |
| Best-of-N Runtime | Future | multiple runtimes produce candidates, verifier compares |
| Team Leader Summary | Yes | Mira summarizes completed or provided results |

## Fast Route

Suitable when:

- task is clear
- risk is low
- one Pal can own it
- the final deliverable does not require materially different work stages
- no extra verification workflow is needed

Inputs:

- user goal
- contacts / registry
- selected owner assets

Outputs:

- direct answer, short handoff, or compact task package

Isolation:

- no other Pal drafts are loaded by default

Verification:

- evidence requested only when task claims execution or completion

## Single Owner

Suitable when:

- one registered Pal can reasonably own the output
- the user expects a professional answer
- the context slice is bounded
- the task does not contain multiple obvious final deliverables or capability phases

Not suitable when:

- independent verification is required
- multiple conflicting perspectives are materially useful
- the topic domain and final deliverable require different stage-level capabilities

v0.1 active: yes.

## Staged Task Package

Suitable when:

- the user goal contains multiple obvious deliverables
- the final deliverable differs from the content-stage work
- one directly called Pal can own only part of the task
- implementation, verification, research, product, writing, document, or system stages need different capability candidates

The current Main Pal or owner Pal should identify domain focus, content deliverables, final deliverables, work stages, capability needs, Pal / Runtime / Skill candidates, and verification needs.

All stage recipients are candidates, not fixed routes. Capability profiles and Pal descriptions are judgement inputs only.

v0.1 active: yes, as a written Task Package inside Simple Pal Mode. It does not run multiple Pals, Subagents, external Agents, or Deep Conductor automatically.

## Owner + Verifier

Suitable when:

- acceptance evidence matters
- false completion risk is meaningful
- release, safety, or quality gate review is needed

v0.1 active: no. It can be described as a future workflow or represented manually in a Task Package.

## Plan -> Execute -> Verify

Suitable when:

- work requires file edits, commands, or external execution
- planning and execution evidence should be separated

v0.1 active: no automated topology. The plan can be written as a Task Package.

## Parallel Independent Review

Suitable when:

- disagreement is useful
- anchoring risk is high
- product, implementation, quality, or research perspectives should be independently assessed

Context isolation:

- each reviewer receives its own Context Access List
- reviewers do not read each other's drafts before submission

v0.1 active: no.

## Sequential Chain

Suitable when:

- output naturally moves through staged judgement
- each stage consumes only the previous stage's accepted output

v0.1 active: no.

## Best-of-N Runtime

Suitable when:

- high-risk tasks justify extra cost
- multiple runtimes are available
- a verifier can compare evidence

v0.1 active: no. Do not call external runtimes from AgentPal v0.1.

## Team Leader Summary

Suitable when:

- multiple results are already provided
- user asks for a digest, status, next actions, or final report

v0.1 active: yes, as Mira-owned team-leadership work.
