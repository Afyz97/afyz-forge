# codeweave

Evidence-driven architecture audit and behaviour-preserving refactoring for existing codebases.
One manual-invoke skill (`disable-model-invocation: true`), so it never competes for triggers.

```text
/plugin install codeweave@afyz-forge
/codeweave --audit-only
/codeweave focus on Laravel controllers, services and stored procedures
```

Contents, modes, manual install paths and script usage: [skills/codeweave/README.md](skills/codeweave/README.md).

Not for scalability or reliability reviews (single points of failure, caching, queues) - use the
**system-design** plugin's `system-design-review`.

Developed in the `Afyz97/ai-skills` playground and mirrored here. Changes over the source 1.0.0:
`git_cochange.py` no longer fails to compile on Python 3.9-3.11 (backslash inside an f-string
expression), ASCII-only text, `${CLAUDE_PLUGIN_ROOT}` script paths, the zip-only `INSTALL.md`
folded into the skill README.
