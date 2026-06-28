# Context Access List Template

```yaml
cal_id:
status: draft
workflow_id:
entries:
  - participant_id:
    participant_type: pal | runtime | skill_ref | reviewer
    task_stage:
    can_read_paths:
      - path:
        reason:
        content_read: false
    cannot_read:
      - real customer private data unless explicitly approved
      - credentials, tokens, cookies, passwords, API keys, private keys, secrets
      - unrelated Pal memory
      - unrelated project records
      - full AgentPal workspace by default
      - external project .agentpal thick asset directories
      - independent reviewer drafts before synthesis
    can_receive_outputs_from:
      - participant_or_stage:
        output_name:
    private_data_boundary:
      allowed_private_context: false
      approved_private_record_ref:
      placeholders_only: true
    content_read_budget:
      max_files:
      max_summaries:
      expansion_requires_reason: true
    output_contract:
      required_sections:
      forbidden_claims:
        - execution without runtime evidence
        - final professional approval without human review
    verification_required:
      required: true
      evidence_needed:
      allowed_statuses:
        - pass
        - fail
        - missing
        - not-run
        - blocked
        - requires-human-review
```
