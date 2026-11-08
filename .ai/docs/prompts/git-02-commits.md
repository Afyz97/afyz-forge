# git-02 — one commit per logical change

Run from: `c:\laragon\www\afyz-forge` (Git Bash: `/c/laragon/www/afyz-forge`), after git-01.

Each block stages exact paths and commits with a Conventional Commit message. Run them in order.
`git status` at the end must be clean.

## 1. system-design (imported unchanged)

```bash
git add plugins/system-design
git commit -m "chore(system-design): import plugin unchanged from ai-skills"
```

## 2. user-first-ux

```bash
git add plugins/user-first-ux
git commit -m "feat(user-first-ux): own all behaviour rules; absorb ux-laws, accessibility, copy and research" -m "Adds skills ux-laws, ui-accessibility, ui-ux-copy, ui-research, commands ui-a11y and ui-copy, agent a11y-auditor, 15 trigger evals and e-commerce/enterprise/mobile domain playbooks. Single owner of priority order, workflow, severity, WCAG numbers (44px house floor, ~7:1 recommended), laws of UX, ethics, states, forms, flows, BM/EN. Version 1.1.0."
```

## 3. ui-studio

```bash
git add plugins/ui-studio
git commit -m "feat(ui-studio)!: add visual-polish and ui-styles; hand behaviour rules to user-first-ux" -m "Adds visual-polish (Ten Fixes rules, audit/fix/build modes, measurement scripts), commands polish-audit/polish-fix/polish-new, agent ui-ten-fixes-auditor, ui-styles (classifier, dials, 10 styles), scored audit, token architecture and new visual-direction references. visual-system.md is the single token owner. Removes the copies of user-first-ux. Version 1.0.0." -m "BREAKING CHANGE: /ui-studio:ui-a11y and /ui-studio:ui-copy moved to /user-first-ux:ui-a11y and /user-first-ux:ui-copy; ui-accessibility, ui-ux-copy and ui-research moved to user-first-ux."
```

## 4. orbit-design-engine and session-orchestrator

```bash
git add plugins/orbit-design-engine plugins/session-orchestrator
git commit -m "chore: migrate orbit-design-engine and session-orchestrator to afyz-forge" -m "orbit-design-engine stays a dedicated plugin: repo URLs updated, seven descriptions gain a Not-for ending, one target-size line points to user-first-ux. session-orchestrator: repo URL and install commands updated."
```

## 5. Marketplace

```bash
git add .claude-plugin/marketplace.json
git commit -m "feat(marketplace)!: rename marketplace to afyz-forge and list the consolidated plugins" -m "ux-laws, ui-ten-fixes, omni-design and ultimate-design-suite are merged and no longer listed." -m "BREAKING CHANGE: install commands change from <plugin>@ai-skills to <plugin>@afyz-forge; re-add the marketplace from Afyz97/afyz-forge."
```

## 6. Agent infrastructure

```bash
git add .ai/agents
git commit -m "docs(ai): describe the two-plugin layout, one-owner rule and afyz-forge repo"
```

## 7. Docs, merge records and root files

```bash
git add README.md CHANGELOG.md MIGRATION.md LICENSE .gitignore ui-design.skill docs evaluations scripts .ai/docs
git commit -m "docs: add migration guide, changelog and merge records; refresh README and docs"
```

## 8. Check

```bash
git status
git log --oneline
```

`git status` should say "nothing to commit, working tree clean", and the log should show 7 commits.

Next: `git-03-release.md`.
