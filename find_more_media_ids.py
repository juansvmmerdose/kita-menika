import urllib.request
import urllib.parse
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
    except Exception as e:
        print(f"[ERROR] {media_id}: {e}")
    return False

def find_ig_media_ids(handle):
    q = f'"{handle}" "lookaside.instagram.com"'
    url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers)
    found_ids = []
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            text = r.read().decode('utf-8', errors='ignore')
        ids = re.findall(r'media_id=(\d+)', text)
        found_ids.extend(ids)
    except Exception as e:
        pass
    
    # Also search site:instagram.com/p
    q2 = f'site:instagram.com "{handle}"'
    url2 = f"https://www.bing.com/search?q={urllib.parse.quote(q2)}"
    req2 = urllib.request.Request(url2, headers=headers)
    try:
        with urllib.request.urlopen(req2, timeout=8) as r2:
            text2 = r2.read().decode('utf-8', errors='ignore')
        ids2 = re.findall(r'media_id=(\d+)', text2)
        found_ids.extend(ids2)
    except Exception as e:
        pass

    return list(dict.fromkeys(found_ids))

handles = [
    "mamuktukangmakeupjogja",
    "arniesuryo",
    "scratchby.mwulandey",
    "vidicatering",
    "shintacatering",
    "royalambarrukmo",
    "kalyanaresort",
    "ilonaorganizer",
    "mahkota_wo.jogja",
    "dananidecoration",
    "albertus_mcjogja"
]

for h in handles:
    mids = find_ig_media_ids(h)
    print(f"{h}: {len(mids)} media IDs -> {mids[:3]}")
