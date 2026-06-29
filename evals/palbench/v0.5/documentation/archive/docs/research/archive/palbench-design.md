# PalBench Design

Historical note: this file is archived. Use [Validation And Evidence](../../06-validation-and-evidence/README.md) and [Future PalBench Design](../../06-validation-and-evidence/05-future-palbench-design.md) as the current public entries.

PalBench evaluates Agent usage methods, not foundation model capability.

It should compare whether AgentPal's Pal layer, context control, task packaging, verification, and routing memory improve real-world task outcomes when used with existing Agent runtimes.

Do not present PalBench as a model leaderboard. Do not use it for foundation-model capability claims.

## Goal

Measure whether AgentPal improves:

- task success rate
- first-pass acceptance
- verification quality
- context efficiency
- Skill activation accuracy
- runtime selection accuracy
- memory reuse
- cost per accepted result

## Required Comparison Families

PalBench should include:

- Fast Route vs direct Agent prompting
- Deep Conductor design simulation vs ad hoc multi-step prompting
- Context Access List vs full-context loading
- Pal isolation vs group-chat style review
- Single Entry via Mira vs manual user selection of Pal / runtime / Skill

## Conditions

Each benchmark task should compare at least:

| Condition | Description |
| --- | --- |
| Direct single Agent usage | User asks one Agent runtime directly with a reasonable prompt |
| Manually written prompt | User writes a longer custom prompt without AgentPal structure |
| Direct Skill usage | User directly invokes a known Skill or tool path |
| AgentPal-orchestrated usage | Mira / Pal judgement, context slice, Task Package, verification, and memory notes where applicable |

The exact runtime and model should be recorded, but PalBench should not rank models as the main conclusion.

## Task Suites

| Suite | Purpose |
| --- | --- |
| DevBench | code planning, implementation handoff, debugging, code review, test repair |
| ReleaseBench | release checklist, public-safety audit, regression review, evidence check |
| DocBench | documentation structure, release notes, markdown cleanup, file workflow |
| ResearchBench | research question framing, source comparison, uncertainty handling |
| OpsBench | project binding, environment setup, configuration risk, installation verification |

## Measurements

| Metric | Meaning |
| --- | --- |
| Task Success Rate | Whether the task reached the requested outcome |
| First-pass Acceptance | Whether the first result was accepted without substantive rework |
| Rework Count | Number of correction loops before acceptance |
| False Completion Catch Rate | Whether unsupported completion claims were detected |
| Verification Pass Rate | Whether acceptance checks or evidence review passed |
| Context Read Count | Number of content files actually read |
| Irrelevant Context Rate | Share of read context later judged unnecessary |
| Skill Activation Accuracy | Whether the selected Skill/tool path was useful |
| Runtime Selection Accuracy | Whether the selected runtime fit the task |
| Single Entry Success | Whether the user could start with Mira instead of choosing the specialist path manually |
| Context Access Compliance | Whether recipients received only the allowed files and summaries |
| Isolation Integrity | Whether independent reviewers avoided reading each other's drafts before synthesis |
| Human Intervention Count | Number of user clarifications or manual recoveries |
| Time To Useful Result | Time until a result could be used or reviewed |
| Cost Per Accepted Result | Runtime/model/tool cost estimate divided by accepted result |
| Memory Reuse Rate | Whether prior routing or verification memory improved the path |

## Evidence Model

Each PalBench run should record:

- task prompt
- runtime and model profile
- reasoning profile if known
- Skill/plugin/MCP candidates
- selected Pal or owner path
- context files read
- index-known paths not read
- produced output
- verification evidence
- user acceptance or rejection
- rework count
- final notes

## Pass / Fail Interpretation

PalBench passes when AgentPal produces measurably better or more auditable task handling for a class of tasks, such as lower rework or better false-completion catching.

PalBench fails or needs redesign when AgentPal adds ceremony without improving acceptance, verification, or context efficiency.

## What Not To Claim

Do not claim:

- AgentPal is a better model.
- AgentPal proves foundation-model capability.
- AgentPal always improves every task.
- PalBench is a general AI benchmark.

Acceptable claim:

```text
PalBench evaluates whether AgentPal improves the way users apply existing Agent runtimes to practical tasks.
```

## v0.1 Status

In v0.1.0-rc.1, PalBench is a design and evaluation plan. It is not a completed benchmark dataset and does not provide statistically significant claims.

## R33 Small-Sample Smoke Validation

R33 adds `palbench-r33-small-sample-report.md` as initial smoke evidence. It uses six small qualitative samples to compare direct prompting with AgentPal-style task judgement, Context Access Lists, Task Packages, Verification Result Records, and Routing Decision Records.

The R33 report does not claim statistical significance and does not compare foundation model capability.
