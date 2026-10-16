import urllib.request
import urllib.parse
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def search_images(query):
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        return murls
    except Exception as e:
        print(f"Err {query}: {e}")
        return []

queries = [
    ("mamuk", 'site:instagram.com "mamuktukangmakeupjogja" OR "mamuk" paes ageng jogja'),
    ("arniesuryo", 'site:instagram.com "arniesuryo" paes ageng jogja'),
    ("scratchby", 'site:instagram.com "scratchby.mwulandey" makeup paes jogja'),
    ("ilona", 'site:instagram.com "ilonaorganizer" wedding organizer jogja'),
    ("vidi", 'site:instagram.com "vidicatering" jogja wedding catering prasmanan'),
    ("albertus", 'site:instagram.com "albertus_mcjogja" MC wedding jogja'),
    ("prosound", 'site:instagram.com "prosound.jogja" sound system wedding jogja'),
]

for name, q in queries:
    imgs = search_images(q)
    print(f"{name}: found {len(imgs)} images")
    for u in imgs[:3]:
        print(f"  {u[:110]}")
