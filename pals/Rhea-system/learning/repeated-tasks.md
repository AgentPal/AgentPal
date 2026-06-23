# Rhea Repeated Tasks

Record repeated system-domain task families here.

```text
Task family:
Trigger examples:
- 
Count:
- 0
Candidate threshold:
- explicit user request to save a Skill, or similar operation count > 3, creates a formal Skill under Rhea's `skills/` directory
- explicit user request for a Runbook creates a Runbook under Rhea's `runbooks/` directory when safe and sufficiently specified
Potential future Skill:
- 
Notes:
- Use fallback method only when dedicated assets are missing.
- Candidate does not equal formal Skill.
```

## Example: startup-item-audit

This is a non-real-data example.

```text
Task family: startup-item-audit
Trigger examples:
- Check what starts with Windows
- Find apps that launch on login
- Review startup items before disabling

Count:
- 0

Candidate threshold:
- count >= 3, or explicit user request

Potential future Skill:
- windows-startup-item-audit

Notes:
- Use read-only checks first.
- Do not disable startup items without user confirmation.
- If the user asks whether this can become a fixed workflow, generate a Runbook candidate even when historical count is unknown.
- Trigger reason should be recorded as `explicit user request`.
- Suggested Runbook candidate: `windows-startup-item-audit-runbook`.
- Storage target: `pals/Rhea-system/learning/runbook-candidates.md`.
```

