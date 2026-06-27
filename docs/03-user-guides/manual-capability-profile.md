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

## Where Templates Live

Copyable templates live in:

```text
templates/capability-inventory/
```

Templates are reusable shapes. They are not facts and do not prove any capability is installed.

## Where Examples Live

Examples live in:

```text
examples/capability-inventory/
```

Examples are synthetic or illustrative. Do not treat them as current organization capability records.

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

## Step 6: Save To The Right Place

Use organization records for public-safe, organization-level capability notes:

```text
workspace/organization/capability-inventory/
```

Use project records for capability notes specific to a bound external project:

```text
workspace/projects/<project-id>/capability-inventory/
```

Do not copy profile records into the external user project's `.agentpal/` directory by default.

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
