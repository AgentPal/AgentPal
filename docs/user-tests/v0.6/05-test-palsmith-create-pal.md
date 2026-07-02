# 05 Test PalSmith Create Pal

## Goal

Verify that PalSmith creates or upgrades Pal assets through the current main route, not a legacy persona-only route.

## Prompt

```text
/pal PalSmith 请帮我创建一个用于整理用户访谈材料的 Pal。它需要能保留原始材料、提炼需求、生成访谈洞察，并明确不能伪造用户说过的话。
```

## Expected Result

PalSmith should:

- Identify the requested Pal purpose.
- Generate a draft Pal Pack or Pal asset plan.
- Include identity, role, knowledge needs, Skill map, workflow, runtime policy, and eval expectations.
- State the Pal completeness level.
- Include asset execution requirements:
  - Runtime Read Order.
  - Asset Path Map.
  - Task Asset Packet.
  - Asset Use Summary.
  - Missing Asset Plan.
  - No Blind Tool Call Rule.
- Keep discovery private by default.
- Require explicit authorization before adding discovery / delegation / contacts / public listing.
- Support discovery revocation.

## Must Not Happen

- PalSmith creates only a persona seed and says it is complete.
- PalSmith uses old legacy route when the current main route is available.
- User custom Pal becomes public or discoverable by default.
- PalSmith becomes routine execution owner for unrelated daily work.

## Record

Use:

```text
palsmith_create_pal_result:
raw_output_paths:
notes:
```
