# Memory Protocol

## 记忆类型

- user：用户偏好和长期约定。
- project：项目目标、任务、决策和阻塞。
- tools：工具用法经验。
- runtime：Runtime、模型、推理强度、Skill、插件、外部 Runtime 和路由决策经验。
- collaboration：协作经验。
- skill-memory：可沉淀技能。

## 隐私规则

敏感信息不得写入公开包。共享上下文前必须剔除密码、凭据、支付信息和无关个人记忆。

运行时记忆也可能包含用户环境信息。发布公开包前，应检查 `memory/runtime/`，避免提交私人配置、内部工具名称、密钥路径或敏感服务信息。

