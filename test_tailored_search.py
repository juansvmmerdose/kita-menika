import urllib.request
import urllib.parse
import re
import html
import os
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

def search_bing_murls(query):
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            text = r.read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', text)
        return murls
    except Exception as e:
        print(f"Error for query '{query}': {e}")
        return []

# Test queries for Jawara, Kitakancerita, Neiscala, Luna Nouva
queries = {
    "jawara": ["jawara photo wedding jogja", "bersamajawara wedding prima fauzan"],
    "kitakancerita": ["kitakancerita wedding jogja", "kitakancerita sungkeman siraman jogja"],
    "neiscala": ["neiscala wedding photo yogyakarta", "neiscala prewedding jogja"],
    "lunanouva": ["lunanouva studio gumuk pasir bantul", "lunanuova photo film wedding"],
    "luxvisual": ["luxvisual wedding photography jogja", "lux visual id lamaran jogja"]
}

for k, qlist in queries.items():
    print(f"\n--- {k} ---")
    for q in qlist:
        res = search_bing_murls(q)
        print(f"Query '{q}': found {len(res)} murls")
        for u in res[:3]:
            print("  ", u[:120])
