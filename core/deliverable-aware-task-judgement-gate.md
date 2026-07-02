# Deliverable-Aware Task Judgement Gate

Deliverable-aware Task Judgement is a system-level capability for the current Main Pal and any current owner Pal. It is not Mira-only.

Mira is the default Main Pal, Leader Pal, and Conductor, but any directly called Pal or current owner Pal must apply this gate before accepting a complex task as single-owner work.

## Required Fields

For composite deliverable tasks, identify:

- `domain_focus`
- `content_deliverables`
- `final_deliverables`
- `work_stages`
- `capability_needs`
- `selected_stage_owner_pal`
- `pal_candidates`
- `runtime_candidates`
- `skill_candidates`
- `verification_needs`

All Pal, Runtime, and Skill assignments are case-specific candidates or selected stage owners. They are not permanent routes.

## Implementation-Shaped Deliverables

If the final deliverable includes an HTML page, static webpage, frontend implementation, code artifact, repository change, or similar implementation-shaped result, the implementation stage needs a Pal-layer owner before Runtime execution.

The AI must select the implementation-stage owner from current contacts / registry by case-specific judgement. In the bundled Pal pool, Atlas is a registered development Pal and may be a strong candidate when the current request, deliverable, risk, and available assets justify it. The task wording itself must not force Atlas or any other Pal.

This is AI owner judgement with capability evidence, not `HTML -> Atlas` keyword routing.

## Forbidden

- keyword routes
- fixed task/domain to Pal maps
- `HTML -> Atlas` as a standing rule
- saying the content-stage owner owns the whole task
- saying Runtime owns the implementation stage
- treating clarification questions as a substitute for stage owner judgement
- Mira writing the professional body for a selected owner, participant, or
  verifier
- reporting a Team label as if it were a participant output
- claiming a Workflow Execution Contract is closed when a named owner,
  participant, verifier, open role, child task, Runtime tool, Skill, plugin, or
  promised output has no output, blocker, skip, failure, cancellation, or replan
  record

## Durable Team Pack And Compound Team Design

If the request asks for durable Team Pack creation, compound team design, a new
reusable team package, team governance or repair, roster design, or workflow
package design, the owner is PalSmith after Team Pack discovery confirms that no
existing Team Pack should simply be reused.

Mira's role is intake, Team Pack discovery, handoff, and final summary. Mira
must not write the PalSmith-owned durable Team Pack design body herself.

If the response assigns Faye, Nova, Vega, Harper, Rhea, Quinn, or any other Pal,
each named Pal must have its own output, skip reason, blocked reason, or replan
record. If Quinn is named as verifier, a Quinn verification result or legal
skip / block / replan record is required before Closure Gate can pass.

## Current v0.6 Output

Composite tasks should normally produce a staged judgement, Workflow Execution
Contract, or DeepConductor no-code package with explicit owner and closure
records. This does not activate automatic Subagent Mode, external Agent calls,
or automated multi-runtime execution without host-runtime evidence.
