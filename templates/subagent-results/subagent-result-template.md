<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Result Template

```yaml
pal_name:
agent_id: coordinator_fills_after_spawn
role:
mode: Codex Subagent Mode
task_goal:
assets_read:
  - 
output_contract_used:
findings:
  - 
recommendations:
  - 
risks:
  - 
evidence:
  - 
confidence:
blocked: false
needs_followup:
  - 
```

Use this result shape for each Codex Subagent Mode specialist Pal.

The subagent does not need to know its own `agent_id`. Mira or the coordinator fills that field from `spawn_agent` and records wait / close status separately.


