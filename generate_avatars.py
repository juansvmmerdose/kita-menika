from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets/vendors/avatars", exist_ok=True)

avatar_configs = [
    {
        "id": "jawara",
        "title": "JAWARA",
        "subtitle": "PHOTO • JOGJA",
        "bg": (14, 14, 16),
        "fg": (255, 255, 255),
        "border": (212, 175, 55), # gold
        "font_size_main": 34,
        "font_size_sub": 12,
        "serif": True
    },
    {
        "id": "sandiliem",
        "title": "SANDI LIEM",
        "subtitle": "PHOTOGRAPHY",
        "bg": (12, 12, 14),
        "fg": (255, 255, 255),
        "border": (220, 220, 225), # silver
        "font_size_main": 28,
        "font_size_sub": 12,
        "serif": True
    },
    {
        "id": "luxvisual",
        "title": "LUX",
        "subtitle": "VISUAL ID",
        "bg": (10, 10, 12),
        "fg": (255, 255, 255),
        "border": (200, 200, 200),
        "font_size_main": 44,
        "font_size_sub": 13,
        "serif": False
    },
    {
        "id": "kitakancerita",
        "title": "KITA KAN",
        "subtitle": "CERITA",
        "bg": (18, 16, 15),
        "fg": (250, 245, 240),
        "border": (198, 166, 120), # warm champagne
        "font_size_main": 30,
        "font_size_sub": 15,
        "serif": True
    },
    {
        "id": "nijo",
        "title": "NIJO",
        "subtitle": "PHOTOGRAPH",
        "bg": (8, 8, 8),
        "fg": (255, 255, 255),
        "border": (180, 180, 180),
        "font_size_main": 42,
        "font_size_sub": 12,
        "serif": True
    },
    {
        "id": "neiscala",
        "title": "NEISCALA",
        "subtitle": "PHOTO & VIDEO",
        "bg": (10, 15, 14),
        "fg": (245, 250, 248),
        "border": (160, 190, 180),
        "font_size_main": 28,
        "font_size_sub": 11,
        "serif": True
    },
    {
        "id": "lunanouva",
        "title": "LUNA NUOVA",
        "subtitle": "STUDIO BANTUL",
        "bg": (16, 12, 18),
        "fg": (255, 255, 255),
        "border": (210, 180, 140),
        "font_size_main": 26,
        "font_size_sub": 11,
        "serif": True
    },
    {
        "id": "mamuk",
        "title": "MAMUK",
        "subtitle": "PAES AGENG JOGJA",
        "bg": (18, 12, 6),
        "fg": (255, 220, 130),
        "border": (230, 190, 80),
        "font_size_main": 34,
        "font_size_sub": 11,
        "serif": True
    },
    {
        "id": "ambarrukmo",
        "title": "ROYAL",
        "subtitle": "AMBARRUKMO",
        "bg": (8, 12, 22),
        "fg": (255, 255, 255),
        "border": (212, 175, 55),
        "font_size_main": 34,
        "font_size_sub": 14,
        "serif": True
    },
    {
        "id": "danani",
        "title": "DANANI",
        "subtitle": "DECORATION",
        "bg": (16, 14, 12),
        "fg": (255, 255, 255),
        "border": (205, 175, 145),
        "font_size_main": 32,
        "font_size_sub": 12,
        "serif": True
    },
    {
        "id": "vidi",
        "title": "VIDI",
        "subtitle": "CATERING JOGJA",
        "bg": (14, 16, 14),
        "fg": (255, 255, 255),
        "border": (180, 200, 170),
        "font_size_main": 40,
        "font_size_sub": 11,
        "serif": True
    },
    {
        "id": "mahkota",
        "title": "MAHKOTA",
        "subtitle": "WEDDING ORGANIZER",
        "bg": (15, 10, 12),
        "fg": (255, 235, 200),
        "border": (220, 180, 100),
        "font_size_main": 28,
        "font_size_sub": 10,
        "serif": True
    }
]

size = (300, 300)

for cfg in avatar_configs:
    img = Image.new("RGB", size, cfg["bg"])
    draw = ImageDraw.Draw(img)
    
    # Outer subtle glow / border circle
    draw.ellipse([(10, 10), (290, 290)], outline=cfg["border"], width=3)
    draw.ellipse([(16, 16), (284, 284)], outline=(cfg["border"][0]//3, cfg["border"][1]//3, cfg["border"][2]//3), width=1)
    
    # Text fonts
    try:
        font_serif = ImageFont.truetype("georgia.ttf", cfg["font_size_main"])
        font_sub = ImageFont.truetype("arial.ttf", cfg["font_size_sub"])
    except:
        font_serif = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    
    # Draw title
    title = cfg["title"]
    bbox = draw.textbbox((0, 0), title, font=font_serif)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (size[0] - w) / 2
    y = (size[1] - h) / 2 - 14
    draw.text((x, y), title, fill=cfg["fg"], font=font_serif)
    
    # Divider line
    div_w = 60
    draw.line([(size[0]/2 - div_w/2, y + h + 10), (size[0]/2 + div_w/2, y + h + 10)], fill=cfg["border"], width=1)
    
    # Subtitle
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
