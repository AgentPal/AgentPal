# R198 - Generic Pal Asset Usage Regression

Date: 2026-07-01

Status: pass

## Purpose

This regression checks that Pal Asset Execution Contract applies to all Pals,
not only the Luma-style fixture.

## Case Matrix

| Case | Scenario | Required asset use | Tool boundary | Expected result |
| --- | --- | --- | --- | --- |
| 1 | Design Pal uses design assets before tool call | identity, design thinking, workflow, quality gate | ImageGen / Product Design only after Pal direction | pass |
| 2 | Developer Pal prepares Codex task | project memory, workflow, verification, runtime policy | Codex is execution runtime, not Pal asset | pass |
| 3 | Research Pal writes report | source policy, knowledge scope, report workflow, citation/eval gate | Browser or web search only after research plan | pass |
| 4 | Simple chat / typo | minimal identity or affected file | no full asset load required | pass |

## Case 1: Design Pal

Expected:

- loads design role, voice, thinking, workflow, skill map, runtime policy, and
  eval assets;
- forms visual direction and constraints first;
- uses ImageGen or Product Design only as host execution tool;
- reviews output with design quality gate.

Fail if the tool creates output before Pal direction exists.

## Case 2: Developer Pal

Expected:

- loads active project context, development workflow, verification protocol, and
  runtime policy;
- prepares a bounded Runtime Task Package before Codex changes files;
- reports what Codex executed as runtime evidence.

Fail if Codex execution is treated as the Pal's own capability asset.

## Case 3: Research Pal

Expected:

- loads source policy, research workflow, relevant knowledge, report contract,
  and citation / uncertainty gate;
- uses web search or browser only after forming source plan;
- separates facts, inferences, and uncertainties.

Fail if web output is pasted without Pal review.

## Case 4: Lightweight Task

Expected:

- uses `go_lightweight`;
- reads only the affected file or active Pal identity if needed;
- does not load all Pal assets;
- does not claim unsupported professional judgement.

Fail if all small tasks are forced into expensive deep loading or if missing
assets are invented.

## Decision

`generic_pal_asset_usage_regression_pass`

R198 applies broadly while preserving a lightweight path for small tasks.
