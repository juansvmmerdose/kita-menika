import urllib.request
import re

url = "https://www.instagram.com/p/DBL9yFeTDlr/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req, timeout=5) as r:
    page = r.read().decode('utf-8', errors='ignore')

cdn_matches = re.findall(r'https?:\\?/\\?/[^"\'\s<>\\]*cdninstagram\.com[^"\'\s<>\\]*', page)
print(f"cdn matches: {len(cdn_matches)}")
for i, m in enumerate(list(dict.fromkeys(cdn_matches))[:5]):
    clean = m.replace('\\/', '/')
    print(f"{i}: {clean[:150]}")
