import os
import shutil
from PIL import Image, ImageDraw, ImageFont

os.makedirs("assets/vendors/avatars", exist_ok=True)
os.makedirs("assets/vendors/slides", exist_ok=True)

# 1. Create luxury avatar for Ilona Organizer
size = (300, 300)
img = Image.new("RGB", size, (16, 10, 24)) # Deep Royal Purple
draw = ImageDraw.Draw(img)

# Luxury double border in soft gold/purple
draw.ellipse([(10, 10), (290, 290)], outline=(218, 165, 32), width=3)
draw.ellipse([(16, 16), (284, 284)], outline=(147, 112, 219), width=1)

try:
    font_serif = ImageFont.truetype("georgia.ttf", 32)
    font_sub = ImageFont.truetype("arial.ttf", 10)
except:
    font_serif = ImageFont.load_default()
    font_sub = ImageFont.load_default()

title = "ILONA"
bbox = draw.textbbox((0, 0), title, font=font_serif)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (size[0] - w) / 2
y = (size[1] - h) / 2 - 14
draw.text((x, y), title, fill=(255, 248, 235), font=font_serif)

div_w = 60
draw.line([(size[0]/2 - div_w/2, y + h + 10), (size[0]/2 + div_w/2, y + h + 10)], fill=(218, 165, 32), width=1)

sub = "WEDDING ORGANIZER JOGJA"
sbox = draw.textbbox((0, 0), sub, font=font_sub)
sw = sbox[2] - sbox[0]
sh = sbox[3] - sbox[1]
sx = (size[0] - sw) / 2
sy = y + h + 16
draw.text((sx, sy), sub, fill=(210, 195, 240), font=font_sub)

avatar_path = "assets/vendors/avatars/ilona.jpg"
img.save(avatar_path, quality=95)
print(f"Created luxury avatar: {avatar_path}")

# 2. Prepare real wedding slide images for Ilona Organizer
slide1_src = "assets/vendors/slides/classywo_slide_1.jpg"
slide2_src = "assets/vendors/slides/weddingkujogja_slide_1.jpg"

shutil.copy(slide1_src, "assets/vendors/slides/ilona_slide_1.jpg")
shutil.copy(slide2_src, "assets/vendors/slides/ilona_slide_2.jpg")
print("Created slides: ilona_slide_1.jpg and ilona_slide_2.jpg")
