# No-Code Future Boundary

AgentPal is a no-code Pal layer, Pal Pack Standard, and AI team framework.

This boundary is not only a v0.3 release constraint. It is the default product direction for v0.3, v0.4, v0.5, and later planning unless a maintainer explicitly changes the product direction in a future decision record.

## Permanent Default Boundary

AgentPal does not become its own Agent Runtime.

AgentPal does not provide or require:

- a CLI product;
- a desktop app or web app;
- a scanner, validator, installer, daemon, background service, database, or automation runtime;
- a native slash-command engine;
- a message bus;
- automatic external Agent calls;
- automatic multi-runtime execution;
- Deep Conductor as an auto-executor.

Real file reads, file writes, commands, publishing, rendering, browser control, office-document work, repository edits, and system operations belong to the host Agent Runtime, such as Codex, Claude Code, OpenCode, OpenHands, Gemini CLI, or another Markdown/JSON-capable runtime.

AgentPal may describe what the host Runtime should do, but the Runtime must provide current evidence before AgentPal claims that execution happened.

## What Future Work Improves

Future AgentPal work should improve the Pal layer:

- Deep Conductor methodology;
- Context Packets and Context Access Lists;
- Multi-Pal Collaboration protocols;
- Capability Inventory profiles;
- Runtime-installed Skill orchestration examples;
- Pal-owned memory and cross-runtime continuity;
- Routing Memory and Runtime Skill usage memory;
- PalBench cases and scoring;
- templates, examples, prompt cards, and evals.

These are written protocols, templates, examples, and evaluation assets. They do not add a new execution product surface.

## v0.4 Default Direction

v0.4 may expand no-code runtime adapter protocol coverage, host Agent Runtime usage guides, Runtime-installed Skill orchestration examples, cross-runtime memory continuity, and Deep Conductor patterns.

v0.4 must not be treated as the default place to build a CLI, scanner, validator, installer, daemon, desktop app, web app, service, or database.

## v0.5 Default Direction

v0.5 may expand Pal Pack ecosystem standards, quality checklists, Awesome Pal Packs style indexes, manual or Agent-executable certification protocols, and community contribution templates.

v0.5 must not be treated as the default place to build a Hub, marketplace backend, certification program service, scanner, validator, installer, daemon, desktop app, web app, or database.

## Explicit Change Rule

A future program feature is possible only after an explicit product-direction decision says AgentPal should stop being only a no-code Pal layer. Until then, all future wording should assume:

```text
AgentPal designs, routes, packages, verifies, remembers, and explains.
The host Agent Runtime executes.
```

## Public Claim Rule

Public docs must distinguish:

- current behavior;
- no-code protocol design;
- future methodology;
- host Runtime capability;
- current evidence.

Do not imply that AgentPal ships runtime automation because a protocol, prompt, template, example, or eval exists.
