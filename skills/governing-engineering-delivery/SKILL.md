---
name: governing-engineering-delivery
description: Use when starting or materially changing a software product that needs a clear delivery path across requirements, implementation, verification, or handoff.
---

# Engineering Delivery Workflow

Use this skill to make product work understandable, testable, and easy to continue. Project instructions and explicit user boundaries always win.

## Default loop

Scale these five steps to the change. A small local correction may need a few lines; a new product surface may need durable product documents.

1. **Understand** — state the user value, boundary, and non-goals. Resolve only the unknowns that would change the first slice.
2. **Define** — state the first slice's input, output, acceptance signal, and affected files, data, or service.
3. **Implement** — complete one observable vertical slice before expanding scope.
4. **Verify** — run focused checks and retain direct evidence. A planned check is not a completed check.
5. **Handoff** — state the actual change, residual risk, rollback or revert point, and next action.

## Add depth only when triggered

| If the work changes… | Add… |
|---|---|
| A user interface | A visual reference and the important interaction states. |
| An API, data model, migration, or external integration | The interface/data flow, failure behavior, and retry or rollback considerations. |
| A secret, real user data, identity/permission boundary, provider cost, publication, or deletion | Exact authority, the relevant security boundary, and recovery planning. Get separate approval immediately before an irreversible external action. |
| A reproducible defect | The smallest failing case, a falsifiable cause, a focused repair, and a regression check. |

## Optional task card

Use [context-pack.md](assets/context-pack.md) when work spans conversations, has a handoff, or has enough moving parts that intent could be lost. It is a short task card, not a mandatory form or a transcript. Do not put secrets or raw production data in it.

## Always

- Keep secrets out of source, prompts, logs, and task cards.
- Validate untrusted input where the changed system accepts it.
- Never treat a plan, build, or prior approval as permission for a destructive, paid, public, hosted, or otherwise irreversible external action.
- Report only the scope supported by fresh evidence; label fixtures and synthetic results accurately.

## Completion

Name what changed, the checks and direct evidence, remaining risk, rollback or revert point, and the next action or authority needed. Preserve project-local rules that require stronger controls.
