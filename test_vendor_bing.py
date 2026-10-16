import urllib.request
import urllib.parse
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

queries = [
    ("jawara", 'jawara.photo wedding'),
    ("jawara2", 'bersamajawara instagram'),
    ("jawara3", 'site:instagram.com jawara.photo'),
    ("lux", 'luxvisual.id wedding'),
    ("kitakancerita", 'kitakancerita wedding'),
    ("neiscala", 'neiscala wedding'),
    ("lunanouva", 'lunanouovastudio wedding'),
    ("lunanouva2", 'lunanuovaphotofilm wedding')
]

for label, q in queries:
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(q)}&first=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        media_ids = re.findall(r'media_id=(\d+)', html)
        print(f"[{label}] Found {len(murls)} murls, {len(media_ids)} media_ids")
        if media_ids:
            print("   media_ids:", list(dict.fromkeys(media_ids))[:5])
        # Also print any instagram/fbcdn/scontent urls
        ig_urls = [u for u in murls if 'instagram' in u or 'fbcdn' in u or 'scontent' in u]
        if ig_urls:
            print("   ig_urls:", ig_urls[:3])
    except Exception as e:
        print(f"[{label}] Err: {e}")
