# Runtime Skill Availability Check Package

Use this no-code package when a Pal needs the host Runtime to confirm whether a Skill, plugin, or MCP tool is installed and usable.

```yaml
schema: agentpal.runtime_skill_availability_check_package.v0.1
check_id: ""
host_runtime_candidate:
  name: ""
  known_from_current_context: false
skill_or_plugin_or_mcp_candidates:
  - name: ""
    type: "" # Runtime Skill | plugin | MCP tool | browser tool | office document tool | repo analysis tool | other
    reason: ""
reason_for_check: ""
where_to_check:
  - "current host Runtime visible skills/plugins/tools only"
expected_response:
  must_include:
    - candidate_name
    - available # true | false | unknown | blocked
    - evidence
    - constraints
    - permission_notes
if_available:
  - "Use only within the allowed task package scope."
  - "Return evidence of actual use."
if_unavailable:
  - "Do not substitute silently."
  - "Follow the fallback package or ask for user confirmation."
not_a_fixed_route: true
privacy_notes:
  - "Do not reveal private local Runtime configuration in public reports."
  - "Do not expose credentials, tokens, or internal absolute paths."
```

Availability checks are current-environment checks. They are not public documentation claims and not future guarantees.
