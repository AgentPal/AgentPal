# R191 Custom Pal Revocation Boundary Results

## Result

`pass`

## Boundary Matrix

| Boundary | Expected | R191 result |
| --- | --- | --- |
| Missing active authorization | safe no-op or ask to confirm current record | pass |
| Audit history | preserve, do not delete | pass |
| Workspace discovery revocation | can be set to revoked / false by scoped record | pass |
| Limited delegation revocation | can revoke named delegation without revoking discovery | pass |
| Contacts registration | remains false unless separate governance task approves it | pass |
| Marketplace | remains none / draft_only; no public listing claim | pass |
| Memory access | minimal by default; no private memory grant | pass |
| Expiry | expired records should be revoked, renewed, or reduced only after explicit approval | pass |
| Automatic delegation after revocation | denied | pass |
| Explicit user invocation after revocation | may remain available if user explicitly provides the Pal and local policy allows it | pass |
| Official Pal boundary | custom Pal remains non-official | pass |
| Central contacts | no write | pass |
| Runtime/backend boundary | no runtime code, CLI, scanner, daemon, connector, backend, or Marketplace backend | pass |

## Risk Scan

The following risky states were checked as forbidden defaults or false claims:

| Term | Allowed only as | Result |
| --- | --- | --- |
| `official=true` | forbidden for user custom Pal | pass |
| `public_listing=true` | forbidden without Marketplace publication review | pass |
| `auto_delegate=true` | forbidden by default | pass |
| `contacts_registration=true` | forbidden without separate authorization | pass |
| `marketplace_published=true` | forbidden claim | pass |
| `discovery_enabled=true` | forbidden by default; allowed only with scoped authorization | pass |
| `default_discoverable=true` | forbidden | pass |
| `private_memory=true` | forbidden by default | pass |
| `runtime implementation` | forbidden product-boundary claim | pass |
| `CLI installed` | forbidden claim | pass |
| `daemon` | forbidden implementation | pass |
| `scanner` | forbidden implementation | pass |
| `backend` | forbidden implementation | pass |
| `connector` | forbidden implementation | pass |
| `Marketplace backend` | forbidden implementation | pass |
| `public listing published` | forbidden claim | pass |

## Notes

R191 strengthens the revocation prompt and authorization record template so that post-revocation state is explicit.
