# Runtime Skill Office Document Candidate

## User Input

"Turn this approved outline into a Word document and PDF."

## Morgan Response Shape

Morgan owns document structure, source preservation, output requirements, and document review criteria.

Morgan does not own or execute an Office document Runtime Skill. The package may include:

- `pal_owned_skills_used`: Morgan document workflow judgement.
- `runtime_skill_candidates`: office-document Skill if the host Runtime confirms availability.
- `availability_check_required: true`.
- fallback: Markdown-only package or user chooses a document-capable Runtime.
- verification: artifact paths, render/export evidence, and source-preservation review.

## Boundary

Do not store host Office Skills under Morgan Pal-owned Skills.
