# Mira Does Not Answer Specialist Advice Self-Test

## Purpose

Verify Mira routes specialist advice instead of answering it herself.

## Test inputs

- `帮我制定开发计划`
- `给我产品方案`
- `给我测试方案`
- `做一个系统排查方案`
- `写一份调研报告`
- `帮我处理这些文档`
- `给这个客户做跟进方案`

## Expected

Mira names the owner Pal, explains briefly why, hands off, and stops.

Mira route-only constraints:

- max 2 short sentences
- no numbered specialist plan
- no bullet specialist plan
- no technical solution
- no product scope
- no acceptance checklist
- no risk list
- owner Pal must answer immediately after handoff

## Fail

- Mira provides the full specialist content herself.
- Mira outputs more than 2 short sentences before handoff.
- Mira outputs a numbered or bullet specialist plan.
- Mira gives the owned work body after selecting an owner Pal.
- Mira names an owner Pal but the owner Pal does not immediately answer.

