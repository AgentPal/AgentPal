# R190 PalSmith Custom Pal Creation Authorization Integrated Matrix

## Summary

R190 closes the PalSmith v0.5 no-code chain from composite Pal creation to user custom Pal authorization and revocation readiness.

Result: `integrated_closeout_pass_with_notes`

This matrix does not introduce runtime code, a CLI, installer, scanner, daemon, connector, backend service, Marketplace backend, official Pal, or central contacts update.

## Integrated Chain

| Stage | Evidence | Host / file level | Current conclusion | Residual risk |
| --- | --- | --- | --- | --- |
| Composite Pal creation capability | `official/pals/PalSmith-pal-governor/core/composite-pal-distillation-protocol.md`; `prompts/palsmith/create-composite-pal.md`; `examples/palsmith/composite-pal-creation-examples.md`; `evals/palbench/v0.5/palsmith/r169-composite-creation-real-task-tests.md`; `evals/palbench/v0.5/palsmith/r171-palsmith-host-dialogue.md`; `evals/palbench/v0.5/palsmith/r171-quinn-host-review.md` | mixed real-host and file-level evidence | PalSmith can produce bounded no-code composite Pal creation plans and evidence without creating official Pals by default. | External user fresh-clone UX can still be improved, but no blocker for no-code chain closure. |
| Draft Pal Pack creation | `evals/palbench/v0.5/palsmith/draft-pal-packs/FirstPrinciplesProductReviewer/`; `evals/palbench/v0.5/palsmith/r174-draft-pal-pack-creation.md`; `evals/palbench/v0.5/palsmith/r174-quinn-draft-pal-pack-review.md`; `evals/palbench/v0.5/palsmith/r175-draft-pal-pack-quality-regression.md` | file-level creation and regression evidence | Non-official draft Pal Pack can be created and reviewed as an eval artifact. | Draft Pack remains a test artifact, not a bundled official Pal. |
| Draft Pal Pack use regression | `evals/palbench/v0.5/palsmith/r177-draft-pal-loading-regression.md`; `evals/palbench/v0.5/palsmith/r177-draft-pal-product-review-task.md`; `evals/palbench/v0.5/palsmith/r177-draft-pal-boundary-pressure-test.md`; `evals/palbench/v0.5/palsmith/r177-quinn-draft-usage-review.md`; `evals/palbench/v0.5/palsmith/r177-draft-pal-usage-regression-summary.md` | real host usage regression evidence | Draft Pal identity, task behavior, and boundary refusal passed for the tested scenario. | Not a broad benchmark over all possible draft Pals. |
| Draft-to-custom installation path | `official/pals/PalSmith-pal-governor/core/custom-pal-installation-protocol.md`; `prompts/palsmith/install-draft-as-custom-pal.md`; `examples/palsmith/draft-to-custom-pal-installation-example.md`; `evals/palbench/v0.5/palsmith/r179-draft-to-custom-pal-installation-flow.md`; `evals/palbench/v0.5/palsmith/r181-draft-to-custom-real-host-summary.md` | protocol, prompt, example, and real host rehearsal evidence | A reviewed draft can be planned and installed as a private user custom Pal through explicit Runtime Task Package approval. | Current evidence uses one test Pal path. |
| User custom Pal explicit invocation | `workspace/resources/user-pals/FirstPrinciplesProductReviewer/`; `evals/palbench/v0.5/palsmith/r183-user-custom-pal-explicit-invocation.md`; `evals/palbench/v0.5/palsmith/r183-user-custom-pal-invocation-discovery-summary.md` | local artifact and host dialogue evidence | Explicit invocation is allowed for the installed user custom Pal while general discovery remains off. | Invocation is host-context dependent and must report unavailable capabilities honestly. |
| Discovery default refusal | `evals/palbench/v0.5/palsmith/r183-discovery-refusal-regression.md`; `evals/palbench/v0.5/palsmith/r183-unauthorized-delegation-refusal.md`; `evals/palbench/v0.5/palsmith/r183-contacts-registration-refusal.md`; `evals/palbench/v0.5/palsmith/r183-quinn-user-custom-pal-discovery-review.md` | host regression evidence | Default discovery, unauthorized delegation, and central contacts registration are refused. | Hosts must continue to respect local policy files and not infer discovery from file presence. |
| Explicit discovery authorization | `official/pals/PalSmith-pal-governor/core/user-custom-pal-discovery-authorization-protocol.md`; `docs/06-palsmith/user-custom-pal-discovery-authorization.md`; `prompts/palsmith/authorize-user-custom-pal-discovery.md`; `templates/palsmith/user-custom-pal-authorization-record.md`; `templates/palsmith/user-custom-pal-discovery-policy.md`; `evals/palbench/v0.5/palsmith/r185-user-custom-pal-discovery-authorization-design.md`; `evals/palbench/v0.5/palsmith/r186-user-custom-pal-authorization-quality-regression.md` | protocol, user docs, prompt, templates, regression evidence | Discovery authorization is scoped, auditable, and separate from delegation, contacts registration, and Marketplace listing. | Actual policy enforcement depends on the host runtime honoring the no-code authorization record. |
| Refuse full automatic delegation | `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-boundary-results.md`; `evals/palbench/v0.5/palsmith/r189-custom-pal-authorization-e2e-quality-regression.md` | real host and quality regression evidence | Full automatic delegation is refused unless an explicit limited delegation scope exists. | Future host adapters should continue to test this as a high-risk boundary. |
| Contacts registration separate authorization | `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-boundary-results.md`; `evals/palbench/v0.5/palsmith/r188-quinn-authorization-e2e-review.md`; `evals/palbench/v0.5/palsmith/r189-quinn-custom-pal-authorization-e2e-quality-review.md` | real host and Quinn review evidence | Contacts registration remains a separate governance task and does not follow from discovery authorization. | No central contacts write was performed in this chain. |
| Marketplace draft/request boundary | `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-record-sample.md`; `evals/palbench/v0.5/palsmith/r188-custom-pal-authorization-e2e-summary.md` | real host evidence and sample records | Marketplace draft metadata may be planned, but public listing and backend Marketplace behavior are not claimed. | Marketplace backend remains out of scope by design. |
| Revocation readiness | `prompts/palsmith/revoke-user-custom-pal-discovery.md`; `docs/06-palsmith/custom-pal-creation-to-authorization-flow.md`; `evals/palbench/v0.5/palsmith/r190-quinn-palsmith-custom-pal-authorization-closeout-review.md` | R190 prompt and closeout review | Revocation path is documented as a no-code governance task that preserves audit records and separates authorization fields. | No live revocation write was executed in R190. |

## Boundary Checks

- Official Pal count remains 10.
- `workspace/organization/contacts/` must have no diff.
- `official/pals/` must have no diff for user custom Pal registration or promotion.
- User custom Pal discovery is not enabled by file presence alone.
- Runtime Task Packages are plans until the host runtime returns evidence.

## Closeout Decision

`ready_to_close_r168_to_r190_palsmith_custom_pal_creation_authorization_chain`

The chain is complete for v0.5 no-code documentation, prompt, template, evidence, and boundary purposes. Future work should focus on user-facing usability tests, not on broadening the product boundary into a runtime or backend.
