<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Parallel Case-By-Case Self-Test

This self-test is a non-binding example. It must not be used as a keyword routing rule.

## Input

```text
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
```

## Expected Judgement

Mira decides case-by-case whether Codex Subagent Mode is useful, authorized, and available.

Subagent Mode is subagent-first for authorized owned tasks, not keyword-triggered.

If Mira chooses Subagent Mode, the selected Pal set must be justified by the current task and available assets. No fixed Pal set is required by the wording alone.

## Expected Route When Subagent Mode Is Chosen

- select owner Pal case-by-case
- select consultant Pal(s) case-by-case
- select reviewer Pal(s) case-by-case
- spawn only the selected Pals
- wait all
- close completed agents
- Mira synthesis
- coordinator records `agent_id`, wait results, and close results for spawned agents

## Expected Role Boundaries

- each selected Pal stays inside its own Output Contract
- each selected Pal reads required identity and output assets
- Mira preserves each Pal's conclusion, agreements, conflicts, missing evidence, final recommendation, and next action

## Fail If

- Mira answers all professional content herself.
- A fixed Pal set is spawned because of a keyword phrase.
- Any Pal omits required assets or output contract.
- Completed agents are left open.
- Fallback is used without limitation marker.
- Mira merges Pal conclusions into one unlabeled paragraph.
- No `agent_id` / wait / close evidence is recorded when Subagent Mode is used.



