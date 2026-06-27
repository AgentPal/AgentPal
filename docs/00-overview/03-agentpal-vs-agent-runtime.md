# AgentPal Vs Agent Runtime

## Purpose

This document explains the boundary between AgentPal and the runtime that uses AgentPal.

## AgentPal Provides

- Pal identity and role boundaries.
- Knowledge, skills, runbooks, workflows, and output contracts.
- Context-loading rules.
- Contacts and registry for Pal discovery.
- Public/private memory and state boundaries.
- Handoff, review, verification, and learning rules.

## The Runtime Provides

- Model execution.
- File reads and writes.
- Shell commands.
- Tool calls.
- Browser, search, or MCP access when available.
- Publishing, uploads, deletion, installation, or system modification when authorized.
- Evidence that an action happened.

## Current Status

AgentPal v0.3.0-rc.1 uses Simple Pal Mode for task handling and provides Deep Conductor as no-code protocols, templates, examples, evals, task packages, and replay reports. It does not provide an execution layer or active multi-agent runtime.

## Related

- [What is AgentPal?](00-what-is-agentpal.md)
- [Current status](01-current-status.md)
- [Simple Pal Mode](../01-concepts/05-simple-pal-mode.md)
