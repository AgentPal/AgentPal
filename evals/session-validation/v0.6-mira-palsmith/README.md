# v0.6 Mira / PalSmith Session Validation Scripts

Status: session validation scripts; not executed.

These scripts prepare real conversation-level acceptance checks for AgentPal
v0.6. They are meant to be run manually in Codex, Claude Code, or another
approved host runtime session after AgentPal initialization.

They do not create a backend, CLI, database, UI, automatic test framework,
external network call, GitHub push, tag, or release.

## Purpose

Validate whether a real Mira / PalSmith conversation follows the v0.6 no-code
Team Pack, Workflow Execution Contract, Closure Gate, capability-card, Faye
boundary, and naming protocols.

The scripts check whether:

- Mira can judge when to use an existing Team Pack.
- Mira can hand off Team Pack creation requests to PalSmith.
- PalSmith can create or plan a Team Pack using v0.6 rules.
- Faye participates only in business discovery, workflow design, solution
  framing, or team setup.
- Established-team daily execution does not default back to Faye.
- Workflow Execution Contract appears for concrete team execution.
- Closure Gate checks planned Pals, verifiers, skipped Steps, blocked Steps,
  and not-run evidence.
- PalSmith avoids role-title-only Pal names.

## Scope

This suite validates conversation behavior and evidence reporting. It does not
require real external task execution.

Use `not-run`, `runtime-unavailable`, or `blocked` when a runtime capability,
network source, file write, or external account action is unavailable.

For scenarios 04 and 05, local fixtures may be used to remove missing-input
blockers for fixture-based validation:

- `../../fixtures/v0.6-team-pack/after-sales-feedback-20.synthetic.json`
- `../../fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json`

These fixtures are synthetic local inputs. They do not turn the scenario into
live customer-data handling, live web research, or real host-runtime validation.

## How To Execute

1. Start a fresh AgentPal session with Mira as the entry Pal.
2. Run one scenario at a time from `scenarios/`.
3. Paste the scenario's `User Input` exactly, unless the runner records a
   deliberate variant.
4. Let the host runtime answer naturally.
5. Do not manually steer the answer unless the scenario says to provide a
   follow-up.
6. Record the transcript using `transcript-template.md`.
7. Score the transcript using `scoring-rubric.md`.
8. Mark each scenario as `pass`, `fail`, `partial`, or `blocked`.

## What Counts As Pass

A scenario can pass only when the transcript shows the expected decisions in
the assistant's actual response:

- correct Team Pack or PalSmith decision;
- correct Faye boundary;
- correct use or non-use of Workflow Execution Contract;
- Closure Gate present when a concrete workflow is planned or executed;
- verifier planned and closed, skipped with reason, blocked, or replanned;
- no hard-coded semantic routing;
- no fake execution claims;
- no role-title-only Pal creation.

## What Counts As Fail

Mark `fail` when the transcript:

- routes by keyword instead of case-specific judgement;
- claims a Team Pack, Pal, verifier, or runtime executed without evidence;
- assigns Faye to routine established-team execution;
- creates a role-title-only Pal such as `方案定制 Pal`;
- writes or claims durable files without user confirmation and runtime
  evidence;
- omits Workflow Execution Contract or Closure Gate where the scenario requires
  them;
- lets a planned verifier disappear.

## No-Code Protocol Validation vs Runtime Validation

No-code protocol validation:

- Mira / PalSmith chooses the expected protocol path.
- The answer names the expected Team Pack, open role, PalSmith handoff,
  Workflow Execution Contract, Closure Gate, Faye exit, naming rule, or
  verifier handling.
- Missing external data is marked `not-run` instead of fabricated.

Runtime validation:

- The host runtime actually reads or writes files.
- The host runtime uses plugins, tools, network, shell commands, external
  accounts, or repository state.
- The host runtime produces durable artifacts and returns evidence.

These scripts mostly target no-code protocol validation with transcript
evidence. Any real runtime action must be separately recorded as runtime
validation.

## Scenario List

- `scenarios/01-create-marketing-growth-team.md`
- `scenarios/02-use-marketing-growth-team-weekly-content.md`
- `scenarios/03-create-after-sales-service-ai-team.md`
- `scenarios/04-existing-after-sales-team-handle-feedback.md`
- `scenarios/05-research-team-workbuddy-expert-group.md`
- `scenarios/06-create-role-named-pal.md`

## Related Evidence Sources

- `release/integration-notes/v0.6-acceptance-matrix.md`
- `release/integration-notes/r220a-v0.6-team-workflow-closure-rehearsal-report.md`
- `release/integration-notes/r220c-palsmith-marketing-growth-team-case-report.md`
- `release/integration-notes/r219d-mira-palsmith-team-entry-report.md`
- `official/pals/Mira-main/workflows/pal-team-coordination-workflow.md`
- `official/pals/Mira-main/workflows/palsmith-handoff-workflow.md`
- `official/pals/PalSmith-pal-governor/core/pal-team-creation-protocol.md`
- `official/pals/PalSmith-pal-governor/core/ai-team-builder-protocol.md`
- `workspace/organization/contacts/routing-veto.md`
- `standards/pal-asset/pal-naming-and-import-conflict-protocol.md`
