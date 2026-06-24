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

The AI must select the implementation-stage owner from current contacts / registry by case-specific judgement. In the bundled v0.1 Pal pool, Atlas is a registered development Pal and may be a strong candidate when the current request, deliverable, risk, and available assets justify it. The task wording itself must not force Atlas or any other Pal.

This is AI owner judgement with capability evidence, not `HTML -> Atlas` keyword routing.

## Forbidden

- keyword routes
- fixed task/domain to Pal maps
- `HTML -> Atlas` as a standing rule
- saying the content-stage owner owns the whole task
- saying Runtime owns the implementation stage
- treating clarification questions as a substitute for stage owner judgement

## Current v0.1 Output

Composite tasks should normally produce a staged Task Package or staged judgement inside Simple Pal Mode. This does not activate Deep Conductor, Subagent Mode, external Agent calls, or automated multi-agent execution.
