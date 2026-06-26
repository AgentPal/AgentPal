# Web Research To Knowledge Task Package

task_name: Web Research To Knowledge Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Use Runtime-performed web research to improve a Pal's job expertise and create candidate knowledge, skills, workflows, templates, and evals.

## Allowed Actions

- search web sources if user confirms
- read selected sources
- record source metadata
- draft candidate Pal assets

## Forbidden Actions

- no crawler or downloader inside AgentPal
- no automatic promotion to stable knowledge
- no unsourced live-research claim
- no copying private or copyrighted long-form source text beyond allowed use

## Verification Requirements

- source inventory
- credibility notes
- applicability notes
- uncertainty notes
- candidate vs stable status
- `web research not run` if no live research happened

## Expected Output

Candidate knowledge package with source notes, skill/workflow/template/eval suggestions, and user confirmation questions.
