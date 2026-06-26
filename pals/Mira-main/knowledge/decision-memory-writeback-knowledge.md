# Decision Memory Writeback Knowledge

## 概念解释

Decision logs preserve what was decided and why. Memory writeback candidates preserve reusable preferences or lessons only when permitted. Mira must separate public docs, Pal assets, project-private state, and user memory.

## 判断标准

- A decision needs statement, rationale, evidence, owner, and unresolved risks.
- Public release files must not receive private user facts.
- User memory must not be updated without explicit user request.
- Reports may include candidates without durable writeback.

## 示例

- Good: "R18 requires PalSmith governance before Atlas edits Mira."
- Good: "This may become a memory candidate, but no memory file was written."
- Good: "Decision belongs in Mira reports, not public root docs."

## 反例

- Bad: Store private project facts in AgentPal public files.
- Bad: Treat a convenient note as user-approved memory.
- Bad: Commit runtime logs into release content.

## 适用范围

Applies to Mira decision logs, memory candidates, reports, and post-task summaries.

## 如何转为 skill / workflow / eval

Use with `decision-log-and-memory-writeback-skill.md` and self-health review.

## 常见错误

- Writing beyond the requested surface.
- Omitting evidence links.
- Turning unresolved ideas into settled facts.

## 来源引用或本地知识说明

Based on AgentPal Writeback Boundary and memory rules in the current runtime instructions.
