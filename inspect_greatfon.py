import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://greatfon.com/c/jawara.photo"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=8) as r:
    html = r.read().decode('utf-8', errors='ignore')

# find image urls
imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|webp|png)[^\s"\'<>]*', html)
print(f"Total image matches: {len(imgs)}")
for i, img in enumerate(list(dict.fromkeys(imgs))[:10]):
    print(f"Img {i}: {img}")
