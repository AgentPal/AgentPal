# R127 / R128 - v0.5 Overall Regression Readiness Decision

## Decision

Decision: ready_for_v0_5_overall_regression_execution

R127 planning is sufficient to proceed to R128 as a bounded v0.5 overall regression execution round.

## Basis

- R126 concluded `approved_for_v0_5_overall_regression_planning`.
- v0.4 baseline evidence exists and is included in the R127 evidence map.
- v0.5 Org Pack, FDE Pack, Asset Boundary, Combined Pack, Usage Scenario, Workflow, and Governance surfaces have an explicit 12-group regression plan.
- The R128 checklist includes JSON parse, clean-copy validation, thin-binding simulation, roster and official Pal checks, PalSmith metadata/manifest pilot checks, public safety scans, issue classification, and no-release safeguards.
- The R127 issue template separates blocker/high findings from medium/low execution-round fixes.

## Conditions For R128

R128 must:

- execute all 12 regression groups;
- record command/manual evidence;
- use `missing` and `not-run` honestly;
- avoid push, pull, fetch, tag, and GitHub Release actions;
- avoid new runtime code, scanners, validators, connectors, marketplace flows, installers, daemons, and API clients;
- avoid central roster and official Pal metadata edits unless a separate approved task explicitly authorizes them;
- move blocker/high findings to a dedicated fix round unless an exception is explicitly justified and safe.

## Next Recommended Round

Recommended next round: R128 - v0.5 overall regression execution.

Recommended R128 outputs:

- regression results;
- regression issues table using the R127 issue template;
- local validation record;
- readiness decision for v0.5 local completion reporting or for a dedicated R129 fix round.
