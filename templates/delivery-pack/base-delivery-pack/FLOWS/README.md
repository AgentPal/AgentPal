# Flow Packs

Flow Packs describe reusable business processes inside one Project.

Use one file per flow when a real Delivery Pack is filled.

## Flow Pack Shell

```text
flow_id:
flow_name:
business_goal:
inputs:
outputs:
candidate_pals:
candidate_agent_skill_refs:
customer_private_inputs:
human_review_needed:
acceptance_checks:
status:
```

Candidate Pals and Agent Skill refs are AI judgement inputs only. They are not route maps or execution claims.
