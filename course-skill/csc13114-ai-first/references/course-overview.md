# AWAD01 / AWAD02 — course baseline

Source: user-provided `CSC13114 Course Introduction (Copy).md`, AWAD01, 17/09/2026, and `CSC13114 Specifications for Agents (Copy).md`, AWAD02, 24/09/2026. Both read in full on 07/10/2026. These are summaries, not the full syllabus or later rubrics.

## What the course teaches

CSC13114 Advanced Web Application Development, 4 credits, 45 theory + 30 lab; semester 1, 2026–2027, CQ2023/3. Instructor Nguyễn Huy Khánh. Technical spine: React/state management, REST and GraphQL, JWT, Docker, cloud/scaling/observability. AI engineering spine: specification, delegation, project rules/MCP/least privilege, validation, LLM evaluation/guardrails/cost/latency, technical defence.

Plan → Implement → Validate → Human Gate. Students brief and check the agent rather than merely accept code. Tests, lint, types and reviews should reveal failure. Gates matter at actions involving money, deletion, production or people; do not interpret the course as permission to perform those actions without the user's actual authorization.

## Project baseline

- Real web application; team of at most three.
- One LLM feature a user relies on, with identifiable cost when wrong.
- Database, authentication and deployability are explicit requirements. “Local-only demo with no authentication” is not a sufficient semester scope, even if the LLM feature is good.
- Course objectives also cover SPA, REST/GraphQL services, containers, cloud and observation. Plan coherent coverage; do not infer that every feature must use every technique or that RAG/streaming/tool calling are all compulsory from a content list alone.
- A call-model-and-print-answer feature without evals, limits and human confirmation does not count as delivered. Place confirmation before a meaningful commitment, not as ritual on every harmless step.
- Git and CI early. AWAD01 asks for a rules file and CI already running before the next session; AWAD02 repeats the CI requirement. At proposal stage, validate the documentation with honest limits; expand to code and security/quality checks as implementation appears.
- High marks favour specs before code, gates that actually blocked a merge, hard eval cases with a threshold and known failure, and students who can explain their own repository. Do not fabricate blocked merges or deliberately weaken checks to obtain a green badge.

## Grading context

Final theory exam 40%; project 40%; exercises/seminar 20%. The individual oral is 15% of course total; with the final exam, 55% is defended in person. Final is closed-book and without AI.

AWAD01 project components: proposal/specification 4%, harness/quality gate 4%, working LLM prototype 7%, evals/guardrails/red-team report on another team 7%, final build 3%, individual oral 15%. These components are not a supplied mapping to CP1–CP6 or dates. AWAD02 corrects PA#1 to proposal/planning without spec. Exercises: at-home AI-allowed/log-required 13%, seminar 7% with another team's red-team critique.

Exam emphasis: concepts 30%, spec critique/harness design 35%, non-determinism and harm/failure controls 35%. Use this for preparation, not assistance during the no-AI exam.

## Precedence and missing sources

AWAD01 says proposal and spec at checkpoint 1. AWAD02 explicitly says no spec in PA#1 and notes syllabus changes; the current PA#1 assignment agrees. Follow the later, specific instruction. IA#1 is separate and individual. Still obtain Classroom syllabus sections 5/7/9, detailed IA#1 rubric/deadline, later milestone rubrics and seminar list before claiming exact compliance with those items.
