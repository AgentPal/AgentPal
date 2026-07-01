# R213 Revocation Record

```yaml
revocation_status: revoked_fixture
target_pal:
  name: Mia CrossBorder Coach
  path: evals/palbench/v0.5/palsmith/r213-functional-fixtures/user-pals/MiaCrossBorderCoach/
previous_authorization:
  status: active_fixture
  record_path: authorization/authorization-record.md
  expires_at: 2026-08-01
revoked_scope:
  discovery: true
  invocation: false
  delegation: false
  contacts_registration: false
  marketplace: none
preserved_scope:
  invocation: explicit_user_call_only
  delegation: false
  contacts_registration: false
  marketplace: none
post_revocation_state:
  discovery: false
  invocation: explicit_user_call_only
  delegation: false
  contacts_registration: false
  marketplace: none
  memory_access: minimal
audit:
  preserve_history: true
  revoked_by: R213 functional rehearsal
  revoked_at: 2026-07-01
  reason: user requested workspace discovery revocation
write_boundary:
  contacts_unchanged: true
  official_pals_unchanged: true
  runtime_changes: false
```
