# R250 Old Simple Pal Mode Scan

## Scope

Checked active fresh-install and binding entry surfaces:

- `AGENTS.md`
- `agentpal.json`
- `core/`
- `orchestration/runtime-response-gate.md`
- `templates/project-binding/`
- `plugins/codex/plugins/agentpal/skills/`
- `integrations/claude-code/agentpal-project-binder/`
- `shared/agentpal_binding_common.py`
- `official/pals/Mira-main/PAL.md`
- `official/pals/Mira-main/AGENTS.md`
- `official/pals/Mira-main/SKILL.md`
- selected Mira core and routing skills

## Exact Legacy Phrase Scan

Command:

```powershell
rg -n "Current active mode: Simple Pal Mode only|Current v0\.1 patterns|Current v0\.1 output|Current v0\.1 Output|active_mode.*Simple Pal Mode|Simple Pal Mode remains" .
```

Result:

```text
archive/migration-from-v0.3/release-candidate-docs/10-agentpal-final-release-verification-report.md:27:Simple Pal Mode remains the current runtime policy. Future orchestration content is marked as design foundation rather than active Deep Conductor or Subagent Mode behavior.
plugins/codex/plugins/agentpal/skills/agentpal-repair/SKILL.md:33:   "Current active mode: Simple Pal Mode only", `active_mode: "Simple Pal Mode"`,
plugins/codex/plugins/agentpal/skills/agentpal-repair/SKILL.md:34:   "Current v0.1 patterns", or "Current v0.1 output".
```

Interpretation:

- `archive/...` is historical archive, not a fresh-install entry.
- `agentpal-repair/SKILL.md` keeps the old phrases only as negative detection examples for damaged bindings.
- No active fresh-install entry still asserts `Current active mode: Simple Pal Mode only`.
- No active fresh-install entry still asserts `Current v0.1 patterns` or `Current v0.1 output`.

## Active Entry Scan

Command:

```powershell
rg -n "agentpal-v0\.5|AgentPal v0\.5|Current runtime policy: AgentPal v0\.5|Current active mode: Simple Pal Mode only|Current v0\.1 patterns|Current v0\.1 output|Current v0\.1 Output|Simple Pal Mode remains|active_mode.*Simple Pal Mode|simple-pal-mode-runtime-contract" AGENTS.md agentpal.json core official/pals/Mira-main/PAL.md official/pals/Mira-main/AGENTS.md official/pals/Mira-main/SKILL.md official/pals/Mira-main/core official/pals/Mira-main/skills/task-triage official/pals/Mira-main/skills/pal-router templates/project-binding plugins/codex integrations/claude-code shared/agentpal_binding_common.py
```

Result:

```text
plugins/codex/plugins/agentpal/skills/agentpal-repair/SKILL.md:33:   "Current active mode: Simple Pal Mode only", `active_mode: "Simple Pal Mode"`,
plugins/codex/plugins/agentpal/skills/agentpal-repair/SKILL.md:34:   "Current v0.1 patterns", or "Current v0.1 output".
```

Interpretation:

- Active entry scan passes.
- Remaining hits are intentional repair detection strings, not active runtime instructions.
