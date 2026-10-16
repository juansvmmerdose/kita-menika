import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'}
url = "https://greatfon.com/c/luxvisual.id"
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://cdn2\.dumpor\.io/a/[a-zA-Z0-9-]+\.jpg', html)
    print("Luxvisual images:", list(dict.fromkeys(imgs))[:6])
    for i, u in enumerate(list(dict.fromkeys(imgs))[:4]):
        try:
            req_img = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36', 'Referer': 'https://greatfon.com/'})
            with urllib.request.urlopen(req_img, timeout=8) as ir:
                with open(f"assets/vendors/slides/luxvisual_slide_{i+1}.jpg", "wb") as f:
                    f.write(ir.read())
            print(f"Downloaded lux slide {i+1}")
        except Exception as e:
            print(f"Err {i}: {e}")
except Exception as e:
    print("Err lux:", e)
