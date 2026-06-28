# R141 Official Pal Readiness Matrix

Status: pass.

Audit date: 2026-06-29.

## Scope

This matrix checks the 9 registered official Pals as usable v0.5 Pal Packs. It
does not require full metadata / manifest rollout for every Pal because that
rollout is deliberately paused. PalSmith remains the v0.5 metadata /
asset-manifest pilot.

## Summary

| Metric | Result |
| --- | --- |
| central roster registered Pals | 9 |
| central roster active Pals | 9 |
| official Pal directories | 9 |
| official Pal `pal.json` parse | 9 / 9 pass |
| root entries present | 9 / 9 have `PAL.md`, `pal.json`, `SKILL.md`, `AGENTS.md` |
| official asset manifests | 1, PalSmith only |
| usable in v0.5 | 9 / 9 yes |
| full manifest rollout complete | no, deliberately paused |

## Matrix

| pal_id / name | directory exists | central roster registered | active | root entries present | pal.json parse | memory / skills / research / runbooks / reports / state index status | public-safe status | v0.5 metadata status | asset-manifest status | role clarity | usable in v0.5 | gap | next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mira-main` / Mira | yes | yes | yes | yes | pass | memory 1; skills 30; research 3; runbooks 13; reports 2; state 1; knowledge 63; workflows 15; evals 16 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear Main Pal / Leader / Conductor | yes | no manifest pilot | Keep as usable; test routing/intake in R142. |
| `atlas-developer` / Atlas | yes | yes | yes | yes | pass | memory 3; skills 39; research 2; runbooks 8; reports 1; state 1; knowledge 39; workflows 11; evals 12 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear developer / implementation lead | yes | no manifest pilot | Keep as usable; test owner-boundary examples in R142. |
| `nova-product` / Nova | yes | yes | yes | yes | pass | memory 5; skills 42; research 2; runbooks 12; reports 1; state 1; knowledge 30; workflows 12; evals 12 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear product / strategy lead | yes | no manifest pilot | Keep as usable; test role clarity in R142. |
| `vega-research` / Vega | yes | yes | yes | yes | pass | memory 3; skills 44; research 2; runbooks 13; reports 1; state 1; knowledge 37; workflows 11; evals 11 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear research / intelligence lead | yes | no manifest pilot | Keep as usable; test evidence-boundary examples in R142. |
| `quinn-quality` / Quinn | yes | yes | yes | yes | pass | memory 5; skills 39; research 2; runbooks 12; reports 1; state 1; knowledge 27; workflows 11; evals 13 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear quality / verification lead | yes | no manifest pilot | Keep as usable; test validation/reporting boundary in R142. |
| `morgan-document` / Morgan | yes | yes | yes | yes | pass | memory 5; skills 40; research 2; runbooks 12; reports 1; state 1; knowledge 28; workflows 12; evals 12 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear document / file workflow lead | yes | no manifest pilot | Keep as usable; test document workflow boundary in R142. |
| `harper-writing` / Harper | yes | yes | yes | yes | pass | memory 3; skills 40; research 2; runbooks 12; reports 1; state 1; knowledge 28; workflows 12; evals 12 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear writing / content craft lead | yes | no manifest pilot | Keep as usable; test writing role boundary in R142. |
| `rhea-system` / Rhea | yes | yes | yes | yes | pass | memory 3; skills 39; research 2; runbooks 12; reports 1; state 1; knowledge 28; workflows 11; evals 12 | pass by scans | root `pal.json` usable; full v0.5 rollout paused | absent by design | clear system / runtime safety lead | yes | no manifest pilot | Keep as usable; test safety-boundary checks in R142. |
| `palsmith-pal-governor` / PalSmith | yes | yes | yes | yes | pass | memory 1; skills 18; research 3; runbooks 4; reports 5; state 1; knowledge 11; workflows 6; evals 24 | pass by scans | v0.5 metadata / manifest pilot complete | present | clear Pal asset governance lead | yes | no full roster rollout | Keep as pilot; test manifest and governance path in R142. |

## Metadata / Manifest Interpretation

PalSmith has the v0.5 `pal.json` + official `asset-manifest.json` pilot. The
other 8 official Pals do not have official asset manifests. That is a deliberate
pause, not a current blocker for v0.5 usability under the central-roster +
root-entry + no-code-asset standard.

If the release criterion changes to "all official Pals must be full
metadata/manifest ready", then v0.5 is not complete under that stricter
criterion and should enter a v0.5.1 or v0.6 metadata rollout round before
remote publication.

