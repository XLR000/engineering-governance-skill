# Lightweight Engineering Workflow Design

**Status:** Approved in chat on 2026-08-25.

**Goal:** Make the reusable skill help an agent deliver work in an orderly way, without turning ordinary product work into a compliance process.

## Product decision

The skill has one default loop:

1. **Understand** — state the user value, boundary, and non-goals.
2. **Define** — define the first slice's input, output, acceptance signal, and affected files or data.
3. **Implement** — complete one observable vertical slice.
4. **Verify** — run focused checks and retain direct evidence.
5. **Handoff** — state the change, residual risk, rollback or revert point, and the next action.

The loop is guidance, not a gate checklist. The agent should scale each step to the change: a small local correction can be a few lines; a new product surface warrants a PRD, design, and architecture artifacts.

## On-demand additions

| Trigger | Add before or during the relevant slice |
|---|---|
| New or changed user interface | Visual reference plus key interaction states. |
| API, data model, migration, or external integration | Interface/data-flow decision, failure behavior, and retry or rollback considerations. |
| Secret, real user data, identity/permission change, provider cost, publication, or deletion | Exact authority, security boundary, and recovery plan; obtain separate approval for irreversible external action. |
| Reproducible defect | Record the smallest failing case, test a cause, repair it, and add a regression check. |

## Context packaging

`context-pack.md` becomes an optional, one-page task card. Use it when work spans conversations, has handoffs, or has enough moving parts that the next agent would otherwise need to reconstruct intent. It records only: outcome, boundary, I/O/acceptance, affected area, evidence, risk, and next action. It never contains secrets or raw production data.

The package will not ship a validator, configuration schema, risk-class model, mandatory authorization ledger, or compulsory independent-AI review. A consuming project may add stricter project-local rules when its risk and operating environment require them; those local rules override this generic skill.

## Non-negotiable universal boundaries

- Do not put secrets in source, prompts, logs, or task cards.
- Validate untrusted input where the changed system accepts it.
- Do not perform a destructive, paid, public, hosted, or otherwise irreversible external action without explicit scope-specific approval.
- Describe verification truthfully: a planned check is not a completed check, and a synthetic fixture is not production evidence.

## Package shape after the change

```text
skills/governing-engineering-delivery/
├── SKILL.md
├── agents/openai.yaml
├── assets/context-pack.md
└── references/project-adapter.md
```

The existing `risk-adaptive-governance-design.md` remains an unimplemented historical draft; it is not the design implemented by this change.

## Acceptance checks

1. The entrypoint describes the five-step loop and gives clear, narrow triggers for extra depth.
2. A small local feature request can follow the skill without producing a PRD, risk class, validator configuration, or 12-section form.
3. A risky external-action request still directs the agent to obtain exact approval and plan the relevant security/recovery work.
4. The optional task card is usable in one screen and excludes any mandatory authorization ledger or placeholder-heavy security matrix.
5. Package metadata, README, and CI match the reduced package layout and pass their checks.
