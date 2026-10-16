from PIL import Image, ImageDraw
import numpy as np

# Let's inspect phone_raw
raw = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\phone_raw.png').convert('RGBA')
w, h = raw.size
print(f"phone_raw: {w}x{h}")

# The screen inside phone_raw:
# Left edge of screen ~ 8px
# Right edge of screen ~ 265px
# Top edge of screen ~ 8px
# Bottom edge of screen ~ 560px
# Let's verify screen borders:
print("Pixel at (137, 25):", raw.getpixel((137, 25)))
print("Pixel at (137, 50):", raw.getpixel((137, 50)))
