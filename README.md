# Engineering Delivery Workflow Skill

A portable Codex skill for helping an agent move through software-product work in an orderly way: understand the change, define a first slice, implement it, verify it, and hand it off.

It is intentionally lightweight. UI, API/data, high-risk external actions, and debugging add focused preparation only when the change actually needs it. Project rules, product facts, authorizations, and current evidence remain in the project repository.

## Package layout

```text
skills/governing-engineering-delivery/
├── SKILL.md
├── agents/openai.yaml
├── assets/context-pack.md
└── references/project-adapter.md
```

## Install

Clone this repository, then copy the skill directory into Codex's personal skill directory:

```bash
mkdir -p ~/.codex/skills
test ! -e ~/.codex/skills/governing-engineering-delivery
cp -R skills/governing-engineering-delivery ~/.codex/skills/
```

The existence check prevents silently merging files into an older installation. Review, rename, or remove an existing installation explicitly before replacing it. Start a new Codex task if its skill catalog does not refresh immediately.

## Use

```text
Use $governing-engineering-delivery to organize this product change from the first slice through verification and handoff.
```

For a new repository, read `references/project-adapter.md`. Use `assets/context-pack.md` only when a short task card will make a multi-step change or handoff clearer.

## Validation

The GitHub workflow checks package metadata, the expected package layout, portable-content hygiene, and unresolved placeholders outside template assets. It does not certify a project change, grant authority, or substitute for project-local checks.

## Safety boundary

- Do not place secrets or raw production data in skill artifacts.
- Validate untrusted input where the changed system accepts it.
- Obtain exact approval before destructive, paid, public, hosted, or irreversible external actions.
- Report verification evidence truthfully.

## License

MIT. See [LICENSE](LICENSE).
