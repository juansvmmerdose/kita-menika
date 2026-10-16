import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

vendors = [
    ("kitakancerita", "site:instagram.com/p/ kitakancerita"),
    ("kitakancerita_reel", "site:instagram.com/reel/ kitakancerita"),
    ("thenijo", "site:instagram.com/p/ thenijophotograph"),
    ("neiscala", "site:instagram.com/p/ neiscala"),
    ("lunanouva", "site:instagram.com/p/ lunanouovastudio"),
    ("luxvisual", "site:instagram.com/p/ luxvisual.id"),
    ("mamuk", "site:instagram.com/p/ mamuktukangmakeupjogja"),
    ("arniesuryo", "site:instagram.com/p/ arniesuryo")
]

for tag, q in vendors:
    url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            codes = re.findall(r'instagram\.com/(?:p|reel)/([a-zA-Z0-9_-]{9,15})', content)
            print(f"{tag}:", list(dict.fromkeys(codes))[:5])
    except Exception as e:
        print(f"Err {tag}: {e}")
