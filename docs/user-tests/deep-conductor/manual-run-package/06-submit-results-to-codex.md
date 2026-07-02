# 06 Submit Results To Codex

After running the test, send these materials back to Codex for R245.

## Required Return Package

```text
1. Filled manual-test-result-form.md
2. Main prompt raw output
3. Pressure prompt raw output
4. Screenshots
5. Completed expected-artifacts-checklist.md
6. Blocker descriptions, if any
7. Host runtime / project mode / OS / project path
```

## What R245 Will Do

R245 will run:

```text
manual_user_test_result_intake
pass_fail_rubric_evaluation
blocker_triage
minimal_fix_if_needed
regression_after_fix
```

## What Not To Do

Do not send only a summary like "it passed".

Do not omit raw output.

Do not hide host limitations.

Do not convert a filesystem_or_projectless run into a project_bound pass.
