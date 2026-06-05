import pypdf
import os
import re

pdf_path = "academic_rules.pdf"

if not os.path.exists(pdf_path):
    print("PDF file not found.")
    exit(1)

print(f"Opening {pdf_path}...")
reader = pypdf.PdfReader(pdf_path)
num_pages = len(reader.pages)
print(f"Total pages: {num_pages}")

keywords = ["attendance", "cie", "continuous internal evaluation", "eligibility", "condonation", "minimum", "cie marks", "marks distribution"]
found_pages = {}

for page_num in range(num_pages):
    page = reader.pages[page_num]
    text = page.extract_text()
    text_lower = text.lower()
    
    matched = []
    for kw in keywords:
        if kw in text_lower:
            matched.append(kw)
            
    if matched:
        found_pages[page_num + 1] = {
            "keywords": matched,
            "text": text
        }

print(f"Keywords found in {len(found_pages)} pages.")

# Write results to a file
with open("extracted_academic_info.txt", "w", encoding="utf-8") as f:
    for page_num, data in found_pages.items():
        f.write(f"=== PAGE {page_num} (Matched: {', '.join(data['keywords'])}) ===\n")
        f.write(data["text"])
        f.write("\n\n" + "="*50 + "\n\n")

print("Saved matching pages to extracted_academic_info.txt")
