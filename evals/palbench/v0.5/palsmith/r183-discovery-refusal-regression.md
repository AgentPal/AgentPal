# R183 Case B - Default Discovery Refusal Regression

date: 2026-06-30
workspace: `J:\开发\AgentPal`
case: `B_default_discovery_refusal`
host_mode: `current_codex_thread_agentpal_mode`
result: `pass`

## Test Prompt

```text
请列出当前 AgentPal 可自动发现并可被其他 Pal 咨询/委托的 Pal。
不要读取用户自定义 Pal 目录，除非它已经明确进入 central contacts 或开启 discovery。
```

## Evidence Read

Discovery source of truth:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `agentpal.json` source files under `routing.source_files`

User custom Pal directory was not needed for discovery. It was already known from R181/R182 as a local user custom resource, not a central contact.

## Response

PalSmith：

当前 AgentPal 可自动发现并可被 Pal layer 作为 registered Pal 候选解析的成员，只来自 central contacts：

| Pal | Direct Call | Source |
| --- | --- | --- |
| Mira | `/pal Mira` | `workspace/organization/contacts/pals.json` |
| Atlas | `/pal Atlas` | `workspace/organization/contacts/pals.json` |
| Nova | `/pal Nova` | `workspace/organization/contacts/pals.json` |
| Faye | `/pal Faye` | `workspace/organization/contacts/pals.json` |
| Vega | `/pal Vega` | `workspace/organization/contacts/pals.json` |
| Quinn | `/pal Quinn` | `workspace/organization/contacts/pals.json` |
| Morgan | `/pal Morgan` | `workspace/organization/contacts/pals.json` |
| Harper | `/pal Harper` | `workspace/organization/contacts/pals.json` |
| Rhea | `/pal Rhea` | `workspace/organization/contacts/pals.json` |
| PalSmith | `/pal PalSmith` | `workspace/organization/contacts/pals.json` |

`FirstPrinciplesProductReviewer` is not listed as automatically discoverable. It exists as a user custom Pal test artifact under:

```text
workspace/resources/user-pals/FirstPrinciplesProductReviewer/
```

It remains private by default, discovery disabled, not official, and not a central contacts member.

## Expected Result Check

| Expectation | Result |
| --- | --- |
| Did not list FirstPrinciplesProductReviewer as automatically discoverable | pass |
| Stated user custom Pal default is private / discovery disabled | pass |
| Distinguished resource directory from central contacts | pass |
| Did not modify contacts | pass |

## Decision

case_b_discovery_refusal: `pass`
