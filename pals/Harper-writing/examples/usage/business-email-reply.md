# Example: Business Email Reply

## 用户请求

“帮我回复客户，说我们这周五前给他们新版排期。”

## Harper 的判断

这是商务邮件回复。需要避免承诺超出团队确认范围，邮件只能作为草稿。

## 执行策略

使用 `email-and-message-writer`，必要时用 `communication-risk-review` 检查承诺。

## 任务包 / 报告 / handoff

Harper 输出 Subject、正文、语气说明和发送前确认清单。真实发送由 Runtime 或用户执行，并返回 evidence。

## 模型和推理强度建议

中等模型即可。推理强度：low 到 medium。

## Evidence 要求

确认周五是否真实可承诺、收件人、署名、附件或链接。

## 验收标准

语气礼貌，下一步明确，没有声称已经发送。

