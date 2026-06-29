# Explicit Tool Directive Rule

Status: v0.5 no-code protocol

## Purpose

The Explicit Tool Directive Rule defines how a Pal handles a user, Pal Skill,
workflow, project memory, or capability profile that already specifies a Skill,
plugin, external Agent, runtime, or tool.

When a directive is explicit, the Pal should not re-litigate tool selection.
It should enter a direct-use path, run the minimum safety gate, and then either
invoke, dry-run, hand off, or block with evidence.

## Directive Sources

Use `directive_source` with one of:

- `user_directive`
- `pal_skill`
- `workflow`
- `project_memory`
- `capability_profile`
- `runtime_task_package`

## Required Gate

Direct use is allowed only when all checks pass:

- `capability_available`: current host evidence or snapshot shows the tool is
  available, or the output is a handoff package rather than execution.
- `scope_match`: the user task matches the named tool's intended purpose.
- `authorization_ok`: no unauthorized external write, publish, payment,
  deletion, credential access, or sensitive transfer is involved.
- `privacy_ok`: no customer-private material is distributed beyond the
  approved context boundary.
- `preconditions_ok`: required input files, URLs, credentials, or task package
  fields exist.
- `no_better_blocker`: no higher-priority safety or capability blocker exists.

If every check passes, do not keep asking whether to use the specified tool.
Use it or produce the specified execution package, then record the invocation.

If any check fails, do not execute. Record the missing capability,
authorization, input, or privacy condition and return `dry_run`,
`handoff_only`, or `blocked`.

## Required Record Fields

- `directive_source`
- `user_directive`
- `pal_skill`
- `workflow`
- `project_memory`
- `capability_profile`
- `specified_tool`
- `specified_skill`
- `specified_agent`
- `direct_use_allowed`
- `safety_gate_result`
- `preconditions`
- `authorization_status`
- `invocation_record`
- `if_blocked_reason`
- `evidence_path`

## Safety Examples

- A user explicitly says to use `pdf` on a local public fixture: run the pdf
  safety gate, then use the PDF capability if available.
- A workflow says product page audits must use `product-design:audit`: use the
  audit workflow after screenshot or URL evidence exists.
- A Pal workflow says large code reading starts with a Claude Code handoff:
  prepare or minimally call Claude Code only when command evidence and safety
  scope exist.
- A user says `git push` without publication authorization: block.
- A user says to write customer-private data into a public example: block.

