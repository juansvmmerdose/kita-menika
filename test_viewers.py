import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

services = [
    ("imginn", "https://imginn.com/jawara.photo/"),
    ("pixwox", "https://www.pixwox.com/profile/jawara.photo/"),
    ("picnob", "https://www.picnob.com/profile/jawara.photo/"),
    ("greatfon", "https://greatfon.com/c/jawara.photo")
]

for name, u in services:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print(f"Service {name} returned status 200, length: {len(html)}")
            # look for img tags
            imgs = re.findall(r'<img[^>]+src="([^">]+)"', html)
            print(f"{name} found imgs:", imgs[:3])
    except Exception as e:
        print(f"Service {name} error: {e}")
