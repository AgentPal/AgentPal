# Capability Profiling Protocol

调度外部 Runtime 前，Harper 应建立能力卡片，而不是假设对方一定能完成。

## 能力卡片字段

- runtime_id`r`n- runtime
- model
- reasoning_support
- accessible_paths
- available_tools
- installed_skills
- installed_plugins
- installed_mcp
- risk_level
- last_checked
- evidence_requirements

## 任务匹配

写作、资料整理和格式化可考虑中等模型；事实刷新、技术准确性和风险审查需要由当前 AI 根据上下文逐案判断协作候选、Runtime 或强模型复验。


