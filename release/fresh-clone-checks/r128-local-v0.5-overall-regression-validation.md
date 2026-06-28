# R128 - Local v0.5 Overall Regression Validation

## Summary

Validation round: R128 v0.5 overall regression execution.

Result: fail_with_medium_issues.

Decision target: `ready_for_r129_fix_round`.

## Execution Coverage

| Check | Result | Evidence |
| --- | --- | --- |
| all 12 groups executed | pass | R128 results list Groups 1-12 with pass/fail status. |
| JSON parse result | pass | 100 visible JSON files parsed; failures 0. |
| clean-copy result | fail | required paths and JSON passed in clean copy, but internal development path references remain in public files. |
| thin binding result | fail | temp simulation passed, but active/current guidance still has stale legacy template path references. |
| central roster result | pass | registered 9, active 9, `routing_policy=ai_judgement_only`, `keyword_routing_allowed=false`. |
| official Pal result | pass | official Pal directories 9; all official `pal.json` files parse. |
| PalSmith manifest result | pass | official manifest count 1; only PalSmith has `asset-manifest.json`; PalSmith files parse. |
| Org/FDE/Asset Boundary result | pass | required standards/templates/examples exist; Org/FDE/Combined JSON parse; conservative safety flags retained. |
| customer-private leak scan | pass with issue separation | no real customer data found in v0.5 reusable assets; internal development path references are tracked separately as R128-MED-001. |
| no connector/scanner/marketplace scan | pass | active forbidden JSON true flags 0; text hits are boundary/negative/example/release contexts. |
| no keyword routing scan | pass | exact JSON route keys 0; broad text hits are forbidden, example, archive, eval, or non-binding capability contexts. |
| issue summary | pass | blocker 0, high 0, medium 2, low 0, note 1. |
| no push / pull / fetch / tag / release | pass | no remote, tag, or release action performed in R128. |

## Command Evidence Summary

| Evidence | Result |
| --- | --- |
| start status | `master...origin/master [ahead 78]`, start commit `8cc312f` |
| visible JSON parse | total 100, failures 0 |
| required root dirs | missing 0 |
| central roster | registered 9, active 9 |
| official Pal dirs | 9 |
| official `pal.json` parse failures | 0 |
| official manifest count | 1 |
| exact JSON route key hits | 0 |
| active forbidden JSON true hits | 0 |
| refined secret-pattern hits | fake-token negative example only |
| R127 evidence-map literal path missing | 1 |
| protected roster / official metadata diff | clean |

## Clean Copy

Final clean-copy validation was run after R128 public artifacts were written.

Clean-copy path: `C:\Users\ADMINI~1\AppData\Local\Temp\AgentPal_R128_clean_20260628232952`

Clean-copy result:

- required R128 paths missing: 0
- scoped JSON files parsed: 100
- scoped JSON parse failures: 0
- central roster active count: 9
- official Pal dirs: 9
- official manifest count: 1
- internal development path hits: 58, tracked as R128-MED-001

## Group Validation

| Group | Result |
| --- | --- |
| 1 Repository / JSON / clean-copy | fail |
| 2 External project thin binding | fail |
| 3 Central roster / no keyword routing | pass |
| 4 Official Pals / Pal Asset state | pass |
| 5 PalSmith metadata / manifest pilot | pass |
| 6 Pal Asset / PalSmith standards | pass |
| 7 Org Pack standards / templates / examples | pass |
| 8 FDE Pack standards / templates / examples | pass |
| 9 Asset Boundary | pass |
| 10 Combined Pack | pass |
| 11 Usage Scenario / Workflow / Governance | pass |
| 12 Public safety / no program expansion | fail |

## Not Performed

- no `git push`
- no `git pull`
- no `git fetch`
- no tag creation or modification
- no GitHub Release creation or modification
- no runtime code, scanner, validator, connector, marketplace, installer, daemon, database, or API client added

## Conclusion

R128 executed the v0.5 overall regression, but the current workspace should not move to v0.5 completion reporting yet.

Next required state: R129 fix round.
