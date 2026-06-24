# Pal Pack English Templates

This directory contains the English AgentPal Pal Pack template set. Use it to create a new public-safe Pal Pack that can be copied into an AgentPal Workspace and registered through `contacts/` and `registry/`.

A Pal is a long-lived working companion that a compatible runtime can read. It is not a single prompt, not an ordinary one-off Skill, and not an Agent runtime. A Pal Pack should contain identity, responsibility boundaries, output contracts, knowledge, skills, workflows, learning notes, self-tests, examples, and public-safe placeholders for runtime-only data.

## Contents

| Path | Purpose |
| --- | --- |
| `PalName-role-template/` | Copyable template directory for a new Pal Pack. Rename it to a real Pal directory such as `Luna-designer`. |
| `README.md` | This guide for using and maintaining the English template set. |

## Template Structure

| Path | Purpose |
| --- | --- |
| `PAL.md` | Human-facing Pal identity: who the Pal is, what it owns, what it refuses, and how it collaborates. |
| `SKILL.md` | Runtime entry file for loading this Pal Pack as a structured Pal, not as a single small Skill. |
| `AGENTS.md` | Runtime instructions for Codex or another AGENTS-aware runtime when the current directory is this Pal Pack. |
| `pal.json` | Machine-readable metadata: id, display name, aliases, direct call, collaboration flags, and entry files. |
| `README.md` | Developer-facing guide for adapting this template into a real Pal Pack. |
| `identity/` | Persona, voice, and boundary files. |
| `core/` | Output contract, collaboration protocol, memory protocol, and runtime boundary. |
| `skills/` | Formal Pal-owned Skills. |
| `knowledge/` | Reusable domain knowledge and judgement principles. |
| `workflows/` | Multi-step work patterns. |
| `runbooks/` | Repeatable operating guides or checklists. |
| `learning/` | Candidate knowledge gaps, repeated tasks, Skills, Runbooks, and Workflows. |
| `examples/` | Non-binding examples. |
| `evals/` | Self-tests and release checks for this Pal Pack. |
| `memory/` | Runtime memory placeholders only. Do not publish real memory. |
| `state/` | Runtime state placeholders only. Do not publish live state. |
| `reports/` | Report placeholders only. Do not publish real task reports. |

## Create A New Pal

1. Copy `PalName-role-template/`.
2. Rename the copied directory to `Name-role`, for example:

   ```text
   Luna-designer
   Kai-finance
   Momo-study
   ```

3. Replace placeholders in:

   - `pal.json`
   - `PAL.md`
   - `SKILL.md`
   - `AGENTS.md`
   - `README.md`
   - `identity/`
   - `core/output-contract.md`

4. Add real public-safe knowledge, Skills, workflows, examples, and evals as needed.
5. Place the finished Pal Pack under:

   ```text
   AgentPal/pals/
   ```

6. Register it only after it is complete, public-safe, and reviewed.

## Register The Pal Pack

Copying the directory into `pals/` does not register it by itself. Registration updates the AgentPal Workspace contacts / registry files so Mira routing, `/pal Name`, and `@Name` can discover the Pal.

Run `prompts/add-pal-to-agentpal.md` from the AgentPal Workspace:

- Codex: open the AgentPal directory as its own Codex project, then paste the prompt into that AgentPal project conversation.
- Claude Code: open a terminal in `<path-to-AgentPal>`, run `claude`, then paste the prompt.
- Generic CLI Agent: open the CLI agent from `<path-to-AgentPal>`, then paste the prompt.

If you normally use AgentPal from an external project, complete registration in the AgentPal Workspace first. Then reinitialize the external project session only if it still shows the old Pal list.

## Public-Safe Rules

Do not include private user memory, real project state, customer data, credentials, tokens, private keys, local absolute paths, internal development reports, or unauthorized logs.

Keep `memory/`, `state/`, and `reports/` as placeholders in public templates and public releases.

## Minimum Release Check

Before publishing or registering a Pal Pack:

- `pal.json` parses as valid JSON.
- `PAL.md`, `SKILL.md`, `AGENTS.md`, `README.md`, and `core/output-contract.md` exist.
- Identity, role, responsibility, and boundaries are clear.
- Direct call and aliases are readable.
- The Pal Pack does not hard-code fixed routes to other Pals.
- No private or runtime-only data is included.
