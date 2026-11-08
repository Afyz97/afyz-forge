# Verification and Framework-Aware Heuristics

First use the project's own lockfile, CI scripts, documentation and build commands. The examples below are **options, not commands to run blindly**. Do not install dependencies or connect to production solely for this skill.

## Evidence hierarchy

1. Observable behavior before/after, externally visible contract or security regression.
2. Repository tests, reproducible failing case, static analyzer finding and actual runtime call chain.
3. Git co-change evidence and dependency-cycle analysis, corroborated by source.
4. Heuristics such as duplicate text, long file, `if`, `sleep`, or `TODO` - only leads.

A large file is not automatically wrong. Duplication of a phrase is not necessarily duplication of responsibility. Git co-change may be caused by formatting sweeps or feature releases. A stable dependency is defined by **rate and reason of change**, not layer labels.

## Laravel / PHP

- Read `routes/`, `app/`, `database/`, `resources/views/`, service providers, events/listeners, jobs, policies, models, migrations, seeders, and tests only as relevant.
- Consider controller -> domain/service -> database boundaries only when the actual change reasons justify them. Avoid adding a service/repository layer just to add one.
- Watch for implicit model observers, route-model binding, container resolution, facades, middleware, Blade components, event listeners, form requests, scheduled tasks, global helpers and stored procedures: static import scans **will miss** many of these.
- Examples where configured: `php artisan test`, `php artisan route:list`, `composer test`, `./vendor/bin/phpunit`, `./vendor/bin/pint --test`, `./vendor/bin/phpstan analyse`. Check available scripts first.
- Beware migrations and stored procedure changes: preserve transaction semantics, constraints, indexes, access control, and data compatibility; never migrate real databases without approval.

## TypeScript / JavaScript and UI frameworks

- Check package scripts/lockfiles and configured tools: `npm test`, `npm run typecheck`, `npm run build`, `pnpm test`, `vitest`, `jest`, ESLint etc. Choose the project's actual package manager.
- Watch for path aliases, barrel reexports, context/state providers, dynamic imports, generated clients, RPC schemas, feature flags and backend/frontend data contracts.
- Preserve user-facing flows, keyboard/accessibility behavior, loading/error/empty states, and correct semantics. Never treat a visual snapshot as sufficient regression evidence.

## Python / other languages

- Favor project-defined `pytest`, `ruff`, `mypy`, `cargo test`, `go test ./...`, `dotnet test` or equivalent only when present.
- Look for registry/plugin discovery, implicit imports, reflection, generated code and distributed system contracts before calling something unused.

## Positive evidence of improvement

- Fewer distinct locations required to change a common business rule (demonstrate with an example change).
- Declining cross-boundary duplicate decisions and confirmed inappropriate dependency edges.
- Behaviorally equivalent observable outputs and relevant test checks.
- Faster navigation through clear module owners and public interfaces (not merely fewer tokens in a single prompt).
- No added unnecessary abstraction, unexpected query/runtime cost or unexplained contract change.

## Safety edge cases

- Read-only audits may produce a report but must not write source, create migrations or auto-format files.
- An old test failure must be recorded separately from new failures.
- If environment services or secrets are unavailable, report checks as **blocked**, not passed.
- When acceptance criteria cannot be verified, stop short of declaring the affected slice complete.
