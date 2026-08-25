# Lightweight Engineering Workflow Implementation Plan

**Goal:** Replace the heavy default governance process with an adaptive five-step delivery workflow and an optional short task card.

**Spec:** `docs/superpowers/specs/2026-08-25-lightweight-engineering-workflow-design.md`

## Implemented work

1. Replace the default workflow with Understand, Define, Implement, Verify, and Handoff.
2. Make UI, API/data, high-risk external, and debugging preparation conditional on the actual change.
3. Replace the mandatory 12-section context pack with a one-page optional task card.
4. Remove the generic risk classes, validator, configuration schema, full governance contract, and their CI enforcement.
5. Verify package layout, content hygiene, metadata, and the three delivery pressure scenarios.

## Constraints

- Preserve the skill name and normal implicit invocation policy.
- Do not change the consuming GEO repository or installed personal skill.
- Do not commit, push, tag, release, publish, or delete the historical draft.
- Retain secret protection, input validation, explicit approval for irreversible external work, and truthful evidence.
