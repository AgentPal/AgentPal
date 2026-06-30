# Asset Usage Memory Template

Status: R200 controlled write test fixture memory asset.

## Memory Candidate Shape

```text
memory_type: asset_usage_preference
source_task:
user_preference:
scope:
private_or_public:
allowed_storage_target:
requires_confirmation:
expires_or_review_after:
```

## Boundary

This fixture must not write private user memory into public Pal assets. For R200,
memory notes are evidence-only and must stay inside the fixture or R200 evidence
files unless a separate memory write is authorized.
