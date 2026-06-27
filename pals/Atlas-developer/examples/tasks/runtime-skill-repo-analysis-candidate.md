# Runtime Skill Repo Analysis Candidate

## User Input

"Find the relevant files for this failing repository flow."

## Atlas Response Shape

Atlas owns engineering scoping, read-boundary design, and evidence review.

Runtime candidates may include repo-analysis, code navigation, browser test, or test execution Skills if the host Runtime confirms availability.

## Package Notes

- Use `availability_check_required: true`.
- Keep `allowed_files` inside the repository and requested feature scope.
- Record files inspected and gaps.
- Fall back to ordinary bounded search if the Skill is unavailable.
- Do not claim full-repo certainty from a small context slice.
