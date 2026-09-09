---
name: orchestrate
description: Coordinate discovery, planning, implementation, and independent review with continuous handoffs. Use for end-to-end delivery, resuming work, or choosing the applicable stage; honor explicit stage requests and keep small settled edits light.
---

# Orchestrate

Be the operator's continuous point of contact. Read the shared [workflow harness](../../HARNESS.md) and own its checkpoints, authorization record, progress updates, and optional Claude consultation. Keep brainstorming in the main conversation; this skill explicitly requests separate planning, implementation, and independent review workers when those stages apply.

## Route by intent and evidence

Read the conversation, applicable project instructions, and supplied artifacts/changes; inspect enough current evidence to choose the next stage and requested stopping point.

| Situation | Stage |
| --- | --- |
| Uncertain goals, competing ideas, or requested exploration | [Brainstorm](../brainstorm/SKILL.md), in the main conversation |
| Approved proposal or clear requirements need an executable approach | [Plan](../plan/SKILL.md), delegated to `planner` |
| Authorized implementation with an actionable plan or settled requirements | [Implement](../implement/SKILL.md), delegated to `implementer` |
| Existing changes need assessment or implementation is ready to check | [Review](../review/SKILL.md), delegated to an independent `reviewer` |

Enter where the task belongs. A review request needs no new plan; a usable plan needs no rewrite; a small settled edit needs no manufactured discovery brief or formal plan. For a build with material ambiguity, inspect and resolve the focused uncertainty before dependent work, using longer brainstorming only when warranted. Honor open-ended exploration and stopping instructions through the harness.

Load only the relevant stage skill. The parent's proposal presentation and approval precede writing an exploratory plan, following the harness; existing authorization can already cover the handoff. After approval, invoke the plan writer automatically. After verifying its saved plan, present the path and readiness/revision checkpoint or continue already-authorized implementation. The operator need not invoke another skill or start a new session.

## Delegate concrete work

Resolve stage links within this plugin and pass exact installed paths, even when similarly named standalone skills exist. Read the relevant bundled definition: [planner](../../agents/planner.toml), [implementer](../../agents/implementer.toml), or [reviewer](../../agents/reviewer.toml). Use the named custom role when available, supplying its instructions and stage path.

If only generic subagents are available, provide the bundled definition's `developer_instructions`, exact stage path, and bounded assignment to a generic worker. This needs no role installation. The optional [setup helper](../../scripts/install_agents.py) supports native role selection; see [companion agents](../../README.md#companion-agents). Do not invent role-selection parameters or claim configuration was enforced when only instructions were supplied. Inherit model/reasoning settings unless applicable instructions specify others.

When delegation is unavailable, disclose it and work sequentially where feasible. Another available independent reviewer/tool, including Claude review, may satisfy independent review only when actually assigned the stable changes and requirements and able to assess the required scope. Consultation or self-review alone does not satisfy it. Label review by the implementing agent as self-review, record remaining coverage gaps, and leave an explicit independent-review requirement unmet when no qualifying review is available.

Each assignment supplies project root, exact inputs/change scope, objective/acceptance criteria, constraints/non-goals, decisions versus assumptions, blockers, allowed edits, requested output, and existing/missing validation evidence. Include useful consultation results. Tell workers to read their stage skill, the shared harness, and applicable project instructions, then return the deliverable or blocker to the parent without launching stages or consulting Claude recursively.

Delegate one dependent stage at a time; parallelize only concrete independent work with disjoint ownership. Keep the main thread available for steering. Agents share the workspace: finish edits and establish a stable review scope before assigning review.

## Preserve handoffs

Use the harness's compact working record. Handoffs must stand alone without worker memory: discovery preserves rationale/evidence/uncertainty; plans specify executable tasks and checks; implementation reports identify actual changes, deviations, and validation; reviews substantiate findings and limits. Recheck consequential claims against current files.

Save only artifacts needed for authorized work, respecting keep-in-chat. Follow [plan's naming and migration rules](../plan/SKILL.md#save-and-hand-off), carrying resulting paths through handoffs. Use [brainstorm's brief conventions](../brainstorm/SKILL.md#converge-and-hand-off) when a separate brief is useful. Maintain existing artifacts instead of adding duplicate status documents.

Return a planner's material question or changed proposal to the operator after checking existing evidence/decisions; routine implementation details remain delegated. Revise affected artifacts and authorization state before dependent work. Progress updates remain in the parent conversation, including while workers are running.

## Review and correct

After implementation, give a separate reviewer the requirements, actual stable changes, plan when present, and implementation report. For review-only work, return findings and stop. For an authorized implementation workflow, send substantiated in-scope findings to the implementer, then have the reviewer verify corrections and affected behavior. Keep optional preferences and unrelated improvements separate.

Continue while corrections make concrete progress. If a finding recurs without progress, reassess reproduction, disagreement, and repair approach rather than repeating the same attempt. Pause dependent work only for a real unresolved decision or unavailable dependency, explaining the evidence and needed input; continue independent authorized work. Difficulty or an arbitrary retry count is not a completion condition.

At the requested stopping point, provide the deliverable, artifact links, actual checks/results, and remaining limitations. Report incomplete acceptance or review honestly; do not use a handoff to stop short of already-authorized delivery.
