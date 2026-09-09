---
name: backlog
description: Maintain a repository-local backlog of bugs, improvements, and project work. Use to scaffold a backlog, capture or triage issues, update their status, choose next work, or connect issues to discovery briefs and implementation plans. Do not turn ordinary code exploration into an unsolicited backlog audit.
---

# Backlog

Keep project work in version-controlled Markdown that travels with the repository. Make capture inexpensive and maintenance evidence-based. Tracking an issue or planning its solution does not authorize implementation, commits, publishing, or external issue creation. For cross-stage handoffs, follow the shared [workflow harness](../../HARNESS.md); an affirmative to a backlog offer applies only to that offer.

## Find the existing workflow

Read applicable repository instructions and locate the project root, existing backlog, issue conventions, and relevant plans before asking questions or writing files. Inspect the code and documentation needed to understand the requested item; avoid a full audit for a quick capture request. Reuse established paths, identifiers, fields, and statuses. Do not create a second competing backlog or migrate an existing one without a request. If multiple trackers exist, use the one applicable to the work; ask only when the ambiguity cannot be resolved from context.

When no local backlog exists, default to `docs/backlog.md` relative to the project root. A request to initialize a backlog or add an item authorizes creating this file and its parent directory. A read-only request to list or inspect an absent backlog should report its absence. Do not invent issues to populate an empty scaffold.

## Default Markdown format

Use this format only for a new backlog. Keep a short format legend at the top and one section per issue; the issue sections are the source of truth, so a separately maintained index is unnecessary.

```markdown
# Project backlog

Statuses: open, in-progress, blocked, done, dropped.
Priority: untriaged, high, medium, low.
IDs are stable and never reused.
Plans use docs/plans/{nnn}-{SLUG}.md, numbered 001, 002, 003, ... across all slugs.

## BL-001: Concise issue title

- Type: bug | improvement | task | investigation
- Status: open
- Priority: untriaged
- Evidence: reported | suspected | confirmed

### Problem and impact
Describe the current behavior or need, who it affects, and the intended outcome.

### Evidence and context
Record the report or observation, relevant file references, and reproduction steps when known. Distinguish observed facts from hypotheses and note material unknowns.

### Acceptance criteria
- An observable outcome that would resolve the issue; mark provisional criteria explicitly.

### Links and dependencies
Link related issues and saved plans using relative Markdown links. Omit this section if empty.
```

For an empty scaffold, include only the title and legend, without the example issue. Choose one value for each field when capturing an item. Keep quick entries short; missing reproduction details or a settled solution need not block capture. Label unknowns instead of filling them with guesses. Use `investigation` for an unresolved concern when a bug has not been established.

Allocate the next unused `BL-NNN` identifier above all existing IDs, including closed items; use at least three digits and never renumber existing entries. Preserve closed entries and links. If the repository archives items, include its archives when checking identifiers and duplicates.

## Capture and maintain

For a direct request such as “add this bug,” inspect the relevant context, search existing items by behavior and affected area, then write the entry without another approval round. If the same issue exists, add useful evidence or links to that item and report its ID. Keep distinct causes or independently actionable work separate, with links where useful. Do not reopen a closed item without evidence that the issue remains or has returned.

Default new items to `open` and `untriaged` unless the operator or repository provides a priority. When asked to prioritize, use impact, urgency, dependencies, and available evidence, explaining consequential choices. Avoid invented deadlines, owners, estimates, and claims of confirmation.

When asked to maintain or reconcile the backlog, inspect relevant code, tests, and plans, then update entries supported by that evidence. Record why a status changed. `in-progress` requires work to have actually started; a saved plan alone leaves the item open. `blocked` needs a named dependency or unresolved decision. `done` requires evidence that the acceptance criteria are met, or an explicit operator report recorded as such. Preserve the reason for `dropped` work rather than deleting its history. Do not silently mark stale issues complete.

For “what next,” summarize actionable open work with IDs, priorities, blockers, and a supported recommendation. Do not begin implementation merely because an item is recommended.

Before finishing a write, review the diff or reread the affected content: check IDs, duplicate entries, valid fields, relative links, and preservation of unrelated edits. Report changed IDs and link the backlog. Markdown maintenance generally needs no application test run; verify behavior when making new claims about whether an issue is resolved.

## Findings during exploration

When exploration reveals useful out-of-scope work, prepare a concise candidate with the affected behavior, impact, evidence, and any uncertainty. Offer to record it at a natural stopping point; batch related findings into one offer. Do not interrupt the primary task with a separate questionnaire or record every speculative concern.

Write incidental findings only when the operator accepts the offer or has already authorized capturing findings for this work. Honor that authorization without repeatedly asking. Search for duplicates before adding accepted candidates, and preserve suspected versus confirmed status. This skill supplies a workflow when loaded; it does not install a background watcher or guarantee capture in unrelated sessions.

## Work with discovery and planning

Use the companion [brainstorm](../brainstorm/SKILL.md) skill when the operator wants to explore an item whose direction is unsettled, and [plan](../plan/SKILL.md) when a sufficiently clear direction needs an executable plan. Load only the needed companion. Pass the issue ID, evidence, constraints, and related artifacts into that workflow. Simple issue capture and status updates do not require brainstorming or planning. If a companion is unavailable, continue backlog maintenance and report that limitation only when the requested handoff needs it.

When discovery or planning starts from a backlog item, include its ID and a link in the resulting brief or plan. Keep the issue as the concise record of the problem and status, the discovery brief as the rationale and decisions, and the plan as the detailed implementation approach. After an authorized artifact save, link it from the originating issue; writing a brief or plan alone does not change issue status. Resolve relative links from each containing file, so a brief under `docs/briefs/` or plan under `docs/plans/` links to `../backlog.md#bl-001-concise-issue-title`, and the backlog links to `briefs/<brief-file>.md` or `plans/<plan-file>.md`.

For authorized plan saving or maintenance, apply [plan's naming and migration rules](../plan/SKILL.md#save-and-hand-off) to existing plans too. Update affected backlog links to the resulting paths and verify them; read-only backlog work does not rename plans.

If discovery or planning reveals additional work, offer to capture it using the findings workflow. Saving a brief or plan does not by itself authorize creating new backlog entries. Do not automatically convert every implementation step into an issue; capture independently trackable outcomes at the operator's requested level of detail.
