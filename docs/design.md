# Why these rules exist

Memento borrows useful ideas from cognitive psychology. These are design hypotheses for agents, not evidence that human memory mechanisms or published effect sizes transfer to language models.

| Principle | Research | Application in Memento | What to evaluate |
| --- | --- | --- | --- |
| Source monitoring | [Johnson, Hashtroudi & Lindsay, 1993](https://pubmed.ncbi.nlm.nih.gov/8346328/) describes judgments about where memories originate. [Dodson & Johnson, 1993](https://pubmed.ncbi.nlm.nih.gov/8296926/) experimentally examines how source questions affect false attributions. | Distinguish observation, instruction, inference, and suggested checks; keep the original source and tested state. | Does the agent reject a fabricated approval or an unsupported test result? |
| Cognitive offloading | [Risko & Gilbert, 2016](https://pubmed.ncbi.nlm.nih.gov/27542527/) reviews using external actions and aids to reduce cognitive demand. | Keep a compact checkpoint outside the conversation, with links to large artifacts. | Can a new session finish the task without the original conversation? At what token and time cost? |
| Implementation intentions | [Smith et al., 2014](https://pubmed.ncbi.nlm.nih.gov/24929276/) experimentally examines specific situation/action plans in prospective memory. | `When → Action → Expect`, with a safe fallback when prerequisites are missing. | Does the successor take the right first action and notice a failed prerequisite? |

The 500-word target is an engineering default, not a psychological constant. Evidence checks are selective because verification itself consumes time. No claim of clinically validated behavior, guaranteed injection resistance, or measured token savings is made.

## Product boundary

Memento serves task continuity across sessions and agents with persistent file access. Existing project plans remain authoritative records of their subject; link rather than duplicate them. It does not replace platform memory, permission enforcement, a secret scanner, or concurrency control.

## Evaluation practice

Follow the [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills): compare fresh contexts with and without the skill, include realistic boundary cases, and retain outputs. Include an ordinary handoff baseline, not just a deliberately weak opponent. Record failures, model identity if available, elapsed time, and tokens only when actually reported.
