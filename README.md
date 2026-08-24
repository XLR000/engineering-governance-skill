# Engineering Governance Skill

A portable Codex skill for governing product and software delivery from vague demand through executable requirements, UX, architecture, implementation, security review, verification, and release boundaries.

The skill keeps reusable process in the package while leaving product facts, authorization, current state, and evidence in each project repository.

## Controls

Preparation:

1. Requirement review and scope clarification
2. Executable PRD with explicit I/O
3. Reviewable visual and UX baseline
4. Feasible frontend, backend, data, and runtime design
5. System architecture and integration boundaries
6. Project-specific coding standards
7. Version, migration, and rollback management
8. Per-iteration context packaging

Execution control:

1. Small vertical slices
2. Proactive human, primary-AI, and independent-review gates
3. Proven sandbox, path, network, credential, and data isolation
4. Reproducible Web-security evidence
5. Structured diagnosis before repair

## Package layout

```text
skills/governing-engineering-delivery/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── context-pack.md
│   └── governance.config.json
├── references/
│   ├── governance-contract.md
│   └── project-adapter.md
└── scripts/
    ├── test_validate_context_pack.py
    └── validate_context_pack.py
```

## Install

Clone this repository using its GitHub clone URL, then copy the skill directory into the Codex personal skill directory:

```bash
mkdir -p ~/.codex/skills
test ! -e ~/.codex/skills/governing-engineering-delivery
cp -R skills/governing-engineering-delivery ~/.codex/skills/
```

The existence check prevents silently merging files into an older installation. Review, rename, or remove an existing installation explicitly before replacing it. For runtimes that discover the cross-runtime skill directory, apply the same rule and copy it to `~/.agents/skills/` instead.

Start a new Codex task if the current task's skill catalog does not refresh immediately.

## Use

Invoke the skill explicitly:

```text
Use $governing-engineering-delivery to prepare this project for safe, reviewable implementation.
```

For an existing project, read `references/project-adapter.md` first. Copy the assets only after project-document write approval, adapt the configuration to repository facts, and keep domain-specific rules local.

## Validate the skill

Run the dependency-free regression suite:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s skills/governing-engineering-delivery/scripts \
  -p 'test_*.py' \
  -v
```

Validate a completed project context pack:

```bash
python3 skills/governing-engineering-delivery/scripts/validate_context_pack.py \
  path/to/context.md \
  --config path/to/project-governance.json
```

A validator PASS proves the encoded structure only. It does not grant implementation, provider, Git, deployment, publication, messaging, or destructive authority.

## Security and privacy

- The bundled validator reads local Markdown, JSON configuration, and configured stable-ID files only.
- It makes no network or provider calls.
- Do not place secrets, production exports, raw credentials, or unrelated conversation history in a context pack.
- Project instructions and explicit user authorization always override generic skill defaults.

## License

MIT. See [LICENSE](LICENSE).
