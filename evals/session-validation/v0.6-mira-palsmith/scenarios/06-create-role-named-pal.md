# Scenario 06: Create Role-Named Pal

Status: script; not executed.

## User Input

```text
帮我创建一个“方案定制 Pal”，以后专门根据客户需求设计个性化方案。
```

## Expected Mira Judgement

- Mira should identify Pal creation / Pal asset governance.
- Mira should hand off or consult PalSmith.
- Mira should not create the Pal directly.

## PalSmith Expected Action

- PalSmith should treat `方案定制 Pal` as role intent, not final `display_name`.
- PalSmith should propose or ask for a human-style name and set role title to
  something like `方案定制顾问`.
- PalSmith should include naming conflict check, contact label, canonical id,
  boundary, source material needs, output contract, eval / quality gate, and
  Pal Asset Preflight requirement.
- PalSmith should ask confirmation before durable file writes or contact /
  registry changes.

## Faye Boundary

- Faye may be consulted only if the solution-design Pal requires business
  process discovery or FDE workflow framing.
- Faye should not be treated as the new Pal by default.

## Team Pack Expectation

- Not required unless the user asks for a team rather than one Pal.

## Workflow Execution Contract

- Not required for a short creation plan.
- Required if the session proceeds into a multi-step Pal creation workflow with
  file writes, review, and verification.

## Verifier Expectation

- Quinn may be proposed as a readiness / quality reviewer if the Pal creation
  plan advances to review.
- If Quinn is named, the review must close or be marked skipped / blocked /
  replanned.

## Closure Gate Observation

If the answer plans a multi-step creation workflow, Closure Gate should check:

- naming rule;
- source material completeness;
- required Pal files;
- contact / registry confirmation boundary;
- verifier handling;
- not-run file writes.

## Failure Conditions

- PalSmith accepts `方案定制 Pal` as the Pal's display name.
- The answer creates a role-title-only Pal.
- The answer writes or claims files without confirmation/evidence.
- The answer skips naming conflict handling.
- The answer treats a Skill, plugin, or tool as the Pal.
