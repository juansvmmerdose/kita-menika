import os
from PIL import Image, ImageDraw, ImageFont

# Load cleaned homescreen
screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_perfect.png').convert('RGBA')

# Load the user's app logo (silver rings with black luxury background)
logo_path = r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\app_logo.png'
logo = Image.open(logo_path).convert('RGBA')

# Resize logo to 60x60 (matching standard iOS icon size in this 460x980 screen)
icon_size = (60, 60)
logo_resized = logo.resize(icon_size, Image.Resampling.LANCZOS)

# Create iOS squircle mask for the icon
mask = Image.new('L', icon_size, 0)
draw_mask = ImageDraw.Draw(mask)
# rounded rectangle with 14px radius
draw_mask.rounded_rectangle((0, 0, 59, 59), radius=14, fill=255)

# Place icon at Row 5, Column 0:
# Col 0 left is 32, top is 635
icon_x = 32
icon_y = 635

# Also add subtle iOS icon shadow
icon_with_shadow = Image.new('RGBA', (66, 66), (0, 0, 0, 0))
# paste icon into screen
screen.paste(logo_resized, (icon_x, icon_y), mask=mask)

# Add label text: "(kita menikah)"
draw = ImageDraw.Draw(screen)
# Try to load a nice clean sans-serif font or default
font = None
font_paths = [
    r'C:\Windows\Fonts\segoeui.ttf',
    r'C:\Windows\Fonts\arial.ttf',
]
for p in font_paths:
    if os.path.exists(p):
        font = ImageFont.truetype(p, 11)
        break

text = "(kita menikah)"
if font:
    # calculate text width to center under icon
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    tx = icon_x + (60 - tw) // 2
    ty = icon_y + 64
    # subtle drop shadow for iOS text
    draw.text((tx, ty+1), text, font=font, fill=(0, 0, 0, 140))
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

screen.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_with_app.png')
screen.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_with_app.png')
print("Successfully created ios_homescreen_with_app.png!")
