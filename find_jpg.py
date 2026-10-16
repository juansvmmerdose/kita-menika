import urllib.request
import re
import html
import json

url = "https://www.instagram.com/p/DBL9yFeTDlr/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req, timeout=5) as r:
    page = r.read().decode('utf-8', errors='ignore')

# Search for patterns containing jpg
jpgs = re.findall(r'https:\\/\\/[^"\'\s]+\.jpg[^"\'\s]*', page)
if not jpgs:
    jpgs = re.findall(r'https://[^"\'\s]+\.jpg[^"\'\s]*', page)

print(f"Total jpg matches: {len(jpgs)}")
clean_jpgs = list(dict.fromkeys([html.unescape(j.replace('\\/', '/')) for j in jpgs]))
print(f"Unique jpgs: {len(clean_jpgs)}")
for i, j in enumerate(clean_jpgs[:5]):
    print(f"JPG {i}: {j[:150]}")
