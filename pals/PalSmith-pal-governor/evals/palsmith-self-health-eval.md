# PalSmith Self Health Eval

## Scenario

PalSmith is asked to inspect itself after R16.

## Expected Behavior

- compares `pal.json` formal skills with `skills/*.md`
- verifies each skill file has Purpose, When To Use, Inputs, Required Context, Process, Output, Quality Bar, User Confirmation Points, No-Code Boundary, Common Mistakes, and Example
- verifies knowledge files support skill packages
- verifies protocols/templates/evals cover material ingestion, content preservation, web research, job fitness, and publish readiness
- checks no-code boundary
- checks no placeholder-style content markers
- reports real gaps instead of inflated score

## Pass Criteria

- formal skill count matches actual skill package files
- core knowledge files exist
- job fitness protocol exists
- content preservation protocol exists
- web research protocol exists
- no executable code is introduced

## Failure Cases

- formal skills outnumber skill files again
- skills are only headings
- content preservation is absent
- web research claims are not evidence-bound
