# Faye Delivery Governance Loop Example

## Scenario

A user asks for three product video scripts. Faye treats this as a video-growth
Delivery Pack task with research, script, brand check, and video QA stages.

## Governance Loop

| Stage | Example Record | Status |
| --- | --- | --- |
| User request | "Need 3 product video scripts" | pass |
| Faye task judgement | `faye-video-growth-task-judgement.example.md` | pass |
| missing information | product, audience, proof points, brand voice | missing |
| assumptions | placeholder product and generic audience | requires-human-review |
| Delivery Pack update | public-safe video-growth task shell | not-run |
| Pal Team Blueprint | candidate research, writing, brand, QA perspectives | not-run |
| Context Access List | `faye-delivery-context-access-list.example.md` | pass |
| Task Package | script drafting package shell | not-run |
| Human review | brand / claim reviewer required | requires-human-review |
| Verification Result | no real evidence or publication check yet | not-run |
| Governance Record | this example record | pass |
| Routing Memory candidate | `routing-memory-record.json` shape | not-run |
| reusable/private review | placeholders only, no customer data | pass |

## Verification Result Shell

```yaml
overall_result: partial
checks:
  - requirement: three scripts can be drafted only after brief confirmation
    status: missing
    evidence: missing product brief
  - requirement: external publication
    status: not-run
    evidence: no connector or publishing platform used
  - requirement: customer-private data excluded
    status: pass
    evidence: placeholders only
human_review:
  required: true
  review_status: not-run
```

## Boundary

This example does not publish videos, call a connector, inspect private
analytics, store credentials, write to an external project `.agentpal/`
directory, or convert candidate Pals into routes.
