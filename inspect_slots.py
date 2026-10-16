from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# Let's crop each of the 6x4 slots and save a collage or check standard deviation of color
# A flat wallpaper area will have smooth gradients; an icon has sharp borders and squircle shape
import numpy as np

for r in range(6):
    y = 100 + r * 110
    for c in range(4):
        x = 50 + c * 105
        # crop 70x70
        box = im2.crop((x, y, x+70, y+70))
        arr = np.array(box.convert('RGB'))
        std = np.std(arr)
        print(f"Row {r}, Col {c} (x={x}, y={y}): std={std:.1f}")
