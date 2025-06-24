# PMP Command Center Import

This repo provides a JSON structure and a Python script to build the
**PMP Certification Command Center** in your Notion workspace.

## Files

- `pmp_template.json` – defines pages and databases (properties, relations).
- `import_template.py` – reads the JSON and creates pages + databases via Notion API.
- `README.md` – this guide.

## Setup & Execution

1. **Install dependencies**
   ```bash
   pip install notion-client
   ```

2. **Prepare Notion**
   - Create an **Internal Integration** in Notion.
   - Copy the **Internal Integration Token** (keep it secret).
   - Create a blank page named **PMP Import Root**.
   - Go to **Settings → Connections**, find your integration, and **Add to a page** → **PMP Import Root**.

3. **Run the import**
   ```bash
   git clone https://github.com/iRapacheco/pmp-command-center.git
   cd pmp-command-center
   python import_template.py --token YOUR_TOKEN --parent YOUR_PAGE_ID
   ```

4. **Finalize in Notion**
   - Open each database view and set **Filters/Sorts** as needed.
   - Add icons/covers if desired.

## Security

- Keep your token private; do not commit it.
- You can **revoke** the integration after import.
