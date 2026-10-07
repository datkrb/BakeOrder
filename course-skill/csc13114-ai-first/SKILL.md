---
name: csc13114-ai-first
description: Support CSC13114 AI-first web coursework across individual assignments, project milestones, specifications, implementation, evaluation, AI logs, submission reviews, and oral preparation. Use when the task is identified as this course; do not apply its grading or submission rules to unrelated projects.
---

# CSC13114 — AI-first Web

Treat this as web engineering coursework with encouraged, disclosed AI assistance, not just a proposal-writing task. Preserve the current assignment's scope. Respond in Vietnamese unless the user requests otherwise.

## Start from the actual assignment

- Read [references/course-policy.md](references/course-policy.md) for the supplied AI rules and source limitations. Distinguish instructor requirements, student scheduling choices, project assumptions, and recommendations.
- Read [references/course-overview.md](references/course-overview.md) for the project baseline, grading and workflow. For PA#1, read [references/pa1-rubric.md](references/pa1-rubric.md). For IA#1 or feature specifications, read [references/specifications.md](references/specifications.md). Obtain assignment-specific Classroom rubrics when missing; do not extrapolate PA#1's rules to every assignment.
- The user supplied Markdown exports of AWAD01 (17 Sep 2026) and AWAD02 (24 Sep 2026); both have been read. Direct Claude URLs were inaccessible. Cite the exports rather than claiming successful browsing. AWAD02 and the PA#1 assignment explicitly supersede AWAD01's earlier statement that checkpoint 1 needs a spec: PA#1 has no specification. Full syllabus sections 5/7/9, detailed checkpoint dates and later rubrics remain unavailable.
- Six project checkpoints and five project milestones PA#1–PA#5 are distinct counts. Never invent a mapping. Dates provided by the student can be used as planned dates; do not label them instructor-confirmed deadlines.

## Work with AI transparently

- AI use is encouraged in assignments; the final exam is written without it. For ordinary coursework, implement the authorized task and explain material decisions so the student can own the result. For an active final exam, respect the supplied no-AI rule; offer preparation outside the exam instead.
- Keep `AI-LOG.md` with every project milestone PA#1–PA#5. Append concise entries during work using the format in the policy reference. Record actual tools, requested work, retained/changed/rejected output, and human contribution. Heavy use is not a reason to conceal assistance or invent a percentage.
- Never claim AI-written text/code was handwritten. User-provided facts, corrections and decisions are human contributions; identify them precisely. If there was no manual code, say so. Do not fabricate rejections, interviews, tests, reviews or understanding.
- When recovering a missing log from available conversation/commits, say it is a retrospective account and identify the evidence boundary. Do not backdate an entry to look contemporaneous. Later entries should be appended, not silently rewrite earlier history.
- No secrets, real user data or classmates' work in prompts. Use synthetic examples. For an LLM feature inside the product, explicitly describe outbound data, recipient, purpose, minimization, and why the transfer is acceptable. Local storage, model-provider handling and retention are separate questions; do not invent provider guarantees.

## Develop and review at the right stage

- PA#1 is proposal/planning, not implementation or specification. Its semester scope must still include the course baseline: a database, authentication and a deployable web application with a relied-upon LLM feature. The repository needs rules and running CI early; a workflow file alone is not a verified successful run.
- Follow Plan → Implement → Validate → Human Gate. Use meaningful tests, lint, types and review as code exists. Human gates belong at consequential/irreversible actions, not every reversible edit. A read-only document CI at PA#1 is an initial check, not the later full harness or proof that a merge was blocked.
- IA#1 is an individual one-page spec for splitting a table bill in the existing smart-restaurant application, not the BakeOrder core feature. Preserve the silent handoff, actual implementer's question list and revision requirements in the specification reference. Do not invent a question list and present it as peer feedback.
- When writing a feature spec, use the eight supplied sections and cover empty states, partial failures, permissions, concurrency/duplicates and limits. Acceptance criteria must be executable and map to test names. Do not write a spec retroactively and claim it preceded code.
- In plans, identify a named accountable owner and date for each checkpoint. Multiple people can contribute. For team work, assign concrete contributions instead of hiding ownership under “the team”; do not imply a contributor has completed planned work.
- Evaluate the core LLM behavior through wrong answers, harmed users, magnitude/reversibility of harm and observable errors. Human confirmation reduces risk but does not make mistakes cost-free. Label targets and hypothetical costs as such.
- Explain changed behavior, verification actually performed, and limitations. Keep implementation understandable to the student. On request, rehearse oral questions about their code, data flow, model mistakes and tradeoffs; do not claim they understand until demonstrated.

## Submit honestly

- Compare each claim with the current rubric and a real file, section, commit or test. A request to “get 100” means improve the work, not mechanically set every score to maximum. A top-band description is not proof of full points.
- Maintain a short “what we did not manage.” Separate required missing work from future work outside the present milestone. Use the current evidence for self-assessment and explain unresolved scoring uncertainty.
- Check required files, functioning links, dates, team identifiers, totals and ZIP contents. Markdown does not waive page limits; pagination depends on rendering. Do not claim a Markdown file is two pages merely because an older PDF was two pages.
- Reuse the current project and team context from its files rather than hardcoding BakeOrder into this course-wide skill. Do not publish, contact people, or push changes merely because the skill is invoked; use the user's actual authorization.
