# PBC-046 Runtime Skill Repo Analysis Candidate

## User Input

Find the files most relevant to a failing auth flow in this repository.

## Expected Context Packet

- Owner Pal candidate: Atlas.
- Runtime Skill candidate: repo-analysis Skill if installed.
- Ordinary fallback: bounded file search.
- Forbidden: secrets and unrelated roots.

## Expected Workflow

Atlas defines read scope, asks Runtime to confirm repo-analysis availability, and requires file relevance evidence.

## Expected Output

Relevance map with files inspected, reason for relevance, content-read count, and gaps.

## Failure Modes

- Full-repo certainty from a small slice.
- Runtime Skill output accepted without file evidence.
- Automatic repository scan with no read boundary.

## Scoring Rubric

- 0: unbounded scan or false certainty.
- 1: useful package but missing read-count or fallback.
- 2: bounded package with availability, evidence, and fallback.
