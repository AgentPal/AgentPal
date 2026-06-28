# R119-D Org Pack / FDE Pack Integration Checklist

Date: 2026-06-28

## Purpose

This checklist is for the next R120 single-thread integration round that combines R119-A, R119-B, and R119-C outputs.

R119-D cannot assume the final contents of the parallel threads. Treat all expected paths below as integration targets to verify against the final worktree, not as evidence that files already exist.

## Expected A Files

Record the final R119-A owner, selected paths, and decisions before integration.

| Item | Expected Evidence | Result |
| --- | --- | --- |
| Org Pack practical structure standard / note | public Markdown under `standards/org-pack/`, `templates/org-pack/`, `examples/org-packs/`, `evals/palbench/org-pack/`, or `release/integration-notes/` | pending |
| Org Pack templates | present if R119-A created them; JSON templates parse | pending |
| Org Pack examples | present if R119-A created them; JSON examples parse | pending |
| R119-A validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R119-A integration note or index update note | public Markdown under `release/integration-notes/` | pending |
| R119-A internal report | `private completion report outside the public repository` | pending |

## Expected B Files

Record the final R119-B owner, selected paths, and decisions before integration.

| Item | Expected Evidence | Result |
| --- | --- | --- |
| FDE Pack standard | public Markdown under `standards/fde-pack/` or `release/integration-notes/` | pending |
| FDE Pack templates | present if R119-B created them; JSON templates parse | pending |
| FDE Pack examples | present if R119-B created them; JSON examples parse | pending |
| R119-B validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R119-B integration note or index update note | public Markdown under `release/integration-notes/` | pending |
| R119-B internal report | `private completion report outside the public repository` | pending |

FDE Pack files must remain no-code delivery assets and must not implement a connector, API client, scanner, marketplace, or execution engine.

## Expected C Files

Record the final R119-C owner, selected paths, and decisions before integration.

| Item | Expected Evidence | Result |
| --- | --- | --- |
| reusable/private asset-boundary standard or note | public Markdown under `standards/asset-boundary/`, `evals/palbench/`, or `release/integration-notes/` | pending |
| reusable asset examples | present if R119-C created them; public-safe | pending |
| private asset examples | placeholders only; no customer-private data | pending |
| R119-C validation | public Markdown under `release/fresh-clone-checks/` | pending |
| R119-C integration note or index update note | public Markdown under `release/integration-notes/` | pending |
| R119-C internal report | `private completion report outside the public repository` | pending |

R119-C must prove customer-private material does not enter reusable public packs.

## Expected Validation Files

The integration round should expect one validation record per parallel thread plus R119-D validation:

| Validation | Required Handling |
| --- | --- |
| R119-A validation | must exist or issue |
| R119-B validation | must exist or issue |
| R119-C validation | must exist or issue |
| `release/fresh-clone-checks/r119d-local-org-fde-integration-gate-validation.md` | must exist |
| R120 integration validation | create during R120 |

Each validation must state `not-run` items explicitly.

## Commands To Run

Use equivalent local checks. These are manual evidence commands, not a new validator program.

```powershell
git status --short --branch
git diff --name-only -- README.md README.zh-CN.md RESOURCE_INDEX.md agentpal.json
git diff --name-only -- workspace/organization/contacts official/pals
Get-Content workspace/organization/contacts/pals.json -Raw | ConvertFrom-Json | Out-Null
Get-ChildItem official/pals -Directory | Measure-Object
Get-ChildItem official/pals -Directory | ForEach-Object { Get-Content (Join-Path $_.FullName 'pal.json') -Raw | ConvertFrom-Json | Out-Null }
Get-ChildItem -Recurse -File -Include *.json standards templates examples evals release | ForEach-Object { Get-Content $_.FullName -Raw | ConvertFrom-Json | Out-Null }
Get-ChildItem -Recurse -Filter asset-manifest.json official/pals
rg -n '"(keyword_map|domain_map|role_map)"\s*:' standards templates examples evals release docs
rg -n "sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY" standards templates examples evals release docs
git diff --check
```

If `rg` is unavailable, use another search tool and record the substitution.

## Shared Entry Update Plan

R120 may update shared navigation files only after A/B/C are verified:

- `README.md`: add concise Org Pack / FDE Pack navigation if missing.
- `README.zh-CN.md`: mirror the public navigation in Chinese if the file exists and is in scope.
- `RESOURCE_INDEX.md`: add exact links to new standards, templates, examples, evals, and validation records.
- `agentpal.json`: update navigation metadata only if the schema supports it and the change is explicitly scoped.

Shared entry updates must remain navigation-only. They must not change runtime behavior, central roster, Pal routing, connector availability, or release status.

## Conflict Policy

If R119-A/B/C overlap:

- prefer the narrower source-of-truth file named by the owning thread;
- preserve `missing`, `not-run`, `needs-review`, and `unknown`;
- do not silently merge conflicting public/private boundary language;
- create an issue for wording that could imply marketplace, connector, scanner, keyword route, or external project thick binding;
- require human review for customer-private boundary ambiguity.

## Commit Policy

Before commit:

- classify all R119-looking untracked files;
- stage only approved R120 integration files;
- verify staged diff contains no unrelated thread work;
- run `git diff --cached --check`;
- record validation evidence.

Suggested R120 commit message:

```text
docs: integrate org fde pack foundations
```

R119-D commit message:

```text
test: add org fde integration gate
```

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
