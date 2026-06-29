# R149 Local Pre-Manual Readiness Validation

Status: executed
Date: 2026-06-29

## Validation Summary

| Check | Result |
| --- | --- |
| Visible JSON parse | pass, 106 parsed, 0 failures |
| `agentpal.json` parse | pass |
| Central roster count | pass, 10 registered / 10 active |
| Official Pal directories | pass, 10 |
| Official Pal `pal.json` parse | pass, 10 parsed, 0 failures |
| Faye directory exists | pass |
| Faye `pal.json` parses | pass |
| Faye contact entry exists | pass |
| Faye `PAL_CONTACTS.md` entry exists | pass |
| Faye aliases exist | pass |
| Faye `RESOURCE_INDEX.md` reference exists | pass |
| Faye `agentpal.json` reference exists | pass |
| Current entry hardcoded 9-Pal stale wording | pass, no true stale hit |
| R149 manual Faye-unregistered wording | pass, 0 hits |
| Initialization prompts central contacts source | pass |
| Deep Conductor Faye candidate references | pass |
| No connector / executor / runtime expansion | pass |
| No executable code added | pass |
| No external project write | pass |
| Clean-copy validation | pass, `C:\Users\ADMINI~1\AppData\Local\Temp\agentpal-r149-pre-manual-clean-20260629-174201` |
| Remote sync / tag / GitHub Release | not-run, intentionally not performed |

## Notes

The broad text scan still finds older historical evidence files with 9-Pal counts. Those are retained as historical records. Current entry, contact, R149 readiness, and manual execution artifacts use the 10-Pal current roster.

Manual testing has not been executed in this validation.
