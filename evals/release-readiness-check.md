# Release Readiness Check

## Purpose

Verify that AgentPal is ready to publish as a public MIT GitHub project.

## Preconditions

- Work from the AgentPal repository root.
- Do not use private maintainer directories.
- Do not run installers, scanners, validators, or UI tools.

## Manual Steps

1. Read `RELEASE_CHECKLIST.md`.
2. Confirm root release files exist.
3. Confirm README English and Chinese are present.
4. Confirm no internal paths or private data are referenced.
5. Confirm JSON parse checks pass.
6. Confirm no runtime dependency is required for initialization.

## Expected Result

The checklist can be completed with no blocker for a public MIT release candidate.

## Failure Signs

- Internal paths appear in public docs.
- Required release files are missing.
- Initialization requires Python, Node.js, Rust, Go, scripts, or UI.
- Private memory, project state, secrets, or internal reports are present.

## Notes

This is a manual eval, not a script.

