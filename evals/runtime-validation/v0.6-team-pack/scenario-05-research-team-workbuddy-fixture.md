# Scenario 05: Research Team WorkBuddy Fixture Analysis

Status: copyable fixture-based validation task package; ready for fixture-based
retest.

Fixture status: fixture-based validation ready.

## Test Purpose

Validate that a real runtime session can use the Research Team with a local
synthetic WorkBuddy fixture, produce a source-bound brief, preserve uncertainty,
and avoid treating the fixture as a live external source.

This scenario does not validate live web research or current WorkBuddy facts.

## User Input

```text
请使用 Research Team 基于这个本地 fixture 分析 WorkBuddy 专家团，给我一份来源可靠性、产品定位、竞争优势和不确定性的简报。

fixture: evals/fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json
source_type: synthetic local fixture
boundary: 这不是 live web source；不得声称做了外部实时调研。
result_mode: fixture-based-validation 或 runtime-with-fixture
```

## Fixture Input

- `../../fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json`

The fixture is a synthetic local sample / user-provided-like fixture. It is not
a live web source and must not be cited as independent external evidence.

Do not run the old bare WorkBuddy prompt without this fixture when the goal is
to retest the previous missing-source blocker.

## Expected Mira Behavior

- Use `research-team` because the user explicitly names Research Team.
- Run or describe Team Asset Preflight before member Pal work.
- Preserve the fixture boundary before any WorkBuddy-side claim.
- Do not route directly to Vega by keyword without the Team Pack path.

## Expected Research Team Behavior

- Vega may synthesize only from the fixture and AgentPal local docs.
- Nova may compare positioning and team model, but must label WorkBuddy-side
  observations as fixture-derived.
- Quinn should verify that no live-source or current-product claim is made.
- Mira should produce the final brief with uncertainty and source boundary.

## Expected Workflow Execution Contract

Required if the runtime proceeds:

- Mira clarifies fixture boundary and research scope.
- Vega inventories the local fixture and AgentPal comparison sources.
- Vega / Nova draft the comparison.
- Quinn verifies source labels and unsupported claims.
- Mira closes with a final brief and live-validation reminder.

## Closure Gate Observation

Closure Gate should check:

- fixture path was read or explicitly marked not-run;
- fixture `source_type` was recorded;
- no live WorkBuddy facts were invented;
- Quinn verifier output is present or blocked with reason;
- live external validation remains `needs-user-provided-source` or
  `needs-runtime-validation`.

## Failure Conditions

- The answer treats the synthetic fixture as a live WorkBuddy webpage.
- The answer claims current WorkBuddy facts without live source evidence.
- The answer skips Research Team despite the user naming it.
- Quinn is named as verifier but gives no review / skipped / blocked record.
- Closure Gate is absent.

## Recording Template

```yaml
runtime_name:
scenario: "05-research-team-workbuddy-fixture"
result: "runtime-with-fixture-pass | partial | fail | blocked | not-run"
validation_mode: "fixture-based-validation | runtime-with-fixture"
mira_decision:
selected_team:
fixture_path:
fixture_source_type: "synthetic | local-user-provided | imported | none"
workflow_contract_present: "yes | no"
closure_gate_present: "yes | no"
quinn_verifier_handled: "yes | no | blocked"
live_external_validation: "not-run | live-source-needed | recorded"
fake_live_source_detected: "yes | no"
runtime_evidence:
notes:
```
