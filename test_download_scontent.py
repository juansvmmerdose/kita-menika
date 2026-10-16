import re
import html
import urllib.request
from PIL import Image

with open('test_lookaside.jpg', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

og = re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', t)
if og:
    img_url = html.unescape(og[0])
    print("Direct scontent URL:", img_url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(img_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
        with open('real_wedding_sample.jpg', 'wb') as f:
            f.write(data)
        with Image.open('real_wedding_sample.jpg') as im:
            print("SUCCESS! Real image downloaded:", im.size, im.format)
    except Exception as e:
        print("Failed to download scontent:", e)
else:
    print("No og:image found")
