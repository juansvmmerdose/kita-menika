import os
from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')
bbox = im2.getbbox()
print("im2 bbox:", bbox)

# Let's inspect where pixels are non-transparent in im2
# Also let's check im1
im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')
# In im1, find bounding box of front phone (right half)
# Width 600, right half is x: 280 to 600
# Let's find pixels where r, g, b != 255
w, h = im1.size
min_x, max_x, min_y, max_y = w, 0, h, 0
for x in range(250, w):
    for y in range(h):
        p = im1.getpixel((x, y))
        if p[0] < 250 or p[1] < 250 or p[2] < 250:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y
print("im1 front phone bbox:", (min_x, min_y, max_x, max_y))
print("im1 front phone width, height:", max_x - min_x, max_y - min_y)
