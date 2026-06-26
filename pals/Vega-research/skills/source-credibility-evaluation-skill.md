# source-credibility-evaluation

## Purpose

Evaluate whether a source is suitable for a claim, using authority, freshness, evidence, bias, traceability, and task fit.

## When to use

Use whenever Vega receives sources from Runtime, a user, or another Pal.

## Inputs

Source metadata, source content summary, claim to support, domain risk, and competing sources.

## Required context

Source credibility knowledge, source inventory, copyright boundary, and task risk level.

## Process

1. Identify source type: official, primary, academic, standards, reputable secondary, community, marketing, repost, or unknown.
2. Check author or publisher authority for this topic.
3. Check publication and update date against freshness need.
4. Check evidence trail, citations, methodology, or reproducible details.
5. Check commercial, political, institutional, or community bias.
6. Cross-check against at least one independent source when risk warrants.
7. Mark suitability for each claim type.

## Output

Credibility note with trust level, usable claims, unusable claims, bias notes, freshness notes, and confidence effect.

## Quality bar

The review must distinguish "source exists" from "source supports this exact claim."

## User confirmation points

Ask before relying on weak sources for high-impact decisions or when only a single source supports a critical claim.

## No-code boundary

This skill evaluates evidence. It does not automate verification tooling or add scanners.

## Common mistakes

- Treating an official source as current without checking date.
- Treating popularity as evidence.
- Ignoring a source's business interest.
- Using a source outside its expertise.

## Example

A vendor pricing page is strong for its own current price if freshly accessed, but weak for claims about competitor quality.

