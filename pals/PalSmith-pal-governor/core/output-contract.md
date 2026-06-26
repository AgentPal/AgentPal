# PalSmith Output Contract

PalSmith outputs must separate Pal judgement from runtime evidence.

## Required Fields

- owner judgement
- user goal
- target Pal, team, source, or path
- task package type
- trust boundary
- allowed read paths
- allowed write paths
- forbidden paths
- required confirmation questions
- expected runtime evidence
- what PalSmith will review after execution

Use `not-run` for checks that were not executed. Do not claim file operations happened unless the current Agent Runtime provides evidence.
