import numpy as np
from PIL import Image, ImageFilter, ImageDraw

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png').convert('RGB')
w, h = screen.size
arr = np.array(screen).astype(float)

# 1. Clean the top notch area (y: 0..55, x: 80..380):
# In the original wallpaper, y=0..55 is a smooth warm orange gradient from left to right.
# Left side at x=80: arr[y, 80]
# Right side at x=380: arr[y, 380]
for y in range(60):
    c_left = arr[y, 80]
    c_right = arr[y, 380]
    for x in range(80, 381):
        t = (x - 80) / 300.0
        # Target color is smooth interpolation
        target = (1 - t) * c_left + t * c_right
        arr[y, x] = target

# 2. Clean the bottom-right smudge where AssistiveTouch was (x: 370..455, y: 720..815):
# Notice that the wave curve at y=720..815 can be sampled from the smooth wave just to the left (x: 280..365)
# or by horizontal shift + vertical slope:
for y in range(715, 825):
    for x in range(370, min(458, w)):
        # Sample color from x-80 (which is completely clean smooth wave)
        # and adjust slightly if there's a slow vertical gradient
        arr[y, x] = arr[y, x - 80]

# Smooth the seams with a gentle blur on the modified regions
clean_img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

mask = Image.new('L', (w, h), 0)
d = ImageDraw.Draw(mask)
d.rectangle((75, 0, 385, 62), fill=255)
d.rectangle((365, 710, 458, 830), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(4))

blurred = clean_img.filter(ImageFilter.GaussianBlur(3))
clean_img.paste(blurred, mask=mask)

clean_img.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_pristine.png')
clean_img.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_pristine.png')
print("Pristine homescreen background generated successfully!")
