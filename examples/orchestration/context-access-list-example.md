# Context Access List Example

This is a synthetic example.

```yaml
schema: agentpal.context-access-list.v0.1
workflow_id: example-workflow
step_id: step-1
recipient_type: pal
recipient_id: selected-owner
task: prepare a bounded task package
need_output: Task Package with goal, constraints, relevant assets, steps, acceptance criteria, risks, and evidence required
can_read_paths:
  - path: README.md
    reason: project overview
  - path: docs/relevant-note.md
    reason: task-specific detail
can_read_summaries:
  - summary_id: prior-routing-summary
    reason: similar task outcome
can_receive_outputs_from:
  - step_id: mira-intake
    output_type: user goal summary
cannot_read:
  - full_agentpal_workspace
  - all_pals
  - all_project_files
  - private_user_memory
  - credentials_or_secrets
content_read_budget:
  max_files: 5
index_known_paths:
  - path: docs/
    source: directory listing
content_read_files:
  - path: README.md
    evidence: opened as content
output_contract: Task Package
verification_required: true
```

## Quinn Quality Recheck Example

```yaml
schema: agentpal.context-access-list.v0.1
workflow_id: r30-claude-binding-review
step_id: quinn-quality-recheck
recipient_type: pal
recipient_id: Quinn-quality
task: Recheck whether the Claude Code project binding regression result is supported by evidence.
need_output: pass/fail judgement, failure points, evidence gaps, files requiring rework
can_read_paths:
  - path: reports/release-binding-report.example.md
    reason: reported regression result
  - path: evals/claude-code-one-prompt-install-self-test.md
    reason: expected install behavior
  - path: docs/04-runtime-guides/02-use-with-claude-code.md
    reason: public user-facing binding guidance
can_read_summaries:
  - summary_id: project-binding-public-safe-summary
    reason: prior binding outcome without private content
can_receive_outputs_from:
  - step_id: atlas-binding-fix
    output_type: final implementation summary only
cannot_read:
  - private_user_memory
  - unrelated_pal_persona
  - unauthorized_external_directories
  - credentials_or_secrets
  - raw_external_agent_full_trace
  - all_project_files
content_read_budget:
  max_files: 5
  max_large_files: 0
index_known_paths:
  - path: reports/
    source: resource index
content_read_files:
  - path: reports/release-binding-report.example.md
    evidence: opened as content for quality recheck
output_contract: quality-review-pass-fail-with-evidence
verification_required: true
```
