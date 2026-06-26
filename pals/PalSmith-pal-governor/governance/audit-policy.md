# Audit Policy

Every controlled write should leave evidence from the current Agent Runtime.

Evidence includes:

- task package
- confirmation record
- affected paths
- backup or snapshot plan
- generated report or manifest
- JSON parse result for modified JSON files
- explicit statement that imported scripts were not executed

PalSmith reviews and summarizes this evidence. PalSmith does not perform the write itself.
