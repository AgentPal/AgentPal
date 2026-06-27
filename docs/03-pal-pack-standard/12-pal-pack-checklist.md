# Pal Pack Checklist

## Status

Current for AgentPal `v0.1.0-rc.1`.

Use this checklist before adding a Pal Pack to central contacts or publishing it.

## Minimal Required Files

- [ ] `AGENTS.md`
- [ ] `PAL.md`
- [ ] `README.md`
- [ ] `SKILL.md`
- [ ] `pal.json`
- [ ] `core/output-contract.md`
- [ ] `core/task-loop.md`
- [ ] `identity/persona.md`
- [ ] `identity/boundaries.md`
- [ ] `identity/voice.md`
- [ ] `knowledge/index.md`
- [ ] `skills/index.md`
- [ ] `runbooks/index.md`
- [ ] `workflows/index.md`
- [ ] `memory/README.md` or `memory/user/README.md`
- [ ] `state/README.md`
- [ ] `reports/README.md`
- [ ] `evals/definition-of-done.md`

## Root File Checks

- [ ] `SKILL.md` says this is a Pal Pack entry, not one ordinary Skill.
- [ ] `pal.json` has id, display name, directory name, role, path, aliases, direct call, type `pal-pack`, and collaboration flags.
- [ ] `PAL.md` clearly states responsibilities, non-responsibilities, privacy boundary, and fallback behavior.
- [ ] `core/output-contract.md` states required output and what the Pal must not claim.

## Directory Checks

- [ ] Empty knowledge, skills, runbooks, and workflows directories have indexes.
- [ ] Memory, state, and reports contain only public-safe placeholders unless they are runtime-private and ignored.
- [ ] Examples and evals use synthetic data.
- [ ] Pal-owned Skills are stored under this Pal's own `skills/` directory.

## Discovery Checks

- [ ] The directory is a valid Pal Pack before central contacts are updated.
- [ ] Contacts and registry are the source of truth for discovery.
- [ ] No ordinary Skill, plugin, model, MCP server, runtime, raw repository, knowledge pack, or persona pack was added as a Pal.
- [ ] No Pal Pack contains a hard-coded route map for other Pals.

## Public-Safe Checks

- [ ] No secrets, tokens, credentials, private keys, or passwords.
- [ ] No private user memory.
- [ ] No private project state.
- [ ] No real task reports or internal development notes.
- [ ] No local absolute paths.
- [ ] No future design described as current `v0.1.0-rc.1` behavior.

## Valid Pal Answer Check

- [ ] The Pal can answer with its own prefix.
- [ ] The answer uses `core/output-contract.md`.
- [ ] The answer uses at least one relevant asset or an honest fallback method.
- [ ] The Pal does not claim execution without evidence from the host runtime.
