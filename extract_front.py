from PIL import Image, ImageDraw
import numpy as np

im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg').convert('RGBA')

# Crop the front phone region
# The front phone runs from x=256 to x=530, y=15 to y=585
crop_box = (255, 15, 530, 585)
phone_img = im1.crop(crop_box)
w, h = phone_img.size

# We want to make any pixel outside the phone transparent:
# 1. Any white background (R>245, G>245, B>245) -> transparent
# 2. Any pixel to the left of the front phone's titanium edge (the back phone bleed) -> transparent
# Let's inspect the phone's left edge profile
# The front phone has rounded corners.
# Let's save phone_img to test
phone_img.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\phone_raw.png')
print("phone_raw size:", phone_img.size)
