# Reviewer Context Packet Template

Use one packet per reviewer candidate. The packet should give a reviewer enough context to answer one review angle without seeing peer drafts or full chat history.

```yaml
schema: agentpal.reviewer-context-packet.v0.3
packet_id:
review_id:
from_pal:
to_reviewer_candidate:
review_mode:
user_goal:
review_question:
review_angle:
current_state:
constraints:
  - <constraint>
allowed_context:
  - <summary-or-path-or-evidence>
cannot_read:
  - full_chat_history_by_default
  - private_user_memory
  - unrelated_pal_assets
  - secrets
excluded_peer_outputs:
  - peer_reviewer_drafts
  - peer_hidden_reasoning
  - peer_intermediate_notes
needed_output:
  - verdict
  - confidence
  - key_findings
  - risks
  - missing_context
  - recommendation
output_contract:
  template: templates/orchestration/reviewer-final-report.md
evidence_requirements:
  - <evidence-or-not-run-label>
privacy_policy:
return_to:
deadline_or_budget:
```

`to_reviewer_candidate` is a candidate for this case, not a fixed route. `review_angle` may be product, implementation, quality, research, system, writing, document, governance, or another capability angle, but the angle itself must not become a routing rule.

`excluded_peer_outputs` defaults to other reviewer drafts, hidden reasoning, and intermediate notes. Do not copy full chat history or unauthorized private memory into this packet.
