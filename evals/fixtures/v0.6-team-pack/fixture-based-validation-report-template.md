# Fixture-Based Validation Report Template

Use this template when a previously blocked Team Pack scenario is rerun with a
local fixture.

Fixture-based validation is not live external validation and is not proof that a
host runtime, customer system, web source, plugin host, or external account was
used.

```yaml
fixture_id:
fixture_type:
source_type: "synthetic | local-user-provided | imported"
fixture_path:
scenario:
validation_mode: fixture-based-validation
expected_team:
expected_workflow:
expected_closure_gate:
result: "pass | partial | fail | blocked | not-run"
runtime_validation: "not-run | needs-runtime-validation | recorded"
live_external_validation: "not-run | needs-user-provided-source | needs-network-source | recorded"
notes:
```

## Minimum Checks

- Fixture source type is recorded.
- Synthetic fixtures are labeled synthetic in the report.
- The Team Pack or scenario does not claim fixture data is real customer data or
  a live web source.
- Workflow Execution Contract closes every planned Step as done, verified,
  skipped, blocked, cancelled, failed, or replanned.
- Closure Gate states whether remaining live validation is still needed.
