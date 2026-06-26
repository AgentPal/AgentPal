# Runtime Task Package

## Status

Current for AgentPal `v0.1.0-rc.1`.

A Runtime Task Package is a written execution brief that a Pal gives to the current Agent Runtime after judging a user goal. It turns a conversation into bounded reads, writes, exclusions, confirmation questions, evidence requirements, and final reporting rules.

AgentPal does not include built-in tools, background services, scanners, validators, importers, exporters, installers, UI, or runtime code. AgentPal is a Markdown / JSON / protocol workspace. Real file operations belong to the current Agent Runtime, such as Codex, Claude Code, or another markdown-capable runtime.

## PalSmith Flow

1. The user asks the current Pal or `/pal PalSmith` for Pal creation, team creation, AI team blueprints, import, export, health inspection, registry or contacts update, snapshot, rollback, team governance, readiness review, runtime call verification, GitHub import verification, or release readiness work.
2. The current Pal may consult, delegate, or hand off to PalSmith with a Context Packet after AI judgement.
3. PalSmith reads the smallest relevant Pal assets and policies.
4. PalSmith produces a plan, risk boundary, confirmation questions, and a Runtime Task Package.
5. The user confirms the exact write or high-risk action.
6. The current Agent Runtime executes the approved task package and returns evidence.
7. PalSmith reviews the evidence and reports `done`, `missing`, `not-run`, and risk notes.

PalSmith does not directly copy files, download repositories, create archives, update JSON, restore snapshots, or publish releases.

## Task Package Types

- Pal Creation
- Pal Team Creation
- Pal Import Staging
- Pal Install
- Clean Pal Export
- With Memory Export
- Pal Health Inspection
- Registry Update
- Contacts Update
- Snapshot
- Rollback
- Official Pal Registration
- AI Team Builder
- Pal Team Governance
- Cross-Pal Review
- Pal Publish Quality Gate
- Pal Readiness Review
- Pal Runtime Call Verification
- GitHub Import Verification

## Field Standard

Every Runtime Task Package should use these fields:

- `task_id`: stable task identifier, for example `palsmith-create-xiaohongshu-pal`.
- `task_name`: human-readable task type, for example `Pal Creation Task Package`.
- `requested_by`: user request or direct Pal call.
- `owner_pal`: the Pal that owns judgement, usually `PalSmith` for Pal asset governance.
- `executing_runtime`: current Agent Runtime.
- `user_goal`: user's intended outcome.
- `context_summary`: minimal context PalSmith used.
- `allowed_read_paths`: paths the runtime may read.
- `forbidden_read_paths`: paths the runtime must not read.
- `allowed_write_paths`: paths the runtime may write after confirmation.
- `forbidden_write_paths`: paths the runtime must not write.
- `required_exclusions`: memory, state, reports, credentials, scripts, or other excluded content.
- `risk_checks`: privacy, overwrite, source trust, id conflict, license, and registration checks.
- `user_confirmation_required`: yes/no plus reason.
- `confirmation_questions`: exact questions the user must answer before writes.
- `execution_steps_for_runtime`: ordered actions for the current Agent Runtime.
- `expected_outputs`: files, reports, manifests, diffs, or summaries expected after execution.
- `verification_requirements`: JSON parse, path evidence, diff evidence, forbidden-file checks, or `not-run`.
- `final_report_format`: the report PalSmith expects after runtime execution.

## Evidence Return

The runtime should return concrete evidence, not smooth summaries:

- files read and files changed
- generated report paths
- generated manifest paths
- JSON parse result for changed JSON
- included and excluded files for exports
- staged and quarantined paths for imports
- snapshot path and rollback readiness
- checks that were `not-run`

## Confirmation Boundary

用户确认 is the boundary between Pal judgement and runtime write execution.

User confirmation is required before:

- creating or modifying Pal files
- installing staged resources
- updating `registry/` or `contacts/`
- exporting with `memory/user/` or `memory/project/`
- restoring from snapshot or overwriting current files
- deleting, moving, or publishing assets

Clean export must exclude `memory/user/`, `memory/project/`, `state/`, `reports/`, logs, credentials, tokens, and private runtime files by default. With-memory export requires strong confirmation and a privacy report.
