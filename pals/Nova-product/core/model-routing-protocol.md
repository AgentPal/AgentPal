# Model Routing Protocol

Nova recommends model strength by task risk and ambiguity.

Use a strong reasoning model for:

- Product strategy and scope tradeoffs.
- Ambiguous PRDs.
- Risk and assumption review.
- Prompt shaping for weaker execution agents.
- Final evidence review.

Use medium or lower-cost models for:

- Formatting already-decided PRDs.
- Turning clear notes into decision records.
- Low-risk feedback clustering.
- Bounded acceptance-criteria drafting.

Weak or small models require stricter prompts:

- Restate scope and non-scope.
- Provide exact output format.
- Include explicit evidence requirements.
- Add "do not infer missing product facts" instructions.

Recommended default for Nova RC work: GPT-5.4 or GPT-5.4-Codex equivalent, reasoning strength medium.

Record notable choices in `memory/runtime/model-usage-memory.md`.

