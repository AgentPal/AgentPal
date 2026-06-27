# Manual Capability Profile Guide

## What This Guide Is For

Use this guide when a user, Pal, or host Runtime needs to add or update a Capability Inventory profile by hand.

Capability Inventory is a no-code profile layer. It records capability notes that Brain / Pal / Runtime can read during judgement. Profiles may be filled by a user, organized by a Pal from user-confirmed facts, or written back by a host Runtime after it reports evidence during a task.

## What Capability Inventory Is Not

Capability Inventory is not:

- an automatic scanner
- an automatic validator
- automatic discovery of every runtime, model, Skill, plugin, or MCP server
- an automatic execution engine
- a keyword router
- proof that a capability is currently available without evidence

Do not claim AgentPal scanned the machine unless the current host Runtime actually provided evidence.

## Where Standards Live

Standards live in:

```text
standards/capability-inventory/
```

Use standards to understand which fields and boundaries a profile should follow.

For Business System profiles, use:

```text
standards/capability-inventory/business-system-profile-standard.md
```

For Business System profile review flow, use:

```text
standards/capability-inventory/business-system-profile-review-flow.md
```

For Business System profile manual update evidence packs after an approved review, use:

```text
standards/capability-inventory/business-system-profile-manual-update-evidence-pack.md
```

For Business System profile manual writeback replay records after a manual writeback has happened, use:

```text
standards/capability-inventory/business-system-profile-manual-writeback-replay-record.md
```

For Business System profile audit trail indexes across review, evidence, replay, rollback, and second verification records, use:

```text
standards/capability-inventory/business-system-profile-audit-trail-index.md
```

## Where Templates Live

Copyable templates live in:

```text
templates/capability-inventory/
```

Templates are reusable shapes. They are not facts and do not prove any capability is installed.

Business System profile review packets use:

```text
templates/capability-inventory/business-system-profile-review-packet.md
```

Business System profile manual update evidence packs use:

```text
templates/capability-inventory/business-system-profile-manual-update-evidence-pack.md
```

Business System profile manual writeback replay records use:

```text
templates/capability-inventory/business-system-profile-manual-writeback-replay-record.md
```

Business System profile audit trail indexes use:

```text
templates/capability-inventory/business-system-profile-audit-trail-index.md
```

## Where Examples Live

Examples live in:

```text
examples/capability-inventory/
```

Examples are synthetic or illustrative. Do not treat them as current organization capability records.

Business System profile examples live in:

```text
examples/capability-inventory/business-system-profiles/
```

Start with `manual-github-profile-walkthrough.md` for a GitHub manual flow, `manual-notion-profile-walkthrough.md` for a non-code system flow, `github-project-record-reference.example.md` for a project reference example, `unknown-not-run-missing-examples.md` for the difference between `unknown`, `not-run`, and `missing`, and `non-verifiable-business-system-fields.md` for fields AgentPal cannot verify by itself.

Public-safe central project record examples that reference Business System profiles live in:

```text
examples/project-records/business-system-profile-references/
```

These examples are not real private project records. They show project-level scope, limitations, not-run checks, missing evidence, and project usage memory without updating organization truth.

Business System profile review examples live in:

```text
examples/capability-inventory/business-system-profile-reviews/
```

These examples show project usage memory proposing review without automatically updating organization capability profiles. They also include a manual update evidence pack example for the approved-review stage, a manual writeback replay example for the after-writeback audit stage, and an audit trail index example for summarizing related records, still without performing profile updates, automatic rollback, external API calls, connector setup, missing-evidence closure, or credential storage.

## Where Organization Records Live

Organization-level capability records live in:

```text
workspace/organization/capability-inventory/
```

Use this location for public-safe capability notes that apply across the AgentPal organization.

## Where Project Records Live

Project-level capability records live in:

```text
workspace/projects/<project-id>/capability-inventory/
```

Use this location for a specific bound project's available or used capabilities. Real project records are private by default and should not be committed unless they are explicitly made public-safe examples.

External user projects should not receive copied Capability Inventory directories. They keep only thin binding files such as `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and protected root instruction blocks.

## Step 1: Choose Profile Type

Choose the closest profile type:

- Runtime
- Model
- Reasoning
- Skill
- Plugin
- MCP
- Business System
- Pal capability

If the profile does not fit any type, stop and write a short note explaining what is unclear before inventing a new category.

## Step 2: Copy A Template

Copy the closest template from:

```text
templates/capability-inventory/
```

Save the new profile in the correct organization or project record location. Do not edit examples as if they were current records.

## Step 3: Fill Only Confirmed Information

Fill only information that is confirmed by the user, a current file, or current host Runtime evidence.

Use `unknown` for unconfirmed information. Do not guess model access, plugin installation, tool permissions, cost, speed, or capability limits.

## Step 4: Mark Source And Confidence

Every profile should make source and confidence clear.

Suggested source labels:

- `user_confirmed`
- `runtime_reported`
- `file_evidence`
- `inferred`
- `unknown`

Suggested confidence labels:

- `high`
- `medium`
- `low`
- `unknown`

Use `inferred` only when the inference is obvious from evidence, and explain the basis.

## Step 5: Add Limitations

Record what the capability is not suitable for, what is unavailable, and what needs confirmation.

Examples:

- model name is unknown
- reasoning strength controls are unknown
- plugin is listed but not tested
- Skill exists but requires user approval
- business system access is role-limited

Do not claim availability unless confirmed.

## Business System Profile Notes

Use Business System profiles for external systems such as GitHub, Feishu, Notion, CRM, Jira, Linear, WordPress, ERP, OA, databases, or customer-specific tools.

A Business System profile records capability notes and governance boundaries only. It is not a connector, API client, permission grant, credential store, automatic scanner, automatic validator, background sync job, release tool, or automatic execution path.

Business System profiles should record only confirmed or user-approved facts, such as:

- system name and system type
- access method
- required permissions
- allowed operations
- forbidden operations
- output destinations
- verification method
- privacy boundary
- credential policy
- source and confidence
- limitations

If availability, permissions, write access, API access, or output destinations are not confirmed, keep them as `unknown` or empty arrays. Do not infer access from the system name.

Do not store credentials, private tokens, passwords, API keys, session cookies, or private secrets in Business System profiles.

External writes to business systems require explicit user authorization and current host Runtime evidence. The profile may inform AI judgement, but it must not trigger writes or routing by itself. A system name or `system_type` must not become a keyword route to a Pal, Runtime, Skill, plugin, MCP server, or external tool.

Manual Business System examples should keep three evidence states separate:

- `unknown`: a fact has not been confirmed and must not be invented.
- `not-run`: a check or operation did not execute and must not be reported as pass or fail.
- `missing`: required evidence is absent and must be reported or requested.

Do not convert `unknown` into available. Do not convert `not-run` into pass. Do not hide missing evidence.

For non-code systems such as Notion, CRM, Feishu, OA, ERP, WordPress, or customer-specific tools, access, write permission, admin permission, API availability, export permission, billing or plan capability, user role, and business workflow ownership usually cannot be verified by AgentPal itself. They need user confirmation, host Runtime evidence, an exported report, a screenshot or UI confirmation provided by the user, or a documented admin setting. If that evidence is absent, keep the fields as `unknown`, checks as `not-run`, and evidence as `missing`.

## Step 6: Save To The Right Place

Use organization records for public-safe, organization-level capability notes:

```text
workspace/organization/capability-inventory/
```

Use project records for capability notes specific to a bound external project:

```text
workspace/projects/<project-id>/capability-inventory/
```

Do not copy profile records into the external user project's `.agentpal/` directory by default. Do not create `.agentpal/capability-inventory/` or `.agentpal/business-systems/` during thin binding unless a future user-approved workflow explicitly changes that boundary.

Do not store credentials, private tokens, API keys, session cookies, private customer data, or secret machine paths in Capability Inventory records.

## Step 7: Use As AI Judgement Input

Brain / Pal may read Capability Inventory profiles to judge options, risks, prompt shape, Runtime suitability, and verification needs.

Core must not route by keywords. Capability profiles must not become:

- `keyword_map`
- `domain_map`
- `role_map`
- deterministic task-to-Pal routing
- deterministic task-to-runtime routing without current evidence

Explicit `/pal Name` or `@Name` calls are user intent signals, not keyword routes.

## Step 8: Update Usage Memory After Tasks

After a real task, update usage memory only from evidence. Record what worked, what failed, what was not run, and what should be rechecked next time.

Do not turn usage memory into an automatic score, benchmark, or certification claim. If verification did not run, write `not-run` or `unknown`.

Project usage memory records what happened in one project. It is not organization truth, must not silently update organization capability profiles, must not update the central Pal roster, and must not be copied into external project `.agentpal/` by default. See `docs/03-user-guides/project-usage-memory-boundary.md`.

If project usage memory suggests an organization-level Business System profile change, create a review packet and keep the decision blocked until explicit user confirmation and reviewable host Runtime evidence are present. If the review is later approved for manual update, create a Manual Update Evidence Pack with a rollback note and second verification checklist before any organization profile writeback. If a manual writeback later happens, create a Manual Writeback Replay Record to audit changed fields, rollback record, and second verification result. If several related records need summary, create an Audit Trail Index to list paths, statuses, open unknowns, not-run checks, missing evidence, risk notes, and next manual action suggestions. If second verification did not run, keep the status as `second_verification_not_run`; do not report it as pass. If evidence remains missing, keep it missing; do not auto-close it from the index.
