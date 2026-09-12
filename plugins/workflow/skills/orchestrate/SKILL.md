---
name: orchestrate
description: Route a request through the workflow team — discovery, planning, implementation, and independent review — and carry it to the requested stopping point. Use for building features or fixes end to end, for "plan this", "review this", or "help me figure out what I want", and for resuming a saved brief or plan. Not for factual questions about code; answer those directly.
---

# Orchestrate

You are the operator's single point of contact. Decide which stage the request needs, run or dispatch that stage, and carry the work through review until the requested stopping point. With subagents available, the implementer edits application code and a separate reviewer assesses it. See Delegation for the fallback when agents are unavailable.

## Roles

| Stage | Who | Where | Procedure |
| --- | --- | --- | --- |
| Discovery | you, with the operator | main conversation | [brainstorm](../brainstorm/SKILL.md) |
| Planning | `workflow-planner` | subagent | [writing-plans](../writing-plans/SKILL.md) |
| Implementation | `workflow-implementer` | subagent | [implement](../implement/SKILL.md) |
| Review | `workflow-reviewer` | subagent | [review](../review/SKILL.md) |

Discovery stays in the main conversation because it is a dialogue with the operator and subagents cannot talk to them. Everything else runs in a subagent so the main conversation stays small and each stage starts from the artifacts, not from chat history.

## Establish the request

Read the request, the project's instructions (AGENTS.md and other applicable instructions), and any brief, plan, branch, or diff it names. Inspect enough of the project to choose a stage; do not ask for what the code can tell you.

Identify two things and hold them across turns:

- **Entry stage.** Where the work starts.
- **Stopping point.** Where the operator wants you to stop. "Plan this" stops after the reviewed plan. "Review this branch" stops after findings. "Build this" includes planning, sign-off, implementation, review, and corrections; do not ask permission again for those steps. "Don't stop for approval" or similar waives the plan sign-off gate.

Routing:

| Request looks like | Entry stage |
| --- | --- |
| No clear goal, competing ideas, "help me think about", or an explicit ask to explore | Discovery |
| Goal is clear enough to design against, but there is no executable plan | Planning |
| A reviewed and approved plan exists, or the change is small and fully settled | Implementation |
| "Review this" — a branch, diff, PR, or plan to assess | Review only |
| A factual question or a lookup | No stage; answer directly |

A small settled change (a typo, a one-line fix with an obvious answer) skips discovery and planning but still goes through the implementer and then the reviewer. Every change and every plan gets an independent review; that is the point of the team.

### Resuming

`Brief: <path>` — read the brief. If its planning handoff names a product question that blocks planning, continue discovery on that question; otherwise go to planning.

`Plan: <path>` — read the plan and its status block. If status is missing, including in plans from the retired workflow-loop plugin, establish it from review evidence and explicit operator approval for the current plan. Default unknown review to `not started` and unknown approval to `pending`; do not infer either from a filename or completed task boxes. Record the status when writing is authorized.

`Review: not started` or `findings pending` means review the plan first, even if it already has approval. `Review: passed` with `Approval: pending` means go to the sign-off gate. Implement only with both `Review: passed` and `Approval: approved` or `waived`, picking up from the progress section if work already started. Do not re-plan work that has an adequate plan.

## Run the stages

### Discovery

Load the brainstorm skill and run it here in the main conversation. It ends with a saved brief. If the stopping point is beyond discovery, hand the brief to planning without a transition question; otherwise report the brief path and stop.

### Planning, then plan review

Dispatch `workflow-planner` with the assignment (see Delegation). It returns the saved plan path, readiness, open questions, and the first task.

If it returns a material product question, check whether the brief, the code, or an earlier decision already answers it; otherwise put it to the operator and, once answered, send the planner back to revise. Routine technical choices are the planner's to make; do not relay those.

Then dispatch `workflow-reviewer` to review the plan against the brief or request and the actual codebase. Findings go back to the planner; set `Review: findings pending` until the reviewer rechecks the revised plan. Repeat while there is progress. When the review passes, set `Review: passed` in the plan's status block.

### Sign-off gate

Honor approval or a waiver already given for this scope; do not ask for it again. Otherwise stop here and ask the operator to approve the reviewed plan. One short message with what they need to decide:

- The plan path.
- Three to six lines: the approach, what is in and out of scope, consequential decisions, open risks.
- The review outcome: how many rounds, and anything the reviewer flagged as a risk rather than a defect.
- How to answer: approve, describe changes, or stop. If they stop, they can resume with `$workflow:orchestrate Plan: <absolute path>`.

On approval, set `Approval: approved` in the status block. On requested changes, set `Review: findings pending` and `Approval: pending`, send the planner back, re-review, and return to the gate. If a waiver still covers the revised scope, retain it and set `Approval: waived` after review instead. Never start implementation on a plan whose status is not approved or waived.

### Implementation, then code review

Dispatch `workflow-implementer` with the plan. It returns an implementation report: changed files, deviations, validation run, remaining work.

Then dispatch `workflow-reviewer` with the report, the plan, and the exact change scope. Review a stable snapshot: implementation is finished before review starts, and nothing else edits those files during the review.

Substantiated in-scope findings go back to the implementer, then the reviewer rechecks the corrections. Optional improvements and out-of-scope observations are reported to the operator, not forced into the loop.

### Review only

Dispatch `workflow-reviewer` with the target and stop with its findings. Do not assign repairs unless the operator asks for them.

## Correction loops

Keep looping while each round makes concrete progress. Stop and go to the operator when:

- A finding needs a product decision or a change to the objective.
- The same finding comes back unchanged after a fix attempt, or the author and reviewer disagree with evidence on both sides. Present both positions; do not pick a side by fiat or keep retrying the same fix.
- The next step needs something unavailable: credentials, a service, an external dependency.

A hard repair or a round count is not a reason to return unfinished work. Never call work complete while a required acceptance criterion is unmet, and never report a clean review when checks could not run.

## Delegation

Resolve this plugin from the path of this loaded `SKILL.md`: its root is two directories above the skill directory. Resolve all linked files there and pass absolute paths in assignments. Do not assume an environment variable or a fixed installation/cache path.

Use the session's available Codex subagent tools. If custom roles are available, select `workflow-planner`, `workflow-implementer`, or `workflow-reviewer` using the tool's supported role selector. Otherwise read the corresponding bundled TOML definition and supply its `developer_instructions` to a general-purpose subagent:

- [workflow-planner](../../agents/workflow-planner.toml), with [writing-plans](../writing-plans/SKILL.md).
- [workflow-implementer](../../agents/workflow-implementer.toml), with [implement](../implement/SKILL.md).
- [workflow-reviewer](../../agents/workflow-reviewer.toml), with [review](../review/SKILL.md).

Always include the resolved stage skill path and ask the worker to read it first; these definitions do not preload skills. Start workers with a fresh context when supported, supplying the assignment and artifacts rather than the full conversation. The reviewer must be separate from the author of the artifact under review.

Each assignment includes:

- Project root and the exact inputs: brief, plan, report, branch, diff, or file list.
- Objective, acceptance criteria, constraints, and explicit non-goals.
- Decisions already made with their status (operator decision, delegated, assumption), and open questions.
- What the agent may change, what to return, and where to save it.
- For review: what the author already validated and what still needs independent verification.

Dispatch one dependent stage at a time. Run agents in parallel only for independent subtasks with disjoint files.

Installing the plugin exposes its skills; companion native roles have a separate optional [installer](../../scripts/install_agents.py). The general-purpose fallback does not require installation. The native reviewer requests a read-only sandbox; a generic worker receiving its instructions does not inherit TOML permission settings, and live parent permissions can override custom role defaults. In every mode explicitly forbid edits to the reviewed files, including through shell commands. Report checks blocked by permissions without loosening those permissions.

If no subagents are available at all, say so and do only the stage work already authorized. Label any review as self-review; it does not satisfy the independent-review requirement. Do not mark `Review: passed`, cross a required independent plan-review gate, or report the full workflow complete on self-review alone. Return the artifact and the missing independent review as remaining work.

## Keep the operator informed

One or two plain sentences at each transition: what just finished, what starts now, who is doing it. When a review sends work back, say what the finding was. Surface changes of direction and blockers as soon as they appear. These are status updates, not approval requests; keep going on authorized work after posting them. Do not narrate subagent internals or predict a result that has not come back.

## Artifacts

Follow the project's existing conventions if it has any. Otherwise:

- Briefs: `docs/briefs/NNN-slug.md`
- Plans: `docs/plans/NNN-slug.md`

`NNN` is the next number across all files in that directory, zero-padded to three digits, starting at `001`. Slugs are short, lowercase, hyphenated. Artifacts belong to the project being worked on, not to this plugin.

Write these artifacts without a separate approval at each transition when the request authorizes the stages that need them. Keep a trivial fix free of a brief and a plan.

## Finishing

At the stopping point, report: what was delivered, the artifact paths, what validation ran and its result, what the reviewer inspected, and any limitations or remaining work. If work stopped early, give the resume command with the artifact's absolute path.
