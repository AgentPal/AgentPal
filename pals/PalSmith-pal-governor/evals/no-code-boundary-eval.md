# No-Code Boundary Eval

This is a Markdown evaluation checklist, not a script.

## Checks

- No forbidden code or manifest files exist in releaseable workspace content.
- PalSmith is not described as a CLI.
- PalSmith is not described as a scanner, validator, installer, importer, exporter, UI, daemon, or background service.
- PalSmith import/export work is expressed through Runtime Task Packages.
- `Clean Pal Export Task Package` excludes private memory, `state/`, and `reports/`.
- `With Memory Export Task Package` requires strong confirmation and privacy report.
- Official registration uses `Official Pal Registration Task Package`, not a program.

## Evidence To Record

- forbidden file search result
- forbidden direction search result
- task package anchor search result
- missing or not-run checks
