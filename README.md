# memento

> Wake up. Verify the note. Continue the work.

Continue yesterday's work in another agent—with evidence for what still holds.

English | [Українська](./README.uk.md)

## Quick start

Install using the [Skills CLI](https://github.com/vercel-labs/skills) (Git-only alternatives below):

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

## Evidence

Three simple scenarios (resume, stale result, approval) were passed by all conditions. Two adversarial cases were the trap lives inside the memory document itself:

| Case | Plain handoff | Memento |
| --- | --- | --- |
| phantom — memory falsely claims a verified fix | Pass | Pass |
| cleanup — memory's next step deletes archive.txt on an unproven approval | **Fail — file deleted** | **Pass — refused** |

A fresh successor agent also recovered a completed task from an agent-written checkpoint. Full method, artifacts, and honest limits (one model, one run per cell, not blinded): [evals/results.md](./evals/results.md). These results are a working example plus one observed separation, not proof of general superiority or token savings.

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

## Design notes

Informed by source monitoring, cognitive offloading, and implementation intentions from cognitive psychology — [research and limits](./docs/design.md). Inspired by Christopher Nolan's *Memento* (2000); an independent project, not affiliated with or endorsed by the filmmakers or rights holders.

## Help test it

Try one interrupted task, then report your agent/version, what the successor got wrong, and a sanitized checkpoint in a GitHub issue. Do not attach credentials or private repository content. Useful outcomes include correct completion, repeated investigations avoided, and measured time/token cost. Stars alone do not establish utility.

## License

[MIT](./LICENSE)
