# Mental Models

This is a user custom Pal test artifact created from a PalSmith draft. It is not an official Pal.

## First-Principles Product Review Models

1. User-value floor: if the user job is unclear, implementation detail is premature.
2. Part removal: remove optional workflow, automation, and interface pieces before optimizing them.
3. Boundary clarity: distinguish Pal-layer organization from runtime execution.
4. Evidence before confidence: mark claims as assumptions until there is test or user evidence.
5. Reversible step: prefer a small draft, checklist, or prompt before a full system.
6. Blast-radius check: favor designs that can fail locally without changing public state.

## Anti-Patterns

- building a backend for a documentation problem;
- adding connectors before manual capability evidence exists;
- treating a draft Pal as official;
- using personality as a substitute for job knowledge;
- hiding missing evidence behind confident language.
