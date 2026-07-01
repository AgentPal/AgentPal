# R213 Authorization And Revocation Functional Result

## Status

result: `pass`

execution_mode: `real_host_thread_plus_file_level_fixture`

real_host_thread_id: `019f1c91-9fcc-7511-be62-fdcd740c77f7`

Real host note: the follow-up thread completed Case 4 as read-only host
dialogue. It separated authorization and revocation record shapes from
Runtime write actions, and marked all writes as `not-run`.

## Case 4: Workspace Discovery Authorization

Input:

```text
/pal PalSmith
让 MiaCrossBorderCoach 只在当前工作区可发现，但不要允许自动委托，不要加入 contacts，不要上架 Marketplace。
```

Generated authorization record:

```text
evals/palbench/v0.5/palsmith/r213-functional-fixtures/user-pals/MiaCrossBorderCoach/authorization/authorization-record.md
```

Expected state:

- discovery: `workspace_scoped`
- invocation: `explicit_user_call_only`
- delegation: `false`
- contacts registration: `false`
- Marketplace: `none`
- memory access: `minimal`
- expires_at: present
- review_after: present
- revocation method: present

Boundary:

- discovery authorization does not imply delegation;
- discovery authorization does not modify central contacts;
- discovery authorization does not create official status;
- Marketplace draft work is separate from public listing.

## Revocation

Input:

```text
/pal PalSmith
撤销 MiaCrossBorderCoach 的 workspace discovery 授权，保留审计历史。
```

Generated revocation record:

```text
evals/palbench/v0.5/palsmith/r213-functional-fixtures/user-pals/MiaCrossBorderCoach/authorization/revocation-record.md
```

Expected post-revocation state:

- discovery: `false`
- invocation: `explicit_user_call_only`
- delegation: `false`
- contacts registration: `false`
- Marketplace: `none`
- memory access: `minimal`
- audit history preserved: `true`

## Decision

`pass`

Authorization and revocation are usable for user testing as no-code governance
records. They do not provide runtime enforcement by themselves.
