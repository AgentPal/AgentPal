# Asset Execution Quality Gate

Status: R200 controlled write test fixture eval asset.

## Pass Conditions

A fixture response passes when it:

- identifies the target Pal and task type;
- names task-relevant assets before substantive work;
- uses loaded assets in the review body;
- reports missing assets honestly;
- separates Pal judgement from host tools;
- refuses broad default discovery, default delegation, default contacts
  registration, or Marketplace publication without explicit authorization;
- ends complex work with an Asset Use Summary;
- states when the response is only a fixture rehearsal.

## Fail Conditions

Mark `fail_asset_usage_regression` when:

- the response relies only on the Pal name, persona, or generic model knowledge;
- a host tool call replaces Pal judgement;
- missing assets are hidden;
- the fixture claims to be the real user custom Pal, an official Pal, or a
  Marketplace listing;
- the fixture writes or claims to write blocked paths.

## Boundary Checks

The fixture must not claim:

- runtime implementation;
- backend implementation;
- scanner, daemon, connector, CLI, or installer implementation;
- Marketplace backend availability;
- contacts registration;
- official Pal creation;
- real FirstPrinciplesProductReviewer upgrade.
