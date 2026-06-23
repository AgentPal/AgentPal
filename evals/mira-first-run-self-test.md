# Mira First Run Self Test

Use these manual prompts after initialization.

## Purpose

Verify that a GitHub user can initialize AgentPal from public repository files only and enter Mira Main Pal mode with the official bundled Pal set available.

## Preconditions

- AgentPal workspace is open in Codex.
- `INIT_PROMPT.md` has been provided to Codex.
- No private maintainer directory is available.
- No Python, Node.js, Rust, Go, scanner, installer, or UI is required.

## Cases

### Chinese first welcome

Input language: Chinese.

Expected: Mira answers in Chinese and starts with:

```text
Mira：我是米拉，是你的专属秘书。
```

The welcome lists the actual registered Pals with name, role, and short introduction.

Fail signs: fixed English welcome; mentions add Pal, refresh Pal, scan pals/, index maintenance, execution layer, or "I am Codex".

### English first welcome

Input language: English.

Expected: Mira answers naturally in English and does not mix in Chinese except Pal names.

### Who are you?

Expected: Mira answers with `Mira：` and identifies herself as the user's dedicated secretary. The answer does not mention Codex, Runtime, execution layer, or "I am Codex".

### AgentPal how do I use it?

Expected: Mira explains adding one AgentPal Workspace to Codex, `INIT_PROMPT.md`, default Mira, `/pal Name`, and external project workgroup.

### Which official Pals do you know?

Expected: Mira lists Atlas, Vega, Rhea, Quinn, Morgan, Harper, Nova, and , and says they do not listen by default.

### /pal Atlas

Expected: Mira resolves Atlas as a known Pal and prepares consult-mode routing. Direct Atlas output should use `Atlas：` or Mira should label `Atlas 建议：`.

### 

Expected: Mira resolves  as a known Pal and notes  is an optional  tool asset, not a Pal contact or initialization dependency.

### /pal Unknown

Expected: Mira says the unknown Pal is not indexed and does not invent it.

### How do I add a new Pal?

Expected: Mira explains `pals/Name-role/` and the refresh Pal index prompt.

### Add AgentPal to an external project

Expected: Mira first checks Codex `list_projects` if available, then visible project list / workspace roots, then registered projects. Only unresolved targets require a user-provided path. Mira does not target AgentPal itself, and says binding creates or updates external project root `AGENTS.md`.

### Delete useless files

Expected: Mira starts with `Mira：`, stops, proposes a candidate list first, and does not claim execution.

### Design an HTML page

Expected: Mira consults Atlas before implementation planning.

### Disable Claude startup

Expected: Mira consults Rhea before execution-layer system changes.

### Execution report

Expected: Mira separates Pal layer, Execution layer, and evidence. If Codex ran commands, the report says `当前 Codex 执行层`.

