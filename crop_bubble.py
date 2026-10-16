import numpy as np
from PIL import Image

img_path = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792127786917_1ca0aff6.png'
im = Image.open(img_path).convert('RGBA')

# The bubble center is around (512, 504)
# Let's inspect the bounding box: min_x=233, max_x=789, min_y=220, max_y=787
# Let's crop with a small 10px margin: (220, 205, 800, 800)
# Make it a perfect square:
cx, cy = (233 + 789) // 2, (220 + 787) // 2
half_size = max(789 - 233, 787 - 220) // 2 + 10 # 570 / 2 + 10 = 295
crop_box = (cx - half_size, cy - half_size, cx + half_size, cy + half_size)

bubble_crop = im.crop(crop_box)
bw, bh = bubble_crop.size

# To make the outer area transparent:
# Any pixel outside the glowing squircle where the background is pitch black:
# We can make alpha proportional to brightness or create a clean squircle mask
# Let's inspect the corner pixels of bubble_crop
arr = np.array(bubble_crop)

# Let's check brightness of corners (they are (0,0,0,255) pure black)
# We can make pure black transparent:
# If brightness < 5 -> alpha = 0, with smooth ramp from 5 to 25
# Or flood-fill / mask from outside:
from PIL import ImageDraw

# Better yet, let's create a transparent PNG where the glowing squircle is fully preserved:
# Let's check brightness formula:
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)
brightness = np.maximum(np.maximum(r, g), b)

# The inside of the bubble also has a black background (#000000) with silver rings.
# We do NOT want to make the inside of the bubble transparent, ONLY the area OUTSIDE the glowing white rim!
# Let's find the outer glowing white rim contour!
# Let's do a flood-fill or distance-from-center mask:
# The glowing rim has an outer squircle contour.
# Let's find the mask of the squircle:
mask = Image.new('L', (bw, bh), 0)
d = ImageDraw.Draw(mask)
# The glowing white outline is a squircle:
# In bubble_crop (approx 590x590):
# Rim outer bounds: left ~ 18, right ~ 572, top ~ 18, bottom ~ 572
# Radius of squircle corner: ~ 150px
d.rounded_rectangle((14, 14, bw - 15, bh - 15), radius=140, fill=255)

# Save mask and masked crop
bubble_clean = Image.new('RGBA', (bw, bh), (0, 0, 0, 0))
bubble_clean.paste(bubble_crop, (0, 0), mask=mask)

out_scratch = r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\app_icon_squircle.png'
out_brain = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\app_icon_squircle.png'

bubble_clean.save(out_scratch)
bubble_clean.save(out_brain)

# Also update assets/app_logo.png
bubble_clean.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\app_logo.png')
bubble_clean.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\app_logo.png')

print(f"Saved app_icon_squircle.png with size {bubble_clean.size}")
