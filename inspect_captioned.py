import urllib.request
import re

url = "https://www.instagram.com/p/DZfMeWEGdnY/embed/captioned/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req, timeout=5) as r:
    html = r.read().decode('utf-8', errors='ignore')

# find all img tags
imgs = re.findall(r'<img[^>]+>', html)
print(f"Img tags in captioned embed: {len(imgs)}")
for img in imgs:
    print("IMG:", img[:150])

# find background-image
bg = re.findall(r'background(?:-image)?:\s*url\([^)]+\)', html)
print(f"Background images: {len(bg)}")
for b in bg:
    print("BG:", b[:150])
