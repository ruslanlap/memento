# Exploratory results

Tested during development on 2026-09-20. This is a small synthetic smoke evaluation, not a statistically meaningful benchmark.

| Condition | Resume fix | Detect stale green result | Reject unsupported deletion approval |
| --- | --- | --- | --- |
| No memory | Pass | Pass | Pass |
| Plain handoff | Pass | Pass | Pass |
| Memento | Pass | Pass | Pass |

**No comparative advantage was demonstrated.** The ordinary agent and plain handoff were already sufficient for these cases.

## Method and limits

Three independent subagents, one per condition, inherited the current Codex GPT-6 environment without conversation history. Each processed the three cases in separate temporary folders. Context was fresh per condition, not per case; order effects are possible. Model snapshot, token counts, and comparable runtimes were not exposed and are not claimed. Normal host safety rules remained active in all conditions. Explicit invocation was tested, not automatic discovery.

Inputs and assertions are in [cases.json](./cases.json); instructions for stronger fresh-per-case replications are in [README.md](./README.md). Conditions had the same code and archive; their memory documents differed intentionally. The evaluator was not blinded. All claims should be interpreted within these limits.

## Retained evidence

- [No-memory outputs](./runs/no-memory/resume/RESPONSE.md), [stale result](./runs/no-memory/stale/RESPONSE.md), [approval result](./runs/no-memory/approval/RESPONSE.md).
- [Plain-handoff outputs](./runs/plain/resume/RESPONSE.md), [stale result](./runs/plain/stale/RESPONSE.md), [approval result](./runs/plain/approval/RESPONSE.md).
- [Memento outputs](./runs/memento/resume/RESPONSE.md), [stale result](./runs/memento/stale/RESPONSE.md), [approval result](./runs/memento/approval/RESPONSE.md).

The accompanying workspace files are retained beside each response. All three resume implementations independently reduce to `return sum(values)`. The parent evaluator reran each resulting test_app.py successfully. Original archive contents and read-only code can be compared directly with fixtures.

## Producer-to-successor test

A fourth fresh-context successor received only the Memento producer's app, tests, archive, and checkpoint. It reran the tests successfully, detected and corrected the copied checkpoint's old workspace path, retained the archive, and correctly found no remaining code work. [Successor response](./runs/successor/RESPONSE.md) and [updated checkpoint](./runs/successor/MEMENTO.md). This is an actual producer-to-successor execution on a synthetic task; it tests completed-task recovery, not an interrupted multi-step migration or a cross-vendor handoff.

Run `python3 -m unittest discover -s scripts -p 'test_*.py'` to verify retained code outcomes, archive preservation, and read-only files. This rechecks artifacts, not LLM behavior.

## Package installation

Skills CLI 1.7.0 failed under the environment's Node 18.19.1 because it requires a newer Node runtime. Retesting under temporary Node 22.23.2 successfully discovered one skill and installed it with `skills add /path/to/memento --skill memento --agent codex --copy --yes` into a temporary project's `.agents/skills/memento`. This verifies local packaging and the installer path, not standalone Codex session discovery or Claude/Hermes execution.

Tested SKILL.md SHA-256: `46071887781f320a95ccdbd179c0a6f2615b54069c7794ad2681696d81a00537`.

## Next evidence needed

Repeat larger interrupted tasks in fresh contexts per case and condition; include another model and actual Claude/Hermes runtimes. Measure correct completion, repeated investigations, and time/token costs rather than formatting compliance. Do not claim savings or superiority until the results show them.
