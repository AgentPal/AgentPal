# How To Read PalBench

Read PalBench as a way to inspect AgentPal's workflow discipline.

It asks whether a Pal-layer method makes task handling more explicit: who owns the task, which context is needed, what evidence is required, and what boundary should not be crossed.

## Recommended Reading Frame

Use PalBench to understand:

- whether the task was turned into a clearer package
- whether verification evidence was separated from completion language
- whether the context scope was bounded before reading broadly
- whether Mira reduced the user's need to choose among Pal, runtime, Skill, and workflow concepts
- whether routing notes were reusable without becoming a hard-coded route
- whether current behavior and future design stayed separated

## What The Scores Mean

The R33 score scale is simple and qualitative:

- `0`: the behavior was not shown
- `1`: the behavior was partially shown
- `2`: the behavior was clearly shown

The scores help compare observations inside the six samples. They should not be aggregated into a broad benchmark score.

## Good Use

Good use of PalBench:

- release smoke validation
- regression checks for documentation and protocol boundaries
- improving future task-package and verification templates
- identifying which workflow claims need stronger evidence

## Bad Use

Bad use of PalBench:

- claiming statistical significance
- claiming general performance improvement
- comparing underlying model capability
- treating the six samples as representative of all tasks
- saying future Deep Conductor behavior is active in v0.1.0-rc.1
