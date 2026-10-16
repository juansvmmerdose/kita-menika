import urllib.request
import re
import html
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_from_lookaside(media_id, output_path):
    url = f"https://lookaside.instagram.com/seo/google_widget/crawler/?media_id={media_id}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            content = r.read().decode('utf-8', errors='ignore')
        og = re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', content)
        if og:
            img_url = html.unescape(og[0])
            img_req = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(img_req, timeout=8) as ir:
                data = ir.read()
            with open(output_path, 'wb') as f:
                f.write(data)
            with Image.open(output_path) as im:
                print(f"[OK] Downloaded {output_path}: {im.size}")
                return True
        else:
            print(f"[FAIL] No og:image for media_id {media_id}")
    except Exception as e:
        print(f"[ERROR] {media_id}: {e}")
    return False

# Test the nijo media_ids
download_from_lookaside("3547284168406645759", "assets/vendors/slides/nijo_slide_1.jpg")
download_from_lookaside("3661266673958025465", "assets/vendors/slides/nijo_slide_2.jpg")
