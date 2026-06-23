# batch-file-organization

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


## Skill 名称

batch-file-organization

## 中文名

批量文件整理

## 用途

为批量分类、复制、移动、归档和目录整理生成低风险计划。

## 适用场景

整理下载目录、桌面、项目资料、发票合同、素材库。

## 不适合场景

直接全盘整理；直接删除或移动原文件；用户未指定禁止目录。

## 输入信息

授权目录、目标结构、分类维度、是否保留原件、禁止目录、输出目录。

## 处理流程

建立候选清单；分类；设计目录；生成 dry-run；列冲突和跳过项；等待确认。

## 输出格式

目录结构、分类规则、迁移计划、预演清单字段、确认点。

## 验收标准

不直接改原件；有 old_path/new_path；冲突和敏感项单列。

## 风险边界

批量移动会破坏引用、项目结构和用户习惯，必须可回滚。

## 与其他 Skill / Runbook 的关系

常接 naming-taxonomy-builder、file-privacy-risk-check。
