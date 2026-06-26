# Example Pal Publish Quality Gate

Target: `pals/Example-growth-pal`

## Gate Result

recommended status: testing

| Check | Result | Note |
| --- | --- | --- |
| root files | pass | all present |
| identity consistency | pass | `PAL.md` and `pal.json` agree |
| eval lab | not-run | run before stable |
| clean export safety | pass | private sections excluded |
| contacts / registry | pass | direct call aligns |

## Must Fix

- none before testing

## Should Fix

- run Eval Lab before stable

## User Confirmation

"Do you want to move this Pal to testing after recording this gate report?"
