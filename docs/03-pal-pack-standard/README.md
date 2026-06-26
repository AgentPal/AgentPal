# Pal Pack Standard

## Status

Current for AgentPal `v0.1.0-rc.1`.

This directory is the public standard entry for Pal Packs. It explains the files and folders a runtime-readable Pal should have, what can stay empty, and what must never be published.

## Start Here

- [Standard overview](00-standard-overview.md)
- [Pal Pack structure](01-pal-pack-structure.md)
- [Root files](02-root-files.md)
- [Output contracts and core protocols](03-core-protocols.md)
- [Contacts and registry](10-contacts-and-registry.md)
- [Public/private boundary](11-public-private-boundary.md)
- [Pal Pack checklist](12-pal-pack-checklist.md)
- [Pal import and export](13-pal-import-export.md)
- [Runtime Task Package](14-runtime-task-package.md)
- [Formal Skill assets](15-formal-skill-assets.md)

## Three Levels

| Level | Use it for | Expectation |
| --- | --- | --- |
| Minimal Pal Pack | First working Pal | Required files plus placeholder indexes and public-safe README files |
| Standard Pal Pack | Maintained Pal | Adds usable knowledge, Skills, runbooks, workflows, examples, and evals |
| Official Pal Pack | Bundled AgentPal Pal | Richer assets, self-tests, learning placeholders, and tighter output contracts |

You do not need to fill every directory on day one. Empty directories should still have an index or README placeholder when the standard expects one.

## Not A Pal

Ordinary Skills, plugins, models, MCP servers, runtimes, raw repositories, knowledge packs, and persona packs are not Pals. They may support a Pal, but only valid Pal Pack directories should enter contacts and registry.
