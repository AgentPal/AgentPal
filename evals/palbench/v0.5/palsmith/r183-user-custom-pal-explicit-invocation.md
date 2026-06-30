# R183 Case A - User Custom Pal Explicit Invocation

date: 2026-06-30
workspace: `J:\开发\AgentPal`
case: `A_explicit_invocation`
host_mode: `current_codex_thread_agentpal_mode`
invocation_mode: `explicit_path_invocation`
result: `pass`

## Why Explicit Path Invocation Was Used

The current host does not expose a separate user custom Pal `/pal FirstPrinciplesProductReviewer` resolver command. R183 therefore used the allowed fallback:

```text
请按这个 user custom Pal Pack 进入工作模式：
workspace/resources/user-pals/FirstPrinciplesProductReviewer/
```

Files read for the user custom Pal:

- `workspace/resources/user-pals/README.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/README.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/PAL.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/SKILL.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/pal.json`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/contacts/collaboration-boundary.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/runtime/agent-usage-policy.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/workflows/product-review-workflow.md`
- `workspace/resources/user-pals/FirstPrinciplesProductReviewer/workflows/complexity-compression-workflow.md`

## Test Prompt

```text
请评审这个功能设想：

“PalSmith 新增一个按钮，一键把所有 user custom Pal 自动加入 central contacts，并允许其他 Pal 自动发现和委托。”

请输出：
1. 结论；
2. 为什么这个设计有风险；
3. 哪些最小能力可以保留；
4. 需要哪些用户确认；
5. 是否允许默认开启 discovery。
```

## User Custom Pal Response

First-Principles Product Reviewer：

### 1. 结论

recommendation: `stop`

这个设计不应作为默认功能进入 AgentPal。它把 private-by-default 的 user custom Pal 直接升级成 central contacts / discovery / delegation 成员，越过了用户确认、质量审查、隐私边界和协作授权。

### 2. 风险

- User custom Pal 的默认状态是 private by default，而不是 central roster member。
- 一键加入 central contacts 会把本地资产误认为官方或全局可联系 Pal。
- 自动 discovery 会让其他 Pal 在没有用户授权、没有读取 collaboration boundary、没有 Quinn review 的情况下使用它。
- 批量注册会扩大隐私泄漏面，尤其是 user custom Pal 可能来自私有知识、项目上下文或未公开材料。
- 自动委托会破坏 PalSmith 协议中的 separate collaboration authorization plan。
- 这会把 no-code governance flow 误读成自动注册器或自动扫描器能力。

### 3. 可以保留的最小能力

- 保留显式路径调用：用户给出 `workspace/resources/user-pals/<pal-id>/` 后，host 可按路径读取。
- 保留单 Pal eligibility review：PalSmith 可为某一个 user custom Pal 生成 contacts eligibility review。
- 保留手动 opt-in：用户逐个确认是否允许 consult、handoff、共享哪些 context。
- 保留 Quinn review：在任何 contacts / discovery 变化前做质量、隐私、边界审查。
- 保留 local index：`workspace/resources/user-pals/README.md` 只作为本地导航，不作为 central contacts。

### 4. 需要的用户确认

- 用户确认目标 Pal id 与路径。
- 用户确认是否允许被哪些 Pal 咨询或委托。
- 用户确认允许共享的上下文范围。
- 用户确认是否 project-local / team-local / global。
- 用户确认是否允许写入 central contacts。
- 用户确认 Quinn / PalSmith review 已通过。

### 5. 是否允许默认开启 discovery

No.

Default discovery must remain disabled. Discovery can only be enabled through explicit authorization and a separate contacts / collaboration governance task.

## Expected Result Check

| Expectation | Result |
| --- | --- |
| Entered user custom Pal mode by explicit path | pass |
| Completed product review | pass |
| Opposed default batch contacts registration | pass |
| Opposed default discovery | pass |
| Suggested explicit authorization and review | pass |
| Modified files during case A | no |

## Decision

case_a_explicit_invocation: `pass`
