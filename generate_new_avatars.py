from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/vendors/avatars", exist_ok=True)

new_avatar_configs = [
    {
        "id": "kencana",
        "title": "KENCANA",
        "subtitle": "PHOTO • JOGJA 1980",
        "bg": (12, 12, 16),
        "fg": (255, 255, 255),
        "border": (212, 175, 55),
        "font_size_main": 30,
        "font_size_sub": 11
    },
    {
        "id": "ruangasmara",
        "title": "RUANG ASMARA",
        "subtitle": "WEDDING STORIES",
        "bg": (16, 14, 14),
        "fg": (250, 245, 240),
        "border": (200, 160, 140),
        "font_size_main": 24,
        "font_size_sub": 10
    },
    {
        "id": "kairos",
        "title": "KAIROS",
        "subtitle": "WORKS • YOGYAKARTA",
        "bg": (10, 10, 12),
        "fg": (255, 255, 255),
        "border": (220, 220, 225),
        "font_size_main": 36,
        "font_size_sub": 10
    },
    {
        "id": "senja",
        "title": "TENTANG SENJA",
        "subtitle": "PHOTO & FILM JOGJA",
        "bg": (18, 14, 12),
        "fg": (255, 235, 210),
        "border": (220, 160, 110),
        "font_size_main": 22,
        "font_size_sub": 10
    },
    {
        "id": "shinta",
        "title": "SHINTA",
        "subtitle": "CATERING JOGJA 1985",
        "bg": (14, 16, 14),
        "fg": (255, 255, 255),
        "border": (180, 205, 170),
        "font_size_main": 34,
        "font_size_sub": 10
    },
    {
        "id": "alburuj",
        "title": "AL-BURUJ",
        "subtitle": "CATERING SLEMAN",
        "bg": (12, 16, 14),
        "fg": (240, 255, 240),
        "border": (160, 200, 170),
        "font_size_main": 30,
        "font_size_sub": 10
    },
    {
        "id": "karunia",
        "title": "KARUNIA",
        "subtitle": "CATERING JOGJA",
        "bg": (15, 14, 12),
        "fg": (255, 255, 255),
        "border": (210, 180, 130),
        "font_size_main": 30,
        "font_size_sub": 11
    },
    {
        "id": "kalyana",
        "title": "KALYANA",
        "subtitle": "RESORT KALIURANG",
        "bg": (10, 16, 12),
        "fg": (245, 255, 245),
        "border": (150, 195, 160),
        "font_size_main": 28,
        "font_size_sub": 10
    },
    {
        "id": "ngabean",
        "title": "NDALEM",
        "subtitle": "NGABEAN HERITAGE",
        "bg": (18, 12, 8),
        "fg": (255, 235, 190),
        "border": (225, 180, 90),
        "font_size_main": 32,
        "font_size_sub": 10
    },
    {
        "id": "hyatt",
        "title": "HYATT",
        "subtitle": "REGENCY YOGYAKARTA",
        "bg": (8, 10, 18),
        "fg": (255, 255, 255),
        "border": (212, 175, 55),
        "font_size_main": 38,
        "font_size_sub": 9
    },
    {
        "id": "omahpakem",
        "title": "OMAH PAKEM",
        "subtitle": "RESORT & WEDDING",
        "bg": (14, 14, 10),
        "fg": (250, 245, 220),
        "border": (200, 180, 120),
        "font_size_main": 24,
        "font_size_sub": 10
    },
    {
        "id": "weddingkujogja",
        "title": "WEDDINGKU",
        "subtitle": "PLANNER JOGJA",
        "bg": (16, 12, 16),
        "fg": (255, 255, 255),
        "border": (210, 160, 200),
        "font_size_main": 26,
        "font_size_sub": 11
    },
    {
        "id": "gmproduction",
        "title": "GM PRODUCTION",
        "subtitle": "WEDDING ORGANIZER",
        "bg": (10, 10, 15),
        "fg": (255, 255, 255),
        "border": (180, 180, 210),
        "font_size_main": 22,
        "font_size_sub": 10
    },
    {
        "id": "classywo",
        "title": "CLASSY",
        "subtitle": "WEDDING ORGANIZER",
        "bg": (14, 12, 14),
        "fg": (255, 255, 255),
        "border": (210, 185, 160),
        "font_size_main": 34,
        "font_size_sub": 10
    },
    {
        "id": "arniesuryo",
        "title": "ARNIE SURYO",
        "subtitle": "PAES AGENG & MUA",
        "bg": (16, 10, 8),
        "fg": (255, 230, 170),
        "border": (230, 190, 85),
        "font_size_main": 26,
        "font_size_sub": 10
    },
    {
        "id": "scratchby",
        "title": "SCRATCH BY",
        "subtitle": "WULANDEY MUA",
        "bg": (16, 13, 15),
        "fg": (255, 245, 245),
        "border": (215, 170, 180),
        "font_size_main": 28,
        "font_size_sub": 11
    },
    {
        "id": "suryodecor",
        "title": "SURYO DECOR",
        "subtitle": "YOGYAKARTA",
        "bg": (14, 14, 12),
        "fg": (255, 255, 255),
        "border": (210, 180, 140),
        "font_size_main": 26,
        "font_size_sub": 11
    },
    {
        "id": "excelsior",
        "title": "EXCELSIOR",
        "subtitle": "DECORATION JOGJA",
        "bg": (12, 12, 18),
        "fg": (255, 255, 255),
        "border": (190, 180, 220),
        "font_size_main": 26,
        "font_size_sub": 10
    }
]

size = (300, 300)

for cfg in new_avatar_configs:
    img = Image.new("RGB", size, cfg["bg"])
    draw = ImageDraw.Draw(img)
    
    # Outer luxury double border
    draw.ellipse([(10, 10), (290, 290)], outline=cfg["border"], width=3)
    draw.ellipse([(16, 16), (284, 284)], outline=(cfg["border"][0]//3, cfg["border"][1]//3, cfg["border"][2]//3), width=1)
    
    try:
        font_serif = ImageFont.truetype("georgia.ttf", cfg["font_size_main"])
        font_sub = ImageFont.truetype("arial.ttf", cfg["font_size_sub"])
    except:
        font_serif = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    
    title = cfg["title"]
    bbox = draw.textbbox((0, 0), title, font=font_serif)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (size[0] - w) / 2
    y = (size[1] - h) / 2 - 12
    draw.text((x, y), title, fill=cfg["fg"], font=font_serif)
    
    div_w = 55
    draw.line([(size[0]/2 - div_w/2, y + h + 10), (size[0]/2 + div_w/2, y + h + 10)], fill=cfg["border"], width=1)
    
    sub = cfg["subtitle"]
    sbox = draw.textbbox((0, 0), sub, font=font_sub)
    sw = sbox[2] - sbox[0]
    sh = sbox[3] - sbox[1]
    sx = (size[0] - sw) / 2
    sy = y + h + 16
    draw.text((sx, sy), sub, fill=(200, 200, 200), font=font_sub)
    
    out_path = f"assets/vendors/avatars/{cfg['id']}.jpg"
    img.save(out_path, quality=95)
    print(f"Created luxury avatar: {out_path}")

print("All new avatars created successfully!")
