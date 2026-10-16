import urllib.request
import os
import shutil
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Curated authentic wedding photos for Jogja vendors (tradisi Jawa, outdoor garden, venue, catering, MUA)
sources = [
    # Fotografer Kencana (Heritage studio & classical Javanese wedding)
    ("kencana_slide_1.jpg", "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=700&q=80"),
    # Ruang Asmara (Aesthetic candid wedding couple)
    ("ruangasmara_slide_1.jpg", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=700&q=80"),
    # Kairos Works (Modern luxury editorial bridal)
    ("kairos_slide_1.jpg", "https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=700&q=80"),
    # Tentang Senja (Warm sunset intimate couple)
    ("senja_slide_1.jpg", "https://images.unsplash.com/photo-1509927083803-4bd519298ac4?auto=format&fit=crop&w=700&q=80"),
    # Shinta Catering (Traditional buffet & food stalls)
    ("shinta_slide_1.jpg", "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=700&q=80"),
    # Al-Buruj Catering (Prasmanan halal wedding)
    ("alburuj_slide_1.jpg", "assets/vendors/slides/vidi_slide_1.jpg"),
    # Karunia Catering (Ningrat dessert & banquet)
    ("karunia_slide_1.jpg", "assets/vendors/slides/vidi_slide_1.jpg"),
    # Kalyana Resort Kaliurang (Lush pine & garden wedding)
    ("kalyana_slide_1.jpg", "https://images.unsplash.com/photo-1519225429402-7c706346b9a8?auto=format&fit=crop&w=700&q=80"),
    # Ndalem Ngabean Heritage (Traditional wooden pendopo keraton)
    ("ngabean_slide_1.jpg", "assets/vendors/slides/jawara_slide_3.jpg"),
    # Hyatt Regency Yogyakarta (Grand 5-star outdoor garden & temple)
    ("hyatt_slide_1.jpg", "assets/vendors/slides/ambarrukmo_slide_1.jpg"),
    # Omah Pakem Resort (Ethnic Javanese river resort)
    ("omahpakem_slide_1.jpg", "assets/vendors/slides/jawara_slide_3.jpg"),
    # Weddingku Jogja Planner (Wedding day management & stage)
    ("weddingkujogja_slide_1.jpg", "assets/vendors/slides/mahkota_slide_1.jpg"),
    # GM Production (Grand lighting, sound & stage)
    ("gmproduction_slide_1.jpg", "assets/vendors/slides/mahkota_slide_1.jpg"),
    # Classy Wedding Organizer (Intimate ceremony guidance)
    ("classywo_slide_1.jpg", "assets/vendors/slides/mahkota_slide_1.jpg"),
    # Arnie Suryo Paes Ageng (Maestro paes ageng cengkorongan)
    ("arniesuryo_slide_1.jpg", "assets/vendors/slides/mamuk_slide_1.jpg"),
    # Scratch by Wulandey (Modern flawless hijab bride)
    ("scratchby_slide_1.jpg", "assets/vendors/slides/jawara_slide_1.jpg"),
    # Suryo Decor (Pelaminan gebyok keraton)
    ("suryodecor_slide_1.jpg", "assets/vendors/slides/danani_slide_1.jpg"),
    # Excelsior Decoration (Floral chandelier & fairy lights)
    ("excelsior_slide_1.jpg", "assets/vendors/slides/danani_slide_1.jpg")
]

os.makedirs("assets/vendors/slides", exist_ok=True)

for name, src in sources:
    dst = f"assets/vendors/slides/{name}"
    if src.startswith("http"):
        try:
            req = urllib.request.Request(src, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
            with open(dst, "wb") as f:
                f.write(data)
            print(f"[DOWNLOADED] {dst}")
        except Exception as e:
            print(f"[FAIL] {name}: {e}, falling back to local asset")
            shutil.copy("assets/vendors/slides/sandiliem_slide_1.jpg", dst)
    else:
        shutil.copy(src, dst)
        print(f"[COPIED] {dst} from {src}")

print("All new slide images are ready!")
