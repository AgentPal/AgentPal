# AgentPal v0.1.0-rc.1 Release Notes

AgentPal v0.1.0-rc.1 is a release candidate for the AgentPal Workspace and Pal Pack Standard practice.

## Who This Release Is For

This release is for users and contributors who want to try Pal Packs inside Codex, Claude Code, or another runtime that can read Markdown and JSON files.

It is especially useful if you want to:

- keep multiple professional Pal Packs in one workspace
- initialize Mira as the default Main Pal
- call registered Pals with `/pal Name`
- study the Pal Pack file structure
- author or review release-safe Pal Pack templates, protocols, and examples

## R32 Methodology Clarification

- Mira is documented as the default Main Pal, Leader Pal, and Conductor. The team-leadership identity remains her communication and relationship layer, not the whole product role.
- AgentPal separates Fast Route and Deep Conductor. Fast Route is the current Simple Pal Mode clear-task handoff pattern. Deep Conductor is future complex-workflow design only.
- Context Access List, Pal Isolation, Shared Memory, Routing Reward Memory, PalBench evals, and orchestration examples were strengthened for auditability.
- R33 adds a small-sample PalBench smoke validation. It shows initial evidence for task-package clarity, context-scope control, verification quality, and lower user routing burden. It is not a model benchmark and not statistically significant.

## Who This Release Is Not For

This release is not a finished app or automation platform. It is not the right fit if you need:

- a desktop app or web UI
- a marketplace or hosted Pal Hub
- an automatic installer, daemon, scanner, validator, or service
- an execution engine that runs actions without the host runtime
- active subagent, remote agent, or MCP-hosted agent orchestration
- production enterprise permission management

## What Is Included

- AgentPal Workspace release assets: `AGENTS.md`, `PAL.md`, `SKILL.md`, `agentpal.json`, and the Codex initialization prompt at `prompts/codex/initialize-agentpal-workspace.md`.
- Shared core gates under `core/` so Codex, Claude Code, generic CLI, and project-bound sessions read the same AgentPal rules.
- Mira as the default Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator.
- Official bundled Pal Packs: Mira, Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova.
- Contacts and registry files for Pal discovery, aliases, and direct `/pal Name` calls.
- Simple Pal Mode as the only active v0.1.0-rc.1 runtime path.
- Runtime Response Gate and Pal Mode validity rules.
- Context slicing, asset loading budget, memory summary loading, and Task Package output contract protocols.
- AgentPal original Pal Layer methodology and PalBench validation docs under the current docs information architecture.
- R33 PalBench small-sample smoke validation report.
- Capability Inventory, Task Judgement, Workflow Topology, Context Access List, Pal Isolation, and Routing Reward Memory protocols as future-oriented design assets.
- External project workgroup templates.
- Thin external project workgroup templates that store pointers and minimal metadata instead of copying full AgentPal rules.
- Claude Code one-prompt project install using thin `CLAUDE.md`, `AGENTS.md`, `.agentpal/`, and `.claude/settings.local.json`.
- Claude Code install first welcome output: a `Mira：` welcome that introduces Mira as Main Pal / Leader Pal / Conductor, lists the official Pal set, and explains `/pal Name`.
- Generic CLI Agent one-prompt project install using `AGENTS.md` and `.agentpal/`.
- Runtime adapter thin binding examples and self-tests.
- Public-safe examples, evals, prompts, templates, release notes, checklist, and contribution guidance.

## What Is Not Included

- No desktop app.
- No web UI.
- No CLI requirement.
- No required Python, Node.js, Rust, Go, service, daemon, scanner, validator, or installer.
- No automatic execution layer.
- No active multi-agent runtime.
- No active subagent orchestration.
- No active Deep Conductor or automatic external Agent orchestration; future orchestration notes are design material only.
- No marketplace or commercial Pal distribution system.
- No bundled private user memory, private project state, real reports, or secrets.

## How It Works

AgentPal v0.1.0-rc.1 uses Simple Pal Mode.

Mira receives ordinary messages. When Mira judges that a registered Pal should own a substantive request, Mira gives a short handoff and stops. The owner Pal answers immediately in the same response, using its own Pal assets, Output Contract, and fallback rules when needed.

Direct calls such as `/pal Harper` enter that Pal's working mode. They do not start an independent agent process.

## Getting Started

1. Open the AgentPal Workspace in a supported runtime.
2. Paste or run `prompts/codex/initialize-agentpal-workspace.md`.
3. Start with Mira for ordinary messages.
4. Use `/pal Name` to call a registered Pal directly.
5. Use `RESOURCE_INDEX.md` as navigation when you need to find a specific root asset or directory.

## Claude Code Project Setup

For project work in Claude Code:

```text
cd <your-project>
claude
```

Then paste `prompts/claude-code/install-agentpal-current-project.md` after replacing `AGENTPAL_HOME` with your AgentPal Workspace path.

The prompt updates `.claude/settings.local.json` `permissions.additionalDirectories`, `CLAUDE.md`, `AGENTS.md`, and `.agentpal/`. `--add-dir` remains a fallback / advanced option, not the required default path.

## Generic CLI Agent Project Setup

For Markdown/JSON-capable CLI Agents, run the CLI Agent inside `<your-project>` and paste `prompts/generic-cli-agent/install-agentpal-current-project.md` after replacing `AGENTPAL_HOME` with your AgentPal Workspace path. The generic prompt updates `.agentpal/` and `AGENTS.md` without relying on Claude Code settings.

## Safety And Public Release Boundary

Runtime-private memory, private state, real reports, internal development notes, secrets, credentials, customer data, and local absolute paths must stay out of the public repository.

Examples and templates should use synthetic or placeholder data. Future designs should be marked as future work and must not be described as active v0.1.0-rc.1 behavior.

## Publication Status

This release note describes the v0.1.0-rc.1 release candidate content. A local `v0.1.0-rc.1` tag may exist in a maintainer workspace, but a GitHub Release should be considered published only after the intended commit and tag are pushed to the intended remote and the GitHub Release page is created.

## License

AgentPal is released under the MIT License. See `LICENSE`.
