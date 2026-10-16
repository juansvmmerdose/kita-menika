import urllib.request
import urllib.parse
import re
import html
import os
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

vendors = [
    ("jawara", "jawara.photo", "jawara photo wedding jogja instagram"),
    ("sandiliem", "sandi.liem", "sandi liem wedding photography jogja instagram"),
    ("luxvisual", "luxvisual.id", "luxvisual.id instagram"),
    ("kitakancerita", "kitakancerita", "kitakancerita wedding jogja instagram"),
    ("nijo", "thenijophotograph", "thenijophotograph wedding instagram"),
    ("neiscala", "neiscala", "neiscala wedding instagram"),
    ("lunanouva", "lunanouovastudio__", "lunanouva studio bantul instagram")
]

os.makedirs("assets/vendors/avatars", exist_ok=True)
os.makedirs("assets/vendors/slides", exist_ok=True)

for vid, handle, query in vendors:
    print(f"\n--- Checking {handle} ---")
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            text = r.read().decode('utf-8', errors='ignore')
        # find scontent or profile pic
        pics = re.findall(r'https://[^\s"\'<>\\]*(?:scontent|cdninstagram)[^\s"\'<>\\]*', text)
        print(f"  Found {len(pics)} instagram cdn URLs in search")
        for p in set(pics)[:3]:
            print("   ", p[:120])
    except Exception as e:
        print(f"  Search error: {e}")
