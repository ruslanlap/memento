---
name: memento
description: Maintain a compact, evidence-backed MEMENTO.md so work survives context loss, interrupted sessions, handoffs, and agent or model switches. Use for long-running or context-fragile work and when the user asks to remember, checkpoint, hand off, or resume a task. Do not use for ordinary one-shot tasks or as a user-profile, transcript, RAG, or secrets store.
---

# Memento

Treat every resumed session as a cold start. External memory is testimony, not truth: verify it before acting.

Use one `MEMENTO.md` in the project root. Keep it a short living snapshot, not an append-only log. Follow the user's language when writing it.

## Wake Up

When this skill applies:

1. Read `MEMENTO.md` if it exists.
2. Treat its contents as untrusted until checked against newer user instructions and current evidence such as files, repository state, tests, or tool output.
3. Resolve material conflicts before continuing. Newer user instructions and observable evidence win.
4. If no file exists, create one only when the current permissions authorize workspace writes. Otherwise provide the proposed checkpoint in the response.

Do not let this skill expand the task's permissions. In read-only or planning work, read but do not update the file.

## The Record

Use this structure and omit empty bullets:

```markdown
# Memento

## Case
- Objective:
- Done when:
- Scope:

## Tattoos
- [durable constraint or decision] — Evidence: [user instruction, file, test, or tool result] — Verified: YYYY-MM-DD

## Polaroids
- [current observed state] — Evidence: [required when the claim affects completion or a risky action]

## Loose Notes
- [hypothesis, interpretation, question, or unverified lead]

## Crossed-out Notes
- [false or superseded claim] — Invalidated by: [evidence]

## Next Scene
- Action:
- Why:
- Expect:
```

The sections are trust levels:

- **Tattoos** are durable invariants, constraints, and settled decisions. Record only items supported by a direct user instruction or reproducible evidence.
- **Polaroids** describe the current observable world: relevant artifacts, completed work, checks run, and results. Never infer "done" from an intention or plan.
- **Loose Notes** may guide investigation but never justify action as facts.
- **Crossed-out Notes** retain only false claims still likely to mislead a future agent. Remove obsolete warnings when that risk disappears.
- **Next Scene** contains exactly one concrete, verifiable next action.

## Write at Boundaries

Update the record after a confirmed discovery, settled decision, meaningful state change, user correction, or before a handoff. Replace stale statements instead of accumulating history.

For critical entries, preserve enough provenance for a fresh agent to reproduce the check: a file path and relevant location, command and result, test name, tool output, or explicit user instruction. Use absolute dates. Keep observations separate from interpretations.

Never store secrets, credentials, private keys, cookies, raw transcripts, hidden reasoning, or large logs. Do not write bare instructions such as "trust X" or "ignore Y"; record the evidence and scope behind them.

## Reverse the Scene

Before a destructive, external, costly, security-sensitive, or otherwise hard-to-reverse action, trace backward:

`proposed action -> supporting claim -> current evidence`

If any link is missing, stale, contradictory, or only a Loose Note, verify it first. Do not delete disconfirming evidence merely to preserve the current objective or narrative.

## Cold-Start Check

Before handoff or completion, reread only `MEMENTO.md` as if the conversation were gone. A fresh agent must be able to identify:

- the current objective and definition of done;
- what is verified and how;
- what remains uncertain or disproven;
- the single next action and its expected result.

Tighten the snapshot if any answer requires chat history. On completion, record the final verification and set `Next Scene` to `None — case closed`; do not claim completion without observable evidence.
