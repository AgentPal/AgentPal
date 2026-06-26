# Rhea Source Coverage Matrix

Access date: 2026-06-26

| Capability area | Supporting sources | Coverage | Remaining limitation |
| --- | --- | --- | --- |
| system-runtime-role | SRC-02, SRC-05, SRC-08 | Strong | Local AgentPal boundary remains no-code and narrower than real SRE operations. |
| runtime-capability-assessment | SRC-09, SRC-11 | Strong | Requires current Runtime evidence before claims about local capability. |
| permission-boundary-review | SRC-03, SRC-10 | Strong | Does not replace organization-specific access policy. |
| least-privilege | SRC-03, SRC-10, SRC-11 | Strong | Least privilege is a principle, not a single checklist. |
| no-code-boundary-audit | SRC-05, SRC-09 | Medium-high | AgentPal-specific forbidden file list is local project policy. |
| file-directory-safety-review | SRC-04, SRC-08, SRC-09 | Medium-high | File safety depends on local paths and user intent. |
| risk-classification | SRC-04, SRC-06 | Strong | Rhea scale is local operational judgement. |
| approval-gate-design | SRC-06, SRC-08, SRC-10 | Strong | User confirmation does not remove technical risk. |
| execution-evidence-review | SRC-09, SRC-11 | Strong | Evidence quality depends on Runtime output. |
| environment-troubleshooting | SRC-02, SRC-09, local Rhea assets | Medium-high | Needs current environment details per task. |
| release-safety-review | SRC-01, SRC-02, SRC-12, SRC-14 | Strong | AgentPal release is Markdown/JSON, not service deployment. |
| rollback-readiness | SRC-01, SRC-12, SRC-13 | Strong | Some local file changes may need backup rather than deployment rollback. |
| incident-review | SRC-06, SRC-07 | Strong | Rhea supports review, not incident commander execution. |

