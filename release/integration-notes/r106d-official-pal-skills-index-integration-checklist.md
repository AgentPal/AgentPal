# R106-D Official Pal Skills Index Integration Checklist

Date: 2026-06-28

## Purpose

This checklist is for the next R107 integration round that combines R106-A, R106-B, and R106-C outputs.

R106-D cannot assume the final contents of the parallel threads. Treat all expected paths below as integration targets to verify against the final worktree, not as evidence that files already exist.

## Expected A Files

Record the final R106-A owner, selected paths, and decisions before integration.

Minimum expected shape:

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R106-A boundary note or gate | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| PalSmith memory README outcome | `official/pals/PalSmith-pal-governor/memory/README.md` or documented no-write decision | pending |
| PalSmith research README outcome | `official/pals/PalSmith-pal-governor/research/README.md` or documented no-write decision | pending |
| R106-A validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R106-A integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R106-A internal report | `private completion report outside the public repository` | pending |

Do not infer PalSmith policy approval from directory presence alone.

## Expected B Files

Record the final R106-B owner, selected Pals, and changed files before integration.

Minimum expected shape:

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R106-B boundary note or gate | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| Atlas skills index outcome | `official/pals/Atlas-developer/skills/index.md` or approved equivalent / documented no-write decision | pending |
| Quinn skills index outcome | `official/pals/Quinn-quality/skills/index.md` or approved equivalent / documented no-write decision | pending |
| Morgan skills index outcome | `official/pals/Morgan-document/skills/index.md` or approved equivalent / documented no-write decision | pending |
| R106-B validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R106-B integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R106-B internal report | `private completion report outside the public repository` | pending |

Verify each index references Agent / Runtime Skills only as execution candidates, not copied Pal Skills.

## Expected C Files

Record the final R106-C owner, selected Pals, and changed files before integration.

Minimum expected shape:

| Item | Expected Evidence | Result |
| --- | --- | --- |
| R106-C boundary note or gate | public Markdown under `evals/palbench/pal-asset/` or `release/integration-notes/` | pending |
| Nova skills index outcome | `official/pals/Nova-product/skills/index.md` or approved equivalent / documented no-write decision | pending |
| Vega skills index outcome | `official/pals/Vega-research/skills/index.md` or approved equivalent / documented no-write decision | pending |
| Harper skills index outcome | `official/pals/Harper-writing/skills/index.md` or approved equivalent / documented no-write decision | pending |
| Rhea skills index outcome | `official/pals/Rhea-system/skills/index.md` or approved equivalent / documented no-write decision | pending |
| R106-C validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R106-C integration note or summary | public Markdown under `release/integration-notes/` | pending |
| R106-C internal report | `private completion report outside the public repository` | pending |

Verify R106-C did not overlap with R106-B selected paths.

## Expected Validation Files

The integration round should expect one validation record per parallel thread plus the R106-D validation file:

| Validation | Required Handling |
| --- | --- |
| R106-A validation | must exist or issue |
| R106-B validation | must exist or issue |
| R106-C validation | must exist or issue |
| `release/fresh-clone-checks/r106d-local-official-pal-skills-index-gate-validation.md` | must exist |
| R107 integration validation | create during the integration round |

Each validation must state `not-run` items explicitly.

## Expected Internal Reports

Internal reports belong under:

```text
private completion report outside the public repository
```

Expected handling:

- R106-A internal report: must exist or issue.
- R106-B internal report: must exist or issue.
- R106-C internal report: must exist or issue.
- R106-D internal report: must exist.
- R107 integration report: create during the integration round.

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

Integration fixes may only repair issues inside the R107 integration round's approved paths.

Allowed integration fixes, if explicitly in scope:

- typo or formatting repair in R106 integration notes;
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
- copying Agent Skill files into Pal `skills/`;
- copying report bodies into memory;
- promoting raw research directly to knowledge;
- creating code, scanner, validator, installer, connector, daemon, database, marketplace, or auto-execution behavior.

## Commit Policy

Before commit:

- classify all R106-looking untracked files;
- stage only approved integration files;
- verify staged diff contains no unrelated thread work;
- run `git diff --cached --check`;
- record validation evidence.

Commit message suggestion for the later R107 integration round:

```text
test: integrate official pal skills index backfill
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
