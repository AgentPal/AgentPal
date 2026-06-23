# Release Candidate RC1 Check

## Purpose

Final manual check before tagging `v0.1.0-rc.1`.

## Checklist

- [ ] README / README.zh-CN are understandable for new GitHub users.
- [ ] INIT_PROMPT.md can be copied directly into Codex.
- [ ] No internal maintainer docs are included.
- [ ] No private data, local maintainer paths, screenshots, or task reports are included.
- [ ] No runtime dependency is required for AgentPal initialization.
- [ ] JSON files are valid.
- [ ] No hardcoded semantic routing.
- [ ] AI Judgement protocol is present.
- [ ] Simple Pal Mode is the only active v0.1 task-handling path.
- [ ] Future runtime orchestration material is marked future-design-only.
- [ ] Current runtime entry files do not contain active Subagent / non-Pal runtime orchestration rules.
- [ ] External project binding is documented.
- [ ] External project removal is documented.
- [ ] Contacts only contain Pal Packs.
- [ ] Failure examples are present.
- [ ] MIT License is present.
- [ ] Release notes are present.
- [ ] Default release contains no bundled runtime tool engine.

## Expected Result

All checklist items can pass with no release blocker.

## Failure Signs

- README implies AgentPal is a desktop app or background service.
- INIT_PROMPT requires running a script or installing a runtime.
- Examples contain real maintainer paths.
- Future runtime orchestration is described as active v0.1 behavior.
- Contacts include tools, models, plugins, MCP servers, or non-Pal runtimes.


