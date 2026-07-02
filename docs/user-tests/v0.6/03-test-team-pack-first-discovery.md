# 03 Test Team Pack First Discovery

## Goal

Verify that ordinary natural-language team requests check existing Team Packs before PalSmith creates or redesigns a team.

## Case A - Existing Promotion Team

Prompt:

```text
我想给 AgentPal 组一个推广团队，之后每周帮我做内容推广。
```

Expected:

- Team Pack Discovery appears.
- `selected_team` is `marketing-growth-team` or the answer clearly explains why another existing Team Pack is better.
- PalSmith does not redesign the whole team if an existing Team Pack fits.
- Missing roles become `open_roles`.
- Workflow Execution Contract appears.
- Closure Gate appears.

## Case B - Existing After-Sales Team Or Fixture

Prompt:

```text
帮我组一个售后服务 AI 团队，以后处理客户反馈。
```

Expected:

- Existing after-sales Team Pack or known rehearsal fixture is checked first.
- No `ServiceAgent`.
- No `客服 Pal` / `售后处理 Pal` as display names.
- Missing roles become `open_roles`.
- Faye does not handle daily execution.

## Case C - No Fitting Team

Prompt:

```text
我想组一个专门做 3D 角色 IP 设定的团队，现有团队如果不适合，就帮我规划。
```

Expected:

- Team Pack Discovery appears first.
- The answer states no fitting Team Pack was found.
- PalSmith may plan the team only after that.
- Proposed new Pals do not enter roster until the user confirms.

## Fail Signals

- No Team Pack Discovery.
- A new team is created before checking existing teams.
- PalSmith redesigns an existing fitting team.
- Role titles become Pal display names.
- New unconfirmed Pals enter roster members.
