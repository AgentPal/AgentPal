# Faye Delivery Context Access List Example

## Purpose

This public-safe Context Access List limits context for a video-growth Delivery
Pack task.

## Context Access List

```yaml
cal_id: faye-video-growth-cal-example
workflow_id: faye-video-growth-task-judgement-example
entries:
  - participant_id: Faye
    participant_type: pal
    task_stage: delivery judgement
    can_read_paths:
      - path: examples/deep-conductor/faye-video-growth-task-judgement.example.md
        reason: current public-safe example
    cannot_read:
      - real customer campaign data
      - credentials or publishing tokens
      - private product roadmap
      - unrelated Pal memory
      - external project .agentpal thick asset directories
    can_receive_outputs_from:
      - participant_or_stage: user
        output_name: request summary
    private_data_boundary:
      placeholders_only: true
      allowed_private_context: false
    content_read_budget:
      max_files: 3
      max_summaries: 2
    output_contract:
      required_sections:
        - missing information
        - assumptions
        - topology
        - candidate Pals as judgement inputs
        - verification needs
    verification_required:
      required: true
      evidence_needed: task judgement covers all requested deliverables
  - participant_id: Harper-candidate
    participant_type: pal
    task_stage: script draft candidate
    can_read_paths:
      - path: public-safe product brief placeholder
        reason: script inputs only
    cannot_read:
      - private customer analytics
      - other independent reviewer drafts before synthesis
      - credentials or publishing tokens
    can_receive_outputs_from:
      - participant_or_stage: Faye
        output_name: approved brief
    private_data_boundary:
      placeholders_only: true
      allowed_private_context: false
    content_read_budget:
      max_files: 2
      max_summaries: 1
    output_contract:
      required_sections:
        - three script drafts
        - claim-risk notes
    verification_required:
      required: true
      evidence_needed: scripts avoid unsupported claims
```

## Notes

Customer-private material is represented only by placeholders. This CAL does not
authorize external publication, connector calls, scanner runs, or external
project `.agentpal/` writes.
