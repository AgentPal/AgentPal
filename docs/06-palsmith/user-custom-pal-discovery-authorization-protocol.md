# User Custom Pal Discovery Authorization Protocol

This is the user-docs entry for the PalSmith protocol that governs user custom Pal discovery, invocation, limited delegation, contacts registration, Marketplace draft work, expiry, and revocation.

Canonical protocol file:

```text
official/pals/PalSmith-pal-governor/core/user-custom-pal-discovery-authorization-protocol.md
```

Read this protocol when you need the full rule body. The short rule is:

- user custom Pals are private by default;
- discovery, invocation, delegation, contacts registration, and Marketplace draft work are separate permission fields;
- discovery does not allow automatic delegation;
- contacts registration is a separate governance task;
- Marketplace draft metadata is not public listing;
- expiry and revocation must be recorded before any non-private scope is enabled;
- no runtime, CLI, scanner, daemon, connector, backend service, or Marketplace backend is created by this protocol.

Related user paths:

- [`custom-pal-creation-to-authorization-flow.md`](custom-pal-creation-to-authorization-flow.md)
- [`user-custom-pal-discovery-authorization.md`](user-custom-pal-discovery-authorization.md)
- [`../../prompts/palsmith/authorize-user-custom-pal-discovery.md`](../../prompts/palsmith/authorize-user-custom-pal-discovery.md)
- [`../../prompts/palsmith/revoke-user-custom-pal-discovery.md`](../../prompts/palsmith/revoke-user-custom-pal-discovery.md)
