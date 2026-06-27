# R80 Runtime Example Audit

Date: 2026-06-28

Scope: `examples/runtime/`, `examples/runtime-adapters/`, and `examples/capability-inventory/runtime-profiles/` after R79.

## Summary

`examples/runtime/` contained a single README that linked the README Quick Start paths to Codex, Claude Code, generic CLI, and project-first examples. It was not a runtime profile example directory. Because the directory name visually resembled the archived root `runtime/` path, R80 moved the README to `examples/runtime-adapters/README.md`.

Runtime profile examples remain under `examples/capability-inventory/runtime-profiles/`.

## Audit Table

| source_path | current_role | recommended_target | migrate_now | blocker | reference_count | decision |
| --- | --- | --- | --- | --- | ---: | --- |
| `examples/runtime/README.md` | Runtime adapter / Quick Start navigation | `examples/runtime-adapters/README.md` | yes | none | 1 historical validation reference before update | moved |
| `examples/runtime-adapters/` | Runtime adapter examples | keep | yes | none | 4 direct text refs before update | kept and given README |
| `examples/capability-inventory/runtime-profiles/` | Runtime profile examples | keep | no | none | current active profile example source | kept |

## Moved Paths

| Old path | New path |
| --- | --- |
| `examples/runtime/README.md` | `examples/runtime-adapters/README.md` |

## Boundary

`examples/runtime-adapters/` contains runtime adapter and thin-binding examples. It is not the archived root `runtime/` facts source. Runtime profile examples belong under `examples/capability-inventory/runtime-profiles/`.
