# Core Runtime Response Gate

This file is the core-level entry pointer for the runtime response gate.

For the authoritative detailed gate, read:

- `orchestration/runtime-response-gate.md`

The core contract is:

1. Apply `core/agentpal-core-gate.md`.
2. Apply `core/first-pal-gate.md`.
3. Apply `core/simple-pal-mode-runtime-contract.md`.
4. Apply `core/deliverable-aware-task-judgement-gate.md`.
5. Apply `core/main-pal-conductor-gate.md`.
6. Apply `core/owner-assignment-integrity-gate.md`.
7. Apply `orchestration/runtime-response-gate.md` for detailed response order.

AgentPal-mode natural-language output must start with the current speaking Pal prefix. This includes first replies, staged judgements, progress/status updates, execution-result explanations, and final reports.

Do not copy this gate into runtime adapter prompts or external projects as a long-term rule body. Runtime adapters should point back to the AgentPal workspace core gates.
