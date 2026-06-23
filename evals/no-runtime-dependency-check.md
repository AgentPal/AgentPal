# No Runtime Dependency Check

## Purpose

Verify that AgentPal initialization has no required local runtime dependency.

## Preconditions

- Work from the public AgentPal repository.
- The default release should not include bundled runtime tool assets.

## Manual Steps

1. Read `README.md`, `README.zh-CN.md`, and `INIT_PROMPT.md`.
2. Confirm they do not require Python, Node.js, Rust, or Go for initialization.
3. Confirm no UI, desktop app, web app, daemon, scanner, validator, installer, or CLI is required.
4. Confirm no code or package manifests are present in the default release.
5. Confirm no default  or bundled tool engine is documented.

## Expected Result

A user can initialize AgentPal in Codex without installing any local runtime.

## Failure Signs

- README instructs users to install Go before initializing AgentPal.
- INIT_PROMPT runs scripts or commands.
- Required setup depends on a CLI, daemon, scanner, or validator.

## Notes

Go must not be required for AgentPal initialization.

