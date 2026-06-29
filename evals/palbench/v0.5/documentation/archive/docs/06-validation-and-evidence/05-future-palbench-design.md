# Future PalBench Design

Future PalBench work should expand the sample size and make evidence collection more repeatable while preserving the same cautious claims boundary.

## Design Goals

Future PalBench should help maintainers answer:

- Did the task become clearer?
- Was context access bounded?
- Were evidence requirements explicit?
- Was false completion risk reduced?
- Did the user need less manual routing work?
- Were routing decisions reusable without becoming fixed routes?
- Did the output keep current runtime behavior separate from future design?

## Candidate Improvements

Useful next steps include:

- larger task sets
- repeated runs across different task categories
- clearer before/after artifacts
- recorded content-read counts where the runtime can provide them
- evidence templates for verification results
- separate reporting for Simple Pal Mode and any future orchestration simulations
- human review notes that distinguish facts, observations, and interpretations

## Claim Boundary

Future PalBench can become stronger validation, but each report must state its own evidence level.

Until larger and better-controlled runs exist, the v0.1.0-rc.1 claim should stay narrow:

```text
R33 provides small-sample smoke evidence for observed workflow benefits. It does not prove statistical significance, broad performance improvement, or model capability.
```
