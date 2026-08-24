import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_context_pack import validate_file


AUTH_ROWS = """
| Action category | State | Exact scope | Approver/source | Authorized at | Validity | Consumed/receipt |
|---|---|---|---|---|---|---|
| Read-only inspection | authorized | repository | user request | 2026-08-24T10:00:00+08:00 | task | not-applicable |
| Product document writes | authorized | context only | user request | 2026-08-24T10:00:00+08:00 | task | unused |
| Code/test/local data writes | authorized | slice one | user request | 2026-08-24T10:00:00+08:00 | task | unused |
| Local lint/test/build/browser | authorized | configured checks | project rules | 2026-08-24T10:00:00+08:00 | task | unused |
| External public reads | not-authorized | all external reads | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |
| Provider calls or paid actions | not-authorized | all providers | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |
| Commit/branch/tag/push/PR | not-authorized | all history operations | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |
| Hosted migration/deployment/secrets | not-authorized | all hosted state | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |
| Publication/external message | not-authorized | all public actions | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |
| Destructive action | not-authorized | all destructive actions | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |
""".strip()


def valid_context() -> str:
    return f"""# ITER-001: Account export

- Status: approved
- Risk class: C3
- Lifecycle stage: planning
- Requested target state: implementation
- Owner: Delivery agent
- Created: 2026-08-24T10:00:00+08:00
- Updated: 2026-08-24T10:00:00+08:00

## 1. Objective and scope

- Outcome: An administrator exports one account archive.
- Non-goals: No deployment or publication.
- Stop condition: Stop on authority or data-scope mismatch.

## 2. Requirements and I/O

- Requirements: REQ-001
- Acceptance: AC-001
- Delivery: PLAN-001
- Input: Authenticated account identifier.
- Output: One auditable archive.
- Persistence: One export audit row.

## 3. Visual and experience baseline

- Baseline: Approved wireframe and loading/error/permission states.
- Responsive/accessibility: Desktop and narrow viewport, keyboard and focus behavior.

## 4. Technical design and architecture

- Stack: Existing repository stack.
- Components/integrations: UI to API to database; no external provider.
- Trust boundaries: Browser, API and database.

## 5. Coding, version and context baseline

- Coding standard: Existing repository conventions.
- Branch: main
- Commit: 1111111111111111111111111111111111111111
- `git status --short` captured at: 2026-08-24T10:00:00+08:00
- Worktree state: clean
- Version/rollback: Additive compatible change; revert exact slice.

## 6. Authorization ledger

{AUTH_ROWS}

## 7. Delivery slices

| Slice | Outcome | Gate |
|---|---|---|
| 1 | Export one archive | Focused behavior evidence |

## 8. Review gates

| Checkpoint | Reviewer | Blocking condition |
|---|---|---|
| C3 design and verification | Independent reviewer: Riley | Missing direct evidence |

## 9. Sandbox, security and recovery

- Sandbox proof: Disposable local data, restricted write paths and no external network.
- Authentication/authorization: Server-side account ownership.
- Secrets: Server bindings only; no values in logs or evidence.
- Input/injection: Typed server validation and parameterized queries.
- Web security: CSRF, output encoding, rate/body limits and safe errors.
- Backup/rollback: Additive audit row and exact code rollback.
- Destructive behavior: none.

## 10. Structured debugging

- Sequence: Record, reproduce, preserve, localize, hypothesize, repair, regress, verify and trace.

## 11. Verification and traceability

- Regression signal: Fails before because export is unavailable; passes after when the exact audit row and archive exist.
- Required checks: npm run lint; npm test; npm run build.
- Direct evidence: API result, persistence delta and unchanged neighboring accounts.
- Traceability: REQ-001 → AC-001 → PLAN-001 → evidence.

## 12. Execution log and handoff

- Actual delta: Context only; implementation pending.
- Residual risk: Independent implementation evidence pending.
- Next action: Begin slice one after gate approval.
- Authority still required: Commit, deployment and publication.

### Governance validation

- Mode: deterministic
- Reviewer: Riley / independent reviewer
- Result/evidence: PASS — context structure only
- Active blockers: none
"""


class ContextValidatorTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "product").mkdir()
        (self.root / "product" / "spec.md").write_text(
            "# Spec\nREQ-001\nAC-001\nPLAN-001\n", encoding="utf-8"
        )
        self.config = self.root / "governance.json"
        self.config.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "idPrefixes": ["REQ", "AC", "PLAN", "DEC", "RISK"],
                    "knownIdFiles": ["product/spec.md"],
                    "requiredChecks": ["npm run lint", "npm test", "npm run build"],
                    "independentReviewRiskClasses": ["C3", "C4"],
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def write_context(self, source: str) -> Path:
        path = self.root / "context.md"
        path.write_text(source, encoding="utf-8")
        return path

    def codes(self, source: str):
        findings = validate_file(self.write_context(source), self.config)
        return {finding["code"] for finding in findings}

    def test_accepts_complete_portable_context(self):
        self.assertEqual(self.codes(valid_context()), set())

    def test_rejects_placeholder_and_missing_authorization_category(self):
        source = valid_context().replace(
            "- Outcome: An administrator exports one account archive.",
            "- Outcome: {{describe outcome}}",
        ).replace(
            "| Destructive action | not-authorized | all destructive actions | no approval | 2026-08-24T10:00:00+08:00 | one-shot | unused |\n",
            "",
        )
        codes = self.codes(source)
        self.assertIn("UNRESOLVED_PLACEHOLDER", codes)
        self.assertIn("AUTH_LEDGER_INCOMPLETE", codes)

    def test_rejects_unknown_stable_id_from_project_config(self):
        source = valid_context().replace("REQ-001", "REQ-999", 1)
        self.assertIn("UNKNOWN_STABLE_ID", self.codes(source))

    def test_rejects_c4_pass_without_independent_reviewer(self):
        source = (
            valid_context()
            .replace("- Risk class: C3", "- Risk class: C4")
            .replace("- Reviewer: Riley / independent reviewer", "- Reviewer: primary agent")
            .replace("Independent reviewer: Riley", "Primary reviewer only")
        )
        self.assertIn("MISSING_INDEPENDENT_REVIEW", self.codes(source))

    def test_accepts_chinese_independent_reviewer_label(self):
        source = (
            valid_context()
            .replace("- Risk class: C3", "- Risk class: C4")
            .replace("- Reviewer: Riley / independent reviewer", "- Reviewer: 林 / 独立审查人")
        )
        self.assertNotIn("MISSING_INDEPENDENT_REVIEW", self.codes(source))

    def test_rejects_missing_configured_check(self):
        source = valid_context().replace("; npm run build", "")
        self.assertIn("MISSING_REQUIRED_CHECK", self.codes(source))


if __name__ == "__main__":
    unittest.main()
