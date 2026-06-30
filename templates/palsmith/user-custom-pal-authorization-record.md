# User Custom Pal Authorization Record

Copy this template when a user explicitly authorizes discovery, invocation, delegation, contacts registration, or Marketplace draft work for a user custom Pal.

```yaml
pal_id:
pal_name:
pal_path:
pal_type: user_custom_pal
authorization_status: proposed
requested_by:
approved_by:
approved_at:
expires_at:
review_after:
scope:
  discovery: false
  invocation: false
  delegation: false
  contacts_registration: false
  marketplace: none
allowed_callers: []
allowed_tasks: []
denied_tasks: []
data_access:
  allowed: []
  denied: []
memory_access:
  default: minimal
  allowed: []
  denied: []
  private_memory_allowed: false
revocation:
  method:
  requested_by:
  revoked_at:
  evidence_path:
  preserve_audit_history: true
  post_revocation_state:
    discovery: false
    invocation: false
    delegation: false
    contacts_registration: false
    marketplace: none
    memory_access: minimal
audit_notes:
```

## Defaults

- `authorization_status` starts as `proposed`, not `enabled`.
- `scope.discovery` starts as `false`.
- `scope.invocation` starts as `false` unless the record explicitly limits it to user-initiated invocation.
- `scope.contacts_registration` starts as `false`.
- `scope.delegation` starts as `false`.
- `scope.marketplace` starts as `none` or `draft_only`.
- `memory_access.default` starts as `minimal`.
- `memory_access.private_memory_allowed` starts as `false`.
- `expires_at` or `review_after` is required before enabling any non-private scope.
- `revocation.method` is required before enabling any non-private scope.
- `revocation.preserve_audit_history` stays `true`.
- revocation should update the selected scope only and should list fields that remain unchanged.

## Required Notes

Record whether the authorization:

- keeps the Pal `official: false`;
- keeps central contacts unchanged;
- keeps public Marketplace listing disabled;
- separates discovery from delegation;
- names exactly who may call or delegate to the Pal;
- names data and memory that must not be shared.
