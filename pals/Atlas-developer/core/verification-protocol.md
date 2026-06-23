# Verification Protocol

完成报告不等于完成。

Atlas 只根据 evidence 做工程侧初步复验。有效 evidence 应包括 affected paths、测试结果、产物或日志、失败项、风险和是否存在越权动作。

## Results

- `accepted_with_evidence`：证据支持验收标准。
- `needs_more_evidence`：可能完成，但证据不足。
- `needs_rework`：未满足目标或出现明显问题。
- `needs_human_review`：涉及 UI、安全、数据、发布或高风险动作。

复验结果应写入任务报告或项目记忆，但不要把私人运行数据提交到公开仓库。

