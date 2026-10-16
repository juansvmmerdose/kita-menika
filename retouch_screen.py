import numpy as np
from PIL import Image, ImageFilter, ImageDraw

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png').convert('RGB')
w, h = screen.size
arr = np.array(screen)

# 1. Fill old notch at top: x: 100..360, y: 0..42
# Left side at x=100 is orange, right side at x=360 is orange-red.
# We can smoothly interpolate horizontally and vertically from the surrounding wallpaper.
for y in range(45):
    left_col = arr[y, 100].astype(float)
    right_col = arr[y, 360].astype(float)
    for x in range(101, 360):
        t = (x - 100) / 260.0
        # If this pixel was dark (part of the old notch), replace with interpolated wallpaper
        if arr[y, x, 0] < 120 and arr[y, x, 1] < 120 and arr[y, x, 2] < 120:
            arr[y, x] = (1 - t) * left_col + t * right_col

# 2. Retouch AssistiveTouch circle:
# Center ~ (415, 765), radius ~ 36
# The background in this region is the magenta curve: y increases -> purple/magenta
# At each y in range 720..810, the gradient is almost constant or slow varying horizontally.
# Let's sample the color at x=350 (outside the circle) for each y, or interpolate across x: 365 to 455
for y in range(715, 815):
    ref_col = arr[y, 360].astype(float)
    ref_col_r = arr[y, min(458, w-1)].astype(float)
    for x in range(370, 458):
        # calculate distance to circle center (415, 765)
        dist = ((x - 415)**2 + (y - 765)**2)**0.5
        if dist < 42:
            t = (x - 360) / (458 - 360)
            arr[y, x] = (1 - t) * ref_col + t * ref_col_r

cleaned = Image.fromarray(arr)
# Apply a subtle box blur only to the retouched areas to make them silky smooth
mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)
draw.rectangle((101, 0, 359, 44), fill=255)
draw.ellipse((370, 720, 458, 810), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(3))

blurred = cleaned.filter(ImageFilter.GaussianBlur(2))
cleaned.paste(blurred, mask=mask)

cleaned.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_clean.png')
cleaned.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_clean.png')
print("Saved ios_homescreen_clean.png successfully!")
