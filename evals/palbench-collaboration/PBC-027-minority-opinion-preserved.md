# PBC-027 Minority Opinion Preserved

## Goal

Ensure that a minority reviewer opinion remains visible in synthesis.

## Input

```text
Three reviewers support the idea, but one reviewer raises a serious release risk. Summarize the independent review.
```

## Expected

- Minority opinion is explicitly preserved.
- Risk severity and conditions are shown.
- Decision options include a risk-repair path.
- Synthesis does not count votes as proof.

## Failure

- Minority opinion is deleted.
- Synthesis treats majority agreement as acceptance evidence.
