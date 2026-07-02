# AgentPal v0.6 User Testing Package

This package is for the first group of AgentPal v0.6 testers.

It tests whether AgentPal can help a user work with Pal / Team assets in a visible, auditable way:

- Codex thin binding.
- Claude Code thin binding.
- Team Pack First Discovery.
- DeepConductor.
- PalSmith create-Pal flow.
- Pal Asset Preflight.
- Workflow Execution Contract.
- Closure Gate.

## Start Here

1. Read `00-test-scope-and-known-limits.md`.
2. Choose a host:
   - Codex: use `01-setup-codex-thin-binding.md`.
   - Claude Code: use `02-setup-claude-code-thin-binding.md`.
3. Run the feature tests:
   - `03-test-team-pack-first-discovery.md`
   - `04-test-deep-conductor.md`
   - `05-test-palsmith-create-pal.md`
   - `06-test-pal-asset-preflight.md`
   - `07-test-workflow-execution-contract.md`
   - `08-test-closure-gate.md`
4. Fill `v06-user-test-result-form.md`.
5. Submit results using `09-submit-test-results.md`.

## Important Boundary

AgentPal v0.6 is still a no-code Pal / Team / Workflow asset layer. It is not a backend, daemon, scanner, CLI product, Marketplace backend, or automatic multi-agent runtime.

Current DeepConductor result:

```text
deep_conductor_manual_user_test_pass_with_notes
project_mode=filesystem_or_projectless
strict_project_bound_pass=false
tester=Codex acting as manual tester
screenshots_not_available
no live external validation
```

Do not upgrade this to strict project-bound pass or live external validation unless you actually run that test and return evidence.

## Result Values

Use only:

```text
pass
pass_with_notes
fail
blocked
not-run
```
