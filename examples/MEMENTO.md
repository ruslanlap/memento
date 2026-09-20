# Memento

## Case
- Objective: Prepare release `2.4.0` without publishing it.
- Done when: The package builds, the full test suite passes, and release notes are ready for review.
- Scope: Local release preparation only; publishing and tagging are excluded.

## Tattoos
- Do not publish or create a remote tag without explicit approval. — Evidence: user instruction from 2026-09-20 — Verified: 2026-09-20
- Preserve Node.js 20 support. — Evidence: `package.json` engine constraint and CI matrix — Verified: 2026-09-20

## Polaroids
- `package.json` contains version `2.4.0`. — Evidence: inspected `package.json` on 2026-09-20
- The build passes. — Evidence: `npm run build` exited 0 on 2026-09-20
- The full test suite has not been run since the version change.

## Loose Notes
- The changelog may be missing the authentication fix; compare it with commits since `v2.3.1`.

## Crossed-out Notes
- "The release is already published." — Invalidated by: registry query returned no `2.4.0` version on 2026-09-20

## Next Scene
- Action: Run `npm test`.
- Why: Passing tests are required by the definition of done and have not been verified after the version change.
- Expect: Exit code 0 and no skipped release-critical tests.
