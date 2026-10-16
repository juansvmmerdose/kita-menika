import os
from PIL import Image

img_path = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792127786917_1ca0aff6.png'
im = Image.open(img_path)
print("Image size:", im.size, im.mode)

# Let's find the bounding box of the glowing squircle bubble inside the black background
# Background is black (0, 0, 0)
w, h = im.size
min_x, max_x, min_y, max_y = w, 0, h, 0

for y in range(h):
    for x in range(w):
        p = im.getpixel((x, y))
        # Check brightness
        if p[0] > 15 or p[1] > 15 or p[2] > 15:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Squircle bubble bbox: ({min_x}, {min_y}, {max_x}, {max_y})")
print(f"Width: {max_x - min_x}, Height: {max_y - min_y}")
