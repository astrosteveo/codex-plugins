---
name: review
description: Independently review actual changes for correctness, regressions, and validation gaps, including rechecking fixes. Return substantiated findings; do not edit implementation during review-only work.
---

# Review

Assess delivered behavior against requirements and the actual system. Follow the shared [workflow harness](../../HARNESS.md) for scope, optional consultation, and parent-owned transitions. An implementation report is evidence to check, not the conclusion. Do not edit source or change requirements to fit the result; tests may create ordinary local build/temporary artifacts within the task's permissions.

## Establish the review scope

Read the request, repository instructions, requirements/plan, and implementation report. Identify the exact branch, diff, commit range, or changed files and distinguish pre-existing changes using the supplied baseline. A review without a plan uses the request and established behavior; it needs no artificial planning stage.

Inspect changes and surrounding execution paths, including relevant callers, configuration, tests, and documentation. If edits are still in progress, have the parent establish a stable snapshot. Recheck substantive claims against current files. Route material questions and needs for Claude consultation to the parent when delegated.

## Find consequential failures

Prioritize incorrect or missing required behavior, regressions, and inadequate verification of consequential changes. Examine security, data integrity, concurrency, accessibility, or performance when the actual use case makes them relevant; avoid a generic full-system audit.

Trace concrete triggers and failure paths. Reproduce suspected defects or run focused checks when feasible. Compare tests with acceptance criteria, important invariants, and realistic edge cases. Reuse reliable check results where appropriate while independently examining the code and consequential claims; a passing build or large test count does not prove behavioral coverage.

Separate confirmed defects, supported risks needing verification, optional improvements, and style preferences. Report evidence-backed findings without manufacturing issues. Missing optional polish is not a blocker unless required.

## Return findings and limits

For each material finding, give priority/impact, file and line or symbol, trigger, failure path or reproduction evidence, violated requirement when applicable, and uncertainty or the check needed to resolve it. A remedy may help; implementation remains with the implementer.

Lead with actionable findings ordered by impact, then inspected scope, checks run or reused, and material gaps. If none remain, say so with the limits of that conclusion; do not claim defect-free work. Insufficient evidence yields an incomplete review identifying what is missing.

On re-review, verify each correction and affected behavior; mark findings resolved, unresolved, or disputed with evidence. An implementer's claim alone does not close a finding. Return to the parent without editing, dispatching fixes, creating issues, or launching stages. Direct review-only work stops with findings. If you implemented the changes yourself, label the result self-review.
