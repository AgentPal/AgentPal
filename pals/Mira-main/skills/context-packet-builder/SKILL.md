---
name: context-packet-builder
description: Build minimal Context Packets for Pal collaboration.
---

# Context Packet Builder

## When to use

Use before consult, delegate, handoff, review, or joint work with another Pal.

## Inputs needed

- from Pal
- target Pal
- mode
- user goal
- current state
- relevant files
- privacy constraints
- needed output

## Steps

1. Remove unrelated context.
2. Remove sensitive data unless approved.
3. Define needed output.
4. Add verification requirements.
5. Add Pal Mode Validity fields for specialist work.
6. Keep scope minimal.

## Output format

Context Packet fields.

For specialist handoff, include:

- `required_response_fingerprint`
- `required_output_contract`
- `minimum_asset_loading`
- `allow_codex_generic_answer: false`
- `fallback_if_no_asset: true`
- `asset_usage_proof_required`

The target Pal must use its Response Fingerprint, Output Contract, and at least one Pal asset or fallback method. If no Pal asset or fallback method was used, label it `Codex generic answer`.

如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。

## Safety notes

Never forward full chat history or full project content by default.

