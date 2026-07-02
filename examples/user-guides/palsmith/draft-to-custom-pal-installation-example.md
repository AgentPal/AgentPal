# Draft To User Custom Pal Installation Example

This is a no-code PalSmith example. It does not actually install a Pal and does not create an official Pal.

Example draft:

```text
evals/palbench/v0.5/palsmith/draft-pal-packs/FirstPrinciplesProductReviewer/
```

The example draft is a test artifact. It is useful for showing the flow from reviewed draft Pal Pack to user custom Pal, but it remains non-official.

## What The User Can Say

```text
/pal PalSmith 请把 FirstPrinciplesProductReviewer 草稿 Pal Pack 安装为我的用户自定义 Pal。

草稿路径：
evals/palbench/v0.5/palsmith/draft-pal-packs/FirstPrinciplesProductReviewer/

先输出安装计划。不要直接写文件，不要写 official/pals，不要修改 central contacts，不要启用 discovery。
```

## How PalSmith Should Check It

PalSmith should read:

- `README.md`
- `PAL.md`
- `SKILL.md`
- `pal.json`
- relevant `identity/`, `knowledge/`, `workflows/`, `skills/`, `runtime/`, `contacts/`, `evals/`, and `marketplace/` files
- R174 / R175 / R177 evidence if available

PalSmith should report:

- draft exists or missing;
- `pal.json` parse result;
- quality evidence found or missing;
- usage regression evidence found or missing;
- official boundary;
- contacts boundary;
- Marketplace boundary;
- runtime boundary;
- user confirmation needed.

## Suggested Target Directory

If no user-specific rule is already present, PalSmith may propose:

```text
workspace/resources/user-pals/FirstPrinciplesProductReviewer/
```

This is a proposed user custom Pal path, not an official Pal path.

## Files To Copy

Copy the Pal Pack assets needed for use:

- `README.md`
- `PAL.md`
- `SKILL.md`
- `pal.json`
- `identity/`
- `knowledge/`
- `workflows/`
- `skills/`
- `runtime/`
- `memory/`
- `contacts/`
- `evals/`
- `marketplace/`

Do not copy:

- R174 / R175 / R177 eval reports as if they were Pal runtime assets;
- private memory;
- private reports;
- local state;
- credentials;
- temporary files;
- external reference repositories;
- generated cache files.

## `pal.json` Changes

For the copied user custom package, propose:

```json
{
  "status": "user_custom_pal",
  "official": false,
  "draft": false,
  "source_type": "palsmith_created",
  "visibility": "private_by_default",
  "contact_discovery": "disabled_by_default",
  "marketplace_listing": "none"
}
```

If a field is not supported by the current schema, record it in `INSTALL_REPORT.md` instead of forcing the JSON.

## Files Not Modified

The install plan must state that it will not modify:

- `official/pals/`
- `workspace/organization/contacts/`
- official roster files
- central aliases
- Git remote state

## Install Report

After explicit user confirmation and Runtime execution, the target directory may contain:

```text
INSTALL_REPORT.md
```

The report should include:

- source draft path;
- files copied;
- files excluded;
- `pal.json` changes;
- checks run;
- user confirmation summary;
- rollback instructions;
- `not-run` items.

## How To Use After Install

The user can ask:

```text
/pal PalSmith 请读取我的用户自定义 Pal：
workspace/resources/user-pals/FirstPrinciplesProductReviewer/

让它以 consult-only 方式帮我审查这个功能设想。
```

Or:

```text
Mira，请在这个任务中考虑我的用户自定义 Pal：
workspace/resources/user-pals/FirstPrinciplesProductReviewer/

它不是 official Pal，也没有进入 central contacts。
```

## How To Undo

Rollback should be local and reversible:

1. Remove or archive `workspace/resources/user-pals/FirstPrinciplesProductReviewer/`.
2. Remove its entry from a user custom local index if one was created.
3. Keep the original draft evidence unchanged.
4. Do not edit official Pal files or central contacts.

## Why This Is Not An Official Pal

The installed result remains user custom:

- `official` remains `false`;
- central contacts remain unchanged;
- discovery is disabled by default;
- Marketplace listing is none;
- official promotion requires a separate governance task.
