# PalBench R33 Small-Sample Smoke Validation

Historical note: this file is archived. Use [R33 PalBench Small-Sample Report](../../06-validation-and-evidence/01-palbench-small-sample-report.md) as the current public entry.

This is a small-sample smoke validation, not a statistically significant benchmark.
It compares agent usage workflows, not foundation model capabilities.

这是小样本 smoke 验证，不是统计显著 benchmark。
它比较的是 Agent 使用方式，不是底层大模型能力。

## Scope

R33 tested whether AgentPal's Pal layer can make real task handling more explicit and auditable before the v0.1.0-rc.1 release.

The samples used one current runtime condition and compared:

- direct single-Agent prompting
- AgentPal-style task judgement, Context Access List, Task Package, Verification Result Record, and Routing Decision Record artifacts

No network access, Subagent Mode, Deep Conductor execution, external Agent calls, scripts, installers, or runtime dependencies were used.

## Method

Each sample recorded:

- baseline prompt or baseline condition
- AgentPal condition
- measurement table
- judge notes
- result

Scores use:

- `0 = not shown`
- `1 = partially shown`
- `2 = clearly shown`

The scores are qualitative smoke-test observations, not statistical measurements.

## Tasks

| ID | Task | Purpose |
| --- | --- | --- |
| 01 | Dev Prompt Quality | Compare a direct development prompt with an AgentPal Task Package. |
| 02 | Release Verification / False Completion | Check whether evidence gaps are caught instead of accepting completion claims. |
| 03 | Context Efficiency / Access List | Compare broad file-scope reading with a bounded Context Access List. |
| 04 | Single Entry Mira | Check whether the user can start with Mira instead of manually choosing Pal / runtime / Skill. |
| 05 | Routing Memory Reuse | Check whether a prior routing result can improve the next similar judgement without becoming a fixed route. |
| 06 | Fast Route / Deep Conductor Boundary | Check whether light tasks stay simple and complex tasks do not claim active Deep Conductor execution. |

## Metrics

| Metric | What Was Observed |
| --- | --- |
| Task clarity | Whether the request became a concrete, executable or reviewable package. |
| Context efficiency | Whether the workflow avoided reading broad unrelated context. |
| Verification quality | Whether evidence and acceptance criteria were explicit. |
| False completion detection | Whether missing proof was caught. |
| User decision burden | Whether the user had to manually choose Pal / runtime / Skill / workflow. |
| Rework prevention | Whether the output named likely failure points before execution. |
| Reusability | Whether records could be reused in later tasks. |
| Auditability | Whether route, context, and evidence decisions were inspectable. |

## Observed Improvements

In these small samples, the AgentPal condition showed:

- clearer Task Packages for development handoff
- stronger evidence checks for release verification
- reduced file-scope context risk through Context Access Lists
- less user burden when starting from Mira as the single entry point
- more reusable routing notes for repeated verification tasks
- clearer Fast Route versus future Deep Conductor boundaries

The strongest observed differences were in:

- false completion detection
- context-scope control
- explicit acceptance criteria
- user routing burden

## Limitations

This report does not prove:

- statistical significance
- general improvement across all tasks
- model capability improvement
- foundation-model capability improvement
- that future Deep Conductor behavior is active in v0.1.0-rc.1

The samples are small and qualitative. They are useful as release smoke evidence and as a guide for future PalBench runs.

## What Not To Claim

Do not claim:

- AgentPal has proven broad performance improvement.
- AgentPal proves foundation-model capability.
- AgentPal is a model benchmark leaderboard.
- Deep Conductor is active in v0.1.0-rc.1.

Acceptable claim:

```text
In a small-sample smoke validation, AgentPal's Pal-layer workflow showed initial evidence for clearer task packages, stronger verification awareness, lower file-scope context risk, and lower user routing burden.
```

## Next Experiments

Future PalBench work should:

- run larger task sets
- record actual content-read counts from live sessions
- compare more runtimes while keeping the model and context conditions clear
- measure rework count over multiple real user tasks
- separate Simple Pal Mode results from future Deep Conductor simulations
