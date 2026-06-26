# Example: Create Xiaohongshu Operations Pal

This is an example only. It contains no private user data and is not an execution record.

## User Says

`/pal PalSmith 创建一个小红书运营 Pal`

## PalSmith Questions

- What should the Pal be called: `小红书运营 Pal`, `Xiaohongshu Ops`, or another name?
- What work should it own: content planning, note structure, publish checklist, campaign review, account growth, or something else?
- What should it not do: account login, automated posting, scraping, medical/financial claims, or final business decisions?
- Who will use it: solo creator, brand operator, agency, or team?
- Do you have examples, brand tone, product notes, campaign reports, or preferred post templates to upload?
- Should current Runtime perform web research on public Xiaohongshu content-operation practices, or should this draft use only local knowledge?
- Should registry/contacts updates be suggestions only?

## Job Expertise Model

- Required knowledge: platform content structure, note planning, audience positioning, content calendar, brand voice, risky claim boundaries.
- Required skills: content brief design, title/cover idea review, campaign checklist, performance review, user material ingestion.
- Required workflows: idea intake, draft review, publish checklist, campaign postmortem.
- Required evals: normal content plan, risky unsupported claim, missing brand voice, overbroad growth guarantee.

## Plan

- Define responsibility: Xiaohongshu content planning, note structure, publishing checklist, campaign review.
- Boundary: no account login, no automated posting, no scraping, no unsupported platform claims.
- Use user materials if approved.
- Use web research only through a Runtime Task Package and source report.
- Create a public-safe Pal Pack draft with real knowledge/skills/workflows/evals.
- Keep registration as later `registry update task package` and `contacts update task package`.

## Runtime Task Package

- `task_name`: Pal Creation Task Package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: Pal Pack templates, standard docs, approved user materials, approved research report
- `allowed_write_paths`: `pals/Xiaohongshu-ops/`
- `forbidden_write_paths`: `contacts/`, `registry/`, private memory
- `required_exclusions`: `memory/user/`, `memory/project/`, `state/`, `reports/`
- `user_confirmation_required`: yes

## Handoff To Runtime

After confirmation, the current Agent Runtime creates the draft files and returns file paths plus `pal.json` parse evidence.

## PalSmith Acceptance

Accept if the draft has required root files, job-specific knowledge, actionable skills, workflows, evals, no private memory, no unconfirmed registry/contacts write, and a Pal Job Fitness Report.
