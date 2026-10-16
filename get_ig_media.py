import urllib.request
import re
import html
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

vendors = [
    ("jawara", "DZfMeWEGdnY"),
    ("sandi", "DdB34NMD5lr"),
    ("lux", "DZm2Kbgj4ZZ"),
    ("kitakancerita", "DV2iXGGCSz6"),
    ("nijo", "DaQBRhFGCvF"),
    ("neiscala", "DeB1C4kH5vS"),
    ("lunanouva", "DdRiiJqj3xs")
]

os.makedirs("assets/vendors/avatars", exist_ok=True)
os.makedirs("assets/vendors/posts", exist_ok=True)

for name, code in vendors:
    url = f"https://www.instagram.com/p/{code}/embed/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            page = r.read().decode('utf-8', errors='ignore')
        
        # Check avatar
        avatars = re.findall(r'<img[^>]+class="[^"]*Avatar[^"]*"[^>]+src="([^"]+)"', page)
        print(f"{name} ({code}) -> Avatars in embed: {len(avatars)}")
        if avatars:
            clean_url = html.unescape(avatars[0])
            print("Avatar URL:", clean_url[:100])
            # Try to download
            try:
                a_req = urllib.request.Request(clean_url, headers=headers)
                with urllib.request.urlopen(a_req, timeout=5) as img_r:
                    with open(f"assets/vendors/avatars/{name}.jpg", "wb") as f:
                        f.write(img_r.read())
                    print(f"Downloaded avatar for {name}")
            except Exception as e:
                print(f"Failed to download avatar: {e}")
    except Exception as e:
        print(f"Error {name}: {e}")
