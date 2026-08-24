---
name: governing-engineering-delivery
description: Use when starting or materially changing a software product, especially when requirements are vague, multiple disciplines or external systems are involved, or delivery needs durable governance across projects.
---

# Governing Engineering Delivery

## Overview

Turn product work into a bounded, reviewable and self-proving delivery chain. Keep reusable process in this skill and project facts, authorities and evidence in the repository.

Project instructions always win. Never replace or weaken `AGENTS.md`, repository conventions, product truth rules or explicit user boundaries.

## Start

1. Inspect project instructions, source-of-truth artifacts, repository commands, Git state, runtime/data boundaries and existing failures.
2. If governance is absent, use [project-adapter.md](references/project-adapter.md) and copy only the needed files from `assets/` after write approval.
3. Classify the task before mutation:

| Class | Scope | Minimum control |
|---|---|---|
| C0 | Read-only analysis/review | Evidence boundary and findings |
| C1 | Documentation only | Source/contradiction review and document validation |
| C2 | Bounded implementation | Context pack, focused regression, review |
| C3 | Product/API/data operation | Full preparation chain, security evidence, independent review |
| C4 | Auth, secrets, external cost, hosted/public/destructive boundary | C3 plus sandbox proof, recovery point and one-shot authority |

Raise the class when hidden complexity appears. Do not downgrade it to avoid a gate.

## Enforce the 13 controls

Complete preparation before implementation:

1. Convert vague demand into user, problem evidence, outcome, scope, non-goals, success and kill criteria.
2. Write an executable PRD with actor, trigger, inputs, validation, authority, processing, persistence, outputs, failures, retries and acceptance criteria.
3. Establish a reviewable visual/UX baseline: wireframe/design, tokens, responsive behavior, accessibility and critical states.
4. Select frontend/backend/data/runtime technology from constraints and record a feasible implementation design.
5. Describe components, data flows, integrations, trust boundaries, observability and recovery in the system architecture.
6. Lock repository-specific coding, testing, error, logging, dependency and data conventions.
7. Record branch/commit/dirty state, versioning, migration, commit/release rules and rollback.
8. Package the task context as a manifest, not a conversation dump.

Control execution:

9. Deliver one observable vertical slice at a time; a failed gate blocks expansion.
10. Define proactive checkpoints and name human, primary AI and independent AI responsibilities proportionate to risk.
11. Prove sandbox/environment isolation, allowed paths, network policy, credential class and data target before C2–C4 mutation. If isolation cannot be proved, stop as `BLOCKED`.
12. Exercise applicable Web security controls with reproducible evidence: auth, authorization, CSRF/origin, secret redaction, input bounds, injection, rendering, SSRF/redirect, replay, rate/body/cost limits and dependency integrity.
13. Debug by recording, reproducing, preserving, localizing and falsifying before repair; then regress, verify and trace.

Read [governance-contract.md](references/governance-contract.md) before creating or reviewing preparation artifacts, a security plan, an external action or a completion claim.

## Package context

For C2–C4 work, copy [context-pack.md](assets/context-pack.md) into the project's iteration/evidence area. Fill it from current artifacts and direct inspection. Include outcome/non-goals, stable IDs, I/O/UX/architecture, exact authority, Git/runtime/data baseline, slices/review gates, sandbox/security/recovery, verification/direct evidence, final delta, residual risk and next authority.

Do not include secrets, raw production exports, unrelated conversation history or claims unsupported by current evidence.

If the project adopts deterministic validation, copy [governance.config.json](assets/governance.config.json), adapt it to local facts, and run:

```bash
python3 <skill-path>/scripts/validate_context_pack.py <context.md> --config <project-governance.json>
```

A validator PASS proves structure only. It never grants implementation, provider, commit, deployment, publication or destructive authority.

## Authorization rules

Separate read, document write, code/data write, verification, public read, provider/cost, Git history, hosted state/secrets, publication/message and destructive actions. Record exact scope, source, timestamp, validity and receipt.

Treat external cost, hosted mutation, publication, messages and destructive actions as one-shot. A plan is not execution; a build is not deployment; approval of one item is not approval of its sibling or retry.

## Stop conditions

Stop and report the exact missing gate when:

- a decision-changing requirement or authority is ambiguous;
- a C2–C4 context pack or sandbox proof is missing;
- live identity, data, model, price, revision or target drifted;
- dirty work overlaps and ownership cannot be recovered;
- a security negative path, backup, rollback or required reviewer is missing;
- an external outcome is ambiguous—preserve evidence and never auto-retry;
- fresh direct evidence does not support the requested completion state.

## Common rationalizations

| Rationalization | Required response |
|---|---|
| “Start coding; design later.” | Complete the decision-changing preparation for the first slice. |
| “It is just one call and price shows zero.” | Require exact one-shot authority; billing and side effects remain external facts. |
| “The sandbox probably covers it.” | Record actual paths, network, credentials and data target or stop. |
| “Tests pass, so deploy.” | Prepare release evidence; deployment remains separately authorized. |
| “The AI reviewed its own summary.” | This is not independent review; inspect source and evidence directly. |
| “Copy the whole prior project.” | Extract generic process; keep domain rules and live evidence local. |

## Completion

Claim only the exact verified scope. Name changed files/data/external effects, fresh checks, direct evidence, reviewers, unresolved risk, rollback point and next required authority. Keep partial work `implemented`/`PARTIAL`/`blocked` according to project vocabulary.
