import os
import csv
import json
import re

BASE_DIR = "/home/angsuman/extra_spac/Study_Assam"

def generate_perfect_curated_and_granular_csv():
    os.chdir(BASE_DIR)
    
    # Import the structured rows
    from compile_syllabus_csv import extract_rows_from_all_syllabi
    curated_rows = extract_rows_from_all_syllabi()

    fieldnames = [
        "Category_ID",
        "Category_Name",
        "Exam_Name",
        "Stage",
        "Paper_Name",
        "Subject",
        "Topic",
        "Subtopics",
        "Standard_Marks_Weightage",
        "Source_File"
    ]

    csv_path = "master_assam_exams_syllabus.csv"
    json_path = "master_assam_exams_syllabus.json"

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for r in curated_rows:
            writer.writerow(r)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(curated_rows, f, indent=2, ensure_ascii=False)

    print(f"Generated clean CSV: {csv_path} with {len(curated_rows)} high-precision rows.")
    print(f"Generated clean JSON: {json_path}")

if __name__ == "__main__":
    generate_perfect_curated_and_granular_csv()
