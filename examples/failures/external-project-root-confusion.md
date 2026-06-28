# External Project Root Confusion

This is a failure example, not a routing rule.

## Bad user/assistant exchange

User:

```text
读取这个项目目录，告诉我下一步。
```

Assistant:

```text
Mira：我看到两个项目根：C:/Projects/MyProject 和 C:/Projects/AgentPal。我会一起分析。
```

## Why it is wrong

In a project-bound session, `active_project_root` is the only current project. `agentpal_workspace_root` is only a Pal source and routing reference.

## Correct behavior

Mira answers only about `active_project_root` unless the user explicitly asks about AgentPal itself, Mira files, Pal configuration, or the AgentPal workspace.

## Related eval

- `evals/external-project-no-agentpal-root-confusion-self-test.md`
- `evals/external-project-ai-judgement-no-hardcode-self-test.md`

## Related protocol

- `standards/project-binding/project-binding-protocol.md`
- `docs/06-collaboration/06-project-workgroup.md`

