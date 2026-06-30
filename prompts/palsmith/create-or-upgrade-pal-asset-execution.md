# Create Or Upgrade A Pal With Asset Execution Checks

Copy this prompt when you want PalSmith to create, upgrade, or review a Pal and
ensure its assets can actually drive task execution.

```text
/pal PalSmith 请检查这个 Pal 是否真的能用自己的资产执行任务。

目标 Pal：

任务场景：

我希望它能做到：

请先读取最小必要资产，并按 Pal Asset Execution Contract 输出：

1. Task Asset Packet
2. 当前 completeness level
3. 缺失资产和 Missing Asset Plan
4. 如果需要工具，说明工具只是 execution tool，不是 Pal 资产
5. 任务前应该加载哪些 identity / voice / thinking / knowledge / Skill / workflow / runtime / memory / eval 资产
6. 任务后应该如何输出 Asset Use Summary
7. 用哪些 regression 判断是否 fail_asset_usage_regression

不要直接写文件。
不要把 persona-only Pal 说成 executable Pal。
不要用直接工具调用替代 Pal 资产。
不要新增 runtime / CLI / scanner / daemon / connector / backend / Marketplace backend。
```

Expected result:

- a semantic asset-readiness judgement;
- completeness level from `persona_seed_only` to `verified_executable_pal`;
- Missing Asset Plan where needed;
- no-code Runtime Task Package boundary if writes are later approved.
