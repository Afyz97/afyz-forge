# git-01 — initialise afyz-forge as a repo and connect it to GitHub (no commits)

Run from: `c:\laragon\www\afyz-forge` (Git Bash: `/c/laragon/www/afyz-forge`).

Before you start: create the empty repository **`Afyz97/afyz-forge`** on GitHub yourself, with no
README, licence or `.gitignore`, so the first push isn't rejected.

## 1. Initialise

```bash
cd /c/laragon/www/afyz-forge
git init -b main
git config user.name "AMIR NADZIM KAHARUDIN"
git config user.email "afyzamir97@gmail.com"
```

## 2. Add the remote (option A — chosen: the new repo)

```bash
git remote add origin https://github.com/Afyz97/afyz-forge.git
git remote -v
```

### Option B — not chosen: point at the old repo instead

Only if you later decide to reuse `Afyz97/ai-skills`. Replacing its contents is destructive; see
git-03 §4.

```bash
git remote add origin https://github.com/Afyz97/ai-skills.git
```

## 3. `.gitignore`

Already in place (copied from ai-skills). Check that local state stays
untracked:

```bash
cat .gitignore
git status --short --ignored | grep '^!!' | head
```

Expected ignored items include `.claude/`, `.claude-flow/`, `.impeccable/`, `_source/` and
`plugins/*/evals/results/` if any appear. None of these exist in afyz-forge today.

Next: `git-02-commits.md`.
