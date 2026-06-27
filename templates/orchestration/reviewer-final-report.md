# Reviewer Final Report Template

Use this template for a reviewer candidate's independent final report. A reviewer final report is one perspective, not the total decision.

```yaml
schema: agentpal.reviewer-final-report.v0.3
review_id:
reviewer_candidate:
review_angle:
verdict:
confidence:
key_findings:
  - <finding>
risks:
  - <risk>
missing_context:
  - <missing-context>
recommendation:
conditions:
  - <condition>
questions_for_owner:
  - <question>
notes:
```

Rules:

- The reviewer does not output the final total decision.
- The reviewer only reports its assigned perspective.
- Mira or the owner Pal performs synthesis after all final reports are available.
- If context is insufficient, state missing context instead of reading peer drafts or full history.
