import urllib.request
import urllib.parse
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

searches = [
    ("lux", "site:instagram.com/p/ lux visual jogja"),
    ("lux2", "site:instagram.com/p/ luxvisual"),
    ("kitakancerita", "site:instagram.com/p/ kitakancerita"),
    ("nijo", "site:instagram.com/p/ thenijophotograph"),
    ("nijo2", "site:instagram.com/p/ nijo photograph"),
    ("neiscala", "site:instagram.com/p/ neiscala"),
    ("lunanouva", "site:instagram.com/p/ lunanouvastudio"),
    ("lunanouva2", "site:instagram.com/p/ lunanouva")
]

for tag, q in searches:
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            posts = re.findall(r'instagram\.com/(?:p|reel)/([a-zA-Z0-9_-]+)', content)
            print(f"{tag}:", list(dict.fromkeys(posts))[:5])
    except Exception as e:
        print(f"{tag} error: {e}")
