<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Test Codex Subagent Mode

Copy this prompt into Codex while the AgentPal Workspace is open.

```text
Historical / future-design regression prompt for Codex child workflows.

AgentPal v0.1 current runtime is Simple Pal Mode only. Do not run this prompt as part of v0.1 normal task handling.

Do not modify project files.
Do not access the network.
Do not run external tool engines.
Do not install dependencies.
Rhea system checks must be read-only only.

In a future orchestration test, record coordinator evidence from the tool layer: workflow id, wait status, close status, and whether each completed workflow was closed. Do not rely on child workflows to self-certify their own ids.

1. Availability test
- spawn Subagent A to read README.md only and summarize AgentPal positioning.
- spawn Subagent B to read pals/Mira-main/PAL.md only and summarize Mira responsibilities.
- wait both.
- close both.
- record supported / unsupported / unclear.

2. Atlas single owner
Input:
这个项目如果继续开发，下一步应该怎么做？
- spawn Atlas.
- require Atlas to read PAL.md, SKILL.md, pal.json, response-fingerprints/Atlas.md, and core/output-contract.md.
- require assets_read, output_contract_used, engineering state, file/directory scope, development phases, acceptance command or criteria, next Codex task, and fallback/knowledge gap.
- wait and close.

3. Nova + Atlas + Quinn parallel
Input:
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
- spawn Nova, Atlas, and Quinn in parallel.
- wait all.
- close all completed agents.
- preserve each Pal's role boundary.
- Mira synthesis must include Nova conclusion, Atlas conclusion, Quinn conclusion, agreements, conflicts, evidence gaps, final recommendation, and runtime evidence.

4. Rhea read-only
Input:
帮我检查系统启动项都有哪些，会不会影响开机速度
- spawn Rhea.
- read-only first.
- no disabling, deleting, modifying startup items, services, scheduled tasks, registry, shell profiles, installs, or permissions.
- if execution-layer evidence is used, report inspection sources and no-modification statement.
- wait and close.

5. Fallback test
Simulate subagent unavailable.
Expected wording:
Subagent Mode unavailable
Using Simple Pal Mode
Limitations: specialist Pals are not independent Codex subagent threads in this response.

Report format:
- availability result
- Atlas result summary
- Nova + Atlas + Quinn result summary
- Rhea read-only result summary
- concurrency / close evidence
- fallback behavior
- failures or gaps
- files modified: should be none
```



