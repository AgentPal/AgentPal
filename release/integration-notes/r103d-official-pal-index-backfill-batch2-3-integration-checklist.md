# R103-D Official Pal Index Backfill Batch 2/3 Integration Checklist

Date: 2026-06-28

## Purpose

This checklist is for the next integration round that combines R103-A, R103-B, and R103-C outputs.

R103-D cannot assume the final contents of the parallel threads. Treat all expected paths below as integration targets to verify against the final worktree, not as evidence that the files already exist.

## Expected A Files

Record the final R103-A owner, selected Pals, and changed files before integration.

Minimum expected shape:

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R103-A gate or boundary note | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| R103-A selected Pal README / index files | exact files under approved `official/pals/<Pal>/...` paths | pending |
| R103-A validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R103-A integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R103-A internal report | `J:\开发\AgentPal_dcos\开发记录\` | pending |

Do not infer the selected Pal list from R100-B alone. Use the final R103-A evidence.

## Expected B Files

Record the final R103-B owner, selected Pals, and changed files before integration.

Minimum expected shape:

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R103-B gate or boundary note | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| R103-B selected Pal README / index files | exact files under approved `official/pals/<Pal>/...` paths | pending |
| R103-B validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R103-B integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R103-B internal report | `J:\开发\AgentPal_dcos\开发记录\` | pending |

If R103-B is Batch 3, verify it did not overlap with R103-A selected paths.

## Expected C Files

Record the final R103-C owner, selected Pal, and changed files before integration.

Minimum expected shape:

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R103-C PalSmith runbooks policy note | public Markdown under `release/integration-notes/` or `evals/palbench/pal-asset/` | pending |
| PalSmith runbooks README pilot file | exact approved file, likely `official/pals/PalSmith-pal-governor/runbooks/README.md`, if pilot completed | pending |
| R103-C validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R103-C internal report | `J:\开发\AgentPal_dcos\开发记录\` | pending |

If R103-C decides not to create PalSmith `runbooks/README.md`, record the decision and evidence instead of treating the missing file as a silent pass.

## Expected Validation Files

The integration round should expect one validation record per parallel thread plus the R103-D validation file:

| Validation | Required Handling |
| --- | --- |
| R103-A validation | must exist or issue |
| R103-B validation | must exist or issue |
| R103-C validation | must exist or issue |
| `release/fresh-clone-checks/r103d-local-official-pal-index-backfill-gate-validation.md` | must exist |
| R104 integration validation | create during the integration round |

Each validation must state not-run items explicitly.

## Expected Internal Reports

Internal reports belong under:

```text
J:\开发\AgentPal_dcos\开发记录\
```

Expected handling:

- R103-A internal report: must exist or issue.
- R103-B internal report: must exist or issue.
- R103-C internal report: must exist or issue.
- R103-D internal report: must exist.
- R104 integration report: create during the integration round.

Do not copy internal reports into the public repository.

## Commands To Run

Use equivalent local checks. These are manual evidence commands, not a new validator program.

```powershell
git status --short --branch
git diff --name-only -- official/pals
git diff --name-only -- workspace/organization/contacts README.md RESOURCE_INDEX.md agentpal.json
git diff --name-only -- 'official/pals/**/pal.json'
Get-ChildItem official/pals -Directory | Measure-Object
Get-ChildItem official/pals -Directory | ForEach-Object { Get-Content (Join-Path $_.FullName 'pal.json') -Raw | ConvertFrom-Json | Out-Null }
Get-Content workspace/organization/contacts/pals.json -Raw | ConvertFrom-Json | Out-Null
Get-ChildItem -Recurse -Filter asset-manifest.json official/pals
rg -n '"(keyword_map|domain_map|role_map)"\s*:' evals release official/pals
rg -n "sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY" evals release official/pals
git diff --check
```

If `rg` is unavailable, use another search tool and record the substitution.

## Fix Policy

Integration fixes may only repair issues inside the integration round's approved paths.

Allowed integration fixes, if explicitly in scope:

- typo or formatting repair in R103 integration notes;
- missing validation summary field;
- issue template completion;
- README/index wording that remains documentation-only and public-safe.

Not allowed without a separate approved thread:

- `pal.json` metadata change;
- real `asset-manifest.json` generation;
- moving, deleting, or renaming existing official Pal assets;
- central roster change;
- shared entry change;
- external project `.agentpal` write;
- creating code, scanner, validator, installer, connector, daemon, database, marketplace, or auto-execution behavior.

## Commit Policy

Before commit:

- classify all R103-looking untracked files;
- stage only approved integration files;
- verify staged diff contains no unrelated thread work;
- run `git diff --cached --check`;
- record validation evidence.

Commit message suggestion for the later integration round:

```text
test: integrate official pal index backfill batches
```

Use a different message if the integration owner narrows or changes the scope.

## No Remote Action Policy

Normal development and integration rounds must not run:

- `git push`
- `git pull`
- `git fetch`
- tag creation or modification
- GitHub Release creation or modification
- release/tag migration
- remote overwrite of local work

If a future release manager needs remote action, it must be a separate explicit release task with current evidence and user approval.
