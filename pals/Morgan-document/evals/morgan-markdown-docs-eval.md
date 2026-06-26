# Morgan Markdown Docs Eval

## Scenario

User asks Morgan to review a README for a v0.1 release candidate.

## Expected Morgan behaviour

- Checks title, summary, quick start, current behavior, limitations, verification, and links.
- Distinguishes current release behavior from future design.
- Requests diff or rendered evidence when files are edited.

## Pass criteria

- Findings are tied to exact sections or missing sections.
- Markdown structure is readable and source-backed.

## Fail criteria

- Reviews only grammar.
- Mixes future behavior into current behavior.
- Omits not-run checks.

