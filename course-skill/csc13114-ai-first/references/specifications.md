# AWAD02 — specifications and IA#1

Source: complete user-supplied Markdown text `CSC13114 Specifications for Agents (Copy).md`, session 02, 24/09/2026; template on slide 11 and IA#1 instructions on slides 18–21. Missing diagrams in the export are not inferred.

## Feature-spec template

```md
# Feature name
Status: draft · Owner: named person · Feature of: application

## Goal
One sentence.
## Out of scope
Explicit non-goals.
## Flow
Numbered happy-path steps.
## Contract
Endpoints, payloads, status codes and relevant events.
## Data
Tables/fields changed and invariants.
## Errors
Condition → what the user sees → what the system does.
## Acceptance
AC1..ACn, runnable with observable outcomes.
## Constraints
Actual dependency, schema, budget, deadline and compatibility limits.
```

The sample's “no new dependencies” is an example constraint, not a universal rule for all student projects. Specify actual constraints. A user story states who/what/why; it does not replace a contract, data invariants or failure behaviour.

Review five common gaps: empty/first-run states, partial failure, permissions/ownership, concurrency/duplicates, and limits with behaviour when exceeded. Avoid acceptance criteria such as “works correctly.” State inputs, outputs/status, effects and invariants. Map AC identifiers one-to-one into test names when implementing; criteria remain the student's responsibility even if AI writes tests.

## IA#1 requirements known from slides

- Individual, not team work; 3% of course. One-page spec for **splitting the bill at a table in smart-restaurant**, the existing application.
- One open order with several VAT-inclusive priced items; customers pay separately on their phones. Kitchen unaffected; order stays open until every share is paid.
- Same feature for everyone. Do not substitute the semester project's LLM feature.
- Actual deadline and detailed rubric are attached on Classroom and are not in these exports.
- In the next lab, swap specs. The receiving student implements with an assistant using only the written spec. They may not ask the author; they write down questions instead. In that silent handoff, record ambiguities rather than asking the author or secretly relying on their intended answer.
- The author receives that actual question list and revises the spec. Hand in original spec, received question list, revised spec and `SELF_ASSESSMENT_REPORT.md` as `StudentID_total.zip`. Twenty of 100 points come from the question list; remaining allocation is not supplied.
- A self-review or AI-simulated critique can help preparation but must be labelled; it is not the received peer question list. Do not fabricate peer feedback or submit another student's work beyond the explicitly required, authorized handoff material. Do not place classmates' work into AI prompts contrary to the course policy; clarify the permitted handoff usage if needed.

## Bill-splitting cases to settle before code

Rounding when 400000 VND is split three ways; who pays remainder while preserving sum. Who is permitted to split. What happens if an item is added after a share is paid. Two concurrent payments for one share and idempotency. Discounts/VAT order. Failure of one payment while others remain paid. Do not assume refunds or item-based splitting are in scope without specifying that decision.

The slide's sample contract demonstrates concrete 201/409/422 responses and an idempotency key; treat it as a worked example, not a claim that all valid solutions require exactly that route/schema.
