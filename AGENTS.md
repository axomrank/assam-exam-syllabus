# Working on assam-exam-syllabus

Syllabi, exam patterns and official documents for Assam recruitment boards. Part of AxomRank: see README.md for the overview and roadmap.

## Layout

- `01_APSC/` … `12_Legislative_Assembly_Secretariat/`: one folder per board, with `SYLLABUS.md`, `EXAM_PATTERN.md` and the official PDFs
- `csv/`, `json/`: master datasets. `scripts/`: their generators
- `Diagrams/`: taxonomy diagrams

## Commands

- `python3 scripts/generate_checklist_csv.py`
- `python3 scripts/compile_syllabus_csv.py`

## Rules

- Mark any syllabus not copied from an official notice as a summary, and give its source URL and date
- Use relative links only. Never use `file:///` paths
- Regenerate the CSV and JSON with the scripts. Do not edit them by hand
- Commit as the `axomrank` account, in small reviewable commits.
