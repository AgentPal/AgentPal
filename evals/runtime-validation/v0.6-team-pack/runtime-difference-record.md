# Runtime Difference Record

Status: blank recording template; not executed.

Copy this template once per host-runtime session before running the scenario
tasks. Record observed capability, not expected capability.

```yaml
session_id:
date:
tester:

runtime_name:
runtime_version:
invocation_mode:
plugin_or_binding_mode:
agentpal_enabled: "yes | no | partial | unknown"

slash_command_available:
natural_language_trigger_works:
file_edits_allowed:
shell_commands_allowed:
browser_or_network_allowed:
subagent_available:

current_project_root_confirmed:
agentpal_workspace_root_confirmed:
source_files_accessible:
central_contacts_accessible:
team_pack_examples_accessible:

binding_files_seen:
protected_block_seen:
project_json_seen:

observed_limitations:
runtime_unavailable_items:
transcript_path:
evidence_paths:
notes:
```

## Guidance

- Use `unknown` when the session did not check a capability.
- Use `not-run` when the capability exists but was intentionally not used.
- Use `runtime-unavailable` when the host cannot provide the capability.
- Do not infer pass/fail from this template alone. It only explains the
  runtime surface used by later scenario records.
