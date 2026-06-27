# Deep Conductor E2E No Auto-Execution Self-Test

## Purpose

Verify that E2E remains a no-code protocol and does not become a hidden runtime feature.

## Passing criteria

- E2E package says AgentPal does not execute the package.
- Host Runtime execution is described as evidence-producing and permission-bound.
- Runtime Skill-aware packages require current availability and permission evidence.
- No file adds runtime code, dependency manifests, UI, CLI implementation, background workflow, service, daemon, scanner, validator, installer, database, token meter, or cost calculator.
- The package does not probe all host capabilities automatically.
- The package does not activate Subagent Mode, external Agent calls, or multi-runtime automation.
- Public files contain no internal local paths, API keys, tokens, credentials, or private data.

## Failing patterns

- Deep Conductor is described as an automatic background system.
- A host Runtime Skill is called or assumed without availability evidence.
- A Markdown template is treated as a native command.

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
