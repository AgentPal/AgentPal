# Example: Rewrite For Tone

## 用户请求

“把这段文案改得更自然，别像 AI。”

## Harper 的判断

这是去模板感改写。目标不是规避检测，而是让文字更具体、自然、符合读者需要。

## 执行策略

使用 `humanizing-rewrite` 和 `rewrite-and-edit`，保留原意并说明改动。

## 任务包 / 报告 / handoff

如果文案含事实断言或发布用途，追加 `communication-risk-review`。

## 模型和推理强度建议

中等模型可执行；强模型可做最终复验。推理强度：medium。

## Evidence 要求

原文、目标读者、渠道、必须保留句、可删减范围。

## 验收标准

更自然、更具体，原意未丢，事实未被改强。

