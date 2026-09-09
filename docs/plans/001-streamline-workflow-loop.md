# Streamline Workflow Loop

Status: Complete. The operator explicitly requested this plugin update; implementation, validation, review, and in-scope corrections are authorized.

## Objective and current state

Make Workflow Loop a continuous, lightweight conversation: grounded discovery, a concrete proposed plan, simple approval, a dedicated plan writer, an implementation/revision checkpoint, then implementation and independent review. Preserve flexible entry points and explicit stopping instructions.

Project root: `/home/astrosteveo/Projects/codex-plugins`. Scope is the source package at [`plugins/workflow-loop`](../../plugins/workflow-loop/README.md). It contains six stage/backlog skills, six UI metadata files, three bundled worker definitions, a plugin manifest, and an optional role installer. The source brainstorm, plan, orchestrate, and README currently require or describe new-session handoffs; brainstorm and plan also offer to save completed work. Stage guidance repeats transition and artifact policy. No existing project plans or Git metadata were found during inspection.

## Requirements and boundaries

- Default discovery remains interactive in the main conversation and inspects relevant repository evidence before asking questions. It may be explicitly selected or chosen by Codex when the request warrants it.
- Once direction is sufficiently clear, present a concrete proposed plan in chat with scope, approach, meaningful acceptance/validation, and material uncertainty. Ask how it looks and whether the operator approves it; explain that `y`, `yes`, or `approved` approves the presented proposal.
- Approval hands the proposal and evidence to the plan writer to produce and save a faithful detailed plan, without a separate save prompt. Product questions or material changes discovered during writing return to the parent before dependent work; ordinary technical details are delegated.
- After verifying the saved plan, provide its clickable path and ask whether the operator is ready for implementation or wants revisions. Continue in the same session after approval. This is the final planned revision checkpoint, not a prohibition on later steering.
- A bare affirmative applies only to the latest pending concrete question and current proposal content, not merely its filename. It cannot silently approve both planning and implementation, a superseded proposal, an unrelated backlog offer, conditional revisions, or an override of explicit stop-only instructions. Clear combined authorization such as “approved, write it and implement” is honored.
- Preserve explicit brainstorm-only, plan-only, review-only, read-only, keep-in-chat, and Codex-only instructions. Preserve earlier implementation authorization: build/update requests carry necessary planning and review without inserting redundant permission gates. Existing usable plans and small settled edits enter at the appropriate stage.
- Complicated physics or logic triggers a Claude consultation by default when Claudex is available; other difficult work uses Codex's judgment. Discover the available tool or skill through the environment, without hard-coded personal paths, a required dependency, installation/authentication loops, or automatic API fallback. Codex owns decisions, integration, and verification; unavailable or limited Claude is briefly disclosed and work continues with Codex. Stage workers request consultation through the parent rather than starting nested consultations.
- Keep one compact shared workflow harness for transitions, authorization state, collaboration, and common quality expectations; reference it from relevant stages. Retain the six skills and three roles, local artifact conventions, authorized legacy-plan migration, backlog boundaries, progress updates, evidence-based implementation, and independent review/correction loop.
- Edit source package files only, apart from maintaining this plan. Do not modify installed caches, personal skills, or user configuration. No application code, new plugin dependency, forced-session mechanism, or elaborate workflow runtime is needed.

## Approach and implementation sequence

1. **Create the shared harness.** Add a concise package-relative Markdown reference, for example `references/workflow.md`, defining the default discovery-to-approval-to-writing-to-readiness flow and its explicit stopping/authorization exceptions. Maintain only the necessary working state: scope/stopping point, current proposal or artifact, pending question, approval/revision status, and verification gaps. Include portable, parent-owned Claudex policy and proportionate exploration, research, and validation expectations.
2. **Align the stage instructions.** Update brainstorm convergence and handoff to the proposal/approval experience. Update plan to own the faithful detailed artifact and preserve its `save-and-hand-off` anchor and naming/migration rules. Update orchestrate routing and delegation to consume the shared flow, removing new-session and redundant save transitions. Link implement/review to applicable shared guidance without expanding their procedures unnecessarily. Adjust backlog references only where obsolete handoff language or links require it. Keep user dialogue in the parent and stage workers bounded.
3. **Align packaging and documentation.** Update relevant worker instructions and skill UI metadata when their descriptions conflict with the new behavior. Revise the README flow/examples to explain simple approvals, revisions, same-session continuation, authorized-build exceptions, and optional Claudex. Preserve the `0.1.0` version base and use the available plugin-creator `update_plugin_cachebuster.py` helper after manifest edits, keeping marketplace identity stable and retaining the supported manifest shape. Preserve installation-related restart instructions where still applicable; remove only workflow-mandated session breaks. Prefer deleting duplicated prose over adding new layers.
4. **Validate and review.** Compare changed files with the parent's recorded source snapshot because Git is unavailable. Run package and all six skill validators, parse metadata/roles, verify internal links and anchors, and audit the transition scenarios below against the actual final instructions. Send the stable changed-file scope, scenario results, and any limitations to an independent reviewer. Correct substantiated in-scope findings and recheck affected behavior.

First actionable task: inspect the source snapshot and add the shared harness, then wire its two approval transitions into brainstorm, plan, and orchestrate before updating surrounding documentation.

Parallel ownership: the implementer owns the shared harness, six skill instructions, and three role definitions; the parent owns README/documentation, skill UI metadata, plugin manifest/cachebuster, and packaging verification. Keep edits disjoint until integration.

## Acceptance and validation

Package validation uses the available system `plugin-creator/scripts/validate_plugin.py` against `plugins/workflow-loop`; skill validation uses `skill-creator/scripts/quick_validate.py` against each of the six skill directories. Their current installation root is `/home/astrosteveo/.codex/skills/.system`. Parse `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, all role TOMLs, and all skill YAML metadata/frontmatter. Check relative Markdown links and changed heading anchors. Count instruction words before/after and record whether the shared harness reduces the combined instruction surface; the parent's baseline is 7,516 words across the six skill files and 8,683 including README/roles. These are instruction/package checks, not proof of live model compliance.

Audit these concrete scenarios, recording the expected next action and any contradiction found:

| Input or situation | Required result |
| --- | --- |
| Implicit or explicit brainstorm reaches a clear proposal; operator says `y` | Plan writer saves that proposal's detailed plan; parent presents saved link and the implementation/revision checkpoint. No implementation yet. |
| Operator answers that checkpoint with `yes` or `approved` | Implement, validate, independently review, and correct within scope in the same session. |
| Operator replies “yes, but change X,” revisits a decision, or rejects the proposal | Apply/clarify the revision and present the changed scope; do not reuse the superseded approval. |
| A bare `yes` follows a discovery preference or incidental backlog question | Answer that question only; no implicit future-stage approval. |
| “Approved, write it and implement” or earlier explicit build/update authorization | Carry the authorized sequence forward; do not add redundant approval or save questions. |
| “Brainstorm only,” “plan only,” “review only,” or “keep it in chat” | Honor the stopping point and file-write boundary, with no forced next-stage question or implementation. |
| Direct plan request, existing approved plan, trivial settled fix, or review-only entry | Route at the applicable stage; no artificial discovery, rewrite, or full workflow. |
| Planner discovers a material contradiction or new product choice | Parent resolves the issue before dependent writing/implementation; ordinary technical decisions stay with the planner. |
| Complex physics/logic with Claudex available | Parent requests a bounded consultation and evaluates its findings; workers do not recursively consult. |
| Claudex absent, authentication unavailable, or quota exhausted | Briefly report limitation and continue with Codex, with no install/authentication/API fallback loop. |
| Codex-only instruction; routine task; independently reviewable tough task | Respect Codex-only; avoid automatic consultation for routine work; use discretion where consultation helps. |
| Review needs corrections; legacy plan is maintained; no generic workers exist | Preserve evidence/correction and migration rules; disclose unavailable delegation and distinguish self-review from independent review. |

No material product blocker remains. Routine wording, reference filename, and concise metadata choices are delegated. Actual model behavior across clients and a real Claude-unavailable environment remain outside static validation; report those limits accurately.

## Progress and evidence

- [x] Shared harness and approval semantics implemented.
- [x] Stage, role, and documentation integration completed.
- [x] Package, skill, metadata, link, and scenario checks passed.
- [x] Independent review completed and required corrections verified.

Deviations: The shared contract is `plugins/workflow-loop/HARNESS.md`. Scenario review prompted three compact clarifications: direct plan invocation authorizes saving, callable Claudex tools need no skill file, and an alternative independent reviewer must actually assess the stable changes and required scope. No runtime service, new dependency, or installation/configuration change was added.

Validation evidence:

- Plugin packaging validator and all six skill validators passed. JSON, role TOMLs, and skill YAML parsed; implicit invocation remains enabled and no Claude app/tool dependency is declared.
- All 42 local Markdown links and anchors across the workspace passed. A relocated package copy retained valid references; the optional role installer passed dry-run, install, and idempotence checks with the final role definitions in a temporary directory.
- The instruction surface, including all six skills, three roles, and the shared harness, decreased from 7,912 to 5,777 words (27.0%). Package version preserves `0.1.0` and uses the helper-generated cachebuster `0.1.0+codex.20260909225041`.
- Claude completed a focused transition consultation. A separate Codex reviewer compared all 16 changed/new source files with the initial snapshot and found no actionable defects. An independent 14-scenario dry run identified the three wording edges above; the reviewer rechecked those clarifications and surrounding transitions with no new findings. Affected skill and workspace-link checks passed after clarification.
- Evidence artifacts: baseline `/tmp/workflow-loop-before-0lggukab`, final source comparison `/tmp/workflow-loop-source.patch`, and scenario interpretations `/tmp/workflow-loop-scenarios.md`. Temporary evidence is supplementary; requirements, decisions, and results are preserved here.

Validation limits: These were package checks, instruction/diff reviews, and interpreted scenario dry runs, not live multi-turn model-compliance tests. Unavailable-Claude/subagent conditions were assessed from instructions rather than reproduced in the runtime. The source package was updated; cached installations, personal skills, and user configuration were not changed.
