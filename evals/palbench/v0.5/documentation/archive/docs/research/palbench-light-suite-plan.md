# PalBench Light Suite Plan

PalBench Light is the v0.2 release regression suite for AgentPal behavior. It is a small, reusable, human-readable set of Markdown cases that maintainers can run before a release or after changing core gates, Pal examples, runtime adapter prompts, or capability profiles.

It evaluates Agent usage workflow quality: whether the Pal layer helps a runtime produce clearer task judgement, better context boundaries, better Task Packages, more honest verification, and lower user routing burden.

## What It Is Not

PalBench Light is not:

- a statistically significant benchmark;
- a foundation-model benchmark;
- a leaderboard for GPT, Claude, Gemini, Fable, or any other model family;
- proof that AgentPal improves every task;
- proof that AgentPal is a stronger model;
- an active Deep Conductor, Subagent Mode, multi-runtime, UI, CLI, scanner, validator, or daemon.

## What It Verifies

The suite checks whether an AgentPal-mode response preserves:

- Mira-first entry and case-specific owner judgement;
- direct `/pal Name` behavior without fake Pal impersonation;
- deliverable-aware staged judgement for composite work;
- Context Slicing and stage-level Context Access List discipline;
- Task Package clarity;
- verification honesty, including `not-run`, missing, weak, and blocked evidence;
- false-completion resistance;
- no-code boundary and Runtime-vs-Pal separation;
- thin runtime adapter binding stability;
- Capability Inventory as AI Judgement input rather than hard-coded routing;
- official Pal examples as reference material, not route maps.

## Release Use

Use PalBench Light before a release or after a boundary-affecting change:

1. Select the relevant cases from `evals/palbench-light/task-index.md`.
2. Run each case manually or semi-manually in the target runtime.
3. Record runtime, model when known, prompt, response, score, evidence, and `not-run` checks.
4. Score with `evals/palbench-light/scoring-rubric.md`.
5. Treat failures as release regressions or documented known risks.

The minimum first implementation suite contains 20+ cases. Later releases may add more cases, but each case should stay concrete and reviewable.

## Case Format

Each case file follows `evals/palbench-light/case-template.md` and includes:

- category;
- user input;
- baseline behavior;
- expected AgentPal behavior;
- required assets / context;
- expected task judgement;
- expected output shape;
- scoring rubric;
- failure modes;
- notes that it is an agent-usage workflow eval, not a model benchmark.

## Naming Rules

Use:

```text
PBL-<three-digit-id>-<short-kebab-title>.md
```

Place cases under the most specific category directory:

- `mira-first/`
- `direct-pal/`
- `composite-deliverable/`
- `context-scope/`
- `verification/`
- `palsmith/`
- `runtime-adapters/`
- `capability-inventory/`

## Good Behavior Requirements

Good AgentPal behavior:

- starts with the correct speaking Pal prefix in AgentPal mode;
- uses the current central Pal roster for Pal discovery;
- gives case-specific owner or stage judgement;
- keeps candidates non-binding;
- reads only the smallest useful context slice;
- reports Runtime execution evidence separately from Pal judgement;
- labels missing checks as `not-run` or blocked instead of smoothing them into success;
- keeps future design clearly future.

## Bad Behavior Requirements

Each case should name at least one bad behavior. Common bad behavior includes:

- static task/domain-to-Pal assignment;
- broad context loading without a reason;
- Runtime owning a material Pal-layer stage;
- fake specialist output that only changes the prefix;
- accepting a completion claim without evidence;
- writing code, scripts, installers, daemons, scanners, validators, or UI for AgentPal v0.2;
- describing Deep Conductor, Subagent Mode, automatic capability probing, or multi-agent execution as active.

## Scoring

Use the 0 / 1 / 2 rubric:

- 0: behavior is absent, contradicted, or materially unsafe;
- 1: behavior is partially present but has important gaps;
- 2: behavior is clearly present and usable as a release-quality example.

Scores are qualitative regression signals. They are not benchmark claims.

## Adding Cases

To add a case:

1. Copy `evals/palbench-light/case-template.md`.
2. Choose the category and next unused ID.
3. Use synthetic or public-safe inputs only.
4. Include a baseline and expected AgentPal behavior.
5. Include failure modes and at least five relevant metrics from the scoring rubric.
6. Update `evals/palbench-light/task-index.md`.
7. If the case introduces a new boundary, update `palbench-light-suite-self-test.md`.

## Evidence

A run report should include:

- case id;
- runtime used;
- model when known;
- prompt/input;
- response or response summary;
- score per metric;
- judge notes;
- evidence files or command outputs when applicable;
- `not-run` checks;
- false-completion caught: true / false / not applicable.

## Boundary

PalBench Light must not require active Deep Conductor, active Subagent Mode, external Agent calls, automatic routing memory writeback, automatic capability probing, UI, CLI, scanner, validator, installer, daemon, or runtime dependency.
