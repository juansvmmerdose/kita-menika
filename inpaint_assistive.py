import numpy as np
from PIL import Image, ImageFilter

# Load original screen_crop.png
base = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png').convert('RGB')
arr = np.array(base).astype(float)
w, h = base.size

# 1. Clean the top notch (y: 0..40, x: 95..365)
# In iPhone 16 Pro, the Dynamic Island will be placed right in the center (x: 180 to 280, y: 15 to 45).
# Let's cleanly interpolate the orange gradient across y: 0..40, x: 95..365
for y in range(45):
    c_left = arr[y, 90]
    c_right = arr[y, 370]
    for x in range(95, 366):
        t = (x - 95) / 270.0
        # only replace dark pixels (the old notch)
        if arr[y, x, 0] < 110 and arr[y, x, 1] < 110 and arr[y, x, 2] < 110:
            arr[y, x] = (1 - t) * c_left + t * c_right

# 2. AssistiveTouch button center is around (413, 764)
# Radius of the circle is ~35px
cx, cy = 413, 764
radius = 36

# Radial harmonic interpolation from circumference
angles = np.linspace(0, 2*np.pi, 120, endpoint=False)
for r in range(radius, -1, -1):
    for a in angles:
        px = int(cx + r * np.cos(a))
        py = int(cy + r * np.sin(a))
        if 0 <= px < w and 0 <= py < h:
            # sample from circumference
            bx = int(cx + (radius + 3) * np.cos(a))
            by = int(cy + (radius + 3) * np.sin(a))
            bx = min(max(bx, 0), w - 1)
            by = min(max(by, 0), h - 1)
            arr[py, px] = arr[by, bx]

res = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

# Subtle blur ONLY over the small circle to make the gradient seamless
mask = Image.new('L', (w, h), 0)
from PIL import ImageDraw
d = ImageDraw.Draw(mask)
d.ellipse((cx - radius - 2, cy - radius - 2, cx + radius + 2, cy + radius + 2), fill=255)
d.rectangle((95, 0, 365, 45), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(3))

blurred = res.filter(ImageFilter.GaussianBlur(2))
res.paste(blurred, mask=mask)

res.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_clean_base.png')
res.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_clean_base.png')
print("Successfully generated ios_homescreen_clean_base.png!")
