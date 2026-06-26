# Web Research To Knowledge Protocol

Status: R-PalSmith-16 v0.4-fix protocol.

PalSmith may request web research through the current Agent Runtime. AgentPal does not include a crawler, downloader, scanner, or validator.

## Process

1. Define target Pal role and responsibilities.
2. List research questions.
3. Ask user confirmation for live web research if needed.
4. Current Runtime searches and reads sources.
5. Record URL, title, publisher, date accessed, source date, and applicability.
6. Assess credibility and uncertainty.
7. Extract job knowledge.
8. Extract skill requirements.
9. Extract workflows/runbooks.
10. Extract output templates.
11. Extract risk boundaries.
12. Generate candidate knowledge and candidate skills.
13. Ask user confirmation before writing stable Pal assets.

## Required Honesty Labels

- `web research not run`
- `based on existing local knowledge, not live web research`
- `candidate knowledge, needs review`

## Output

- research task package
- source inventory
- credibility notes
- candidate knowledge
- candidate skill/workflow/template/eval suggestions
- uncertainty list
