# Mira Context Packet Eval

## Purpose

Check whether Mira creates bounded and useful Context Packets.

## Scenario

User provides a large source prompt and asks for a bounded project asset update.

## Required inputs

- User prompt or attachment.
- Allowed write paths.
- Forbidden actions.
- Relevant Pal owner assets.
- Verification needs.

## Pass criteria

- Objective, owner, inputs, allowed files, forbidden files, risks, acceptance criteria, and report format are present.
- Read files and index-known files are separated.
- Active external project root and AgentPal workspace root are not confused.
- Sensitive or broad context sharing has approval.

## Fail criteria

- Whole repository is loaded without need.
- Context includes private material without approval.
- Acceptance criteria are missing.
- Runtime decides owner after receiving the packet.

## Evidence required

Context Packet text, file list, exclusions, and final report.

## No-code boundary

This eval is a written review guide. It does not create scanners or validators.
