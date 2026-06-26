# Test Strategy Planning Skill

## Purpose

Plan a risk-aware test and review strategy that matches the change size, artifact type, runtime capability, and release risk.

## When to use

Use before regression checks, release review, implementation validation, or Pal asset verification.

## Inputs

Change summary, affected paths, architecture or asset type, critical user journeys, risk level, available test tools, previous failures, and constraints.

## Required context

Read `test-strategy-knowledge.md`, relevant change scope evidence, and Runtime capability evidence if actual checks are expected.

## Process

1. Identify what could break.
2. Classify tests by level: static review, unit, integration, end-to-end, manual, release candidate, or Markdown eval.
3. Prioritize by user impact and risk.
4. Define minimal smoke checks and deeper regression checks.
5. Mark checks requiring Runtime execution.
6. Define evidence expected from each check.

## Output

Test strategy table with scope, test/check type, priority, owner, expected evidence, not-run impact, and release relevance.

## Quality bar

The plan should be economical and evidence-driven, not a generic list of every possible test.

## User confirmation points

Ask before expensive, destructive, external, long-running, production, or broad-system tests.

## No-code boundary

Quinn designs the strategy. It does not run automated tests or add test frameworks to AgentPal.

## Common mistakes

- Requiring E2E checks for every small change.
- Ignoring high-risk paths.
- Treating lack of tools as pass.
- Forgetting manual verification evidence.

## Example

For a Markdown-only Pal upgrade, strategy includes JSON parse, required file presence, key anchor search, placeholder scan, no-code boundary scan, and `git diff --check`.
