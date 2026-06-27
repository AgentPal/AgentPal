# Git Tag And Release Process

This page records the release-process boundary for v0.1.0-rc.1.

## Observed Local Git Evidence

Before publication, the repository should show:

- local tag: `v0.1.0-rc.1`
- tagged commit: the final intended release commit
- working tree: clean

No online GitHub Release should be considered created until maintainers push the intended commit and tag, then create the release page.

If the working tree contains documentation changes after a local tag is created, maintainers should commit those final contents and retag `v0.1.0-rc.1` before publishing.

## Maintainer Process

Before publishing:

1. Confirm the working tree contains only intended public release files.
2. Run public-safe review for secrets, private state, local paths, and future-feature overclaims.
3. Confirm Markdown and JSON files required for the release are valid enough for publication.
4. Commit the final intended release contents.
5. Create or update the annotated `v0.1.0-rc.1` tag to point to the intended release commit.
6. Create the GitHub repository if it does not exist yet.
7. Add the intended `origin` remote.
8. Push the release commit to the intended branch.
9. Push tag `v0.1.0-rc.1`.
10. Create the GitHub Release from the pushed tag.
11. Paste or adapt `GITHUB_RELEASE_DRAFT.md` into the release body.
12. Confirm the release page links to the intended tag and commit.

## Do Not Overstate

Do not write that v0.1.0-rc.1 has been published online until the tag has been pushed and the GitHub Release page exists.

Do not treat a local tag as proof of a remote release.
