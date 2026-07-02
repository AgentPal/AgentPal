# R246 Test Coverage Matrix

| Feature | Test File | P0 Coverage |
| --- | --- | --- |
| Codex thin binding | `01-setup-codex-thin-binding.md` | AgentPal trigger, thin binding, project/workspace distinction |
| Claude Code thin binding | `02-setup-claude-code-thin-binding.md` | protected block, local binder boundary |
| Team Pack First Discovery | `03-test-team-pack-first-discovery.md` | no bypass, no premature PalSmith creation, no role-title Pal |
| DeepConductor | `04-test-deep-conductor.md` | discovery, work plans, asset preflight, trace, gates, Quinn verification |
| PalSmith create Pal | `05-test-palsmith-create-pal.md` | current route, draft Pal Pack, private discovery default |
| Pal Asset Preflight | `06-test-pal-asset-preflight.md` | Pal asset use before work, no blind tool call |
| Workflow Execution Contract | `07-test-workflow-execution-contract.md` | owner per step, verifier output, skip/replan reason |
| Closure Gate | `08-test-closure-gate.md` | required steps, verifier, child step return, asset/routing checks |
| Submission | `09-submit-test-results.md` | raw outputs, screenshots status, notes, blockers |
| Rubric | `v06-pass-fail-rubric.md` | P0/P1/P2 and overclaim classification |

## Coverage Conclusion

The package covers the requested v0.6 testing surface and collects enough material for R247 intake.
