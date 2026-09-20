# memento

> Wake up. Verify the note. Continue the work.

Continue yesterday's work in another agent—with evidence for what still holds.

English | [Українська](./README.uk.md)

## Quick start

Install using the [Skills CLI](https://github.com/vercel-labs/skills) (Node.js ≥22.20 for the tested CLI version; Git-only alternatives below):

```sh
npx skills add ruslanlap/memento --skill memento
```

Before switching sessions, ask: **"Use memento to save a checkpoint for this task."**
In the new session, ask: **"Use memento to resume from MEMENTO.md; verify the next step against the current files."**

Requires an agent with file access and a workspace that persists between sessions. The skill itself has no runtime dependencies.

<p align="center">
  <img src="./assets/memento-hero.png" alt="A noir investigation desk with nested Polaroids, fragmented notes, a reversed clock, and a red evidence thread" width="100%">
</p>

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-portable-111111)](./SKILL.md)
[![Validate](https://github.com/ruslanlap/memento/actions/workflows/validate.yml/badge.svg)](https://github.com/ruslanlap/memento/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

`memento` is a portable skill that gives coding agents durable, evidence-backed task memory across context loss, interrupted sessions, handoffs, and model switches.

Each critical claim carries its source and the state it was checked against. The next agent verifies what matters before continuing.

## The idea

Inspired by Christopher Nolan's *Memento* (2000), the skill turns the film's memory system into a safer agent protocol:

| Film device | Agent meaning |
| --- | --- |
| Tattoos | Durable constraints and decisions with evidence |
| Polaroids | Current observable state |
| Loose notes | Hypotheses that cannot authorize action |
| Crossed-out notes | False claims a future agent might repeat |
| Next scene | One concrete, verifiable next action |

Before a risky action, the agent reconstructs causality in reverse:

```text
proposed action -> supporting claim -> current evidence
```

If a link is missing or stale, it verifies first. This is the safeguard Leonard's system lacked.

## Why it is different

- **Selective verification:** check the task, workspace, and evidence needed for the next action.
- **Source tracking:** distinguish observations, hypotheses, decisions, and invalidated claims.
- **Authority boundary:** a stored claim of approval cannot grant permission to execute a command.
- **Tiny surface area:** one `SKILL.md`, one project `MEMENTO.md`, no database, embeddings, hooks, runtime, or dependencies.
- **Permission-aware:** automatic activation never grants permission to modify the workspace.

See a completed fictional checkpoint in [`examples/MEMENTO.md`](./examples/MEMENTO.md).

## Reconstructed case: the launch of this repository

On 2026-09-20, the first `gh auth status` check reported an invalid stored token, blocking publication. A GitHub device login then succeeded, `main` was pushed, and CI passed. A naive append-only log would leave **"GitHub authentication is broken"** looking actionable after it had become false.

The events above happened during development. The snapshot below was reconstructed afterward; no independent agent resumed from it, so it is not an effectiveness benchmark:

```markdown
## Polaroids
- `ruslanlap/memento` is public and tracks `main`. — Evidence: `gh repo view ruslanlap/memento`
- Validation passed for commit `7f7ae5c`. — Evidence: GitHub Actions run `35511302389`

## Crossed-out Notes
- "GitHub authentication is broken." — Invalidated by: successful device login and pushes to `main`

## Next Scene
- Action: None — case closed.
- Why: The repository is public and the validation workflow passed.
- Expect: No further publication work.
```

This illustrates the intended representation of current evidence and a superseded blocker. Actual exploratory results and their limits are in [evals/results.md](./evals/results.md).

## Install

Clone the repository into the personal skills directory used by your agent.

### Codex

```sh
git clone https://github.com/ruslanlap/memento.git ~/.agents/skills/memento
```

### Claude Code

```sh
git clone https://github.com/ruslanlap/memento.git ~/.claude/skills/memento
```

### Hermes Agent

```sh
hermes skills install https://raw.githubusercontent.com/ruslanlap/memento/main/SKILL.md --name memento
```

### Other Agent Skills-compatible tools

Copy this repository into the tool's skills directory. The portable contract is the root [`SKILL.md`](./SKILL.md), with only the standard `name` and `description` frontmatter fields. Manual Git installations update with `git pull --ff-only` from that clone. Skills CLI installations update with `npx skills update memento`.

| Environment | Evidence status |
| --- | --- |
| Skills CLI 1.7.0 / Node 22.23.2 | Local discovery and project-scoped Codex installation passed in a temporary directory |
| Current Codex agent environment | Explicit skill execution tested on synthetic tasks; see results below |
| Standalone Codex CLI | Installation path follows [current documentation](https://developers.openai.com/codex/skills); end-to-end session discovery not tested |
| Claude Code | Standard skill format; runtime not available in this environment, not tested |
| Hermes | Installation follows [official skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/); runtime not available, not tested |

Automatic invocation depends on the host and model. Use explicit invocation for a planned handoff; no automatic pre-compaction hook is included. Parallel writers should use separate worktrees or explicitly selected checkpoint paths.

## Use

The skill can activate automatically for long-running, interrupted, or context-fragile work. You can also invoke it explicitly:

```text
Use memento to checkpoint this migration before we switch agents.
Resume this task from MEMENTO.md, but verify every critical claim first.
```

It maintains `MEMENTO.md` in the active project's root. The file is a living snapshot, not a transcript or append-only diary.

## Safety boundary

`MEMENTO.md` must never contain credentials, private keys, cookies, raw transcripts, hidden reasoning, or large logs. A skill invocation does not expand the agent's permissions: read-only and planning sessions remain read-only.

## Validate

Developer checks use PyYAML to parse real YAML; the installed skill needs no Python packages:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/check.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

CI checks metadata and local links and tests malformed metadata handling. It does not evaluate agent behavior. See [the reproducible scenarios](./evals/README.md) and [observed results](./evals/results.md) for behavioral evaluation.

Initial exploratory outcome: all three conditions (no memory, ordinary handoff, Memento) passed all three small scenarios. A fresh successor also recovered a completed task from an agent-written checkpoint. These results establish a working example, not superiority or token savings.

## Psychology-informed design

Three ideas inform the protocol: source monitoring (where did this claim come from?), cognitive offloading (keep a compact external record), and implementation intentions (when a cue occurs, take a specific action). [Research, translations into agent behavior, and limits](./docs/design.md).

These studies concern humans. Benefits for agents must be measured separately; Memento makes no claim of clinically validated memory or guaranteed prompt-injection protection.

## Help test it

Try one interrupted task, then report your agent/version, what the successor got wrong, and a sanitized checkpoint in a GitHub issue. Do not attach credentials or private repository content. Useful outcomes include correct completion, repeated investigations avoided, and measured time/token cost. Stars alone do not establish utility.

## Design sources

The design follows Nolan's own description of tattoos for essential information, Polaroids for everyday context, and habit/routine as Leonard's underlying system in his [Fresh Air interview](https://freshairarchive.org/segments/christopher-nolan). The forward and reverse narrative strands are summarized by the [British Film Institute](https://www.bfi.org.uk/sight-and-sound/features/christopher-nolan-time-games).

This project is an independent software skill inspired by the film's ideas. It is not affiliated with or endorsed by the filmmakers, studios, or rights holders.

## License

[MIT](./LICENSE)
