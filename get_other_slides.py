import urllib.request
from PIL import Image

urls = [
    ("mamuk_slide_1.jpg", "https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=700&q=80"),
    ("ambarrukmo_slide_1.jpg", "https://images.unsplash.com/photo-1545232979-fbf6c5c8e312?auto=format&fit=crop&w=700&q=80"),
    ("danani_slide_1.jpg", "https://images.unsplash.com/photo-1519225429402-7c706346b9a8?auto=format&fit=crop&w=700&q=80"),
    ("vidi_slide_1.jpg", "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=700&q=80"),
    ("mahkota_slide_1.jpg", "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=700&q=80")
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
        out = f"assets/vendors/slides/{name}"
        with open(out, "wb") as f:
            f.write(data)
        with Image.open(out) as im:
            print(f"Saved {out}: {im.size}")
    except Exception as e:
        print(f"Failed {name}: {e}")
