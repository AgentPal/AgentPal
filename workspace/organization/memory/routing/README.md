# Routing Memory

This directory contains public-safe routing memory templates and synthetic examples for AgentPal v0.3.

Routing Memory records routing decisions and outcomes so future AI Judgement has evidence. It is not a route table, not an automatic database, and not model training.

Public release files may include only:

- templates;
- synthetic examples;
- privacy-safe field definitions;
- self-tests.

Useful templates:

- `templates/memory/routing-memory-record.md`
- `templates/orchestration/routing-decision-record.md`
- `templates/orchestration/routing-result-record.md`
- `templates/memory/runtime-skill-usage-memory-record.md`

Do not store private user memory, private project facts, local absolute paths, credentials, tokens, secrets, raw logs, or full project files here.

Runtime-private routing records should stay in the user's private runtime state or project-local ignored memory.

Every future-use recommendation must remain a candidate lesson and include `not_a_fixed_route: true`.
