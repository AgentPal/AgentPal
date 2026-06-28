# Org Pack / FDE / Asset Boundary Overview

This overview connects the R119 Org Pack, FDE Pack, and Asset Boundary work for
AgentPal v0.5.

## Purpose

Org Pack, FDE Pack, and Asset Boundary assets are no-code organization assets.
They help AgentPal describe reusable AI organization structures, expert delivery
methods, and safe reuse boundaries without turning AgentPal into a runtime,
installer, connector, marketplace, scanner, validator, daemon, database, or
keyword router.

## Org Pack

An Org Pack is an AI organization asset package. It may describe roles,
recommended Pal perspectives, workflows, runbooks, governance, verification,
Capability Inventory references, and public-safe examples.

Org Pack recommendations are AI judgement inputs only. They do not modify the
central Pal roster, assign work by keyword, or replace case-by-case owner
judgement.

## FDE Pack

An FDE Pack is an expert delivery asset package. It captures public-safe expert
delivery knowledge such as delivery scope, reusable assets, update policy,
customer-private boundary, and verification checklist.

An FDE Pack may be referenced by an Org Pack, but it is not a program, API
client, connector, marketplace item, automatic executor, scanner, validator, or
credential store.

## Asset Boundary

The Asset Boundary standards separate reusable assets from customer-private
assets.

Reusable assets must be safe to publish, safe to copy into another AgentPal
Workspace, and free of real credentials, tokens, customer data, private project
context, private meeting content, or reversible identifying clues.

Customer-private assets belong in approved private records or evidence stores,
not in public reusable Org Pack, FDE Pack, Pal Asset, template, or example
directories.

## Relationship To Pal Asset

Pal Asset is the Pal layer. Org Packs and FDE Packs may reference Pal
perspectives, Pal assets, workflows, runbooks, or Capability Inventory records
as AI judgement inputs.

They must not copy official Pal bodies, Pal directories, Pal skills, Pal memory,
Pal manifests, or central roster entries into themselves or into external
project `.agentpal/` directories by default.

## External Project Binding

External projects remain thin-bound. Default binding files may point back to the
AgentPal Workspace, but external projects must not receive Org Pack, FDE Pack,
Pal, workflow, memory, report, capability inventory, business system, or manifest
directories by default.

## PalSmith Role

PalSmith may create, audit, review, maintain, and govern these no-code assets.
PalSmith does not become an automatic execution engine, connector, installer,
marketplace program, scanner, validator, or deterministic router.

## Current v0.5 Direction

R118 paused the full official Pal metadata / manifest rollout after the PalSmith
pilot. R119 and R120 return the v0.5 mainline to Org Pack, FDE Pack, and Asset
Boundary integration.

The next recommended step is a public-safe combined Org Pack + FDE Pack example
with PalSmith audit notes, customer-private boundary evidence, and thin-binding
relationship notes.
