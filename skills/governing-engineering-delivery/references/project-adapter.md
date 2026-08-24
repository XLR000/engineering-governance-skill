# Project Adapter

Use this reference when adopting governance in a repository that lacks a complete process.

## Inspect before writing

Find, without changing files:

- applicable instruction files and existing conventions;
- product/requirements/design/architecture/plan/evidence artifacts;
- build, lint, typecheck, test, browser and release commands;
- language, runtime, data stores, integrations and deployment targets;
- Git branch/commit/dirty state and ownership of existing changes;
- secret sources, network policy, local/test/staging/production boundaries;
- stable ID vocabulary and lifecycle/status vocabulary.

Expose contradictions. Existing repository conventions override generic defaults.

## Adopt with a thin local layer

After document-write approval, create only missing project artifacts. Recommended local structure:

```text
AGENTS.md                    project constraints and authorization boundaries
product/brief.md             validated problem and V1 scope
product/spec.md              executable requirements and acceptance
product/design.md            visual and interaction contract
product/architecture.md      current components, data and trust boundaries
product/plan.md              dependency-ordered delivery and verification
product/traceability.md      requirements to implementation/evidence
product/iterations/          task context packs and handoffs
project-governance.json      validator adapter (path is project-defined)
```

Do not create duplicate sources when equivalent files already exist. Map existing names in the adapter instead.

## Configure validation

Copy `assets/governance.config.json` and set:

- `idPrefixes`: stable identifiers used by this project;
- `knownIdFiles`: repository-relative canonical files containing those identifiers;
- `requiredChecks`: exact configured commands;
- `independentReviewRiskClasses`: risk classes requiring a reviewer independent of the implementing agent.

The validator reads only the context, configuration and named ID files. It does not inspect secrets or execute project checks.

## Keep local

Never move these into the reusable skill:

- product/domain truth rules;
- current requirements, state, denominators or release blockers;
- provider names, credentials, accounts or live targets;
- database identities, deployment receipts or raw evidence;
- project-specific coding commands and technology choices.

## Adoption gate

Before calling adoption complete, prove that a new C2 context can identify project requirements, commands, authorization, workspace baseline, sandbox controls, review gates and direct verification without depending on conversation history.
