import os
from PIL import Image, ImageDraw, ImageFont

# Load cleaned homescreen
screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_perfect.png').convert('RGBA')

# Load the user's app logo (silver rings with black luxury background)
logo_path = r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\app_logo.png'
logo = Image.open(logo_path).convert('RGBA')

# In this screen (460x980):
# Icons are 60x60 with continuous squircle radius 13.5px
icon_w, icon_h = 60, 60
logo_resized = logo.resize((icon_w, icon_h), Image.Resampling.LANCZOS)

# iOS Squircle mask
mask = Image.new('L', (icon_w, icon_h), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.rounded_rectangle((0, 0, icon_w-1, icon_h-1), radius=13, fill=255)

# Coordinates for Row 5, Column 0:
# Col 0: x=32
# Row 5: y=685 (Health icon ends at 640, label ends at 658)
# At y=685..745: app icon
# At y=752..766: label "(kita menikah)"
# Dots are at y=835. Dock is at y=860.
icon_x = 32
icon_y = 685

# Paste icon with squircle mask
screen.paste(logo_resized, (icon_x, icon_y), mask=mask)

# Add iOS notification badge (1) on top right of the icon
badge_r = 9
badge_cx = icon_x + icon_w - 4
badge_cy = icon_y + 4
draw = ImageDraw.Draw(screen)
# Badge circle: red with white border
draw.ellipse((badge_cx - badge_r, badge_cy - badge_r, badge_cx + badge_r, badge_cy + badge_r), fill=(255, 59, 48, 255), outline=(0, 0, 0, 180), width=1)

# Badge text "1"
badge_font = None
for p in [r'C:\Windows\Fonts\segoeuib.ttf', r'C:\Windows\Fonts\arialbd.ttf']:
    if os.path.exists(p):
        badge_font = ImageFont.truetype(p, 11)
        break
if badge_font:
    draw.text((badge_cx - 3, badge_cy - 7), "1", font=badge_font, fill=(255, 255, 255, 255))

# Add label text: "(kita menikah)"
font = None
for p in [r'C:\Windows\Fonts\segoeui.ttf', r'C:\Windows\Fonts\arial.ttf']:
    if os.path.exists(p):
        font = ImageFont.truetype(p, 11)
        break

text = "(kita menikah)"
if font:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    tx = icon_x + (icon_w - tw) // 2
    ty = icon_y + 65
    # iOS label shadow + white text
    draw.text((tx, ty+1), text, font=font, fill=(0, 0, 0, 160))
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

output_path1 = r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_with_app.png'
output_path2 = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_with_app.png'
screen.save(output_path1)
screen.save(output_path2)
print("Updated ios_homescreen_with_app.png successfully!")
