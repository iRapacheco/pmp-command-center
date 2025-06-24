import json, sys
from notion_client import Client

def load_structure(path="pmp_template.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_pages(notion, parent_id, pages):
    for page in pages:
        new = notion.pages.create(
            parent={"page_id": parent_id},
            properties={
                "title": [
                    {"type": "rich_text", "rich_text": {"content": page["title"]}}
                ]
            }
        )
        print(f"Page created: {page['title']} (ID: {new['id']})")

def create_databases(notion, parent_id, dbs):
    for db in dbs:
        props = {}
        for name, ptype in db["properties"].items():
            # Notion uses "rich_text" instead of "text" for database property types
            if ptype == "rich_text":
                ptype = "rich_text"
            # The Notion API expects only the property type key
            props[name] = {ptype: {}}
        newdb = notion.databases.create(
            parent={"page_id": parent_id},
            title=[{"type": "rich_text", "rich_text": {"content": db["name"]}}],
            properties=props
        )
        print(f"Database created: {db['name']} (ID: {newdb['id']})")

def main():
    if "--token" not in sys.argv or "--parent" not in sys.argv:
        print("Usage: python import_template.py --token <TOKEN> --parent <PAGE_ID>")
        sys.exit(1)
    token = sys.argv[sys.argv.index("--token") + 1]
    parent_id = sys.argv[sys.argv.index("--parent") + 1]
    notion = Client(auth=token)
    data = load_structure()
    create_pages(notion, parent_id, data["pages"])
    create_databases(notion, parent_id, data["databases"])
    print("Import complete!")

if __name__ == "__main__":
    main()
