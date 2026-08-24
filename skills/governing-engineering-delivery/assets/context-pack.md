# {{ITER-ID}}: {{Outcome title}}

- Status: proposed
- Risk class: {{C0-C4}}
- Lifecycle stage: {{project lifecycle state or not-applicable}}
- Requested target state: {{target state}}
- Owner: {{owner}}
- Created: {{ISO-8601 timestamp with timezone}}
- Updated: {{ISO-8601 timestamp with timezone}}

## 1. Objective and scope

- Outcome: {{observable result}}
- User/problem evidence: {{source}}
- Non-goals: {{explicit exclusions}}
- Success signal: {{direct evidence}}
- Stop condition: {{authority, drift or safety condition}}

## 2. Requirements and I/O

- Requirements: {{stable IDs and exact sources}}
- Acceptance: {{stable IDs and exact sources}}
- Delivery/decisions: {{stable IDs and exact sources}}
- Actor/trigger: {{permission and entry}}
- Inputs: {{source, shape, validation, limits and authority}}
- Processing: {{authoritative steps and invariants}}
- Persistence: {{entities, immutability, idempotency, concurrency and revision}}
- Outputs/recovery: {{success, partial, error, denied, stale and retry behavior}}

## 3. Visual and experience baseline

- Baseline artifact: {{Figma, wireframe, tokens, screenshot or interaction contract}}
- Routes/actions: {{canonical routes and typed actions}}
- States: {{loading, empty, error, blocked, permission and success}}
- Responsive/accessibility: {{desktop/narrow, keyboard, focus, semantics, contrast and zoom}}

## 4. Technical design and architecture

- Stack and rationale: {{frontend, backend, data, runtime}}
- Components/data flow: {{ownership and integration}}
- API/schema: {{contracts, migration and compatibility}}
- External integrations: {{provider, timeout, retry, idempotency and cost or none}}
- Trust boundaries/observability: {{boundaries, IDs, logs and evidence}}

## 5. Coding, version and context baseline

- Coding standard: {{project conventions}}
- Branch: {{branch}}
- Commit: {{40-character SHA}}
- `git status --short` captured at: {{ISO-8601 timestamp with timezone}}
- Worktree state: clean | dirty-with-inventory
- Existing changes: {{owner, intent and overlap}}
- Runtime/data baseline: {{environment, database/fixture identity and known failures}}
- Version/migration/rollback: {{rules and recovery point}}

## 6. Authorization ledger

| Action category | State | Exact scope | Approver/source | Authorized at | Validity | Consumed/receipt |
|---|---|---|---|---|---|---|
| Read-only inspection | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | {{validity}} | {{receipt}} |
| Product document writes | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | {{validity}} | {{receipt}} |
| Code/test/local data writes | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | {{validity}} | {{receipt}} |
| Local lint/test/build/browser | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | {{validity}} | {{receipt}} |
| External public reads | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | {{validity}} | {{receipt}} |
| Provider calls or paid actions | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | one-shot | {{receipt}} |
| Commit/branch/tag/push/PR | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | {{validity}} | {{receipt}} |
| Hosted migration/deployment/secrets | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | one-shot | {{receipt}} |
| Publication/external message | authorized / not-authorized | {{scope}} | {{source}} | {{timestamp}} | one-shot | {{receipt}} |
| Destructive action | authorized / not-authorized | {{exact resolved target and recovery}} | {{source}} | {{timestamp}} | one-shot | {{receipt}} |

## 7. Delivery slices

| Slice | Observable outcome | Files/data | Focused check | Gate |
|---|---|---|---|---|
| 1 | {{smallest vertical outcome}} | {{scope}} | {{behavior}} | {{review}} |

## 8. Review gates

| Checkpoint | Human/primary AI/independent reviewer | Evidence | Blocking condition |
|---|---|---|---|
| {{gate}} | {{named role}} | {{direct evidence}} | {{condition}} |

## 9. Sandbox, security and recovery

- Sandbox proof: {{root, write allowlist, prohibited paths, network, credential class and data target}}
- Authentication/authorization: {{controls or architecture reason for not-applicable}}
- Secrets: {{bindings and redaction evidence}}
- Input/injection: {{validation, query and rendering probes}}
- Web security: {{CSRF, SSRF/redirect, session, rate/body/cost/replay/dependency controls}}
- Backup/rollback: {{recovery point and preservation}}
- Destructive behavior: {{none or separately authorized exact action}}
- Highest-cost counterexample: {{dangerous precondition, action and required block/preservation}}

## 10. Structured debugging

- Record/reproduce: {{environment, expected/actual and smallest case}}
- Preserve/localize: {{redacted evidence and failing layer}}
- Hypothesis: {{falsifiable cause and discriminating probe}}
- Repair/regress/verify/trace: {{authority, test and evidence route}}

## 11. Verification and traceability

- Regression signal: Fails before because {{reason}}; passes after when {{observable invariant}}.
- Focused checks: {{commands/probes}}
- Required checks: {{configured lint/typecheck/test/build commands}}
- Direct evidence: {{UI/API/persistence/external delta and unchanged neighbors}}
- Review evidence: {{reviewer and artifact}}
- Traceability: {{requirement → acceptance → delivery → implementation → evidence}}

## 12. Execution log and handoff

| Timestamp | Slice/action | Actual delta | Checks/evidence | Remaining risk |
|---|---|---|---|---|
| {{timestamp}} | {{action}} | {{files/data/external effects}} | {{result}} | {{risk}} |

- Final status: {{approved/implemented/verified/blocked}}
- Actual delta: {{files, data and external effects; state zero explicitly}}
- Fresh checks: {{commands, timestamp and result}}
- Residual risk: {{specific risk}}
- Rollback point: {{artifact/backup/commit or not-applicable}}
- Next action: {{one exact action}}
- Authority still required: {{categories}}

### Governance validation

- Mode: manual/PARTIAL | deterministic
- Reviewer: {{named reviewer or missing}}
- Result/evidence: {{PASS/PARTIAL/BLOCKED and artifact}}
- Active blockers: {{none or exact blockers}}
- Enforcement gap: {{what validation cannot prove}}
