# Official Pal Slim Structure

AgentPal's official specialist Pals are embedded modules under `pals/`, not separate repositories that users need to add to Codex one by one.

Example:

```text
pals/Atlas-developer/
  README.md
  PAL.md
  AGENTS.md
  SKILL.md
  pal.json
  identity/
  core/
  knowledge/
  skills/
  workflows/
  runbooks/
  learning/
  evals/
  examples/
  memory/
  state/
  reports/
```

AgentPal root owns the shared workspace systems:

```text
contacts/
registry/
orchestration/
runtime/
models/
plugins/
projects/
templates/
```

The default bundled specialist Pals do not include runtime tool-engine folders:

```text

```

That tool is optional, Pal-owned, and not required for AgentPal initialization.

This split keeps each Pal easier to inspect and makes user-created Pals less intimidating: create identity, professional assets, skills, workflows, learning, examples, evals, and an output contract; leave workspace-level systems to AgentPal root.

