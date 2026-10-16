import urllib.request
import urllib.parse
import re
import html
import os
import json
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

vendors = [
    {"id": "jawara", "name": "Jawara Photo", "handle": "jawara.photo", "search": "jawara.photo instagram wedding jogja"},
    {"id": "sandiliem", "name": "Sandi Liems", "handle": "sandi.liem", "search": "sandi.liem instagram wedding yogyakarta"},
    {"id": "luxvisual", "name": "Lux Visual", "handle": "luxvisual.id", "search": "luxvisual.id instagram wedding jogja"},
    {"id": "kitakancerita", "name": "Kita Kancerita", "handle": "kitakancerita", "search": "kitakancerita instagram wedding yogyakarta"},
    {"id": "nijo", "name": "The Nijo Photograph", "handle": "thenijophotograph", "search": "thenijophotograph instagram wedding"},
    {"id": "neiscala", "name": "Neiscala", "handle": "neiscala", "search": "neiscala instagram wedding yogyakarta"},
    {"id": "lunanouva", "name": "Luna Nouva Studio", "handle": "lunanouovastudio__", "search": "lunanouovastudio instagram wedding"}
]

os.makedirs("assets/vendors/avatars", exist_ok=True)
os.makedirs("assets/vendors/slides", exist_ok=True)

def find_lookaside_and_images(query):
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            page = r.read().decode('utf-8', errors='ignore')
        
        # find murl
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', page)
        return murls
    except Exception as e:
        print(f"Error querying {query}: {e}")
        return []

def extract_real_scontent(lookaside_or_page_url):
    try:
        req = urllib.request.Request(lookaside_or_page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as r:
            t = r.read().decode('utf-8', errors='ignore')
        og = re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', t)
        if og:
            return html.unescape(og[0])
    except Exception as e:
        pass
    return None

for v in vendors:
    print(f"\n=================== Fetching {v['name']} ({v['handle']}) ===================")
    murls = find_lookaside_and_images(v["search"])
    print(f"Found {len(murls)} search result images")
    
    saved_slides = 0
    for idx, u in enumerate(murls):
        if saved_slides >= 3:
            break
        # If it's a lookaside link:
        target_img_url = None
        if "lookaside.instagram.com" in u:
            target_img_url = extract_real_scontent(u)
        elif "scontent" in u:
            target_img_url = u
        
        if target_img_url:
            slide_path = f"assets/vendors/slides/{v['id']}_slide_{saved_slides+1}.jpg"
            try:
                img_req = urllib.request.Request(target_img_url, headers=headers)
                with urllib.request.urlopen(img_req, timeout=8) as ir:
                    img_data = ir.read()
                with open(slide_path, "wb") as f:
                    f.write(img_data)
                with Image.open(slide_path) as im:
                    print(f"  [+] Saved {slide_path}: {im.size} from {target_img_url[:80]}...")
                saved_slides += 1
            except Exception as e:
                print(f"  [-] Failed downloading {target_img_url[:60]}: {e}")

