# git-03 — tag versions and publish afyz-forge

Run from: `c:\laragon\www\afyz-forge` (Git Bash: `/c/laragon/www/afyz-forge`), after git-02.

## 1. Tag each plugin version and the marketplace

```bash
git tag -a user-first-ux-v1.1.0 -m "user-first-ux 1.1.0"
git tag -a ui-studio-v1.0.0 -m "ui-studio 1.0.0"
git tag -a orbit-design-engine-v8.0.0 -m "orbit-design-engine 8.0.0"
git tag -a system-design-v1.0.0 -m "system-design 1.0.0"
git tag -a session-orchestrator-v0.1.0 -m "session-orchestrator 0.1.0"
git tag -a marketplace-v0.10.0 -m "afyz-forge marketplace 0.10.0"
git tag -l
```

## 2. Publish to the new repo (chosen)

The empty `Afyz97/afyz-forge` repository you created on GitHub is the remote from git-01.

```bash
git push -u origin main
git push origin --tags
```

## 3. Check the install from GitHub

In any Claude Code session:

```text
/plugin marketplace add Afyz97/afyz-forge
/plugin install user-first-ux@afyz-forge
/plugin install ui-studio@afyz-forge
```

If that machine still has the old marketplace: `/plugin marketplace remove ai-skills` first.

## 4. Option not chosen — replace the old repo's contents (DESTRUCTIVE)

> **DESTRUCTIVE.** This overwrites the history of `Afyz97/ai-skills` on GitHub with afyz-forge's
> history. Existing clones and installs of `ai-skills` break. Only do this if you decide not to
> keep the old repo. Back it up first.

```bash
git clone --mirror https://github.com/Afyz97/ai-skills.git /c/laragon/www/ai-skills-backup.git
git remote add old https://github.com/Afyz97/ai-skills.git
git push --force-with-lease old main
git push old --tags
```

## 5. Optional — point the old repo at the new one (non-destructive)

To keep `Afyz97/ai-skills` online but tell people where things moved, add a short notice to its
README in the old project and push normally:

```bash
cd /c/laragon/www/ai-skills
printf '\n> **Moved:** this marketplace is now [Afyz97/afyz-forge](https://github.com/Afyz97/afyz-forge). See its MIGRATION.md.\n' >> README.md
git add README.md
git commit -m "docs: point to the new afyz-forge repository"
git push origin main
```
