# memento

> Wake up. Verify the note. Continue the work.

<p align="center">
  <img src="./assets/memento-hero.png" alt="A noir investigation desk with nested Polaroids, fragmented notes, a reversed clock, and a red evidence thread" width="100%">
  <br>
  <sub>Original artwork created for this project; no film stills or official poster assets.</sub>
</p>

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-portable-111111)](./SKILL.md)
[![Validate](https://github.com/ruslanlap/memento/actions/workflows/validate.yml/badge.svg)](https://github.com/ruslanlap/memento/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

`memento` is a portable skill that gives coding agents durable, evidence-backed task memory across context loss, interrupted sessions, handoffs, and model switches.

Most memory tools optimize storage. `memento` optimizes trust: a note is testimony, not truth, even when the agent wrote it itself.

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

- **Cold-start discipline:** every resumed session begins by distrusting and rechecking the record.
- **Evidence tiers:** facts, hypotheses, and invalidated claims cannot silently blur together.
- **Poison-note resistance:** critical entries retain provenance; contradictions are preserved while dangerous.
- **Tiny surface area:** one `SKILL.md`, one project `MEMENTO.md`, no database, embeddings, hooks, runtime, or dependencies.
- **Permission-aware:** automatic activation never grants permission to modify the workspace.

See a completed fictional checkpoint in [`examples/MEMENTO.md`](./examples/MEMENTO.md).

## Install

Clone the repository into the personal skills directory used by your agent.

### Codex

```sh
git clone https://github.com/ruslanlap/memento.git ~/.codex/skills/memento
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

Copy this repository into the tool's skills directory. The portable contract is the root [`SKILL.md`](./SKILL.md), with only the standard `name` and `description` frontmatter fields.

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

The repository has no runtime dependencies:

```sh
python3 scripts/check.py
```

The check validates portable frontmatter, required protocol sections, and the example record. CI runs it on every push and pull request.

## Design sources

The design follows Nolan's own description of tattoos for essential information, Polaroids for everyday context, and habit/routine as Leonard's underlying system in his [Fresh Air interview](https://freshairarchive.org/segments/christopher-nolan). The forward and reverse narrative strands are summarized by the [British Film Institute](https://www.bfi.org.uk/sight-and-sound/features/christopher-nolan-time-games).

This project is an independent software skill inspired by the film's ideas. It is not affiliated with or endorsed by the filmmakers, studios, or rights holders.

## License

[MIT](./LICENSE)
