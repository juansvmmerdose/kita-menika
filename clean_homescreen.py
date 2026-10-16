import os
from PIL import Image, ImageDraw, ImageFont

# Load screen crop from Image 2
screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png').convert('RGBA')
w, h = screen.size
print(f"Screen size: {w}x{h}")

# 1. Let's remove the AssistiveTouch circle:
# Center of AssistiveTouch in screen_preview is around x=410, y=780
# Let's inspect coordinates of AssistiveTouch
# Let's find pixels around x=380..450, y=740..820
assist_crop = screen.crop((360, 720, 450, 830))
assist_crop.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assist_touch.png')
print("Saved assist_touch.png")
