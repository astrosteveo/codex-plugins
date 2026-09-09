---
name: brainstorm
description: Explore ideas through adaptive Socratic conversation and grounded research, then present a proposed plan for approval. Use for uncertain goals or directions, explicitly or when useful; do not intercept straightforward execution requests with settled requirements.
---

# Brainstorm

Help the operator discover what is worth doing, why it matters, and what success means. Keep the conversation in the main thread. Follow the shared [workflow harness](../../HARNESS.md) for approval, plan writing, optional Claude consultation, and subsequent routing; the [plan](../plan/SKILL.md) skill owns the detailed implementation sequence.

## Inspect before asking

Start with the conversation and inspect the relevant codebase when one exists: applicable instructions, implementation, configuration, tests, documentation, and linked backlog items/plans. Follow the paths that establish current behavior and constraints; avoid an exhaustive audit. Retain useful references and summarize findings that affect the discussion. Current implementation describes what exists, not necessarily what the operator wants.

Before asking a question, check whether the baseline or a targeted inspection can answer it. If an answer introduces a new area or conflicts with the baseline, inspect it before making dependent recommendations. Ask only for missing location/access or material preferences that inspection cannot resolve. For a new project or non-code idea, work from the available context.

## Explore adaptively

Meet the operator where they are:

- **No idea yet:** Explore interests, recurring frustrations, people to help, desired capabilities, or appealing examples. Generate possibilities once there is something to ground them in.
- **Rough direction:** Examine the underlying need, important scenarios, assumptions, alternatives, and what would make the idea valuable.
- **Mostly settled:** Concentrate on consequential uncertainty or contradictions without reopening explicit preferences.

Ask one focused question per turn by default, adapting to the previous answer and the uncertainty most likely to change the direction. Seek a reason, concrete example, counterexample, or evidence that could change a decision when useful. Offer your own analysis and alternatives; depth is not a checklist or repeated “why.” Match requests for shorter or deeper exploration.

When helpful, offer 2–4 distinct answers as a numbered list, with a supported recommendation first and tied to the operator's priorities. Interpret a number against the most recent options. Accept freeform replies, combinations, or rejection of all options. Do not manufacture a recommendation when context is insufficient. Suggestions stay provisional until selected or delegated.

Briefly make these controls available early and honor them throughout:

| Response | Behavior |
| --- | --- |
| `skip` | Defer this question; infer no answer. |
| `not sure` | Retain uncertainty; offer an example, smaller question, or deferral. |
| `recommend for me` | Decide this issue with rationale and explicit assumptions; this is not implementation authorization. |
| `back` | Revisit the previous or named decision and update dependent conclusions. |
| `finish` | Stop discovery and present the best available synthesis, retaining blockers and provisional choices. |

Maintain the harness's compact record, distinguishing confirmed requirements, operator decisions, delegated choices, proposals, assumptions, evidence, and open/deferred questions. Summarize consequential decisions periodically and invite corrections naturally without approving every detail.

## Discover what matters

Explore only relevant dimensions: motivation and intended users; concrete scenarios and success criteria; constraints and resources; required scope, optional work and non-goals; dependencies, risks and alternatives. Distinguish the requested solution from the need it serves. Respect explicit choices while examining contradictions and unnecessary complexity.

Use targeted research when facts could change the direction. Preserve sources and explain what remains unverified and which decisions depend on it. Apply the harness's consultation policy when complicated physics or logic arises.

## Converge and hand off

When objective, scope, major constraints, intended direction, and meaningful success criteria are clear, synthesize a self-contained discovery brief and concrete proposed plan. They may be one concise chat deliverable; do not manufacture separate files. Include the problem/users, requirements/non-goals, proposed approach and major work, alternatives and rationale, acceptance/validation, relevant evidence, decisions/assumptions, and material uncertainty. Preserve technical evidence without inventing execution detail or false precision.

Use the harness's proposal checkpoint and route approval to the plan writer through [orchestrate](../orchestrate/SKILL.md). Do not end with an offer to save or ask the operator to restart the session. If writing/implementation is already authorized, continue the relevant handoff. Explicit brainstorm-only work stops with its discovery deliverable. Honor sustained exploration; `finish` need not force a direction when material questions remain.

A saved brief is optional: write one when requested or needed for an authorized handoff, preserving decision statuses. Follow existing conventions; otherwise use `docs/briefs/{slug}-001.md` relative to the project root, allocating the next available three-digit suffix. Verify content/links and return a clickable path. Honor keep-in-chat; never invent a saved artifact.

## Companion backlog

Load [backlog](../backlog/SKILL.md) only when capturing findings or maintaining an originating issue. Preserve its ID/evidence in the handoff; after an authorized artifact save, link it from the issue without changing status merely because planning occurred.

Offer incidental findings at a natural stopping point only when useful, separately from a pending plan checkpoint. Existing capture authorization or acceptance of that offer is required to create new entries. Approval of a plan or brief does not grant it. Brainstorming remains usable without backlog maintenance.
