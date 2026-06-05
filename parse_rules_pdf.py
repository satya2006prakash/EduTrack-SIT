import pypdf
import os
import re

pdf_path = "academic_rules_full.pdf"
output_path = "extracted_rules_summary.txt"

def extract_academic_rules():
    if not os.path.exists(pdf_path):
        print(f"File {pdf_path} not found.")
        return
        
    print(f"Opening {pdf_path}...")
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    print(f"Total pages: {num_pages}")
    
    # Target keywords for academic regulations
    keywords = [
        r"\battendance\b", 
        r"\bcie\b", 
        r"\bcontinuous internal evaluation\b", 
        r"\bcondonation\b", 
        r"\bdetained\b", 
        r"\bsee\b",
        r"\bsemester end examination\b",
        r"\bgrading\b",
        r"\bletter grade\b",
        r"\bsgpa\b",
        r"\bcgpa\b",
        r"\bmarks distribution\b",
        r"\beligibility\b"
    ]
    
    matched_pages = []
    
    for idx, page in enumerate(reader.pages):
        text = page.extract_text()
        text_lower = text.lower()
        
        matches = []
        for kw in keywords:
            if re.search(kw, text_lower):
                matches.append(kw)
                
        if matches:
            matched_pages.append((idx + 1, matches, text))
            
    print(f"Found matches on {len(matched_pages)} pages.")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"SIT TUMKUR ACADEMIC RULES & REGULATIONS 2025-2026\n")
        f.write(f"Extracted from: {pdf_path}\n")
        f.write(f"Total Pages Analyzed: {num_pages}\n")
        f.write(f"Pages with keywords: {len(matched_pages)}\n")
        f.write("=" * 80 + "\n\n")
        
        for page_num, matches, text in matched_pages:
            f.write(f"=== PAGE {page_num} ===\n")
            f.write(f"Matched Keywords: {', '.join(matches)}\n")
            f.write("-" * 40 + "\n")
            f.write(text.strip())
            f.write("\n\n" + "=" * 80 + "\n\n")
            
    print(f"Successfully extracted rules to {output_path}")

if __name__ == "__main__":
    extract_academic_rules()
