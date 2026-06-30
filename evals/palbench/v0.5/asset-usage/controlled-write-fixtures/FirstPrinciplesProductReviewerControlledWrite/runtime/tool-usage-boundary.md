# Tool Usage Boundary

Status: R200 controlled write test fixture runtime policy asset.

## Rule

Tools are execution tools, not Pal assets.

Shell commands, Codex, Claude Code, OpenCode, OpenHands, browser tools, MCP
tools, ImageGen, design tools, video tools, data tools, and repository tools do
not define the fixture's judgement, identity, knowledge, workflow, or quality
gate.

## Allowed Use

The host runtime may read or write files only after:

1. the Pal has loaded task-relevant assets;
2. the Pal has produced a Task Asset Packet or equivalent;
3. allowed and blocked paths are named;
4. user confirmation or explicit task authorization is present;
5. the host reports evidence after execution.

## Blocked Use

This fixture must not ask tools to:

- modify `official/pals/`;
- modify `workspace/organization/contacts/`;
- modify `workspace/resources/user-pals/FirstPrinciplesProductReviewer/`;
- create runtime code, CLI, scanner, daemon, connector, backend service, or
  Marketplace backend;
- publish or tag a GitHub Release;
- claim external system execution without current host evidence.
