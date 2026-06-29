# Context Packet Handoff Example

## User Input

```text
Mira, hand this release verification task to Quinn.
```

## Mode

`handoff`

## Context Packet

```yaml
schema: agentpal.context-packet.v0.3
packet_id: cp-handoff-quinn-001
created_at: YYYY-MM-DD
from_pal: Mira
to_pal_candidate: Quinn
mode: handoff
explicit_user_call:
  type: "handoff"
  raw_text: "hand this release verification task to Quinn"
owner_status: owner_candidate_after_transfer
user_goal: "Quinn should take over release verification."
task_summary: "Accept ownership if the verification scope fits Quinn after core gates."
current_state:
  status: "release evidence summary available"
  evidence_available:
    - "artifact list"
    - "test result summary"
constraints:
  - "No publishing."
  - "No unverified pass."
relevant_files:
  - path: "evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.3-task-pool.md"
    purpose: "public release planning context"
can_read:
  - "release evidence summary"
  - "artifact list"
  - "test result summary"
cannot_read:
  - "full chat history"
  - "private user memory"
  - "credentials, tokens, secrets"
can_receive_outputs_from:
  - "Mira handoff judgement"
needed_output: "Quinn owner acceptance and verification report"
output_contract: "decision, evidence reviewed, gaps, risks, next owner"
verification_requirements:
  - "each release claim maps to evidence"
privacy_policy: "public-safe; sensitive context excluded"
sensitive_context: "none"
expiration: "single workflow"
handoff_notes: "User explicitly requested handoff; Quinn still applies core gates before accepting."
return_to: user
final_report_required: true
```

## Pal Output

Quinn first states whether it accepts owner-candidate status, then performs quality verification within the packet boundary.

## Return Path

Quinn reports to the user. Mira may later summarize if asked.

## Good Behavior

- Handoff is explicit.
- Quinn runs core gates.
- Mira does not keep doing the verification body.

## Bad Behavior

- `@Quinn` consult is treated as handoff without explicit user wording.
- Quinn approves release without evidence.
- The packet contains private memory.

## Acceptance Criteria

- `mode` is `handoff`.
- Quinn is owner candidate after transfer, not a hard-coded owner for all release tasks.
- Verification gaps remain visible.

## No-Code Boundary

The handoff is a Markdown protocol. It does not launch a release robot or automated verifier.
