import json, sys, csv
from notion_client import Client

def load_structure(path="pmp_template.v2.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_pages(notion, parent_id, pages):
    page_ids = {}
    for page in pages:
        new = notion.pages.create(
            parent={"page_id": parent_id},
            properties={"title":[{"type":"text","text":{"content":page["title"]}}]}
        )
        page_ids[page["title"]] = new["id"]
        print(f"Page created: {page['title']}")
    return page_ids

def create_databases(notion, parent_id, dbs):
    db_ids = {}
    for db in dbs:
        props={name:{"type":ptype, ptype:{}} for name, ptype in db["properties"].items()}
        newdb = notion.databases.create(
            parent={"page_id": parent_id},
            title=[{"type":"text","text":{"content":db["name"]}}],
            properties=props
        )
        db_ids[db["name"]] = newdb["id"]
        print(f"Database created: {db['name']}")
    return db_ids

def populate_database(notion, db_id, csv_file):
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            props = {}
            for k,v in row.items():
                if k in ["Course Name","Question","Title"]:
                    props[k] = {"title":[{"type":"text","text":{"content":v}}]}
                elif k == "Duration (h)":
                    props[k] = {"number":float(v)}
                elif k in ["Completed","Reviewed","Visible"]:
                    props[k] = {"checkbox": v.lower() in ["true","1","yes"]}
                elif k in ["Platform","Assigned To","Domain"]:
                    props[k] = {"select":{"name":v}}
                elif k in ["Tags","Tag"]:
                    props[k] = {"multi_select":[{"name":t.strip()} for t in v.split(",") if t.strip()]} 
                else:
                    props[k] = {"rich_text":[{"type":"text","text":{"content":v}}]}
            notion.pages.create(parent={"database_id":db_id}, properties=props)
    print(f"Populated {csv_file}")

def main():
    if "--token" not in sys.argv or "--parent" not in sys.argv:
        print("Usage: python import_template.v2.py --token TOKEN --parent PAGE_ID")
        return
    token = sys.argv[sys.argv.index("--token")+1]
    parent_id = sys.argv[sys.argv.index("--parent")+1]
    notion = Client(auth=token)
    data = load_structure()
    pages = create_pages(notion, parent_id, data["pages"])
    dbs = create_databases(notion, parent_id, data["databases"])
    populate_database(notion, dbs["Course Modules"], "course_modules.v2.csv")
    populate_database(notion, dbs["Flashcards"], "flashcards.v2.csv")
    populate_database(notion, dbs["Snippets"], "snippets.v2.csv")
    print("Import v2 complete!")

if __name__=="__main__":
    main()
