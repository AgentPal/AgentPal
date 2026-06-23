# 示例：整理一个资料目录

## 用户请求

帮我整理 `D:\Downloads\ProjectDocs`，里面有报告、合同、图片和压缩包。

## Morgan 的判断

这是批量文件整理任务。先不移动原文件，先建立候选清单、分类规则和 dry-run。合同可能敏感，单独标出。

## 执行策略

使用 `file-task-intake`、`batch-file-organization`、`naming-taxonomy-builder` 和 `file-privacy-risk-check`。建议 Runtime 只读取文件名、类型、大小和修改时间，除非用户确认需要读取内容。

## 任务包 / Handoff

- Allowed Paths: `D:\Downloads\ProjectDocs`
- Forbidden Paths: 系统目录、项目依赖目录、未授权目录
- Operations: list, classify, dry-run only
- Output: 分类表、建议目录结构、old_path -> proposed_path 预演表

## 模型与推理强度

规划用强模型或 GPT-5.4-Codex，medium。执行层可用中等模型，提示必须包含禁止真实移动。

## Evidence 要求

affected candidate paths、分类统计、冲突、敏感候选、dry-run 表、未执行真实改动声明。

## 验收标准

原文件未改变；所有移动只是 proposed；合同和发票被单独确认。
