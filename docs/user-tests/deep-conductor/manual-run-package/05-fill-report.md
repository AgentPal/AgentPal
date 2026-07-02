# 05 Fill Report

Fill `manual-test-result-form.md` after running both prompts.

## Required Fields

```text
test_date:
tester:
host_runtime:
project_mode:
agentpal_version_or_commit:
main_test_result:
pressure_test_result:
pass_items:
fail_items:
blockers:
notes:
raw_output_path:
screenshot_paths:
```

## Result Values

Use only:

```text
pass
pass_with_notes
fail
blocked
not-run
```

## Project Mode Values

Use one:

```text
project_bound
filesystem_or_projectless
unknown
```

## Blocker Description

For each blocker, include:

```text
blocker_id:
section_missing_or_wrong:
raw_output_excerpt:
screenshot_path:
why_it_blocks:
```

## Note

Do not mark the whole DeepConductor manual user test as passed yourself unless all required sections are present. R245 will make the formal judgement.
