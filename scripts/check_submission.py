"""Check PA1 document consistency, not writing quality or an earned grade."""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
errors = []
required = ["PROPOSAL.md", "SELF_ASSESSMENT_REPORT.md", "AI-LOG.md", "README.md", "AGENTS.md"]
docs = {}
for name in required:
    path = root / name
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"Missing or empty required file: {name}")
    else:
        docs[name] = path.read_text(encoding="utf-8")

report = docs.get("SELF_ASSESSMENT_REPORT.md", "")
rows = []
for line in report.splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) == 5 and cells[0].isdigit():
        try:
            index, maximum, claimed = int(cells[0]), int(cells[2]), int(cells[3])
        except ValueError:
            errors.append("Non-numeric rubric mark")
            continue
        rows.append((index, maximum, claimed))
        if not 0 <= claimed <= maximum or not cells[4]:
            errors.append(f"Invalid mark or missing evidence in criterion {index}")
if [(r[0], r[1]) for r in rows] != list(enumerate([20, 25, 15, 20, 10, 10], 1)):
    errors.append("Expected all six PA1 criteria with their rubric maximums")
total = sum(r[2] for r in rows)
if not re.search(rf"\|\s*\*\*100\*\*\s*\|\s*\*\*{total}\*\*\s*\|", report):
    errors.append("Self-assessment total does not match criterion marks")

ids = sorted(set(re.findall(r"\b23120\d{3}\b", docs.get("PROPOSAL.md", ""))))
if len(ids) != 3:
    errors.append("Expected the three BakeOrder student IDs")
expected_zip = "-".join(ids) + f"_{total}.zip"
for name in ["README.md", "SELF_ASSESSMENT_REPORT.md"]:
    names = re.findall(r"\b\d{8}(?:-\d{8}){0,2}_\d+\.zip\b", docs.get(name, ""))
    if not names or any(n != expected_zip for n in names):
        errors.append(f"Inconsistent ZIP name in {name}: expected {expected_zip}")

log = docs.get("AI-LOG.md", "")
entries = re.split(r"(?m)^## ", log)[1:]
if not entries:
    errors.append("AI-LOG has no dated entries")
for entry in entries:
    if not re.match(r"\d{4}-\d{2}-\d{2} — ", entry):
        errors.append("AI-LOG entry needs a date and work description")
    for field in ["Tool", "Asked for", "Kept", "Changed", "Rejected", "By hand"]:
        if not re.search(rf"(?m)^{re.escape(field)}:\s*\S", entry):
            errors.append(f"AI-LOG entry missing {field}")

for name, text in docs.items():
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
            continue
        target = link.split("#", 1)[0]
        if target and not (root / target).exists():
            errors.append(f"Broken local link in {name}: {target}")

if errors:
    print("\n".join(f"FAIL: {error}" for error in errors))
    sys.exit(1)
print(f"PASS: required documents, rubric arithmetic ({total}/100), ZIP names, AI-log fields and local links")
print("Not checked: page count, earned marks, factual evidence, official dates, application behaviour or merge protection")
