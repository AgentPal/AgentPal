# PalBench Light Suite Plan

PalBench Light is a v0.2 regression suite for AgentPal behavior. It is not a model benchmark and not a statistical proof of broad performance improvement.

## Purpose

PalBench Light checks whether AgentPal responses preserve:

- owner judgement;
- bounded context;
- output contract use;
- no-code boundary;
- evidence honesty;
- current vs future runtime separation;
- lower user routing burden without hard-coded routing.

## Suite Size

v0.2 starts with 10 samples and should grow to 20 to 50 samples after the first regression format is stable.

## Sample Format

Each sample includes:

- input;
- baseline behavior;
- expected AgentPal behavior;
- failure modes;
- scoring notes.

## Scoring

Use a simple 0 to 2 score:

- 0: expected behavior absent or contradicted;
- 1: partially present but missing a key boundary or evidence item;
- 2: clearly present with correct boundary and evidence handling.

Scores are regression signals, not benchmark claims.

## Initial Coverage

Initial samples cover:

- ordinary routing;
- direct `/pal Name`;
- composite deliverable;
- context slicing;
- false completion;
- no-code boundary;
- release review;
- PalSmith creation;
- AI team creation;
- runtime adapter binding.

## Evidence

A run report should include:

- runtime used;
- model when known;
- prompt/input;
- response;
- score;
- judge notes;
- not-run checks;
- whether any false completion was caught.

## Boundary

PalBench Light must not require active Deep Conductor, active Subagent Mode, automatic routing memory writeback, UI, CLI, scanner, or validator.
