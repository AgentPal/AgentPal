# v0.6 Team Pack Real Runtime Validation Package

Status: `needs-runtime-validation`; preparation package only.

This package prepares copyable tasks for validating AgentPal v0.6 Team Pack
behavior in real host runtimes. It does not execute Codex, Claude Code,
OpenCode, external agents, shell commands, publishing flows, or file writes by
itself.

## Purpose

Use this package to check whether a real host session can:

- enable or access AgentPal through the runtime's supported binding path;
- let Mira handle team requests with case-specific judgement;
- let PalSmith create or plan Team Packs when the user asks for a new team;
- show a Workflow Execution Contract for concrete team execution;
- apply Team Asset Preflight before Pal Asset Preflight;
- respect Faye, Quinn, and PalSmith boundaries;
- avoid role-title-only Pal names;
- record evidence without pretending unrun work passed.

## Applicable Runtimes

| Runtime | Entry expectation | Current status |
| --- | --- | --- |
| Codex | Use the AgentPal Codex plugin or workspace initialization path. | Needs scenario transcript. |
| Claude Code | Use the Claude Code project binder slash commands when available. | Needs scenario transcript. |
| OpenCode | Use generic CLI-agent compatibility if it can read Markdown / JSON and maintain context. | Needs scenario transcript. |
| Other CLI agent | Use only if it can read local files, follow AgentPal protocols, and report evidence. | Compatibility not guaranteed. |

## Preconditions

Before running a scenario in a host runtime:

1. Open a disposable or test project, not a production project with sensitive
   data.
2. Enable AgentPal using the runtime's current documented path.
3. Confirm the host can read the AgentPal workspace and the current project.
4. Record runtime differences with `runtime-difference-record.md`.
5. Run one scenario at a time.
6. Save the transcript or evidence before scoring.

## Scenario List

| Scenario | Task package |
| --- | --- |
| Create Marketing Growth Team | `scenario-01-create-marketing-growth-team.md` |
| Use Marketing Growth Team For Weekly Content | `scenario-02-use-marketing-growth-team-weekly-content.md` |
| Create After-Sales Service AI Team | `scenario-03-create-after-sales-service-team.md` |
| Existing After-Sales Team Handles Feedback | `scenario-04-existing-after-sales-team-feedback.md` |
| Research Team WorkBuddy Fixture Analysis | `scenario-05-research-team-workbuddy-fixture.md` |

## R224 Fixture Retest Instructions

Use these copyable retest prompts to avoid repeating the R223A/B missing-input
blockers:

- Codex after-sales fixture: `retest-instructions/codex-scenario-04-after-sales-fixture.md`
- Claude Code after-sales fixture: `retest-instructions/claude-code-scenario-04-after-sales-fixture.md`
- Codex WorkBuddy fixture: `retest-instructions/codex-scenario-05-workbuddy-fixture.md`
- Claude Code WorkBuddy fixture: `retest-instructions/claude-code-scenario-05-workbuddy-fixture.md`

These prompts are for fixture-based or runtime-with-fixture retests. They do not
prove live customer-data handling or live external research.

## Fixture-Based Validation

Some scenarios can be run with local fixtures when private user data or network
sources are unavailable:

- `../../fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json`
- `../../fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json`

Fixture-based validation can prove protocol handling over bounded local input.
It does not prove live customer-data handling, live web research, current
external product facts, or automatic runtime execution.

## What Counts As Pass

A scenario can be marked `pass` only when the actual runtime transcript or
evidence shows the required behavior. For concrete team execution, the record
should show Team Asset Preflight, Workflow Execution Contract, Closure Gate,
boundary handling, and honest runtime evidence.

## What Counts As Partial

Use `partial` when the runtime follows the main protocol path but misses a
non-critical record, cannot access one asset, or has a documented host
limitation that does not create a safety-critical failure.

## What Counts As Fail

Use `fail` when the transcript shows any of these:

- Faye is assigned routine established-team execution.
- PalSmith is used as an ordinary business executor.
- Quinn is treated as the fixed verifier for all tasks.
- A role title is used as a Pal `display_name`.
- The response claims file edits, publishing, customer feedback processing, or
  external actions without evidence.
- A planned verifier disappears without output, skip reason, block, or replan.
- A concrete team task lacks Workflow Execution Contract and Closure Gate.

## Safety Boundary

Do not use real customer data, credentials, secrets, account actions,
publishing flows, or release actions for these scenarios. If the runtime cannot
read, write, browse, invoke a plugin, or access a Team Pack, record the exact
limitation as `blocked`, `not-run`, or `runtime-unavailable`.

## Recording Templates

- Runtime differences: `runtime-difference-record.md`
- Scenario summary: `result-summary-template.md`

## Related Manual Checks

- `../../session-validation/v0.6-mira-palsmith/README.md`
- `../../team-workflows/v0.6-regression-checklist.md`
- `../../../release/integration-notes/v0.6-acceptance-matrix.md`
