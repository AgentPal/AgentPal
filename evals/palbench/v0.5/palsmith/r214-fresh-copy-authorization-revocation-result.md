# R214 Fresh Copy Authorization Revocation Result

## Status

result: `pass`

execution_mode: `fresh_copy_file_write_fixture`

## Case 6: Workspace Discovery Authorization

Input:

```text
/pal PalSmith
让 MiaCrossBorderCoach 只在当前工作区可发现，但不要允许自动委托，不要加入 contacts，不要上架 Marketplace。
```

Authorization record:

```text
evals/palbench/v0.5/palsmith/r214-fresh-copy-test/user-pals/MiaCrossBorderCoach/authorization/authorization-record.md
```

Validation:

- discovery: `workspace_scoped`
- delegation: `false`
- contacts_registration: `false`
- marketplace_public_listing: `false`
- memory_access: `minimal`
- expires_at: present
- review_after: present
- revocation path: present

## Case 7: Discovery Revocation

Input:

```text
/pal PalSmith
撤销 MiaCrossBorderCoach 的 workspace discovery 授权，保留审计历史。
```

Revocation record:

```text
evals/palbench/v0.5/palsmith/r214-fresh-copy-test/user-pals/MiaCrossBorderCoach/authorization/revocation-record.md
```

Validation:

- discovery becomes false / revoked: pass
- delegation remains false: pass
- contacts registration remains false: pass
- Marketplace public listing remains false: pass
- audit history preserved: pass

## Boundary

These records are no-code governance fixtures. They are not runtime
enforcement, central contacts registration, official promotion, or Marketplace
publication.

## Decision

`pass`
