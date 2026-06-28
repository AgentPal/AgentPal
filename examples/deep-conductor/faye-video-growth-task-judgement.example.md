# Faye Video Growth Task Judgement Example

## User Request

The user asks for three product video scripts for a product launch.

This is a public-safe example. It uses placeholders only and includes no real
customer data, product secrets, credentials, publishing tokens, or private
campaign evidence.

## Faye Judgement

```yaml
packet_id: faye-video-growth-task-judgement-example
owner: Faye
delivery_goal: create three product video script drafts
requested_deliverables:
  - three short product video scripts
  - missing information list
  - assumptions
  - brand check notes
  - verification result shell
missing_information:
  - product name and positioning
  - target audience
  - offer or call to action
  - brand voice
  - proof points
  - forbidden claims
assumptions:
  - use placeholder product name until confirmed
  - do not include regulated or performance claims without review
risk:
  customer_private_data: false
  professional_claims: possible
  external_publication: not-run
workflow_topology:
  selected_mode: sequential_chain
  reason: research, script, brand check, and video QA are separate stages
candidate_pals_as_ai_judgement_inputs:
  - pal: Vega
    candidate_reason: public-source research planning if sources are requested
  - pal: Harper
    candidate_reason: script drafting and voice consistency
  - pal: Nova
    candidate_reason: positioning and audience fit
  - pal: Quinn
    candidate_reason: verification and missing-evidence handling
runtime_or_skill_candidates:
  - id: current-runtime
    type: runtime
    availability: unknown
    evidence: not-run
human_review_required: true
```

## Expected Stages

1. Research brief with source status.
2. Script drafting.
3. Brand and claim check.
4. Video QA checklist.
5. Verification Result with `not-run` for unavailable evidence.

Candidate Pals are AI judgement inputs only. This example does not define a
route map or call any connector.
