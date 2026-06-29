# R165 User Path Walkthrough

## Walkthrough

| Step | Expected User Experience | Result |
| --- | --- | --- |
| 1. Open public entry | README explains AgentPal as a no-code Pal team organization layer, not an Agent runtime. | pass |
| 2. Understand the install shape | User sees that AgentPal is cloned or downloaded, then opened in Codex. | pass |
| 3. Initialize in Codex | User is directed to `prompts/codex/initialize-agentpal-workspace.md`. | pass |
| 4. Meet the team | User can see Mira as default entry Pal and 10 bundled Pals including Faye. | pass |
| 5. Bind an external project | User is told binding is thin and project-local `.agentpal/` should only hold binding context, not copied Pal Packs. | pass |
| 6. Read deeper docs | `docs/README.md` points to overview, getting started, runtime guides, PalSmith, Pal Pack authoring, and references. | pass |
| 7. Avoid overclaim traps | Runtime compatibility docs separate Codex-first evidence from limited or unavailable host claims. | pass |

## Notes

- `prompts/README.md` now keeps `initialize-agentpal.md` in a legacy-compatible section so the current Codex path remains clear.
- Historical docs and evidence archives are discoverable for maintainers, but they are not the primary new-user route.
- The walkthrough is documentation-path validation only. It is not a new runtime acceptance test.

## Result

`pass`

The public documentation path is coherent enough for R166 release-candidate preflight.

