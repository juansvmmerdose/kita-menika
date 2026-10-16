import urllib.request
import re
import html
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = "https://www.instagram.com/p/DZfMeWEGdnY/embed/captioned/"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=8) as r:
    page = r.read().decode('utf-8', errors='ignore')

# 1. Avatar is the first img with scontent
avatar_matches = re.findall(r'<img[^>]+src="(https://scontent[^\"]+)"', page)
# 2. Main post photo is EmbeddedMediaImage
media_matches = re.findall(r'<img[^>]+class="EmbeddedMediaImage"[^>]+src="([^\"]+)"', page)

print(f"Avatar matches: {len(avatar_matches)}")
print(f"Media matches: {len(media_matches)}")

if avatar_matches:
    av_url = html.unescape(avatar_matches[0])
    print("Downloading Jawara Avatar:", av_url[:100])
    img_req = urllib.request.Request(av_url, headers=headers)
    with urllib.request.urlopen(img_req, timeout=8) as ir:
        with open("assets/vendors/avatars/jawara.jpg", "wb") as f:
            f.write(ir.read())
    print("Saved jawara.jpg")
    with Image.open("assets/vendors/avatars/jawara.jpg") as im:
        print("Jawara Avatar size:", im.size)

if media_matches:
    media_url = html.unescape(media_matches[0])
    print("Downloading Jawara Post Photo:", media_url[:100])
    img_req = urllib.request.Request(media_url, headers=headers)
    with urllib.request.urlopen(img_req, timeout=8) as ir:
        with open("assets/vendors/slides/jawara_slide_1.jpg", "wb") as f:
            f.write(ir.read())
    print("Saved jawara_slide_1.jpg")
    with Image.open("assets/vendors/slides/jawara_slide_1.jpg") as im:
        print("Jawara Post Photo size:", im.size)
