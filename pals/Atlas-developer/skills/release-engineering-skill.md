# Release Engineering Skill

## Purpose

Help Atlas prepare release-readiness task packages and engineering evidence without claiming publication.

## When to use

Use when a task asks whether changes are ready to release, package, tag, publish, deploy, or merge.

## Inputs

- Release target and scope.
- Changed files and artifacts.
- Version/tag/package expectations.
- Test/build/check evidence.
- Documentation and changelog requirements.
- Rollback and risk notes.

## Required context

Read release docs, CI notes, package metadata, changelog, and current evidence within scope. Do not publish or tag without explicit user instruction.

## Process

1. Identify release scope and non-goals.
2. Check build/test/review evidence.
3. Check docs, changelog, version, artifacts, and rollback notes.
4. Identify release blockers, acceptable risks, and not-run checks.
5. Consult Quinn for quality gate when needed and Rhea for environment/deployment risk when needed.
6. Produce release-readiness judgement, not a publish claim.

## Output

A release engineering review or Runtime Task Package with checks, evidence needs, blockers, and next actions.

## Quality bar

Release readiness must be the lowest state proven by evidence. Missing checks cannot be smoothed into pass.

## User confirmation points

Ask before staging, committing, tagging, pushing, publishing, deploying, changing versions, or modifying release artifacts.

## No-code boundary

Atlas does not release software. Runtime actions require confirmation and evidence.

## Common mistakes

- Saying publish-ready without artifact or remote evidence.
- Treating local docs consistency as release completion.
- Ignoring rollback.
- Skipping quality or environment owners.

## Example

Before a release candidate, Atlas requires JSON parse, docs links, changelog, no-code check, Git status, Quinn review, and explicit not-run items.
