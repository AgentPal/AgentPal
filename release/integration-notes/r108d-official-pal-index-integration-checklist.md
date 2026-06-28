# R108-D Official Pal Index Integration Checklist

Date: 2026-06-28

## Purpose

This checklist is for the next R109 integration round that combines R108-A, R108-B, and R108-C outputs.

R108-D cannot assume the final contents of the parallel threads. Treat all expected paths below as integration targets to verify against the final worktree, not as evidence that files already exist.

## Expected R108-A Files

Record the final R108-A owner, selected paths, and decisions before integration.

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R108-A boundary note or gate | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| Mira skills index outcome | `official/pals/Mira-main/skills/index.md` or approved equivalent / documented no-write decision | pending |
| R108-A validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R108-A integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R108-A internal report | `private completion report outside the public repository` | pending |

Mira-specific work must preserve the Main Pal / Leader Pal / Conductor boundary and must not create keyword routing.

## Expected R108-B Files

Record the final R108-B owner, selected paths, and decisions before integration.

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R108-B boundary note or gate | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| PalSmith skills index outcome | `official/pals/PalSmith-pal-governor/skills/index.md` or approved equivalent / documented no-write decision | pending |
| R108-B validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R108-B integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R108-B internal report | `private completion report outside the public repository` | pending |

Verify that Agent / Runtime Skills are references only and that no runtime skill registry files are copied into Pal `skills/`.

## Expected R108-C Files

Record the final R108-C audit target, findings, and decisions before integration.

| Item | Expected Evidence | Result |
| --- | --- | --- |
| Mira root-entry wording audit | public Markdown under `release/integration-notes/` or `evals/palbench/pal-asset/` | pending |
| audited file list | exact Mira root-entry files recorded | pending |
| old `.agentpal` wording classification | pass / issue / accepted-risk recorded | pending |
| R108-C validation or audit evidence | public Markdown under `release/fresh-clone-checks/` or equivalent integration note | pending |
| R108-C internal report | `private completion report outside the public repository` | pending |

If R108-C edits root-entry wording, verify the edits are explicitly allowed, documentation-only, and behavior-preserving.

## Expected Validation Files

The integration round should expect one validation record per parallel thread plus the R108-D validation file:

| Validation | Required Handling |
| --- | --- |
| R108-A validation | must exist or issue |
| R108-B validation | must exist or issue |
| R108-C validation / audit evidence | must exist or issue |
| `release/fresh-clone-checks/r108d-local-official-pal-index-integration-gate-validation.md` | must exist |
| R109 integration validation | create during the integration round |

Each validation must state `not-run` items explicitly.

## Expected Internal Reports

Internal reports belong under:

```text
private completion report outside the public repository
```

Expected handling:

- R108-A internal report: must exist or issue.
- R108-B internal report: must exist or issue.
- R108-C internal report: must exist or issue.
- R108-D internal report: must exist.
- R109 integration report: create during the integration round.

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

Integration fixes may only repair issues inside the R109 integration round's approved paths.

Allowed integration fixes, if explicitly in scope:

- typo or formatting repair in R108 integration notes;
- missing validation summary field;
- issue template completion;
- README/index wording that remains documentation-only and public-safe;
- narrow stale note correction when the source evidence is current.

Not allowed without a separate approved thread:

- `pal.json` metadata change;
- real `asset-manifest.json` generation;
- moving, deleting, or renaming existing official Pal assets;
- central roster change;
- shared entry change;
- external project `.agentpal` write;
- copying Agent Skill files into Pal `skills/`;
- copying report bodies into memory;
- promoting raw research directly to knowledge;
- creating code, scanner, validator, installer, connector, daemon, database, marketplace, or auto-execution behavior.

## Commit Policy

Before commit:

- classify all R108-looking untracked files;
- stage only approved integration files;
- verify staged diff contains no unrelated thread work;
- run `git diff --cached --check`;
- record validation evidence.

Commit message suggestion for the later R109 integration round:

```text
test: integrate official pal index backfills
```

Use a different message if the integration owner narrows or changes the scope.

## No Remote Action Policy

Normal development and integration rounds must not run:

- `git push`
- `git pull`
- `git fetch`
- tag creation or modification;
- GitHub Release creation or modification;
- release/tag migration;
- remote overwrite of local work.

If a future release manager needs remote action, it must be a separate explicit release task with current evidence and user approval.
