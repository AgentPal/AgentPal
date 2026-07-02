# 09 Submit Test Results

## Required Return Package

Return these materials to Codex for R247 intake:

```text
1. Filled v06-user-test-result-form.md
2. Raw output for each feature tested
3. Screenshots, if the host supports them
4. Host runtime / project mode / OS / project path
5. Blocker descriptions, if any
6. Notes about project-bound or slash-command limitations
```

## Do Not Send Only A Summary

Do not send only:

```text
It passed.
```

The next intake needs raw evidence.

## If Screenshots Are Unavailable

Record:

```text
screenshots_status: screenshots_not_available
raw_output_saved: true
```

Do not mark screenshots as pass if no screenshot exists.

## If The Run Is Projectless

Record:

```text
project_mode=filesystem_or_projectless
strict_project_bound_pass=false
```

## Suggested Folder Name

```text
agentpal-v06-user-test-results-<tester>-<date>
```
