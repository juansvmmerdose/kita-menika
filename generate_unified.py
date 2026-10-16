import os
from PIL import Image, ImageDraw, ImageFont

# Load base screen
screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_clean_base.png').convert('RGBA')

# Font setup
font = None
badge_font = None
for p in [r'C:\Windows\Fonts\segoeui.ttf', r'C:\Windows\Fonts\arial.ttf']:
    if os.path.exists(p):
        font = ImageFont.truetype(p, 11)
        break
for p in [r'C:\Windows\Fonts\segoeuib.ttf', r'C:\Windows\Fonts\arialbd.ttf']:
    if os.path.exists(p):
        badge_font = ImageFont.truetype(p, 10)
        break

def make_squircle_icon(img_or_color, size=(60, 60), radius=13):
    mask = Image.new('L', size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size[0]-1, size[1]-1), radius=radius, fill=255)
    
    if isinstance(img_or_color, Image.Image):
        res = img_or_color.resize(size, Image.Resampling.LANCZOS)
    else:
        res = Image.new('RGBA', size, img_or_color)
    return res, mask

def draw_icon_label(draw, text, icon_x, icon_y, icon_w=60):
    if font:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        tx = icon_x + (icon_w - tw) // 2
        ty = icon_y + 64
        draw.text((tx, ty+1), text, font=font, fill=(0, 0, 0, 170))
        draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

draw = ImageDraw.Draw(screen)
icon_y = 690

# --- APP 1: (kita menikah) at Col 0 (x=35) ---
logo = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\app_logo.png').convert('RGBA')
icon_km, mask_km = make_squircle_icon(logo)
screen.paste(icon_km, (35, icon_y), mask=mask_km)
draw_icon_label(draw, "(kita menikah)", 35, icon_y)

# Badge (1) on (kita menikah)
bx, by = 35 + 60 - 4, icon_y + 4
draw.ellipse((bx - 8, by - 8, bx + 8, by + 8), fill=(255, 59, 48, 255), outline=(0, 0, 0, 200), width=1)
if badge_font:
    draw.text((bx - 3, by - 6), "1", font=badge_font, fill=(255, 255, 255, 255))

# --- APP 2: TikTok at Col 1 (x=141) ---
tiktok_base = Image.new('RGBA', (60, 60), (0, 0, 0, 255))
d_tt = ImageDraw.Draw(tiktok_base)
# Cyan offset
d_tt.ellipse((22, 32, 38, 48), fill=(37, 244, 238, 255))
d_tt.rectangle((34, 18, 38, 40), fill=(37, 244, 238, 255))
d_tt.arc((34, 14, 46, 26), 270, 360, fill=(37, 244, 238, 255), width=4)
# Red offset
d_tt.ellipse((26, 30, 42, 46), fill=(254, 44, 85, 255))
d_tt.rectangle((38, 16, 42, 38), fill=(254, 44, 85, 255))
d_tt.arc((38, 12, 50, 24), 270, 360, fill=(254, 44, 85, 255), width=4)
# White center
d_tt.ellipse((24, 31, 40, 47), fill=(255, 255, 255, 255))
d_tt.rectangle((36, 17, 40, 39), fill=(255, 255, 255, 255))
d_tt.arc((36, 13, 48, 25), 270, 360, fill=(255, 255, 255, 255), width=4)

icon_tt, mask_tt = make_squircle_icon(tiktok_base)
screen.paste(icon_tt, (141, icon_y), mask=mask_tt)
draw_icon_label(draw, "TikTok", 141, icon_y)

# --- APP 3: Instagram at Col 2 (x=247) ---
ig_base = Image.new('RGBA', (60, 60), (0, 0, 0, 0))
d_ig = ImageDraw.Draw(ig_base)
for iy in range(60):
    for ix in range(60):
        t1 = (ix + iy) / 120.0
        r = int(131 * (1-t1) + 245 * t1)
        g = int(58 * (1-t1) + 96 * t1)
        b = int(180 * (1-t1) + 64 * t1)
        ig_base.putpixel((ix, iy), (r, g, b, 255))

d_ig = ImageDraw.Draw(ig_base)
d_ig.rounded_rectangle((14, 14, 45, 45), radius=8, outline=(255, 255, 255, 255), width=3)
d_ig.ellipse((22, 22, 37, 37), outline=(255, 255, 255, 255), width=3)
d_ig.ellipse((38, 19, 41, 22), fill=(255, 255, 255, 255))

icon_ig, mask_ig = make_squircle_icon(ig_base)
screen.paste(icon_ig, (247, icon_y), mask=mask_ig)
draw_icon_label(draw, "Instagram", 247, icon_y)

# --- APP 4: WhatsApp at Col 3 (x=353) ---
wa_base = Image.new('RGBA', (60, 60), (37, 211, 102, 255))
d_wa = ImageDraw.Draw(wa_base)
# White phone bubble
d_wa.ellipse((14, 14, 46, 46), outline=(255, 255, 255, 255), width=3)
d_wa.polygon([(18, 40), (12, 48), (24, 45)], fill=(255, 255, 255, 255))
# Small phone handset inside
d_wa.arc((22, 22, 38, 38), 120, 300, fill=(255, 255, 255, 255), width=3)

icon_wa, mask_wa = make_squircle_icon(wa_base)
screen.paste(icon_wa, (353, icon_y), mask=mask_wa)
draw_icon_label(draw, "WhatsApp", 353, icon_y)

# Save
screen.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_unified.png')
screen.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_unified.png')
print("Saved ios_homescreen_unified.png successfully!")
