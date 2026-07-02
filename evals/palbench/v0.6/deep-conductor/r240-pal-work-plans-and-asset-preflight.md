# R240 Pal Work Plans And Asset Preflight

## Verdict

`asset_preflight_pass`

## Team Asset Preflight

| Asset | Use |
| --- | --- |
| `examples/team-packs/marketing-growth-team/TEAM.md` | confirms mission, suitable tasks, unsuitable tasks, collaboration boundary |
| `examples/team-packs/marketing-growth-team/team.json` | confirms team type, policy, modes, supported task types |
| `examples/team-packs/marketing-growth-team/roster.json` | confirms member references and open roles |
| `examples/team-packs/marketing-growth-team/workflows/weekly-agentpal-promotion-content.md` | shapes planning workflow and weekly content cadence |
| `examples/team-packs/marketing-growth-team/evals/definition-of-done.md` | shapes definition of done for content / plan readiness |
| `examples/team-packs/marketing-growth-team/routing/team-routing-card.json` | confirms routing cautions for Faye, PalSmith, Quinn, and open roles |

## Pal Work Plans

### Mira

```yaml
role: conductor
assets_used:
  - official/pals/Mira-main capability card
  - Team Pack First Discovery rule from workspace instructions
work_plan:
  - decide whether existing Team Pack fits
  - coordinate selected Pals
  - ensure all planned owners have outputs
output_expected: selected_team, execution graph, final synthesis
```

### Nova

```yaml
role: product / strategy lead
assets_used:
  - contacts capability card for nova-product
  - marketing-growth-team mission and supported tasks
work_plan:
  - define target testers
  - define test entry and task scope
  - define feedback loop
output_expected: test-user segments and test scope
```

### Vega

```yaml
role: research / intelligence lead
assets_used:
  - contacts capability card for vega-research
  - marketing-growth-team routing and workflow assets
work_plan:
  - frame recruitment channels
  - label evidence and uncertainty
  - avoid unsupported claims about market availability or launch status
output_expected: channel list and uncertainty notes
```

### Harper

```yaml
role: writing / copy lead
assets_used:
  - contacts capability card for harper-writing
  - marketing-growth-team workflow and definition of done
work_plan:
  - write tester invitation
  - write user-facing task instructions
  - keep copy clear and claim-safe
output_expected: user-facing instructions ready for sharing
```

### Rhea

```yaml
role: system / runtime safety lead
assets_used:
  - contacts capability card for rhea-system
  - AgentPal no-code boundary in workspace instructions
work_plan:
  - check forbidden claims
  - separate plan from execution
  - preserve no-backend, no-runtime, no-Marketplace-live boundary
output_expected: overclaim guard
```

### Quinn

```yaml
role: quality / verification lead
assets_used:
  - contacts capability card for quinn-quality
  - owner assignment integrity gate
  - closure gate evidence
work_plan:
  - verify planned owners produced outputs
  - verify WEC and Closure Gate presence
  - verify final deliverable can be used with notes
output_expected: final verification verdict
```

## Missing Asset Plan

| Missing or not-run asset | Handling |
| --- | --- |
| live GitHub community data | not required for this acceptance; mark as assumption if used later |
| real tester list | user-provided or future recruitment execution required |
| publishing credentials | not requested and not used |
| visual / video production assets | open role only; not part of this text-plan acceptance |
