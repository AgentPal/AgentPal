# search-strategy-design

## Purpose

Design a source and query plan that lets Runtime gather relevant, fresh, and cross-checkable evidence.

## When to use

Use when external web, documentation, academic, market, GitHub, or product evidence is needed.

## Inputs

Research question, source constraints, freshness need, target domains, known terms, excluded terms, and preferred evidence types.

## Required context

Question frame, source credibility knowledge, copyright boundary, and user-approved search scope.

## Process

1. Select source types: official docs, primary data, academic, standards, reputable analysis, user research, community evidence, or news.
2. Create query clusters for primary question and subquestions.
3. Include opposing, risk, limitation, and failure queries.
4. Prioritize primary and official sources where possible.
5. Define source metadata Runtime must return.
6. Define stop conditions and minimum coverage.

## Output

Search plan with source classes, query clusters, domains to prioritize or avoid, evidence metadata, and coverage target.

## Quality bar

The plan must produce diverse enough sources to avoid one-source bias and narrow enough queries to avoid noise.

## User confirmation points

Confirm paid sources, private sources, controversial topics, broad web sweeps, or searches involving sensitive user material.

## No-code boundary

Vega designs the search plan. Runtime executes web access. AgentPal does not gain a crawler, downloader, scanner, or search app.

## Common mistakes

- Searching only the user's first wording.
- Ignoring official documentation.
- Ignoring counter-evidence.
- Treating SEO pages as primary evidence.

## Example

For an AI API comparison, use official docs, pricing pages, changelogs, SDK docs, issue trackers, and independent evaluations; include queries for limits, deprecations, security, and migration risks.

