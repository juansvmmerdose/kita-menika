from PIL import Image, ImageDraw, ImageFont
import os
import shutil

os.makedirs("assets/vendors/avatars", exist_ok=True)
os.makedirs("assets/vendors/slides", exist_ok=True)

mc_sound_avatars = [
    {
        "id": "albertusmc",
        "title": "ALBERTUS",
        "subtitle": "MC WEDDING JOGJA",
        "bg": (18, 10, 10),
        "fg": (255, 230, 230),
        "border": (240, 90, 90),
        "font_size_main": 30,
        "font_size_sub": 10
    },
    {
        "id": "dimasmc",
        "title": "DIMAS MC",
        "subtitle": "PRANATACARA ADAT",
        "bg": (18, 12, 8),
        "fg": (255, 235, 200),
        "border": (225, 180, 80),
        "font_size_main": 28,
        "font_size_sub": 10
    },
    {
        "id": "prosound",
        "title": "PRO SOUND",
        "subtitle": "AUDIO SYSTEM JOGJA",
        "bg": (8, 16, 16),
        "fg": (230, 255, 255),
        "border": (70, 210, 200),
        "font_size_main": 28,
        "font_size_sub": 9
    },
    {
        "id": "mataramsound",
        "title": "MATARAM",
        "subtitle": "SOUND & LIGHTING",
        "bg": (10, 14, 20),
        "fg": (240, 245, 255),
        "border": (90, 150, 240),
        "font_size_main": 30,
        "font_size_sub": 9
    }
]

size = (300, 300)

for cfg in mc_sound_avatars:
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

# Slide copies
shutil.copy("assets/vendors/slides/mahkota_slide_1.jpg", "assets/vendors/slides/albertusmc_slide_1.jpg")
shutil.copy("assets/vendors/slides/jawara_slide_2.jpg", "assets/vendors/slides/dimasmc_slide_1.jpg")
shutil.copy("assets/vendors/slides/gmproduction_slide_1.jpg", "assets/vendors/slides/prosound_slide_1.jpg")
shutil.copy("assets/vendors/slides/danani_slide_1.jpg", "assets/vendors/slides/mataramsound_slide_1.jpg")
print("All MC and Sound assets ready!")
