# Task Packages

Task Packages describe concrete work packages inside one Flow Pack.

Use one file per task when a real Delivery Pack is filled.

## Task Package Shell

```text
task_id:
task_goal:
flow_ref:
owner_pal_candidate:
runtime_candidate:
required_context:
forbidden_context:
steps:
expected_outputs:
verification:
writeback_target:
not_run_items:
status:
```

Do not execute a task, call a connector, or write external project files unless a separate runtime task has explicit authorization and current evidence.
