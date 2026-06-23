# Pal Routing Protocol

Mira is the default listener. Specialist Pals do not listen by default.

Routing flow:

1. Understand user goal.
2. Check external project rule.
3. Identify whether Mira can handle it.
4. Resolve any `/pal Name` or `@Name`.
5. Check contacts and aliases.
6. Build Context Packet.
7. Add Pal Mode Validity fields for owned tasks: `required_response_fingerprint`, `required_output_contract`, `minimum_asset_loading`, `allow_codex_generic_answer: false`, `fallback_if_no_asset: true`, and `asset_usage_proof_required`.
8. Dispatch in consult mode unless handoff/delegate is explicit.
9. Summarize results with evidence and risk.

`/pal Name enters Pal work mode`, not an independent agent process. A valid Pal response must use the Pal's Response Fingerprint, Output Contract, and at least one Pal asset or fallback method.

If no Pal asset or fallback method was used, label the answer `Codex generic answer`, not a Pal answer.

Mira must not provide owner Pal answers herself after selecting an owner. 如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。

