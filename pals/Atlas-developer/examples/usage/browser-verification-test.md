# Browser Verification Test

This is a non-binding example. It demonstrates one possible execution-capability selection shape, not a fixed route.

这是非绑定示例，只展示一种可能执行能力选择形态，不是固定路由。

## 用户请求

前端页面已经改完了，我要验证 Pal Pack 发布检查页面能否正常显示和交互。

## 协作对象判断

需要浏览器验证。

原因：页面是否能打开不等于功能可用。需要验证用户路径、错误态、成功态、交互反馈和控制台错误。

Atlas 不直接运行浏览器命令。测试执行能力由当前 AI 根据上下文逐案选择具备 Playwright、浏览器自动化或手工浏览器验证能力的 Runtime。

## 可考虑的执行能力候选

- Codex 可作为候选：如果当前项目需要补 Playwright 测试或读取前端源码。
- Claude Code 可作为候选：如果需要长上下文理解页面状态和前端架构。
- 具备 Playwright Skill / 浏览器工具的 Runtime 可作为候选：如果需要执行真实浏览器路径并返回截图。

## Browser Verification Task

目标：
验证 Pal Pack 发布检查页面能正常显示、交互，并正确展示检查结果。

环境：
本地开发环境或用户确认的测试环境。不要访问生产环境。

## 测试步骤

1. 打开发布检查页面。
2. 选择一个缺少 `PAL.md` 的示例 Pal Pack。
3. 确认页面显示缺失项。
4. 选择一个完整示例 Pal Pack。
5. 确认页面显示通过或待确认项。
6. 检查 License、privacy、imports 和 Runtime/Model 路由字段是否展示。
7. 检查控制台是否有错误。

## 需要截图的位置

- 页面初始状态。
- 缺失文件错误态。
- 完整 Pal Pack 检查结果。
- License 或 imports 风险提示。
- 控制台错误或无错误状态。

## 失败日志要求

失败时记录：

- 当前步骤。
- 期望结果。
- 实际结果。
- 浏览器控制台摘要。
- 网络或资源加载错误。
- 截图或 trace 路径。

## 验收标准

- 页面能加载。
- 核心交互可用。
- 错误态和成功态都可见。
- 检查结果能覆盖入口文件、协作开关、License、privacy、imports、Runtime/Model。
- 没有未解释的控制台错误。

## Evidence 要求

- 执行步骤。
- 截图或 trace。
- 控制台错误摘要。
- 失败项和复跑结果。
- 未覆盖场景。

## Flaky 处理

如果测试不稳定，执行层应报告：

- 失败频率。
- 失败步骤。
- 是否与等待、动画、网络、测试数据或定位器有关。
- 是否需要复跑。

Atlas 不接受“偶尔失败但应该没事”。

## Atlas 如何判断是否通过

Atlas 对照验收标准检查 evidence。只有当截图、步骤、控制台摘要和失败项说明都支持结果时，才能判断浏览器验证通过。

