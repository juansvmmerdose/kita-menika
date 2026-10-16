import urllib.request
import urllib.parse
import re
import html
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

targets = [
    ("jawara", "jawara.photo"),
    ("sandiliem", "sandi.liem"),
    ("luxvisual", "luxvisual.id"),
    ("kitakancerita", "kitakancerita"),
    ("neiscala", "neiscala"),
    ("lunanouva", "lunanouovastudio__")
]

def search_bing_media_ids(keyword):
    # search bing for lookaside url or instagram post
    q = f'"{keyword}" "lookaside.instagram.com"'
    url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers)
    found_ids = []
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            text = r.read().decode('utf-8', errors='ignore')
        ids = re.findall(r'media_id=(\d+)', text)
        found_ids.extend(ids)
    except Exception as e:
        print(f"Err {keyword}: {e}")
    
    # Also search bing images
    q2 = f'"{keyword}" wedding'
    url2 = f"https://www.bing.com/images/search?q={urllib.parse.quote(q2)}&first=1"
    req2 = urllib.request.Request(url2, headers=headers)
    try:
        with urllib.request.urlopen(req2, timeout=8) as r:
            text2 = r.read().decode('utf-8', errors='ignore')
        ids2 = re.findall(r'media_id=(\d+)', text2)
        found_ids.extend(ids2)
    except Exception as e:
        pass

    return list(dict.fromkeys(found_ids))

for vid, handle in targets:
    mids = search_bing_media_ids(handle)
    print(f"Vendor {vid} ({handle}): found {len(mids)} media IDs: {mids[:5]}")
