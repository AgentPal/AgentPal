# Pal Contact Decoupling Self-Test

## Purpose

Verify that AgentPal uses contacts / registry as the single source of truth for Pal discovery and that individual Pal Packs do not hard-code other Pal identities as fixed collaborators.

## Scope

- `pals/*/PAL.md`
- `pals/*/AGENTS.md`
- `pals/*/SKILL.md`
- `pals/*/identity/`
- `pals/*/core/`
- `pals/*/knowledge/`
- `pals/*/skills/`
- `pals/*/workflows/`
- `pals/*/runbooks/`
- `pals/*/learning/`
- `pals/*/examples/`
- `pals/*/evals/`
- `contacts/`
- `registry/`
- `examples/`
- `evals/`
- `templates/subagent-prompts/`

## Pass Criteria

- `contacts/` and `registry/` are documented as the source of truth for Pal discovery.
- Individual Pal Packs do not keep local lists of other Pal identities.
- Pal internal collaboration text says to resolve collaborators from current contacts / registry.
- Pal internal files do not say a task type must consult, delegate to, hand off to, or spawn a named Pal.
- Examples that mention specific Pals are marked non-binding examples.
- Evals that mention specific Pals are marked test fixtures.
- Subagent maps and templates are capability maps or selected-Pal templates, not route tables.
- Removed Pal names do not remain in the public release directory.

## Allowed References

- Official Pal lists in `contacts/`, `registry/`, README, docs, and initialization examples.
- Self-reference inside a Pal's own directory.
- Explicit `/pal Name` command documentation.
- Non-binding examples.
- Eval test fixtures.
- Response fingerprints and selected-Pal subagent templates.

## Fail Signs

- A Pal Pack says "use Atlas", "consult Quinn", "ask Vega", or equivalent as a fixed rule.
- A Pal Pack keeps its own local list of other Pal names.
- A generic example says a task shape requires a fixed Pal or fixed Pal set.
- A subagent template says a task type must spawn specific Pals.
- A removed Pal appears as a default bundled Pal or direct-call option.

## Expected Result

- `cross_pal_hard_reference = 0`
- `removed_pal_residue = 0`
- JSON parse checks pass.
- no-runtime check passes.
