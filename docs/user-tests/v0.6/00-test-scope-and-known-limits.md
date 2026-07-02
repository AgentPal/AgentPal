# 00 Test Scope And Known Limits

## What This Test Covers

This package tests the v0.6 user-facing behavior of AgentPal:

- A user can enable or inspect a thin binding in Codex or Claude Code.
- Natural-language team requests run Team Pack First Discovery.
- Existing Team Packs are reused when they fit.
- PalSmith creates or upgrades Pal / Team assets only when needed.
- Pal work is asset-aware and uses Pal Asset Preflight.
- Workflow Execution Contract records owners, steps, verifier, skipped work, and replan notes.
- Closure Gate prevents false completion.
- DeepConductor can correct wrong assignment pressure.

## What This Test Does Not Prove

This test does not prove:

- strict Codex project-bound DeepConductor pass unless you run that exact host path;
- live external user validation;
- Marketplace publication;
- one-command public installation;
- automatic backend/runtime execution;
- full certification of all Pal task families;
- live customer-data processing.

## Required Notes To Preserve

```text
DeepConductor current manual result: pass_with_notes
project_mode=filesystem_or_projectless
strict_project_bound_pass=false
tester=Codex acting as manual tester
screenshots_not_available
no live external validation
```

## Safety

Do not provide secrets, customer private data, production logs, payment information, or confidential company material during the test.

Use sample projects, fixtures, or sanitized content.

## Host Modes

Use these values in the result form:

```text
project_bound
filesystem_or_projectless
unknown
```

If the host cannot prove it loaded an independent project-bound thread, record:

```text
project_mode=filesystem_or_projectless
strict_project_bound_pass=false
```
