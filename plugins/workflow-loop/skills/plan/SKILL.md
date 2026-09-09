---
name: plan
description: Write and save a self-contained implementation plan from an approved proposal, settled requirements, or a backlog item. Use when direction is clear and an executable approach is needed; planning alone does not authorize implementation.
---

# Plan

Own the detailed technical approach and execution sequence, preserving product decisions and their status. Follow the shared [workflow harness](../../HARNESS.md) for approval, saving authorization, optional consultation, and the implementation/revision checkpoint. A planning-only assignment does not include application changes.

## Inspect and resolve

Read the proposal/requirements, relevant brief, existing plans/issues, and applicable repository instructions. Inspect current implementation, configuration, dependencies, tests, and documentation far enough to ground the approach. Retain useful file/symbol references and recheck consequential or stale handoff claims. Reuse established patterns where they fit the desired outcome.

When writing an approved proposal, expand it faithfully into an executable plan. Resolve ordinary technical choices with evidence and explicit assumptions. Compare significant alternatives only where a meaningful choice remains; preserve selected solutions and explain consequential tradeoffs.

If inspection reveals a material contradiction, new product choice, changed acceptance criterion, or scope change, return the evidence and dependent work to the parent before proceeding with that work. Do not silently substitute a different plan under the existing approval. Assigned planners do not interview the operator or launch stages/consultations; the parent resolves product questions and Claude needs. When working directly, use the harness's checkpoint as needed, or [brainstorm](../brainstorm/SKILL.md) for materially unsettled goals.

## Write an executable plan

Scale the document to the task. Include what an implementer needs without the conversation history:

- **Objective and current state:** intended outcome, users/scenarios, project root, originating proposal/brief/issue, current behavior, and relevant evidence/patterns.
- **Requirements and boundaries:** required scope, constraints, non-goals, acceptance criteria, and the distinct status of confirmed decisions, delegated choices, assumptions, and provisional targets.
- **Approach:** technical direction, consequential rationale/tradeoffs, and significant alternatives set aside.
- **Sequence:** ordered tasks, concrete outputs, dependencies, relevant areas/files, and completion criteria. Identify useful independent work without assuming a team.
- **Validation:** checks tied to observable acceptance criteria and major risks, important invariants/failure scenarios, grounded commands, and necessary integration or user-flow scenarios.
- **Uncertainty and starting point:** remaining checks/blockers, the work each affects, decisions delegated to the implementer, and the first actionable task/output.

For cross-stage execution, include a compact progress area for task state, deviations with rationale, and validation evidence. Link the originating brief and issue relatively; links provide evidence rather than replacing essential requirements. Do not invent architecture, dependencies, deadlines, or precision merely to fill a template.

Before handoff, verify every required outcome has a task and check, dependencies are feasible, and unknowns have not become implicit decisions. Mark blocked work accurately; a complete document may still be unready to implement.

## Save and hand off

After proposal approval or a direct request for an executable plan, save the complete plan without another save question. An ordinary direct invocation of this skill authorizes writing and saving even without the word “save”; explicit plan-only work still stops before implementation. Plans required by an authorized build/update workflow are also authorized local handoffs. Keep read-only and keep-in-chat work free of file changes, including migrations. Revise a designated existing plan rather than creating a duplicate.

Use `docs/plans/{nnn}-{SLUG}.md` in all projects, with a concise lowercase, hyphenated slug. Resolve it against the project root, or current workspace when no project exists. Number across all slugs: highest existing numeric plan prefix plus one, starting at `001` and zero-padding to at least three digits.

During authorized saving, maintenance, or implementation, migrate existing nonconforming project plans before numbering a new plan. Preserve conforming filenames/numbers. Process the remaining plans in old relative-path order, assigning each the next number above. Retain legacy topics while dropping obsolete counter suffixes. Move/rename into `docs/plans/` without overwriting or collisions. Preserve contents, progress, decision history, and unrelated edits. Update affected backlinks, relative links whose base changes, and active plan/handoff paths; verify them and report the old-to-new mapping.

Verify the written contents and links. Return the saved path (or chat plan), readiness, unresolved material questions, first actionable task, and any migration mapping. The parent checks fidelity to the approved proposal, presents a clickable path, and follows the harness's readiness/revision transition. A direct invocation uses [orchestrate](../orchestrate/SKILL.md) for subsequent authorized stages. Stay in the current conversation; assigned writers return to the parent.

For originating backlog items, load [backlog](../backlog/SKILL.md) when writing links: preserve the ID, add the authorized plan link, and leave status unchanged merely because the plan was written. Incidental issues require separate capture authorization.
