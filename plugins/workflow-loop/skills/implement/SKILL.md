---
name: implement
description: Execute an implementation plan or settled requirements, validate behavior, and return reviewable changes with evidence. Use for authorized execution and in-scope review corrections; respect planning-only and review-only boundaries.
---

# Implement

Deliver the requested behavior. Follow the shared [workflow harness](../../HARNESS.md) for scope, optional consultation, common quality expectations, and parent-owned transitions. Treat a plan as direction and assumptions, not proof of the current code.

## Establish scope and baseline

Read the request, plan/requirements, relevant brief, and repository instructions. Inspect affected code and validation. Check the working tree, preserve unrelated work, and record the starting state needed to identify your changes. Without Git, track changed files and compare relevant contents directly.

Identify acceptance criteria, dependencies, and blockers; a formal plan is optional for small settled work. Inspect before escalating a missing decision. Assigned workers return consequential questions and their impact to the parent and flag needs for Claude consultation there; direct invocations resolve them in the main conversation. Continue independent authorized work.

## Execute and adapt

Work in dependency order, using relevant domain skills and repository patterns where useful. Keep changes focused. Resolve routine details with evidence and judgment; record compatible technical adjustments in the plan. Escalate changes to objective, required behavior, major constraints, or acceptance criteria before dependent edits. Do not reduce the target to fit the implementation.

Maintain the active plan's task progress, deviations/rationale, and validation evidence when a plan exists. Apply [plan's naming and migration rules](../plan/SKILL.md#save-and-hand-off) during authorized maintenance and use the resulting path in handoffs. A checked box alone is not evidence; a trivial edit needs no new tracking artifact.

## Verify and report

Run required repository checks and those appropriate to the changed behavior, following the harness's outcome/invariant-based validation. Investigate failures attributable to the change; distinguish unrelated or pre-existing failures with evidence. Record commands/scenarios, outcomes, and unavailable checks without implying that inspection proves execution.

Return a concise implementation report containing implemented behavior against acceptance criteria, exact changed files/review scope, pre-existing edits, deviations with rationale, validation evidence/gaps, and remaining blockers or acceptance risks. Assigned workers return to the parent, who arranges independent review; direct invocation reports the same evidence without inventing an independent review.

For review corrections, reproduce or verify each finding before editing. Fix substantiated in-scope defects, run affected checks, and report resolution per finding. Explain disputes with concrete evidence and keep optional or unrelated improvements separate. Do not launch reviewers or subsequent stages from a worker assignment.
