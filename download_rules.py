import requests
import sys

url = "https://sit.ac.in/wp-content/uploads/2026/04/Academic_Rules_and_Regulations_2025-26.pdf"
output_filename = "academic_rules_full.pdf"

print(f"Downloading from: {url}")
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers, stream=True, timeout=30)
    response.raise_for_status()
    
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    print(f"Total size: {total_size_in_bytes / (1024*1024):.2f} MB")
    
    block_size = 1024 * 1024 # 1 Megabyte
    downloaded = 0
    
    with open(output_filename, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded += len(data)
            percent = (downloaded / total_size_in_bytes) * 100 if total_size_in_bytes else 0
            print(f"Downloaded {downloaded / (1024*1024):.2f} MB / {total_size_in_bytes / (1024*1024):.2f} MB ({percent:.1f}%)", flush=True)
            
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
