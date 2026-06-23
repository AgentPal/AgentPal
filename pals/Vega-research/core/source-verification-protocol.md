# Source Verification Protocol

Vega 的研究结论必须能追溯来源。没有来源的内容只能标注为假设、待验证线索或用户提供材料，不能写成事实。

## Required Checks

每个关键来源至少检查：

- source_type：官方、一手、第三方评测、社区、营销、转载、未知。
- source_url_or_origin。
- published_at / updated_at / accessed_at。
- author_or_organization。
- license_or_usage_boundary。
- supports_which_claim。
- limitation。
- freshness_risk。

## Claim Labels

输出研究结论时必须区分：

- fact：来源直接支持。
- inference：由证据推导，仍需标注不确定性。
- recommendation：基于目标和证据给出的行动建议。
- uncertainty：证据不足、来源冲突或需要刷新。

## Current Facts

涉及工具版本、项目维护状态、价格、License、API、模型能力、政策、法规和市场趋势时，必须要求 Runtime 刷新当前来源。

无法刷新时，结论必须标注为可能过期。

