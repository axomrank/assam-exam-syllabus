import json
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text[:40]

with open('json/MAster_topics_checklist.json', 'r', encoding='utf-8') as f:
    raw_topics = json.load(f)

processed_topics = []
for idx, item in enumerate(raw_topics):
    domain = item.get("Domain", "").strip()
    subject = item.get("Subject", "").strip()
    topic = item.get("Topic", "").strip()
    subtopic = item.get("Subtopic", "").strip()
    sub_subtopic = item.get("Sub_Subtopic", "").strip()
    study_format = item.get("Study_Format", "").strip()
    era = item.get("Chronology_Era", "").strip()
    assam_specific = item.get("Assam_Specific", "No").strip()

    topic_id = f"t_{idx+1:04d}_{slugify(sub_subtopic or subtopic or topic)}"
    
    processed_topics.append({
        "id": topic_id,
        "index": idx + 1,
        "domain": domain,
        "subject": subject,
        "topic": topic,
        "subtopic": subtopic,
        "subSubtopic": sub_subtopic,
        "studyFormat": study_format,
        "era": era,
        "assamSpecific": assam_specific.lower() == "yes" or "assam" in domain.lower() or "assam" in subject.lower(),
        "searchKey": f"{domain} {subject} {topic} {subtopic} {sub_subtopic}".lower()
    })

import os
os.makedirs("course-maker/src/data", exist_ok=True)
with open("course-maker/src/data/topics.json", "w", encoding="utf-8") as out:
    json.dump(processed_topics, out, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(processed_topics)} indexed topics in course-maker/src/data/topics.json")
