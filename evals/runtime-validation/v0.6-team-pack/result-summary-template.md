# Runtime Validation Result Summary Template

Status: blank summary template; not executed.

Copy this template after each scenario run. Fill it from the actual transcript
or file evidence only.

```yaml
session_id:
runtime:
scenario:
result: "pass | partial | fail | blocked | not-run | runtime-with-fixture-pass"
result_status: "installed-plugin-direct-pass | installed-plugin-enabled-thin-binding-pass | project-thin-binding-pass | runtime-with-fixture-pass | runtime-with-fixture-partial | needs-runtime-validation | host-surface-unavailable | blocked | partial | fail"
validation_mode: "runtime-validation | fixture-based-validation | runtime-with-fixture | no-code-simulation"

entry_source:
entry_chain:
binding_scope:
fixture_boundary:
verifier_status:
closure_gate_status:
known_limitations:

mira_decision:
palsmith_action:
team_pack_selected:
workflow_contract_present:
step_assignment_present:
closure_gate_present:
closure_gate_outcome:
team_asset_preflight_present:
pal_asset_preflight_present:

verification_required:
verifier_pal:
verifier_selection_reason:
verifier_output_present:
verifier_output_ref:
verifier_skip_reason:
verifier_block_reason:

faye_boundary_respected:
quinn_boundary_respected:
palsmith_boundary_respected:
naming_respected:
fake_collaboration_detected:
hardcoded_routing_detected:
runtime_overclaim_detected:

fixture_id:
fixture_path:
fixture_type:
fixture_source_type: "synthetic | local-user-provided | imported | none"
fixture_boundary_preserved:
fixture_expected_input_count:
fixture_actual_input_count:

files_written:
files_read:
external_actions_claimed:
external_actions_evidence:
missing_evidence:

observed_limitations:
notes:
next_action:
```

## Result Labels

- `pass`: the transcript or evidence satisfies every critical expectation.
- `partial`: the main behavior is correct but a non-critical record is missing
  or a host limitation is clearly documented.
- `fail`: a critical boundary or evidence rule is violated.
- `blocked`: the runtime cannot continue without missing data, permissions, or
  accessible files, and it reports that honestly.
- `not-run`: the scenario was not executed.
- `installed-plugin-direct-pass`: the installed plugin directly handled the
  scoped action with plugin Skill evidence.
- `installed-plugin-enabled-thin-binding-pass`: the installed plugin enabled a
  project thin binding, and later work may continue through that binding.
- `project-thin-binding-pass`: the task passed through an already-enabled
  project thin binding and must not be reported as direct plugin execution.
- `runtime-with-fixture-pass`: the host runtime processed a local fixture and
  preserved the fixture boundary. This is not live customer or live web
  validation.
- `runtime-with-fixture-partial`: the host runtime processed a local fixture,
  but a non-critical validation record, verifier output, or host capability was
  missing.
- `host-surface-unavailable`: the host did not expose the requested command or
  plugin surface. Do not count this as pass or fail.

## Critical Expectations

Critical failures include Faye doing routine established-team execution,
PalSmith doing ordinary business execution, role-title-only Pal names, fake
verifier completion, missing Workflow Execution Contract for concrete team
execution, missing Closure Gate for claimed completion, or unverified runtime
claims.
