import urllib.request
import os
import pypdf

pdf_url = "https://sit.ac.in/wp-content/uploads/2026/04/Academic_Rules_and_Regulations_2025-26.pdf"
pdf_path = "academic_rules_clean.pdf"

def download_file(url, path):
    print(f"Downloading {url}...")
    try:
        # User-Agent to avoid blocking
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            with open(path, 'wb') as out_file:
                # Read in chunks and print progress
                total_size = int(response.info().get('Content-Length', 0))
                downloaded = 0
                chunk_size = 1024 * 1024  # 1MB
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    downloaded += len(chunk)
                    out_file.write(chunk)
                    if total_size:
                        percent = (downloaded / total_size) * 100
                        print(f"Downloaded {downloaded}/{total_size} bytes ({percent:.2f}%)")
                    else:
                        print(f"Downloaded {downloaded} bytes")
        print("Download complete.")
        return True
    except Exception as e:
        print(f"Error downloading: {e}")
        return False

if __name__ == "__main__":
    if download_file(pdf_url, pdf_path):
        print("Verifying PDF file...")
        try:
            reader = pypdf.PdfReader(pdf_path)
            print(f"PDF is valid. Total pages: {len(reader.pages)}")
            
            # Simple keyword search
            keywords = ["attendance", "cie", "continuous internal evaluation", "eligibility", "condonation", "minimum"]
            found_pages = {}
            for i, page in enumerate(reader.pages):
                text = page.extract_text().lower()
                matched = [kw for kw in keywords if kw in text]
                if matched:
                    found_pages[i+1] = matched
            print(f"Matching pages: {list(found_pages.keys())}")
        except Exception as e:
            print(f"Verification failed: {e}")
