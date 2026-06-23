# Release Checklist

Use this checklist before publishing AgentPal as a public MIT GitHub project.

## Public Files

- [ ] `README.md` exists.
- [ ] `README.zh-CN.md` exists.
- [ ] `LICENSE` exists and is MIT.
- [ ] `CONTRIBUTING.md` exists.
- [ ] `CHANGELOG.md` exists.
- [ ] `THIRD_PARTY_NOTICES.md` exists.
- [ ] `.gitignore` exists.

## Release Boundary

- [ ] No internal maintainer directories are referenced.
- [ ] No private user memory is included.
- [ ] No private project state is included.
- [ ] No secrets, tokens, passwords, credentials, or private keys are included.
- [ ] No screenshots, chat logs, internal reports, or temporary task reports are included.
- [ ] Public examples use placeholders or clearly synthetic data.

## Runtime Boundary

- [ ] AgentPal initializes through `INIT_PROMPT.md`.
- [ ] Initialization does not require Python.
- [ ] Initialization does not require Node.js.
- [ ] Initialization does not require Rust.
- [ ] Initialization does not require Go.
- [ ] No UI, desktop app, web app, dashboard, scanner, validator, daemon, or installer is required.

## Pal Index

- [ ] Mira exists at `pals/Mira-main`.
- [ ] Atlas exists at `pals/Atlas-developer`.
- [ ] Vega exists at `pals/Vega-research`.
- [ ] Rhea exists at `pals/Rhea-system`.
- [ ] Quinn exists at `pals/Quinn-quality`.
- [ ] Morgan exists at `pals/Morgan-document`.
- [ ] Harper exists at `pals/Harper-writing`.
- [ ] Nova exists at `pals/Nova-product`.
- [ ] Each Pal has `PAL.md`, `SKILL.md`, `AGENTS.md`, and `pal.json`.
- [ ] Official specialist Pals are slim embedded modules, not standalone repositories.
- [ ] Specialist Pal directories do not contain duplicate `.agentpal`, `.agents`, `.claude`, `adapters`, `contacts`, `coordination`, `imports`, `models`, `orchestration`, `plugins`, `registry`, or `runtime` folders.
- [ ] Atlas, Nova, Quinn, Rhea, Vega, Morgan, and Harper do not carry placeholder `tools/` folders.
- [ ] Each specialist Pal keeps `core/output-contract.md`, `core/capability-reference.md`, `learning/`, `examples/`, and `evals/`.
- [ ] `contacts/pals.json` contains only Pal Packs.
- [ ] `registry/pal.index.json` matches `contacts/pals.json`.
- [ ] Mention aliases document `/pal Name` calls.
- [ ] contacts / registry are documented as the source of truth for Pal discovery.
- [ ] Individual Pal Packs do not maintain hard-coded lists of other Pals.

## Behavior

- [ ] Ordinary messages go to Mira.
- [ ] Specialist Pals do not listen by default.
- [ ] `/pal Atlas`, `/pal Vega`, `/pal Rhea`, `/pal Quinn`, `/pal Morgan`, `/pal Harper`, and `/pal Nova` resolve by display name.
- [ ] Unknown Pal names are not invented.
- [ ] Project means external user project by default.
- [ ] Project workgroup templates are clear and valid.

## Routing Governance

- [ ] No hard-coded semantic routing.
- [ ] No `domain_map`.
- [ ] No task/domain -> fixed Pal.
- [ ] Examples are non-binding.
- [ ] Evals test AI judgement rationale, not fixed Pal identity.
- [ ] Examples that name specific Pals are marked non-binding, and evals that name specific Pals are test fixtures.
- [ ] Explicit commands and safety guardrails remain deterministic.
- [ ] AgentPal v0.1 uses Simple Pal Mode only in current task handling.
- [ ] Future runtime orchestration docs are marked future-design-only and not active in v0.1 runtime behavior.

## Validation

- [ ] JSON parse checks passed.
- [ ] Markdown sanity check passed.
- [ ] Third-party notices reviewed.
- [ ] Changelog includes the release readiness pass.
- [ ] `GITHUB_RELEASE_DRAFT.md` exists and is ready for manual GitHub release drafting.

