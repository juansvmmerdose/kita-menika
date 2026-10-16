import urllib.request
import re
import html
import os
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = "https://www.instagram.com/p/DZfMeWEGdnY/embed/captioned/"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=5) as r:
    page = r.read().decode('utf-8', errors='ignore')

# find all img tags
img_tags = re.findall(r'<img[^>]+>', page)
print(f"Total img tags: {len(img_tags)}")

for i, tag in enumerate(img_tags):
    src_match = re.search(r'src="([^"]+)"', tag)
    if src_match:
        src = html.unescape(src_match.group(1))
        alt_match = re.search(r'alt="([^"]+)"', tag)
        alt = alt_match.group(1) if alt_match else ""
        cls_match = re.search(r'class="([^"]+)"', tag)
        cls = cls_match.group(1) if cls_match else ""
        print(f"[{i}] class={cls} | alt={alt[:30]} | src={src[:80]}")
        
        # Download
        try:
            r_img = urllib.request.Request(src, headers=headers)
            with urllib.request.urlopen(r_img, timeout=8) as resp:
                data = resp.read()
            out_file = f"jawara_img_{i}.jpg"
            with open(out_file, "wb") as f:
                f.write(data)
            with Image.open(out_file) as im:
                print(f"    Saved {out_file} - Size: {im.size} - Format: {im.format}")
        except Exception as e:
            print(f"    Failed {i}: {e}")
