# Collaboration Protocol

本 Pal 可以与其它 Pal 协作，但协作者必须从当前 AgentPal 中央 Pal roster 中解析。

## 允许协作模式

- consult：咨询意见，本 Pal 仍是 owner。
- delegate：委托子任务，本 Pal 复验结果。
- handoff：转交 owner，目标 Pal 接管。
- joint_work：共同工作，需要明确 owner / consultant / reviewer。

## Context Packet

转交或协作时，只共享最小必要上下文：

- task_goal
- current_context
- constraints
- requested_output
- evidence_needed
- privacy_boundary

不要共享完整聊天记录、私人记忆、密钥、Token 或无关项目内容。
