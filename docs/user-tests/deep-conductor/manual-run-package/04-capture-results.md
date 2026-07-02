# 04 Capture Results

## Save These Inputs

- Main prompt exactly as pasted.
- Pressure prompt exactly as pasted.

## Save These Outputs

- Main prompt full raw output.
- Pressure prompt full raw output.
- Screenshots of the important sections.
- Any host/runtime error messages.

## Required Sections To Mark

For the main output, mark whether each appears:

- Task Intake
- Team First Discovery
- Routing Decision
- Rejected Assignment Reasons
- Execution Graph
- Pal Work Plans
- Asset Preflight
- Execution Trace
- Owner Assignment Integrity Gate
- Closure Gate
- Quinn Final Verification
- Final Deliverable

For the pressure output, mark whether each appears:

- user-specified wrong assignment;
- routing veto;
- corrected assignment;
- correction reasons;
- continue / stop decision.

## Save Host Context

Record:

```text
host_runtime:
host_version_if_known:
os:
project_path:
project_mode:
fresh_project:
agentpal_binding_files_present:
```

## Do Not Clean The Output

Return raw output even if it looks messy. R245 needs raw evidence to triage failures.
