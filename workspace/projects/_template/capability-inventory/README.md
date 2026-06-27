# Capability Inventory

This directory is the project-level Capability Inventory template.

Use it when creating a central project record under:

```text
workspace/projects/<project-id>/capability-inventory/
```

## Relationship To Organization Records

Organization capability inventory:

```text
workspace/organization/capability-inventory/
```

Project capability inventory:

```text
workspace/projects/<project-id>/capability-inventory/
```

External project binding:

```text
<project>/.agentpal/project.json
```

Organization records describe public-safe capabilities that can apply across the AgentPal organization. Project records describe capabilities that are available, used, limited, or relevant for one bound project.

Project records may reference organization records. Project records may also override or supplement organization records for that project, such as when a project uses a restricted plugin, a customer-specific business system, or a different Runtime setup.

Project records must not modify the central Pal roster. Pal contacts remain under:

```text
workspace/organization/contacts/
```

## Boundary

The external user project should not receive a default `.agentpal/capability-inventory/` directory.

Real project records under `workspace/projects/<project-id>/` are private by default and ignored unless explicitly promoted as public-safe examples.

This is a no-code record. It does not imply automatic scanning, automatic discovery, automatic execution, automatic scoring, or keyword routing.

Do not store credentials, private tokens, API keys, session cookies, or project secrets here.
