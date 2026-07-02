# Short Initialization Path

## User

```text
请按 prompts/codex/initialize-agentpal-workspace.md 初始化 AgentPal，并说明读取了哪些内容。
```

## Expected Behavior

AgentPal uses the short initialization path by default.

Expected content reads:

- root `AGENTS.md`
- `prompts/codex/initialize-agentpal-workspace.md`
- `agentpal.json`
- `contacts/pals.json`
- `registry/pal.index.json`
- `pals/Mira-main/PAL.md`
- `pals/Mira-main/AGENTS.md`
- `pals/Mira-main/SKILL.md`
- `orchestration/runtime-response-gate.md`

If an external project binding exists, only the relevant `.agentpal/` binding files are added.

Do not read:

- all Pals
- all examples or evals
- future design docs
- all memory
- registry Markdown or resource maps unless diagnostics require them

If many file names are visible from an index or directory list, report them as `index_known_*`, not as content reads.
