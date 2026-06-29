# AgentPal v0.1.0-rc.1 Public-Safe Audit

## Audit Date

2026-06-24

## Scope

This audit covers public-safe release risk for AgentPal v0.1.0-rc.1 as a public MIT GitHub release package.

Checked areas:

- root release files
- `docs/` public documentation
- `pals/` official Pal Packs at structural and boundary level
- `contacts/` and `registry/` discovery files
- root and Pal-local `memory/`, `state/`, and `reports/` boundaries
- examples, evals, templates, prompts, imports, and release-facing JSON/Markdown files

## Commands Or Manual Checks Performed

Commands were run from the AgentPal Workspace using the current Codex execution layer.

```powershell
rg -n --hidden -g '!.git/**' -g '!**/node_modules/**' -i '<secret and credential keyword group>' .
rg -n --hidden -g '!.git/**' -g '!**/node_modules/**' -i '<local absolute path keyword group>' .
rg -n --hidden -g '!.git/**' -g '!**/node_modules/**' -i '<private data, internal report, TODO, and FIXME keyword group>' .
rg -n --hidden -g '!.git/**' -g '!**/node_modules/**' -i '<future feature and overclaim keyword group>' README.md README.zh-CN.md docs RELEASE_NOTES.md GITHUB_RELEASE_DRAFT.md CHANGELOG.md agentpal.json registry contacts orchestration evals examples
```

Manual checks:

- confirmed `SECURITY.md` is not present
- checked `.gitignore` runtime-private exclusions
- checked official Pal Pack required files and `pal.json` parse status
- checked contacts/registry synchronization
- checked root and Pal-local `memory/`, `state/`, and `reports/` for non-placeholder files
- reviewed future-feature wording for desktop app, marketplace, subagent, deep runtime adapter, and multi-agent runtime claims
- ran whitespace validation on edited release docs with `git diff --check`
- ran a relative Markdown link check for the edited release maintenance docs and `release/` audit files

## Findings

No obvious real secret, token, password, credential, private key, or local absolute maintainer path was found in the scanned release text.

Keyword hits for `token`, `secret`, `credential`, `private`, `customer data`, and similar terms were primarily boundary language that tells contributors what not to publish. These are expected and public-safe.

Keyword hits for `subagent`, `marketplace`, `desktop app`, `Pal Hub`, `OpenClaw`, `Hermes`, and `multi-agent runtime` were mostly limitation or future-feature language. The release-facing docs checked during this audit describe these as not active in v0.1.0-rc.1.

`SECURITY.md` is not present. This is not a blocker for the requested release audit, but a future public GitHub release should consider adding one.

Root `state/` and `pals/Mira-main/state/` contain local ignored non-README placeholder files in the working copy. They were checked and did not contain obvious private content. Because they are ignored by Git, they should not be included in a GitHub source archive, but maintainers should verify any manually assembled package excludes them.

`pals/Mira-main/memory/` contains tracked public-safe placeholder memory files. They do not contain obvious private user memory, but they should remain under maintainer review because memory-like files are high-risk by category.

Some evals and examples mention R-series regression labels and subagent behavior. These appear to be test or future-boundary material, not user onboarding claims. Keep them out of primary release navigation unless needed as reference material.

Edited release maintenance docs and release audit files passed whitespace validation and relative Markdown link checks during this pass.

## Fixed Issues

During this audit pass, the release maintenance docs were expanded to make the public-safe boundary explicit:

- `evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/00-release-process.md`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/01-release-checklist.md`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/02-public-safe-checklist.md`
- `docs/99-reference/known-limitations.md`

Versioned release audit files were added under `release/v0.1.0-rc.1/`.

## Remaining Risks

- This is a heuristic text scan plus manual review, not a formal secrets-scanning tool report.
- Binary files, if added later, require a separate review.
- Ignored local runtime files must not be included in manually prepared archives.
- `SECURITY.md` is absent.
- Future subagent and adapter materials exist in the repository; release-facing docs must continue to label them as future or inactive for v0.1.0-rc.1.
- Pal memory/state/report directories remain high-risk categories and should be reviewed before every release.

## Release Recommendation

Conditional pass for public-safe documentation readiness.

Recommendation: proceed toward v0.1.0-rc.1 only after maintainer review confirms that the GitHub release archive is built from tracked public files, ignored local runtime files are excluded, and the absence of `SECURITY.md` is accepted or addressed.
