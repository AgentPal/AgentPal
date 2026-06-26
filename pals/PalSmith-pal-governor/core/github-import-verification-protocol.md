# GitHub Import Verification Protocol

Status: PalSmith v0.3 no-code protocol.

GitHub import verification defines how to test real GitHub source imports without adding an AgentPal downloader or importer program.

## Verification Levels

| Level | Name | Meaning |
| --- | --- | --- |
| Level 1 | URL Plan | parse GitHub URL and generate import plan without network |
| Level 2 | Runtime Fetch | current Agent Runtime fetches or reads GitHub content into staging |
| Level 3 | Full Import Trial | staging, risk report, install plan, clean install, and registry / contacts suggestions |

## Safety Boundary

- do not execute imported scripts
- do not automatically install
- do not automatically add contacts
- do not automatically write registry
- do not import private memory
- do not trust unknown license
- do not treat ordinary Skill as Pal

## Output

`GitHub Import Verification Report`:

- level reached
- URL or source
- staging path
- risk report
- install recommendation
- registry / contacts recommendation
- `not-run` items
