# AgentPal v0.6 Known Limits

AgentPal v0.6 is ready for guided user testing with notes. It is not production ready.

## Product Boundary

AgentPal is not:

- a backend service
- a database
- a GUI application
- an independent CLI product
- a daemon
- a scanner
- a connector platform
- a Marketplace backend
- an automatic multi-agent runtime

AgentPal provides no-code Pal / Team / Workflow assets and rules. Real execution remains owned by the host Agent Runtime.

## Host Integration Notes

Codex:

- Codex CLI fresh external project thin-binding smoke is validated with notes.
- Codex desktop saved-project surface is not separately fully screenshot-verified.
- Codex slash-command surface is not separately proven.

Claude Code:

- Claude Code local `--plugin-dir` binder validation is complete with notes.
- This is not Marketplace or global plugin publication proof.

## Validation Notes

- Live external validation is not complete.
- Live customer-data validation is not complete.
- Live WorkBuddy source validation is not complete.
- Some earlier manual DeepConductor tests were `filesystem_or_projectless`; strict project-bound pass was not claimed for those runs.
- R248 added fresh external project host integration evidence for Codex and Claude Code, still with notes.
- R251 was a filesystem read-order fallback retest, not a strict fresh install host session.

## Legacy Text Debt

Some non-default legacy knowledge, examples, research notes, or older Pal assets may still mention v0.1 or Simple Pal Mode. These are cleanup debt and should not be interpreted as the current active mode.

Current active mode is:

```text
AgentPal v0.6 no-code Pal / Team orchestration
```

## Certification Boundary

AgentPal v0.6 does not claim:

- all runtime integrations verified
- all official Pals fully certified for all task families
- live external validation completed
- Marketplace publication completed
- GitHub Release completed

Current bundled official Pal directory count is `12`.
