import os
import json

def update_catalog_with_pdfs():
    with open("metadata_catalog.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Walk through folders and attach official_pdfs list
    for cat in data["categories"]:
        for exam in cat["exams"]:
            folder = exam.get("folder")
            if folder and os.path.isdir(folder):
                pdfs = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".pdf")]
                exam["official_pdfs"] = sorted(pdfs)

    with open("metadata_catalog.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("metadata_catalog.json updated with official PDF references.")

update_catalog_with_pdfs()
