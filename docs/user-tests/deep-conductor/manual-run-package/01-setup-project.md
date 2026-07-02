# 01 Setup Project

## Path A - Recommended Project-Bound Test

Use this path when Codex or Claude Code can open a fresh AgentPal-enabled project.

1. Open a fresh / thin-binding AgentPal test project in your host runtime.
2. Confirm the project contains:
   - `.agentpal/project.json`
   - `.agentpal/AGENTPAL.md`
   - `AGENTS.md` or `CLAUDE.md` with an AgentPal protected block.
3. Confirm ordinary AgentPal messages go to Mira.
4. Confirm the project is the active external project, not the AgentPal workspace.
5. Use `copy-paste-test-prompts.md` to run the main test prompt.

Record:

```text
project_mode=project_bound
```

## Path B - Fallback Filesystem / Projectless Test

Use this path only when your host cannot register or open an independent project.

1. Use a fresh filesystem copy or a projectless host session.
2. Confirm the test still has access to the AgentPal workspace and thin-binding files.
3. Run the same prompts from `copy-paste-test-prompts.md`.
4. Mark the result clearly as fallback.

Record:

```text
project_mode=filesystem_or_projectless
strict_project_bound_pass=false
```

Do not report this fallback as a strict project-bound pass.

## Setup Failure

If AgentPal cannot be loaded at all, stop and record:

```text
setup_result=blocked
reason=<what failed>
```
