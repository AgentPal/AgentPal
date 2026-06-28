# Integration Profiles

## Boundary

This directory contains integration profiles and manual handoff notes only.

It does not contain real connectors, API clients, tokens, cookies, webhooks, credentials, sync code, scheduler code, or external system calls.

## Candidate Systems

| System | Allowed in this reusable pack | Forbidden in this reusable pack |
| --- | --- | --- |
| CRM | field map notes, manual export/import checklist | CRM export body, account IDs, API client, token, webhook |
| Lark | manual handoff note, review checklist | bot token, API call, automatic message send |
| WeCom | manual handoff note, review checklist | connector, webhook, automatic message send |
| Email system | copy review checklist, send approval note | SMTP settings, password, automatic send |

## Manual Handoff Note

If a real customer wants integration, create a private project record that states:

- system owner;
- approved data fields;
- export/import method;
- credential handling owner;
- human approval requirement;
- not-run checks.

Do not store that private record in this reusable pack.
