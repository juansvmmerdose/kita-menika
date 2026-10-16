import urllib.request
from PIL import Image

urls = [
    ("kitakancerita_slide_1.jpg", "https://i.pinimg.com/originals/40/be/d0/40bed0c3fa7a18a4ce7e74c021c90507.jpg"),
    ("kitakancerita_slide_2.jpg", "https://i.pinimg.com/736x/72/4a/4e/724a4eab58573f60247137105be7b50c.jpg")
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
            print(f"Downloaded {out}: {im.size} {im.format}")
    except Exception as e:
        print(f"Failed {name}: {e}")
