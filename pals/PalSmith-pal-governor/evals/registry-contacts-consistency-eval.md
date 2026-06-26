# Registry Contacts Consistency Eval

This is a Markdown evaluation checklist, not a script.

## Checks

- `registry/pal.index.json` PalSmith id equals `pals/PalSmith-pal-governor/pal.json` id.
- `contacts/pals.json` PalSmith id equals registry id.
- Registry path and contacts path both equal `pals/PalSmith-pal-governor`.
- Direct call is `/pal PalSmith` in `pal.json`, registry, and contacts.
- PalSmith role is consistently `pal-asset-governor` or official no-code Pal asset governance wording.
- Ordinary Skills, tools, models, plugins, raw repositories, Knowledge Packs, and Persona Packs are not contacts.

## Evidence To Record

- registry entry
- contacts entry
- pal.json entry
- any mismatch or not-run check
