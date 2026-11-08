# Publishing & Update Workflow — afyz-forge repo

How changes reach users. Remote is `https://github.com/Afyz97/afyz-forge.git`, branch `main`.

## Standard change → publish loop

```bash
cd <repo>
# make edits (skills, manifests, docs)
python -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json',recursive=True)]"  # JSON valid
git add -A
git commit -m "…"
git push origin main
```

Then on any Claude Code client:
```
/plugin marketplace update Afyz97/afyz-forge     # re-pull the marketplace
/plugin install <plugin>@afyz-forge              # or it updates if already installed
```

If a client cached a *broken/old* marketplace, force a clean refresh:
```
/plugin marketplace remove Afyz97-afyz-forge
/plugin marketplace add Afyz97/afyz-forge
```

## Notes / gotchas

- **Network from some sandboxes is intermittent** — `git ls-remote` may work while `push` times out.
  If a push fails to connect, retry; it has succeeded on retry before.
- **Force-push** is only appropriate for history cleanup on this solo repo, and only with explicit
  owner approval (it rewrites published history). Use `--force-with-lease`. Normal changes are
  fast-forward `git push`.
- **Never commit** `.claude-flow/`, `.claude/`, `.impeccable/` (in `.gitignore`). If they ever get
  staged, `git rm -r --cached` them before committing.
- After a **rename** (plugin, marketplace, or moving folders), clients must `remove` + `add` the
  marketplace (a plain `update` may not pick up name changes).

## Install methods offered to users

1. **Plugin/marketplace (primary):** `/plugin marketplace add Afyz97/afyz-forge` →
   `/plugin install <plugin>@afyz-forge`. Works from any project/device.
2. **Manual copy:** copy a skill folder from `plugins/<plugin>/skills/<skill>/` into
   `~/.claude/skills/` (personal) or `.claude/skills/` (project). Copy user-first-ux skill folders
   together (they link `../user-first-ux/references/`).
3. **`npx skills add Afyz97/afyz-forge`** — generic installer; verify it discovers skills under the
   `plugins/<plugin>/skills/` layout before promising it (see `context.md` open follow-ups).

## Release checklist

- [ ] JSON manifests valid; `owner`/`author` are objects.
- [ ] Each `source` folder resolves; folder==plugin==entry names match.
- [ ] Each `SKILL.md` description ≤1024 chars; body operational.
- [ ] No stale internal links after moves/renames.
- [ ] No local tooling state staged.
- [ ] README + `.ai/agents/*` reflect the current structure.
- [ ] Commit, push, refresh marketplace, test one `/plugin install`.
