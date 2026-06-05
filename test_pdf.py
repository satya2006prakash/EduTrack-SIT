import pypdf

pdf_path = "academic_rules_full.pdf"
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

has_text = 0
for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    if len(text.strip()) > 0:
        has_text += 1
        if has_text <= 3:
            print(f"Page {idx+1} has text (length {len(text)}):")
            print(text[:200])
            print("-" * 50)

print(f"Total pages with text: {has_text} / {len(reader.pages)}")
