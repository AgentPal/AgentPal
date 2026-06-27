# Mira Deep Conductor Project Summary Example

## User Input

```text
Mira, help me move this project toward release. First make the overall plan, task split, and next-round execution package.
```

## Mira Output Shape

```text
Mira：这是项目级持续目标，不是单次回答。我会使用 Deep Conductor Master Loop 做 no-code 调度规划；它不会自动执行发布、命令、Runtime Skill 或后台任务。

调度理由：
- topology_selected: Project Conductor Workflow + Owner + Verifier
- memory_used: yes/no, with source summary
- capabilities_read: runtime / reasoning / Pal profile candidates if useful
- context_budget: context_read_count, profile_read_count, memory_used

项目任务图摘要：
1. release-doc-audit：owner candidates: Morgan / Quinn；runtime candidate: current host Runtime；verification: no-code and release evidence.
2. runtime-safety-review：owner candidate: Rhea；verification: permissions and release boundary.
3. final-readiness-summary：owner candidate: Mira; verifier candidate: Quinn.

下一轮 Runtime Task Package：
- round_goal: audit release blockers and evidence gaps
- target_runtime_candidate: current host Runtime, not a fixed route
- runtime_skill_candidates: only if current Runtime proves availability
- forbidden_context: private memory, secrets, full chat history
- final_report_format: files read, evidence, not-run, blockers, verification result

Routing Memory candidate:
- write_candidate: after actual evidence exists
- not_a_fixed_route: true
```

## Boundary

Mira explains the plan and next-round package. Mira does not perform release actions or claim execution without Runtime evidence.
