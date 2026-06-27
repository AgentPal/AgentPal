# Failure: Deep Conductor Skips Capability Inventory

## Wrong Behavior

Mira receives a project-level goal, immediately chooses a Runtime, model, Pal set, and Runtime Skill candidates without reading or referencing Capability Inventory, current Runtime evidence, or profile limits.

## Why Wrong

Deep Conductor must use capability profiles as judgement inputs when Runtime, model, reasoning, Runtime Skill, plugin, MCP, or Pal capability choices materially affect the plan. Profiles are not proof of availability, but skipping them turns the plan into guesswork.

## Correct Behavior

Mira reads the smallest relevant Capability Inventory index or profile, records `profile_read_count`, and names candidates with evidence requirements. If profiles are unavailable or not useful, Mira says so and uses an honest fallback.

## Corresponding Eval

`evals/orchestration/runtime-skill-aware-conductor-self-test.md`
