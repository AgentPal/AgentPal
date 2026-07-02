# R244 Required Return Materials

## Verdict

`required_return_materials_complete`

## User Must Return

```text
1. Filled manual-test-result-form.md
2. Main prompt raw output
3. Pressure prompt raw output
4. Screenshots
5. Completed expected-artifacts-checklist.md
6. Blocker descriptions, if any
7. Host runtime / project mode / OS / project path
```

## Minimum Fields For R245

```text
test_date:
tester:
host_runtime:
host_version_if_known:
os:
project_path:
project_mode:
fresh_project:
agentpal_version_or_commit:
main_test_result:
pressure_test_result:
main_raw_output_path:
pressure_raw_output_path:
screenshot_paths:
blockers:
notes:
```

## Why These Are Needed

R245 cannot classify pass / fail / blocked from a summary alone. It needs raw evidence to verify:

- Team First Discovery;
- Work Plan;
- Asset Preflight;
- Execution Trace;
- Owner Assignment Integrity;
- Closure Gate;
- Quinn verification;
- overclaim boundaries;
- project mode.
