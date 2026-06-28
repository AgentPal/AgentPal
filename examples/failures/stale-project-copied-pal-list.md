# Failure Example: Stale Project-Copied Pal List

Failure shape:

```text
A project-local copied roster file contains a copied list of Pals and says it is authoritative.
```

Why this fails:

- AgentPal contacts / registry are the Pal source of truth.
- A copied Pal list can become stale when a Pal is added, removed, renamed, or repaired.
- Direct `/pal Name` and owner judgement must resolve from the AgentPal workspace, not from a project-local roster copy.

Correct shape:

```text
A thin binding file says the roster is read from:
- agentpal_workspace_root/workspace/organization/contacts/pals.json
- agentpal_workspace_root/workspace/organization/contacts/PAL_CONTACTS.md
```
