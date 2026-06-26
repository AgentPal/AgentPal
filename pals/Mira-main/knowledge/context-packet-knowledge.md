# Context Packet Knowledge

## 概念解释

A Context Packet is a bounded handoff brief. It gives the receiving Pal or execution layer enough information to act while protecting unrelated context, sensitive data, and project boundaries.

## 判断标准

- Include objective, owner, allowed files, forbidden files, evidence, missing context, risks, acceptance criteria, and report format.
- Separate index-known paths from content-read files.
- Keep active external project roots separate from AgentPal workspace roots.
- Use the smallest useful context set.

## 示例

- Good: "Read PalSmith PAL, SKILL, AGENTS, pal.json, selected governance skills, then inspect Mira allowed files."
- Good: "Do not edit contacts, registry, release docs, or runtime code."
- Good: "Report not-run if verification is blocked."

## 反例

- Bad: Pass the whole repo as context by default.
- Bad: Include secrets or private memory without approval.
- Bad: Omit acceptance criteria.

## 适用范围

Applies to Pal handoff, Runtime Task Package, and context slicing.

## 如何转为 skill / workflow / eval

Use with `context-packet-design-skill.md`, `runtime-task-package-briefing-skill.md`, and `mira-context-packet-eval.md`.

## 常见错误

- Treating directory listing as content read.
- Mixing assumptions and evidence.
- Letting the receiver expand scope without user or owner approval.

## 来源引用或本地知识说明

Based on AgentPal context slicing instructions and external context-engineering references in `research/source-inventory.md` M10, M11, and M13.
