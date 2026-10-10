import os
import subprocess
import re

BASE_DIR = "/home/angsuman/extra_spac/Study_Assam"

def clean_pdf_text_to_markdown(raw_text, title):
    lines = raw_text.split('\n')
    cleaned_lines = []
    
    # Header
    cleaned_lines.append(f"# {title}")
    cleaned_lines.append("")
    cleaned_lines.append("> [!NOTE]")
    cleaned_lines.append(f"> This document is an authentic Markdown extraction of the official PDF: `{os.path.basename(title)}`.")
    cleaned_lines.append("")
    cleaned_lines.append("---")
    cleaned_lines.append("")

    in_content = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append("")
            continue
        
        # Check if line looks like a major heading (e.g. ALL CAPS or numbered)
        if re.match(r'^(SECTION|PART|PAPER|UNIT|MODULE|SYLLABUS|CHAPTER)\s+[IVX0-9]+', stripped, re.IGNORECASE):
            cleaned_lines.append(f"## {stripped}")
        elif re.match(r'^[A-Z\s]{4,}$', stripped) and len(stripped) > 4 and len(stripped) < 60:
            cleaned_lines.append(f"### {stripped.title()}")
        elif re.match(r'^\d+\.\s+[A-Z]', stripped):
            cleaned_lines.append(f"#### {stripped}")
        elif re.match(r'^[a-z]\)\s+', stripped) or re.match(r'^\([a-z0-9]+\)\s+', stripped):
            cleaned_lines.append(f"* {stripped}")
        else:
            cleaned_lines.append(stripped)

    return "\n".join(cleaned_lines)

def process_all_pdfs():
    os.chdir(BASE_DIR)
    pdf_count = 0
    converted_count = 0

    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith(".pdf"):
                pdf_count += 1
                pdf_path = os.path.join(root, f)
                md_filename = f[:-4] + "_EXTRACTED.md"
                md_path = os.path.join(root, md_filename)
                
                title = f.replace("_", " ")[:-4]
                print(f"Extracting: {pdf_path} -> {md_filename}...")
                
                try:
                    res = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True, errors="ignore")
                    if res.returncode == 0 and res.stdout.strip():
                        md_content = clean_pdf_text_to_markdown(res.stdout, title)
                        with open(md_path, "w", encoding="utf-8") as out_f:
                            out_f.write(md_content + "\n")
                        converted_count += 1
                        print(f"  [SUCCESS] Created {md_path} ({len(md_content)} chars)")
                    else:
                        print(f"  [WARN] pdftotext produced empty output for {pdf_path}")
                except Exception as e:
                    print(f"  [ERROR] {e}")

    print(f"\nFinished converting: {converted_count}/{pdf_count} PDFs transformed into full Markdown files!")

if __name__ == "__main__":
    process_all_pdfs()
