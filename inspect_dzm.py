import urllib.request
import re
import html

url = "https://www.instagram.com/p/DZm2Kbgj4ZZ/embed/captioned/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req, timeout=5) as r:
    page = r.read().decode('utf-8', errors='ignore')

captions = re.findall(r'<div class="Caption"[^>]*>(.*?)</div>', page, re.DOTALL)
if not captions:
    captions = re.findall(r'class="CaptionText"[^>]*>(.*?)</div>', page, re.DOTALL)

for cap in captions:
    clean = re.sub(r'<[^>]+>', ' ', cap)
    clean = html.unescape(' '.join(clean.split()))
    print(clean.encode('ascii', errors='replace').decode('ascii'))
