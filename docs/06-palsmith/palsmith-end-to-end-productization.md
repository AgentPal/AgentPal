# PalSmith End-To-End Productization

This page defines the v0.2 productized path for using PalSmith to create a single professional Pal or a small AI team. It closes the loop from plain-language user intent to a Runtime Task Package, evidence review, repair package, and first usage example.

PalSmith remains a no-code Pal asset governance Pal. It does not become a CLI, scanner, validator, importer, exporter, installer, daemon, UI, or background service.

## What PalSmith Can Do Now

PalSmith can now prepare end-to-end creation guidance for:

- turning a user goal into a scoped professional Pal proposal;
- turning source material into traceable Pal assets;
- turning a broad work goal into a small AI team design;
- preparing copyable Runtime Task Packages for approved file creation;
- reviewing created Pal or team assets for health, job fitness, privacy, and release readiness;
- preparing a repair package when the first draft is shallow, unsafe, or incomplete;
- ending each creation path with usage examples and a clear readiness status.

The current runtime, such as Codex or Claude Code, is only the execution layer. PalSmith plans and judges. The runtime reads or writes files only after the user confirms the target scope.

## End-To-End Loop

1. User gives a natural-language goal or material bundle.
2. PalSmith asks only missing high-impact clarification questions.
3. PalSmith classifies the request as a single Pal, AI team, material ingestion, health check, or repair task.
4. PalSmith preserves source intent, privacy boundaries, and uncertainty.
5. PalSmith drafts the Pal or team design.
6. PalSmith prepares a Runtime Task Package with allowed reads, allowed writes, forbidden writes, and expected evidence.
7. The execution layer performs approved local work and returns evidence.
8. PalSmith runs a health and job-fitness review from the evidence.
9. PalSmith prepares a repair package when gaps remain.
10. PalSmith provides usage examples and readiness advice.

## Single Professional Pal Flow

Use this flow when the user wants one callable Pal for a real job.

### Required Input

- target job and user group;
- examples of work the Pal should handle;
- work the Pal must not handle;
- source materials and ownership or sensitivity limits;
- desired language, tone, and output shape;
- whether optional external research is allowed;
- private, team-local, or public-shareable target status.

### PalSmith Output

- Pal name and short id proposal;
- role statement and "not responsible for" boundary;
- first-call examples;
- required root files and output contract;
- knowledge, skills, workflows, runbooks, templates, examples, and evals plan;
- material ingestion map when user sources are provided;
- Runtime Task Package for approved file creation;
- health-check report and repair package template.

### Acceptance

The single Pal path is acceptable only when a user can copy one task package, approve a target path, receive draft Pal assets, see evidence, run a health check, and understand the first useful `/pal <Name> ...` call.

## AI Team Flow

Use this flow when the user wants a coordinated set of Pals for a broader goal.

### Required Input

- end goal and recurring work situations;
- preferred team size or maximum team size;
- user-facing entry Pal expectation;
- sensitive materials and private boundaries;
- known existing Pals that should be reused or avoided;
- whether the team is private, team-local, or public-shareable.

### PalSmith Output

- small team purpose and success criteria;
- candidate capability domains;
- member Pal cards with job, boundary, and evidence needs;
- Main Pal / leader / conductor recommendation;
- collaboration boundaries and context-sharing rules;
- clear note that members are candidate capability holders, not permanent route targets;
- Runtime Task Package for approved team asset creation;
- team health check and repair package.

Mira remains the default entry Pal and Conductor unless a user explicitly installs a different team entry Pal and the current central Pal roster supports it. PalSmith must not create fixed natural-language dispatch rules.

## Material Ingestion Flow

When the user supplies notes, documents, chats, examples, procedures, tone samples, or previous outputs, PalSmith maps them into asset types:

- stable facts and concepts become knowledge candidates;
- repeated operation patterns become runbooks, workflows, or Skills;
- representative inputs and outputs become examples;
- failure modes and acceptance cases become evals;
- persona, voice, and boundary material becomes identity or output-contract candidates;
- private user facts stay excluded, private, or internal-only according to the user's boundary.

Source preservation is mandatory. PalSmith should keep a source inventory, a coverage map, and a sensitivity mark instead of compressing all material into a vague summary.

## Health And Repair Flow

Every creation path ends with a health review. The health check inspects:

- PAL clarity and job ownership;
- legal and parseable `pal.json`;
- root files and output contract;
- real content in knowledge, skills, workflows, runbooks, examples, evals, and templates;
- empty-shell risk;
- private data leakage;
- fixed routing or Skill-as-Pal mistakes;
- usage examples and acceptance evidence;
- publish readiness or private-use readiness;
- AI team leader, Main Pal, conductor, and collaboration boundaries when a team is created.

If the result is incomplete, PalSmith prepares a repair package that names each issue, risk, suggested files, runtime repair instructions, and acceptance criteria.

## Not-Do List

PalSmith must not:

- claim it executed local file operations itself;
- create or require a PalSmith CLI, scanner, validator, UI, installer, daemon, importer, or exporter;
- write contacts or registry entries inside the first creation package;
- run imported scripts or untrusted files;
- turn ordinary Skills, tools, repositories, models, or knowledge bundles into Pal contacts;
- expose private memory or user source material in public examples;
- create fixed dispatch rules, fixed collaborators, or permanent domain routes;
- present Deep Conductor, multi-agent execution, or automatic capability probing as current v0.2 behavior.

## v0.2 Boundary

v0.2 productizes the manual no-code creation loop. It gives users practical paths, copyable task packages, examples, health checks, and repair packages.

v0.2 does not ship runtime automation, automatic Pal installation, automatic GitHub publishing, background validation, or active Deep Conductor behavior.

## v0.3 Boundary

v0.3 may further improve AI team governance, cross-Pal review coordination, publish quality gates, runtime call verification, GitHub import verification, and richer team lifecycle guidance. Those remain methodology and Runtime Task Package workflows until a future release explicitly adds runtime behavior.

## v0.2 Acceptance

The productized path is ready for first implementation when:

- a single-Pal task package is copyable and complete;
- an AI-team task package is copyable and complete;
- material ingestion maps user sources to proper Pal assets;
- health checks and repair packages catch shallow or unsafe output;
- examples show realistic creation, clarification, evidence, and usage;
- evals cover the full loop and boundary failures;
- public docs link to the path without claiming v0.2 is complete.
