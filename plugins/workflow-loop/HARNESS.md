# Workflow harness

Read this shared contract when entering a Workflow Loop stage; reuse it across handoffs. The main Codex conversation owns dialogue, approvals, routing, and optional consultation. Assigned workers follow their bounded stage and return to the parent; they do not launch stages or ask the operator questions themselves.

## Continuous flow

For exploratory work, use this default sequence in the same conversation:

1. **Discover and propose.** Inspect and discuss until the direction is sufficiently clear. Present a concrete proposed plan in chat: objective, scope and non-goals, approach, major work, acceptance/validation, and material uncertainty. Keep it proportionate; the plan writer supplies execution detail. Ask: “How does this plan look? Reply `y`, `yes`, or `approved` to have the plan writer write and save it, or describe revisions.”
2. **Write the approved plan.** Hand the current proposal, decisions, and evidence to the [plan writer](skills/plan/SKILL.md), using [orchestrate's delegation](skills/orchestrate/SKILL.md#delegate-concrete-work). Approval authorizes the necessary local plan/handoff writes without a separate save question. The writer preserves the approved direction, resolves routine technical details, and returns material contradictions or new product choices to the parent before dependent work.
3. **Check readiness.** Verify the written plan and its links, present a clickable saved path, and ask: “Ready to implement this plan? Reply `y`, `yes`, or `approved` to begin, or describe any final revisions.” This is the final planned revision checkpoint; later user steering remains welcome. Do not present blocked work as ready.
4. **Deliver.** On implementation authorization, implement, validate, independently review, correct substantiated in-scope findings, and recheck them. Continue in the same session until the authorized outcome or an actual blocker is reached.

These are default transitions, not extra gates for work already requested. Explicit build/update/implement requests authorize the necessary planning, validation, review, and corrections; announce and continue those stages without asking for the same authorization again. Explicit requests to write/save a plan authorize that work. A usable existing plan or small settled edit enters at the applicable stage. Never require a new session or a copy-and-paste continuation prompt.

## Approval and scope

Keep one pending concrete checkpoint at a time. An affirmative (`y`, `yes`, `approved`, or equivalent) answers only that checkpoint's stated action and current content. Approval of the proposal authorizes writing it, not a later implementation checkpoint. An answer to a discovery preference or backlog offer does not approve a plan. Clear combined authorization such as “approved, write it and implement” authorizes both stages. An explicit “change X and implement” authorizes that revision and implementation; apply it and continue within that scope.

“Yes, but change X,” rejection, or a revised decision requires incorporating or clarifying the revision and presenting the updated proposal; do not apply stale approval to superseded content. Routine refinements that preserve the objective, required behavior, constraints, and acceptance criteria remain delegated. Material changes to those require the parent's resolution before dependent work, with a new operator decision when not already authorized.

Honor explicit stopping/file boundaries, including brainstorm-only, plan-only, review-only, read-only, and keep-in-chat. Do not push a next-stage question at the requested stopping point. A bare affirmative cannot lift those restrictions; changing them requires an explicit instruction. Keep-in-chat/read-only suppress local artifact writes and migrations. Approval to plan or implement does not authorize unrelated issue creation or external actions.

Maintain only a compact working record: objective/project, stage and stopping point, current proposal/artifact, pending checkpoint and authorization, decisions versus assumptions, blockers, and verification gaps. Preserve authorization across turns and reconstruct context from actual artifacts when resuming. Do not create a separate state file or duplicate documents merely to satisfy this record.

## Optional Claude consultation

When complicated physics or logic is necessary, the main Codex agent consults Claude by default if Claudex is available. Judge complexity by substantive behavior, interacting constraints, or difficult invariants, rather than routine arithmetic or branches. For other tough planning, debugging, design, or review work, use judgment about whether a second approach materially helps. Respect Codex-only instructions.

Discover Claudex through available tools/tool search or the installed skills catalog. Follow available tool usage instructions and read the Claudex skill if present; a callable tool does not require a skill file. Use discovered paths and capabilities; never assume a personal filesystem location or require a dependency installation. Keep the consultation bounded by the actual uncertainty, relevant evidence, and desired critique. Codex evaluates the advice and owns final decisions, integration, and verification.

If the bridge is absent, unavailable, unauthenticated, or limited, briefly disclose the limitation once and continue with Codex. Do not enter installation/authentication retry loops or use automatic API fallback. Consultation adds no approval checkpoint and grants no authorization. Workers flag consultation needs to the parent instead of recursively invoking Claude; include completed consultation findings in handoffs to avoid duplicate calls.

## Quality and communication

Inspect relevant code, repository instructions, tests, and existing plans/issues before asking for facts they can answer. Research consequential unfamiliar or changing facts using available authoritative sources; distinguish observations, source claims, inference, and unresolved checks. For new projects, use available context without inventing a repository requirement.

Explore meaningful alternatives, then keep the simplest approach that satisfies the requirements. Tie plan tasks and verification to observable outcomes. For complicated physics or logic, identify important invariants and failure scenarios and verify them in implementation. Implement in useful increments and verify them. Use focused tests for meaningful behavior/regressions and relevant integration or user-flow checks; avoid tests that mirror implementation details. Report passed, failed, and unrun checks accurately.

The parent announces stage handoffs, consequential findings, repairs, and blockers in concise commentary, and updates at least every 60 seconds during active work or worker waits. Progress announcements do not request approval. At the requested stopping point, report the deliverable, useful artifact links, validation evidence, and material limitations; never imply unmet acceptance criteria or unavailable independent review have passed.
