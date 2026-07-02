# R247 Feature Coverage Matrix

| Feature | Raw Output Status | Verdict | Blocker Level | Notes |
| --- | --- | --- | --- | --- |
| Codex thin binding | present, but says not-run | not_run | P1 coverage gap | No fresh external Codex project binding was opened. |
| Claude Code thin binding | present, but says not-run | not_run | P1 coverage gap | Claude Code host was not opened. |
| Team Pack First Discovery | present | pass_with_notes | none | Promotion and 3D IP cases pass; after-sales is fixture/rehearsal note. |
| DeepConductor | present | pass_with_notes | none | Full no-code chain appears; project-bound/live notes remain. |
| PalSmith create Pal | present | pass_with_notes | none | Current route and private discovery default are represented. |
| Pal Asset Preflight | present | pass_with_notes | none | Owner, assets, tool boundary, and Asset Use Summary appear. |
| Workflow Execution Contract | present | pass_with_notes | none | Owners, verification, status, skip/replan fields appear. |
| Closure Gate | present | pass_with_notes | none | Required checks appear; simulated/manual boundary preserved. |
| Overall v0.6 test package | present | pass_with_host_integration_notes | P1 coverage gaps | Core no-code chain passes; Codex/Claude host integration not-run. |

## Matrix Conclusion

The core no-code v0.6 content chain is covered and passes with notes.

Host integration coverage is incomplete:

```text
codex_thin_binding_result: not-run
claude_code_binding_result: not-run
```
