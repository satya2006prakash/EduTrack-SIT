import pypdf
import os

pdf_path = "academic_rules_full.pdf"
reader = pypdf.PdfReader(pdf_path)

pages_to_check = [2, 5, 10, 15, 20, 25, 30]
for p_num in pages_to_check:
    if p_num <= len(reader.pages):
        page = reader.pages[p_num - 1]
        text = page.extract_text()
        print(f"=== PAGE {p_num} (Text Length: {len(text)}) ===")
        if text.strip():
            print(text[:400])
        else:
            print("[Empty text on this page]")
        print("-" * 50)
