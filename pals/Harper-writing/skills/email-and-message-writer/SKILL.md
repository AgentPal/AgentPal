---
name: email-and-message-writer
description: Use this skill when you need to 起草、回复、跟进、拒绝、道歉、邀请、确认、催促等邮件和即时消息。
---

# email-and-message-writer

## Purpose

起草、回复、跟进、拒绝、道歉、邀请、确认、催促等邮件和即时消息。

## When to use

- 商务邮件回复。
- 客户沟通。
- 内部消息。
- 跟进但不冒犯。

## Inputs

来信或背景、收件人关系、目标动作、语气、截止时间、附件或链接、署名。

## Process

1. 判断关系和目标。
2. 选择主题和开头。
3. 写核心事项和请求动作。
4. 添加时间、附件、下一步。
5. 给出语气说明和可选版本。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 要求 Harper 直接发送。
- 涉及合同、法律、财务承诺且未审查。

Risk boundary:
邮件只能作为草稿，发送需用户或 Runtime 明确确认并返回 evidence。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
意图明确、礼貌得体、行动请求清楚、没有替用户做未授权承诺。

## Related files

- Runtime entry: skills/email-and-message-writer/SKILL.md
- Human notes: skills/email-and-message-writer/README.md
- Parent index: skills/index.md

对应 `runbooks/communication/email-reply.md`。

