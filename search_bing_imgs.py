import urllib.request
import re
import urllib.parse
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def search_images(query):
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
        # Bing image URLs are in m="{...murl&quot;:&quot;URL&quot;...}"
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        return murls
    except Exception as e:
        print(f"Err {query}: {e}")
        return []

for q in ['"jawara.photo" jogja', '"sandi.liem" jogja wedding', '"kitakancerita" jogja', '"neiscala" wedding', '"thenijophotograph"']:
    res = search_images(q)
    print(f"Query: {q} -> Found {len(res)} images")
    for u in res[:3]:
        print("  ", u[:120])
