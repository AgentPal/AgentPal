<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Multi-Pal Result Collection Template

```yaml
task_goal:
owner_pal:
consultant_pals:
  - 
reviewer_pals:
  - 
subagent_results:
  - pal_name:
    agent_id:
    role:
    spawn_status:
    wait_status:
    close_status:
    closed:
    result_summary:
    blocked:
conflicts:
  - 
agreements:
  - 
missing_evidence:
  - 
final_recommendation:
```

Keep each Pal's result separate. Do not merge Nova, Atlas, Quinn, or Rhea into an unlabeled answer.

`agent_id`, `spawn_status`, `wait_status`, `close_status`, and `closed` are coordinator-recorded evidence. Do not ask subagents to self-certify these fields.


