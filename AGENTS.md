# CSC13114 — repository guidance

For work on this course, read `course-skill/csc13114-ai-first/SKILL.md` and the reference relevant to the current assignment. This is AI-first web coursework, not a blanket instruction to build features at every milestone.

Maintain `AI-LOG.md` honestly as work happens and include it with every project milestone PA#1–PA#5. Do not claim inaccessible course documents were read. The current repository is at proposal stage; six planned checkpoints are not assumed to map to five PA milestones. The names and planned dates in project files are project context, not universal course rules.

The supplied AWAD01 and AWAD02 Markdown exports have now been read. Use AWAD02/current PA#1 instructions over the older AWAD01 “spec at checkpoint 1” wording. Semester scope includes authentication, database, deployability and a controlled LLM feature. IA#1 is individual smart-restaurant bill splitting, not BakeOrder.

Run `python scripts/check_submission.py` before committing PA#1 document changes. CI is a document check at this stage; it is not an application test suite or a protected-branch merge gate. Do not claim later harness requirements are complete. Write the core feature spec before implementation, then map acceptance criteria to tests. Human confirmation belongs before an order is committed for production; ordinary read-only checks and reversible editing do not need ritual approval.
