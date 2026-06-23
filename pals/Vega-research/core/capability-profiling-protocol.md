# Capability Profiling Protocol

Pal 应为 Agent、模型、Skill、插件建立可刷新能力画像。

## Profile Fields

能力画像至少包含：

- name
- kind
- best_for
- not_suitable_for
- prompt_style
- refresh_rule
- confidence
- last_checked
- known_risks

## Matrices

- `capabilities/agent-capability-matrix.md`
- `capabilities/model-capability-matrix.md`
- `capabilities/skill-capability-matrix.md`
- `capabilities/plugin-capability-matrix.md`
- `capabilities/task-routing-matrix.md` as a legacy-named capability consideration matrix, not a route map

## Expiry

能力画像不能永久假设准确。模型升级、插件变化、权限变化、任务失败或用户反馈后，应刷新画像。

## Use

能力选择时先查能力画像，再由当前 AI 根据上下文逐案决定模型、强度、Skill、插件、工具、外部 Runtime 或 Pal 协作候选。

