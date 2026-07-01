# MiaCrossBorderCoach Discovery Revocation Fixture

This fixture revokes the paired R215 authorization sample. It does not edit
global contacts or registry files because those files were never modified.

After revocation:

- automatic discovery is false;
- consult, handoff, and delegation are false;
- explicit invocation still requires a host-loaded path or future separate authorization;
- no official, Marketplace, backend, or connector claim exists.
