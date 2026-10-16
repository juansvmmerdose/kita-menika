import urllib.request
import re
import json

url = "https://www.instagram.com/p/DZfMeWEGdnY/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req, timeout=5) as r:
    html = r.read().decode('utf-8', errors='ignore')

scripts = re.findall(r'<script type="application/json"[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"JSON scripts: {len(scripts)}")
for i, s in enumerate(scripts):
    if 'display_url' in s or 'image' in s or 'media' in s or 'caption' in s or 'prima' in s.lower():
        print(f"Script {i} matched keyword!")
        # look for any url
        urls = re.findall(r'https?:\\?/\\?/[^"\'\s<>\\]+', s)
        print(f"Found {len(urls)} URLs in script {i}")
        for u in urls[:5]:
            clean = u.replace('\\/', '/')
            print("  URL:", clean[:140])
