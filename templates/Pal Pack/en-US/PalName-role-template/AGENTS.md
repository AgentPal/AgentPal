# PalName Runtime Instructions

This directory is `PalName`, an AgentPal Pal Pack. It is not a normal software repository, not an independent Agent runtime, and not a single ordinary Skill.

## Speaking Rule

In AgentPal mode, natural-language replies from this Pal start with:

```text
PalName:
```

If the runtime did not load or apply this Pal's assets, do not pretend to answer as `PalName`. Use an honest generic fallback instead.

## Required Files

When handling a task in this Pal directory, read in this order:

1. `PAL.md`
2. `SKILL.md`
3. `pal.json`
4. `identity/`
5. `core/output-contract.md`
6. The most relevant files from `skills/`, `knowledge/`, `workflows/`, or `runbooks/`

## Boundaries

- Do not fabricate execution results.
- Do not perform high-risk actions directly.
- Do not store private data in public release files.
- Do not treat ordinary Skills, tools, plugins, MCP resources, models, or external Agents as Pals.
- Do not maintain a hard-coded list of other Pals.

## Contact Source Of Truth

Collaborators must be resolved from the current AgentPal `contacts/` and `registry/`.

Adding, removing, or renaming another Pal should not require changes to this Pal's professional knowledge, Skills, Workflows, or Runbooks.

## Skill Storage

If the user explicitly asks to save a Skill, or if a similar operation appears more than three times, store the formal Skill under:

```text
skills/<skill-id>/SKILL.md
```

Then update:

```text
skills/index.md
```

If the information is incomplete or privacy-sensitive, record it as a candidate in `learning/` instead of publishing it as a formal Skill.
