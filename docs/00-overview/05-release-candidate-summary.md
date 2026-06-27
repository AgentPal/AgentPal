# Release Candidate Summary

AgentPal v0.3.0-rc.1 is the release candidate for the AgentPal Workspace, Pal Pack standard practice, and no-code orchestration prototype line for agent runtimes.

## The Short Summary

- AgentPal gives every agent a Pal.
- The current release is a Markdown / JSON / protocol workspace.
- The active task-handling path is `Simple Pal Mode`.
- Deep Conductor is available as no-code protocols, task packages, examples, evals, synthesis reports, and replay reports.
- Mira is the default Main Pal / Leader / Conductor.
- The official bundled Pals are Mira, Atlas, Vega, Rhea, PalSmith, Quinn, Morgan, Harper, and Nova.

## Ready For Current Use

- Open the AgentPal Workspace in Codex and initialize with `prompts/codex/initialize-agentpal-workspace.md`.
- Connect AgentPal to a real project in Claude Code through the one-prompt install.
- Connect AgentPal to a real project in a generic CLI agent through the generic install prompt.

## Important Boundaries

- AgentPal is not an Agent runtime or execution layer.
- It does not claim automatic multi-agent runtime behavior in this release.
- Deep Conductor is not an automatic background executor.
- Subagent launch, parallel child workflows, external Agent calls, and Runtime Skill execution remain host-runtime-dependent or unavailable unless the current host Runtime proves support.
- PalBench Collaboration is qualitative regression coverage, not a statistically significant benchmark.

## Next Reading

- [Current Status](01-current-status.md)
- [Current Capabilities](02-current-capabilities.md)
- [Runtime Compatibility](../04-runtime-guides/00-runtime-compatibility.md)
