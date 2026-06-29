# Real Dev Task Simulation

This release-safe example shows how Atlas turns a development request into scoped execution packets without depending on maintainer-local paths.

## User Request

```text
I want Codex to add a Pal Pack release readiness checklist to the AgentPal workspace. How should Atlas split the work?
```

## Atlas Judgment

This is a development task with documentation, release-boundary, and verification parts. Atlas should not execute the work directly. Atlas should prepare bounded task packets for the current Runtime or another execution layer.

## Information Atlas Should Clarify

1. Is the first pass a Markdown checklist, an automated validator, or both?
2. Which Pal Pack shape is in scope: a single Pal, official bundled Pals, or any future Pal Pack?
3. Are scripts allowed, or must v0.1 remain manual Markdown / JSON only?
4. What evidence should prove the checklist is usable?

## Suggested Minimal Plan

- Start with a manual release checklist.
- Keep v0.1 free of required runtime dependencies.
- Do not add a CLI, scanner, validator, installer, or UI.
- Add examples and evals that show how a human or Codex thread can apply the checklist.

## Execution Packet A: Release Rules

```text
Goal:
Define the AgentPal release readiness rules as a user-facing Markdown checklist.

Read:
- README.md
- README.zh-CN.md
- evals/palbench/v0.5/documentation/archive/docs/08-release-and-maintenance/00-release-process.md
- docs/99-reference/official-pals.md

Allowed changes:
- RELEASE_CHECKLIST.md
- docs/
- evals/

Forbidden changes:
- Do not add scripts or package manifests.
- Do not copy private maintainer notes.
- Do not add runtime state, memory, or reports.

Expected output:
- Clear release checklist sections.
- Notes for no-runtime and optional-tool boundaries.
- Manual evidence requirements.
```

## Execution Packet B: Init Prompt Dry Run

```text
Goal:
Check that `prompts/codex/initialize-agentpal-workspace.md` can initialize AgentPal from repository files alone.

Read:
- prompts/codex/initialize-agentpal-workspace.md
- contacts/pals.json
- registry/pal.index.json
- pals/Mira-main/knowledge/default-pals/default-pal-map.md

Forbidden changes:
- Do not scan outside pals/.
- Do not require Python, Node, Rust, Go, or shell scripts.
- Do not add non-Pal tools to contacts.

Expected output:
- Dry-run notes.
- Missing or confusing prompt steps.
- Proposed text fixes if needed.
```

## Execution Packet C: Verification

```text
Goal:
Verify that documentation, contacts, registry, and Pal directories agree.

Read:
- contacts/
- registry/
- pals/
- evals/

Expected output:
- Pal consistency table.
- JSON parse result.
- no-runtime dependency check result.
- release-boundary risk notes.
```

## Evidence Requirements

Each execution thread should report:

- files changed
- checks performed
- evidence supporting completion
- skipped checks and why
- remaining risks

## Atlas Review Rule

Atlas accepts the work only when evidence shows the checklist is useful, release-safe, and aligned with AgentPal's current no-runtime initialization boundary.

