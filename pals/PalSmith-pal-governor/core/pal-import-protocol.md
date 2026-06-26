# Pal Import Protocol

All imports are untrusted by default.

PalSmith does not download, extract, scan, install, or execute imported resources. PalSmith prepares a Pal Import Staging Task Package for the current Agent Runtime.

## Task Package Must Include

- source type and source location
- staging target
- allowed read paths
- allowed write paths
- forbidden paths
- files that must not be executed
- resource classification checklist
- risk report requirements
- user confirmation questions

## Runtime Must Not

- execute imported scripts
- directly install into formal `pals/`
- automatically update `contacts/`
- automatically update `registry/`
- import `memory/user/` or `memory/project/` into a public Pal Pack

After staging review, PalSmith may prepare a separate Pal Install Task Package.
