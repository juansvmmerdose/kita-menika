from PIL import Image
import numpy as np

# Load the original image 1
im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg').convert('RGBA')

# Let's find the front phone in im1:
# The front phone lies on the right.
# Let's inspect where the front phone outer contour is:
# We know the front phone is roughly from x=256 to 526, y=16 to 582
# Let's test columns at various y
for y in [100, 200, 300, 400, 500]:
    row = [im1.getpixel((x, y)) for x in range(240, 540)]
    # find where it differs from white (255, 255, 255)
    non_white = [i+240 for i, p in enumerate(row) if p[0] < 250 or p[1] < 250 or p[2] < 250]
    print(f"y={y}: min_x={min(non_white)}, max_x={max(non_white)}")
