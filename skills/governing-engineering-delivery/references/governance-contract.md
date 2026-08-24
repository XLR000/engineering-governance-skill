# Portable Engineering Governance Contract

## Contents

1. Preparation gates
2. Context contract
3. Execution control
4. Review model
5. Sandbox and Web security
6. Coding and version control
7. Structured debugging
8. Verification and release

## 1. Preparation gates

### Requirement review

Resolve the user, concrete situation, observed problem, current workaround, desired observable outcome, V1 boundary, explicit non-goals, success signal, kill criterion, assumptions and decision-changing unknowns. A solution label alone does not authorize implementation.

### Executable PRD and I/O

For every material operation define:

- actor, permission, entry route/job/event and trigger;
- each input's source, shape, validation, limits and authority;
- authoritative processing and business invariants;
- persistence, immutability, idempotency, concurrency and revision behavior;
- outputs and downstream routes/actions;
- empty, loading, partial, error, denied, stale, interrupted and retry states;
- archive/delete/undo behavior;
- acceptance criteria and the highest-cost counterexample.

### Visual and UX baseline

Use a reviewable artifact appropriate to the surface: Figma, wireframe, screen specification, design tokens, screenshot baseline or CLI/desktop interaction contract. Define information hierarchy, canonical routes, typed actions, desktop/narrow behavior, critical states, keyboard/focus/semantics, contrast/zoom and destructive recovery. A happy-path screenshot is insufficient.

### Feasible technical design

Select stack and implementation from product, team, runtime, data, security, cost and operability constraints. Record alternatives only when they affect a durable decision. Do not choose technology before resolving constraints that could reverse the choice.

### Architecture and integration

Describe components and ownership, request/data flows, API contracts, schemas/migrations, external services, timeouts/retries/idempotency/cost, authentication/authorization, trust boundaries, observability, failure modes, backup and recovery. Update the project's architecture contract when these materially change.

### Coding and version standards

Lock language/module boundaries, validation, persistence, error/logging, test and dependency rules in the project. Record branch, commit, dirty state, version scheme, migration order, change/commit/release rules and rollback. Never absorb unrelated work.

## 2. Context contract

A context pack is the executable manifest for one outcome. It links facts rather than duplicating the repository or conversation.

Required content:

- objective, non-goals, success and stop conditions;
- requirement, acceptance, plan and decision identities;
- I/O, UX, architecture, integrations and persistence;
- authorization ledger with exact categories;
- Git/runtime/data baseline and dirty-work ownership;
- smallest vertical slices and gates;
- sandbox, security, privacy, backup and rollback;
- regression, commands, direct evidence and reviewers;
- execution log, actual delta, residual risk and next authority.

Create/update it before C2–C4 mutation and keep it current at evidence checkpoints. Put large evidence in linked project artifacts. Never put secret values, production exports or unrelated conversation history in it.

## 3. Execution control

Deliver one observable vertical slice connecting action, service behavior, persistence and feedback. Establish a failing/missing acceptance signal, make the smallest coherent change, run focused checks, inspect exact diff/data delta, repair findings and then expand.

Separate planning, document writes, code/local-data writes, verification, external reads, provider/cost actions, Git history/remotes, hosted migration/deployment/secrets, publication/messages and destructive actions.

External and irreversible actions are one-shot by default. Record consumption and receipt immediately. Ambiguous outcomes stop without automatic retry.

## 4. Review model

Define proactive gates rather than waiting for final review:

| Trigger | Required gate |
|---|---|
| Ambiguous outcome or scope increase | Human product decision |
| Changed visual workflow | Design plus direct UI review |
| API, persistence or migration | Technical and recovery review |
| Auth, secrets, user URLs or external cost | Security review with negative-path evidence |
| C3/C4 implementation | Independent AI or human source/evidence review |
| Human quality judgment | Human reviewer sees raw evidence; machine score stays separate |
| Release/deployment/publication | Exact-target user approval and post-action observation |

The implementing AI may perform primary review. Independent review requires a different reviewer to inspect source and evidence directly; rereading the implementer's summary is insufficient. Human judgment is mandatory for product decisions, subjective quality and exact external authority.

## 5. Sandbox and Web security

Before C2–C4 mutation record the resolved project root, allowed write paths, prohibited operations, network allowlist, credential class, data environment, recovery point and cleanup policy. If any boundary cannot be proved, stop as `BLOCKED`. A sandbox limits capability; it never grants authority.

For changed Web operations exercise applicable controls through real routes:

- fail-closed authentication and server authorization/object identity;
- CSRF/same-origin protection for mutation;
- input type, length, enum/range, revision and body-size limits;
- parameterized queries and injection-shaped negative cases;
- safe rendering/output encoding and non-leaking errors;
- secret/configuration redaction without printing matched values;
- SSRF defenses across parsing, DNS, redirects and connection time;
- safe internal redirects;
- session expiry/revocation/cookie/throttling controls;
- rate, timeout, cost, replay, lease and idempotency controls;
- dependency and build integrity.

Every applicable control needs a named command/direct probe, expected blocking assertion, result and reviewer. A prose checklist is not PASS.

## 6. Coding and version control

Follow local conventions. Where missing, establish strict typing or equivalent checks, clear UI/API/domain/persistence boundaries, server validation, additive/auditable data changes, atomic invariants, stable errors, redacted logs, regression-first tests with neighbor invariants, and synchronized release identity.

Commit, push, tag, PR, deploy and publish remain separately authorized even when version rules are defined.

## 7. Structured debugging

Diagnosis and repair are separate authorities:

1. Record environment, version, actor, time, expected/actual result, severity and IDs.
2. Reproduce the smallest deterministic case; label intermittency.
3. Preserve redacted logs, metadata and data snapshots/counts.
4. Localize UI, API, domain, persistence, integration, runtime or evidence layer.
5. Test a falsifiable cause before editing.
6. Obtain repair authority and make the smallest root-cause change.
7. Add a regression that fails on old behavior.
8. Verify focused/full behavior, persistence and UI path as applicable.
9. Trace result to requirement, plan, evidence and residual risk.

Do not use broad refactors, upgrades, destructive cleanup, secret exposure or disabled security as diagnostic probes.

## 8. Verification and release

Completion requires fresh configured checks, success/highest-risk negative paths, exact persistence/external delta, unchanged neighbors, direct UI/runtime evidence where material, traceability, configured independent review, residual risk, rollback and next authority.

Fixtures and model self-scores prove only their stated software behavior. Never present synthetic evidence as an observed product or business result.

Release-ready means an artifact, migration order, configuration inventory, limitations and rollback are prepared. It does not authorize deployment. Mark released only after exact-target approval and direct post-release evidence.
