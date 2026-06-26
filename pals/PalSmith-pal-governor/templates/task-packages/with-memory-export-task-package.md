# With Memory Export Task Package

## Boundary

With-memory export is private by default and high risk. PalSmith must ask strong confirmation. The current Agent Runtime may include memory only within the approved scope.

## Fields

- `task_id`:
- `task_name`: With Memory Export Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: target Pal, private export purpose, approved memory/state/report scope.
- `allowed_read_paths`: target Pal public files plus explicitly approved `memory/user/`, `memory/project/`, `state/`, or `reports/` sections.
- `forbidden_read_paths`: unrelated private paths, unrelated Pals, credentials, tokens, unapproved memory.
- `allowed_write_paths`: approved private export location.
- `forbidden_write_paths`: public release locations, source Pal mutation, registry/contacts.
- `required_exclusions`: credentials, tokens, keys, unrelated memory, unapproved reports/state, executable files unless explicitly reviewed.
- `risk_checks`: user memory, project memory, state, reports, public sharing, restore safety, privacy report.
- `user_confirmation_required`: yes, strong confirmation and second acknowledgement required.
- `confirmation_questions`: export purpose, public/private destination, exact memory scope, state/report inclusion, privacy acknowledgement.
- `execution_steps_for_runtime`: after confirmation, copy approved sections, generate privacy report, generate restore instructions and manifest.
- `expected_outputs`: private export package, privacy report, restore instructions, manifest.
- `verification_requirements`: list private sections included/excluded, confirm public release is blocked or converted to clean export.
- `final_report_format`: private-data warning, included private sections, excluded sections, privacy risks, restore notes.

## PalSmith Acceptance

Accept only when strong confirmation and privacy report are present. Refuse or convert to clean export for public sharing of private memory.
