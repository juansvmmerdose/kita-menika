import urllib.request
import re

url = "https://www.instagram.com/p/DZfMeWEGdnY/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req, timeout=5) as r:
    html = r.read().decode('utf-8', errors='ignore')

# find all scripts
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} scripts in embed HTML")

for s in scripts:
    if 'graphql' in s.lower() or 'display_url' in s.lower() or 'scontent' in s.lower() or 'shortcode_media' in s.lower():
        print("Script with media data found!")
        matches = re.findall(r'https?://[^\s"\'<>\\]+scontent[^\s"\'<>\\]+', s)
        print("Found scontent:", len(matches))
        if matches:
            print("Sample match:", matches[0][:150])
