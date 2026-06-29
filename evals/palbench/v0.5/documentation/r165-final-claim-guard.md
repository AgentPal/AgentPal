# R165 Final Claim Guard

## Required Current Claims

| Claim | Result | Notes |
| --- | --- | --- |
| AgentPal is a no-code Pal organization layer | pass | README pair and docs navigation use this framing. |
| AgentPal is not an Agent runtime or execution layer | pass | Public docs consistently preserve this boundary. |
| Codex is the primary verified host path | pass | README pair, docs runtime guide, and Codex prompt docs align. |
| Official bundled Pal count is 10 | pass | Central contacts and official Pal directories include Mira, Atlas, Nova, Faye, Vega, Quinn, Morgan, Harper, Rhea, and PalSmith. |
| Faye is official in v0.5 | pass | Faye appears in contacts and public Pal descriptions. |
| External project binding is thin | pass | Public docs describe `.agentpal/project.json` and `.agentpal/AGENTPAL.md` only. |

## Forbidden Or Limited Claims

| Area | Allowed R165 wording | Guard |
| --- | --- | --- |
| Claude Code | limited/minimal handoff evidence only | Do not claim full host acceptance. |
| Generic CLI Agent | compatibility path | Do not claim fully validated runtime support. |
| DeepSeek | version-help / limited evidence only | Do not claim full support. |
| OpenCode / Gemini | unavailable in current evidence | Do not claim current support. |
| Plan Mode UI | unavailable in current UI evidence | Do not claim UI-verified support. |
| Goal Mode | limited evidence | Do not claim complete release coverage. |
| Codex background threads / subagents | evidence-backed and user-authorized only | Do not claim default automatic multi-agent execution. |
| Skills, plugins, MCP, connectors | host-available and explicitly authorized only | Do not imply AgentPal includes or executes these by itself. |

## Scan Summary

| Scan | Result |
| --- | --- |
| Old active-entry wording and old release-candidate terms | pass, no matches |
| Runtime overclaim scan | pass_with_expected_negative_boundary_hits |
| Internal/local path leak scan | pass, no matches |
| Credential assignment scan | pass, no matches |

The runtime overclaim scan returned only negative or limiting statements, such as warnings not to claim unsupported hosts or UI-verified support.

## Decision

`ready_for_r166_release_candidate_preflight`

No blocker or high-risk claim conflict remains in the reviewed public docs surface.

