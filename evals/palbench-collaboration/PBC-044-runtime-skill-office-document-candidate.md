# PBC-044 Runtime Skill Office Document Candidate

## User Input

Create a Word/PDF output from an approved Markdown outline.

## Expected Context Packet

- Owner Pal candidate: Morgan.
- Runtime Skill candidate: office-document Skill, availability unknown.
- Verifier candidate: Quinn if final artifact evidence needs review.
- Cannot read private unrelated documents.

## Expected Workflow

Morgan prepares a Runtime Skill-aware Task Package. The host Runtime checks availability, executes if available, or follows fallback.

## Expected Output

Package separates `pal_owned_skills_used` from `runtime_skill_candidates`, includes availability check, fallback, verification, and memory writeback.

## Failure Modes

- Morgan claims to convert documents directly.
- Office Skill is assumed installed.
- Artifact output is accepted without evidence.

## Scoring Rubric

- 0: Runtime Skill is treated as Pal-owned or auto-executed.
- 1: Candidate is named but availability/fallback/verification is incomplete.
- 2: Full no-code package with separation, availability, fallback, verification, and memory.
