# Revoke User Custom Pal Discovery Authorization

Use this prompt when a user wants PalSmith to revoke or narrow discovery authorization for a user custom Pal.

Copy the whole prompt into the host runtime conversation.

```text
/pal PalSmith

I want to revoke or narrow discovery authorization for a user custom Pal.

User custom Pal:
- name:
- current path:
- authorization record path, if known:
- scope to revoke:
  - workspace_discovery:
  - explicit_invocation_alias:
  - limited_delegation:
  - contacts_registration_request:
  - marketplace_draft_work:
- reason:
- effective date:

Please do the following:

1. Treat this as a no-code governance task.
2. Identify the current authorization record or say `missing` if it cannot be found from the provided context.
3. Prepare a revocation plan that preserves audit history.
4. Separate each authorization field. Revoking discovery must not silently change unrelated fields unless I explicitly approve it.
5. Prepare a bounded Runtime Task Package only for the files that must be changed.
6. Do not delete the user custom Pal.
7. Do not modify `workspace/organization/contacts/`.
8. Do not move anything into `official/pals/`.
9. Do not claim Marketplace unlisting, connector shutdown, background sync, scanner action, daemon action, or runtime enforcement unless the current host runtime proves it.
10. Ask me for confirmation before any write.

Return:
- current status
- scope to revoke
- current authorization record status: `active`, `missing`, `expired`, `revoked`, or `unknown`
- revocation record shape
- files that would change
- fields that remain unchanged
- post-revocation state for discovery, invocation, delegation, contacts registration, Marketplace, and memory access
- rollback or re-authorization path
- Runtime Task Package, if a write is needed
```

Revocation record shape:

```yaml
revocation_status: proposed
target_pal:
  name:
  path:
previous_authorization:
  status:
  record_path:
  expires_at:
revoked_scope:
  discovery: false
  invocation: false
  delegation: false
  contacts_registration: false
  marketplace: none
preserved_scope:
  discovery:
  invocation:
  delegation:
  contacts_registration:
  marketplace:
post_revocation_state:
  discovery:
  invocation:
  delegation:
  contacts_registration:
  marketplace:
  memory_access: minimal
audit:
  preserve_history: true
  revoked_by:
  revoked_at:
  reason:
write_boundary:
  contacts_unchanged: true
  official_pals_unchanged: true
  runtime_changes: false
```
