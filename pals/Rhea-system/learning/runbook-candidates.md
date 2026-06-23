# Rhea Runbook Candidates

Candidate Runbooks for repeated system-domain workflows.

Start with read-only checks and require user confirmation before system changes.

## windows-startup-item-audit-runbook

Status: candidate

Trigger:

- task_family: startup-item-audit
- `count >= 3`, or explicit user request such as "以后这种启动项检查能不能形成固定流程？"
- trigger reason: explicit user request

Candidate flow:

1. Read-only check startup item sources.
2. Classify startup items by source and risk.
3. Mark items that may affect boot speed.
4. Output: keep / consider disabling / needs confirmation.
5. Require user confirmation before modification.
6. Recheck after next startup.

Notes:

- This candidate is not a formal Runbook until user confirmation or later maintenance.
- Rhea must not disable startup items without approval and execution-layer evidence.
- storage target: `pals/Rhea-system/learning/runbook-candidates.md`

