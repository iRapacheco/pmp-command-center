# PMP Command Center Import v2

This repo provides updated JSON and script for version 2 of the
**PMP Certification Command Center** setup in Notion, including seed data.

## Files
- `pmp_template.v2.json`
- `import_template.v2.py`
- `course_modules.v2.csv`
- `flashcards.v2.csv`
- `snippets.v2.csv`
- `README.v2.md`

## Setup & Run
1. `pip install notion-client`
2. Create Internal Integration; copy token.
3. Create 'PMP Import Root' page; share to integration.
4. Run:
   ```bash
   python import_template.v2.py --token YOUR_TOKEN --parent YOUR_PAGE_ID
   ```

## Finalize
- Adjust Filters/Sorts on views.
- Add icons/covers if desired.
