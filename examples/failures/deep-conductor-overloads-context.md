# Failure: Deep Conductor Overloads Context

## Wrong Behavior

Deep Conductor copies full chat history, all Pal Packs, all project files, all profiles, and all previous reports into every Context Packet and Runtime task package.

## Why Wrong

Deep Conductor must control context. Broad loading increases cost, leaks private context, destroys reviewer isolation, and makes verification harder. Index-known paths are not content reads.

## Correct Behavior

Mira creates a Context Budget Plan with index-only, full-text, summarize-first, memory sources, `cannot_read`, `context_read_count`, `profile_read_count`, and `memory_used`. Each packet receives only the context needed for its role.

## Corresponding Eval

`evals/orchestration/token-budget-in-conductor-self-test.md`
