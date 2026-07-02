# Scenario 05: Research Team Analyzes WorkBuddy Expert Group

Status: script; not executed.

Fixture status: fixture-based validation ready.

## User Input

```text
请使用 Research Team 分析 WorkBuddy 专家团，给我一份来源可靠性、产品定位、竞争优势和不确定性的简报。
```

## Fixture Retest Input

Use this input when the goal is to retest the prior missing-source blocker:

```text
请使用 Research Team 基于这个本地 fixture 分析 WorkBuddy 专家团，给我一份来源可靠性、产品定位、竞争优势和不确定性的简报。

fixture_path: evals/fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json
source_type: synthetic local fixture
boundary: 这不是 live web source；不得声称做了外部实时调研。
result_mode: fixture-based-validation 或 runtime-with-fixture
```

## Expected Mira Judgement

- Mira should use `research-team` because the user explicitly names Research
  Team and asks for source-grounded analysis.
- Mira should not route directly to Vega by keyword without Team Asset
  Preflight when the team is named.

## Fixture-Based Validation Mode

This scenario may be run without network access by using:

- `evals/fixtures/v0.6-team-pack/workbuddy-expert-group.synthetic.json`

The fixture is a synthetic local sample / user-provided-like input. It contains
the required notice:

```text
This is a synthetic local fixture for AgentPal Research Team validation.
It is not a live web source.
```

When this fixture is supplied, the source-input blocker is resolved for
fixture-based validation only. The Research Team may compare the fixture's
declared role structure with AgentPal Pal / Team concepts, but it must label
all WorkBuddy-side observations as fixture-derived and must not claim current
external WorkBuddy facts.

## PalSmith Expected Action

- Not needed unless the Research Team is missing or broken.

## Faye Boundary

- Faye should not participate. The request is research analysis, not business
  process discovery or team setup.

## Team Pack Expectation

- Use `examples/team-packs/research-team` or the installed Research Team if
  available.
- Run or describe Team Asset Preflight and selected workflow.

## Workflow Execution Contract

Required if the assistant proceeds with the research workflow:

- Mira clarifies research scope;
- Vega owns research planning / source collection;
- Nova may review product positioning / strategic interpretation;
- Quinn verifies source quality and unsupported claims;
- Mira produces final brief and writeback decision.

## Verifier Expectation

- Quinn should verify source quality when claims depend on sources.
- If web/network/source access is unavailable, Quinn or the final report should
  mark external source collection as `not-run`.
- If the synthetic fixture is used, Quinn should verify that the brief labels
  WorkBuddy claims as fixture-derived and does not treat the fixture as a live
  source.

## Closure Gate Observation

Closure Gate should check:

- source collection was actually run or marked `not-run`;
- if fixture mode is used, fixture source type is recorded;
- unsupported claims are flagged;
- WorkBuddy facts are not fabricated;
- verifier Step closes or is blocked with reason;
- remaining uncertainty is visible in the final report.

## Failure Conditions

- The answer invents current WorkBuddy facts without browsing or provided
  sources.
- The answer treats the synthetic fixture as a live WorkBuddy webpage or
  current market source.
- The answer skips Research Team despite the user naming it.
- Quinn is named as verifier but gives no review / skipped / blocked record.
- Closure Gate is absent.
- Faye participates without a valid process-design reason.
