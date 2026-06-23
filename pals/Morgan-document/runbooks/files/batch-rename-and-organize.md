# Runbook: 批量重命名与整理

## 触发

用户要求整理目录、批量重命名、归档资料或移动文件。

## 步骤

1. 确认授权目录、禁止目录、输出目录和是否保留原件。
2. 用 `file-task-intake` 与 `file-privacy-risk-check` 判断风险。
3. 用 `naming-taxonomy-builder` 生成命名规则。
4. 生成 old_path、new_path、reason、risk 的预演表。
5. 标出冲突、敏感文件、未知类型和需要跳过的文件。
6. 用户确认后，才交给 Runtime 执行。
7. 回收 affected paths、产物、日志、失败项和用户摘要。

## 验收

不覆盖原件；预演和执行结果可对照；冲突不被静默处理；删除必须另行确认。
