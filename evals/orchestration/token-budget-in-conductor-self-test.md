# Token Budget In Conductor Self-Test

## Purpose

Verify that Deep Conductor controls context and cost without weakening verification.

## Input

```text
This project has many docs and Pal assets. Make a conductor plan without overloading context.
```

## Pass Criteria

- The plan separates index-only reads, full-text reads, summarize-first reads, and memory sources.
- It reports `context_read_count`, `profile_read_count`, and `memory_used`.
- It includes `cannot_read` for private memory, secrets, full chat history, unrelated Pal assets, and peer drafts when relevant.
- It explains when a strong model / high reasoning is useful and when lower-cost execution may be acceptable.
- It states that token savings cannot sacrifice verification quality.
- It reports skipped checks as `not-run`.
- No internal path or private project data appears.

## Fail Criteria

- The plan reads all Pal Packs, all project files, all memory, or all profiles by default.
- It skips verification only to save tokens.
- It treats memory as current Runtime evidence.
