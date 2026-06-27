# GitHub Release Steps

Use this page as a public-safe maintainer checklist for creating the v0.1.0-rc.1 GitHub Release.

## Before Creating The Release

- Review `RELEASE_CHECKLIST.md`.
- Review `RELEASE_MANIFEST.md`.
- Review `release/v0.1.0-rc.1/public-safe-audit.md`.
- Confirm `GITHUB_RELEASE_DRAFT.md` matches the release scope and limitations.
- Confirm no private memory, private project state, internal development notes, secrets, credentials, customer data, local absolute paths, or unauthorized logs are included.
- Confirm future design materials are not described as active v0.1.0-rc.1 behavior.
- Confirm the final release commit exists.
- Confirm tag `v0.1.0-rc.1` points to the final intended release commit.
- Confirm whether a Git remote already exists. If not, create the GitHub repository before adding a remote.

## Push The Release

1. Create an empty GitHub repository if the remote repository does not exist yet.
2. Add the intended remote, for example `origin`.
3. Push the final release commit to the intended branch.
4. Push tag `v0.1.0-rc.1`.

Do not say the release is published until both the commit and tag are present on the intended remote.

## Create The GitHub Release

1. Open the repository's GitHub Releases page.
2. Choose `Draft a new release`.
3. Select tag `v0.1.0-rc.1`.
4. Use `AgentPal v0.1.0-rc.1` as the release title.
5. Paste and review the content from `GITHUB_RELEASE_DRAFT.md`.
6. Keep the release marked as a release candidate or pre-release if that matches the repository's publication policy.
7. Publish only after the tag, commit, and release body are reviewed.

## After Publishing

- Confirm the release page points to the intended tag.
- Confirm source archives do not include ignored local runtime files.
- Confirm the public README and release notes still describe v0.1.0-rc.1 as a release candidate.
- Record any publication follow-up in release maintenance notes, not in private memory or internal development logs.
