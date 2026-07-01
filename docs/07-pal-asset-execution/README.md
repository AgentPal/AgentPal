# Pal Asset Execution

Pal Asset Execution is the rule that a Pal should work from its own task
assets, not only from its name, persona, model common sense, or a tool call.

In simple words: a Pal is useful because it has identity, role boundaries,
knowledge, workflows, Skills, runtime policy, memory rules, and quality gates.
For serious work, those assets must shape the answer.

## Why This Exists

A Pal should not be only:

- a nice name;
- a short persona;
- a roleplay prompt;
- a runtime tool with a Pal name attached after the fact.

For a substantive task, the Pal should be able to answer:

- which assets were needed;
- which assets were loaded;
- which assets were missing;
- whether it was safe to continue;
- which tools were used, if any;
- how the Pal checked the result.

## Core Terms

| Term | Meaning |
| --- | --- |
| Asset Loading Gate | The pre-work check that decides which assets are needed and whether the task can proceed. |
| Task Asset Packet | A compact record of required assets, loaded assets, missing assets, allowed tool calls, blocked tool calls, and go/no-go decision. |
| Asset Use Summary | The post-work record of which assets actually shaped the work and how quality was checked. |
| Missing Asset Plan | A repair plan when important assets are absent or too weak. |

## Correct Flow

```text
User asks task
-> Pal identifies task type
-> Pal loads task-relevant assets
-> Pal forms Task Asset Packet
-> Pal executes / selects tools
-> Tool returns output if used
-> Pal verifies with quality gate
-> Pal reports Asset Use Summary
```

## Wrong Flow

```text
User asks task
-> Runtime calls tool directly
-> Pal name is attached after the fact
-> Pal cannot explain which assets were used
```

That wrong flow should be treated as `fail_asset_usage_regression` or downgraded
to an honest missing-asset fallback.

## Tools Are Not Pal Assets

Image generation, browser tools, shell commands, Codex, Claude Code, MCP tools,
design plugins, and other host capabilities are execution tools. They can help
after the Pal has formed direction and verification criteria from its own
assets.

A tool can produce an output. It does not by itself prove that a Pal has design
judgement, product knowledge, workflow discipline, memory rules, or a quality
gate.

## Common User Questions

### Why did you say you did not use Luma assets?

Because a real Luma Pal must have its own Pal assets available and loaded. If
only a design tool or a Luma-style fixture is present, the result must be
reported as a fixture or fallback, not as real Luma work.

### ImageGen generated an image. Why is that not Luma design ability?

ImageGen is a host execution tool. Luma design ability would require Luma's own
identity, voice, design thinking, logo principles, workflow, tool policy, and
quality gate to guide and review the generation.

### Why can a new Pal not be only persona?

Persona can shape tone, but it does not define job knowledge, workflows, tool
boundaries, memory policy, collaboration rules, or evals. Persona-only can be a
seed, not an executable Pal.

### When can a Pal answer lightly?

Small greetings, one-line clarifications, status summaries from current
evidence, and typo fixes can use a lightweight path. Professional tasks,
tool-backed work, Pal creation, Pal upgrades, QA, release, privacy, or
customer-sensitive work should be asset-grounded.

## Missing Assets

When core assets are missing, the Pal should not pretend the task is complete.
It should choose one of these:

- continue with a named limited fallback;
- answer only the safe part and produce a Missing Asset Plan;
- stop and ask for the missing asset, source, or user confirmation.

## Evidence From R198-R200

- R198 created the global Pal Asset Execution Contract, Asset Loading Gate,
  Task Asset Packet, Asset Use Summary, and Missing Asset Plan.
- R199 proved in real Codex host threads that complex Pal tasks enter the
  asset path, direct tool calls are not enough, persona-only is not executable,
  and typo fixes can stay lightweight.
- R200 proved controlled writes can be limited to a test fixture after a write
  plan, with the real user custom Pal, official Pals, and contacts unchanged.

R200's controlled-write fixture is a test artifact. It is not an official Pal,
not a user-installed Pal, and not a public listing.

## Official Pal Adoption Spot-Check

R202 checked the 10 official bundled Pals for Pal Asset Execution adoption. The
result is a spot-check and phased adoption plan, not a completed per-Pal
migration.

R203 completed Phase 1 entry adoption across the official bundled Pals. Each
official Pal now has an entry note for substantive asset-grounded work and a
lightweight path for simple cases. Full per-Pal representative regressions
remain future work.

R204 added Phase 2 Task Asset Packet and Asset Use Summary examples for five
high-priority Pals: Mira, PalSmith, Atlas, Quinn, and Nova. These examples are
guidance, not verified host regression results.

R205 ran representative Codex host regressions for those same five
high-priority Pals. The result is scoped representative task-family evidence
with Quinn review, not a full verification of all official Pals and not a
release or remote publication claim.

R206 adds the Phase 3 plan for all official Pals. It records the 10-Pal
coverage matrix and prepares R207 to run representative host regressions for
Faye, Harper, Morgan, Rhea, and Vega. R206 is planning evidence, not execution
evidence.

R207 ran those five remaining representative Codex host regressions and Quinn
reviewed the set. Combined with R205, all 10 official bundled Pals now have one
representative task-family host regression for Pal Asset Execution adoption.
This remains scoped evidence, not a full certification of every task family and
not a runtime, release, or contacts change.

R208 adds a scoped certification plan. The plan explains that certification can
only be granted for one Pal plus one task family after a separate evidence gate
and Quinn / QA review. R208 does not certify any Pal by itself.

Read:

- [Official Pal adoption spot-check](official-pal-adoption-spot-check.md)
- [Phase 3 official Pal regression plan](phase-3-official-pal-regression-plan.md)
- [Scoped certification plan](scoped-certification-plan.md)
- [Scoped certification checklist](scoped-certification-checklist.md)
