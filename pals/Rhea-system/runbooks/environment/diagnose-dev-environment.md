# Diagnose Development Environment Runbook

用于生成开发环境只读诊断任务。

## Required Context

- 操作系统。
- 目标工具或项目。
- 错误摘要。
- 项目要求或配置文件摘要。
- 允许读取范围。

## Steps

1. 判断目标工具：Node、Python、Git、.NET、Flutter、Rust、Java、Docker 或其他。
2. 设计只读检查：命令存在、版本、解析路径、项目配置、锁文件、常见冲突。
3. 标记禁止动作：安装、删除、清理、修改 PATH、写配置。
4. 定义 evidence。
5. 判断是否需要从 contacts / registry 解析合适协作对象处理项目代码层问题。

## Output

```text
## 诊断目标
## 只读检查项
## 禁止动作
## Evidence 要求
## 可由当前 owner 从 contacts / registry 逐案解析协作对象的问题
```

## Evidence

- 命令版本。
- 命令路径。
- 项目配置摘要。
- 错误摘要。
- 冲突或缺失项。

## Boundary

只读诊断不是修复。需要写入修复时必须另走审批。

