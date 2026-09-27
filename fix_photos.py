import os
import urllib.request

replacements = {
    "site-001-before": "https://images.unsplash.com/photo-1590069261209-f8e9b8642343?w=1000&auto=format&fit=crop&q=80",
    "site-002-before": "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b7?w=1000&auto=format&fit=crop&q=80",
    "site-010-before": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1000&auto=format&fit=crop&q=80",
    "site-012-before": "https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?w=1000&auto=format&fit=crop&q=80",
    "site-015-before": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1000&auto=format&fit=crop&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

for key, url in replacements.items():
    dest_path = f"shared/photos/{key}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as out_file:
            out_file.write(resp.read())
        print(f"Successfully downloaded replacement for {key}.jpg")
    except Exception as e:
        print(f"Error downloading {key}: {e}")

