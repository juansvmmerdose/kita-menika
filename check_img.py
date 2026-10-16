import urllib.request
import re
import html

url = "https://www.instagram.com/p/DBL9yFeTDlr/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req, timeout=5) as r:
    page = r.read().decode('utf-8', errors='ignore')

# find og:image or class EmbeddedMediaImage or similar
og_img = re.findall(r'<img[^>]+class="EmbeddedMediaImage"[^>]+src="([^">]+)"', page)
if not og_img:
    og_img = re.findall(r'<img[^>]+src="([^">]+)"', page)

print("Found img tags:", len(og_img))
for i, img in enumerate(og_img[:3]):
    clean_url = html.unescape(img)
    print(f"Img {i}: {clean_url[:120]}")
