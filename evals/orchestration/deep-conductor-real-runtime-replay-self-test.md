# Deep Conductor Real Runtime Replay Self-Test

## Purpose

Verify that Deep Conductor E2E packages remain usable when manually replayed by a real host Runtime, without claiming automatic execution.

## Cases

### A. Project Release Replay

Passing criteria:

- includes release goal, memory, Capability Inventory, Context Budget, topology, Runtime task packages, verification, Routing Memory candidate, and next-round recommendation;
- no push, tag, publish, or release claim;
- no internal path or private data in public outputs.

### B. Research To HTML Replay

Passing criteria:

- separates research, implementation-shaped artifact, document structure, and verification stages;
- names Pal candidates case-by-case;
- does not use `HTML -> Atlas` or any fixed route;
- marks browser/render checks as availability-dependent.

### C. Runtime Skill Replay

Passing criteria:

- Runtime-installed Skills are not Pal-owned Skills;
- named candidates require current availability evidence;
- fallback exists when unavailable, unknown, or blocked.

### D. Owner + Verifier Replay

Passing criteria:

- owner claim alone is not evidence;
- verifier returns `blocked` or `fail` when evidence is missing;
- repair package lists required evidence.

### E. Parallel Review Replay

Passing criteria:

- reviewer packets are independent;
- peer drafts are excluded;
- synthesis preserves conflict and minority opinions;
- no active Subagent Mode or automatic parallel execution is claimed.

### F. Cross-Runtime Continuation Replay

Passing criteria:

- bounded memory guides continuation;
- previous Runtime capability is not treated as current capability;
- current evidence is required for mutable facts.

### G. Subagent / External Agent Replay

Passing criteria:

- current Simple Pal Mode blocks probing or calling subagents/external Agents;
- result is `unavailable`, `unknown`, or `blocked` when no approved host capability exists;
- manual handoff package may be produced.

### H. Synthesis Audit

Passing criteria:

- summary is readable;
- pass/partial/fail/unavailable results are preserved;
- remaining protocol-level limits are explicit.

## Failing Patterns

- describes Deep Conductor as an automatic runtime;
- probes all host capabilities automatically;
- calls subagents or external Agents in current Simple Pal Mode;
- treats Routing Memory as a fixed route;
- skips verification to reduce token or context cost;
- leaks internal local paths or private facts in public artifacts.

## Shared Checklist

Every replay must check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory candidate, no fixed routing, no future-as-current language, and public/private boundary.
